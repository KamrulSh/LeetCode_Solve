"""
Move the directories generated by [LeetHub](https://github.com/QasimWani/LeetHub)
to the 'leetcode' directory, with the question number is added as prefix.
"""
import json
import logging
import re
import shutil
from pathlib import Path
from typing import List, Dict

WORKDIR = Path('.')
EXCLUDED = ['codility', 'leetcode', 'others']
TARGET_DIRECTORY = WORKDIR / 'leetcode'
SCRIPTS_DIRECTORY = WORKDIR / '.github/workflows/scripts'
EXISTING_QUESTIONS = list(TARGET_DIRECTORY.glob('*'))

# icons are provided by [devicon](https://devicon.dev).
ICONS = json.loads((SCRIPTS_DIRECTORY / 'lang_suffix_to_icon.json').read_bytes())

QUESTION_BASE_URL = 'https://leetcode.com/problems'


class Question:
    def __init__(self, path: Path):
        self.path: Path = path
        if not self.path.exists():
            raise ValueError(f"{self.path.as_posix()} does not exist")
        if self.path.is_file():
            raise ValueError(f"{self.path.as_posix()} should be a directory")

        self.readme_path: Path = self.path / 'README.md'
        if self.is_in_target_directory and not self.readme_path.exists():
            raise ValueError(f"{self.readme_path.as_posix()} does not exist")

        # handle metadata
        self.tag: str = ''
        self.number: int = 0
        self.title: str = 'N/A'
        self.difficulty: str = 'N/A'
        self._init_question_meta()

    def _init_question_meta(self):
        if self.readme_path.exists():
            self._parse_meta_from_md()
            return

        splited_tag = self.path.name.split('_')
        if len(splited_tag) == 2:
            self.tag = splited_tag[-1]
        elif len(splited_tag) == 1:
            self.tag = '-'.join(self.path.name.split('-')[1:])
        else:
            raise ValueError(f'Cannot parse question tag for {self.path}')

        existing_dirs = list(TARGET_DIRECTORY.glob(f'*_{self.tag}'))
        if len(existing_dirs) == 0:
            raise ValueError(f'Cannot find readme of {self.tag}')
        if len(existing_dirs) > 1:
            raise ValueError(f"Multiple existing readme of {self.tag} are found: {existing_dirs}. "
                             "Manually deleting duplicated ones may be required.")
        existing_md = existing_dirs[0] / 'README.md'
        self._parse_meta_from_md(existing_md)

    def _parse_meta_from_md(self, path: Path = None):
        path = path if path else self.readme_path
        pattern: str = r'^<h2><a href="https://leetcode\.com/problems/(.*)[//]+">(\d+)\. (.*)</a></h2><h3>(.*)</h3>.*'
        matched: re.Match = re.search(pattern, path.read_text())
        if matched:
            self.tag = matched.groups()[0]
            self.number = int(matched.groups()[1])
            self.title = matched.groups()[2]
            self.difficulty = matched.groups()[3]
        else:
            logging.warning(f'Failed to parse metadata from question readme from "{self.path}"')

    def move_to_target_directory(self):
        if self.is_in_target_directory:
            return

        dest_directory = TARGET_DIRECTORY / self.folder_name
        if dest_directory.exists():
            for src in self.path.glob('*'):
                dest = dest_directory / src.name
                if dest.exists():
                    dest.unlink()
                src.rename(dest)
            shutil.rmtree(self.path)
            logging.info(f"Moved all files in {self.path} to {dest_directory}")
        else:
            self.path.rename(dest_directory)
            logging.info(f"Renamed {self.path} as {dest_directory}")
        self.path = dest_directory

    @property
    def is_in_target_directory(self) -> bool:
        return self.path in EXISTING_QUESTIONS

    @property
    def solutions_dict(self) -> Dict[str, Path]:
        solutions: Dict[str, Path] = {}  # ext as dict key
        for sol in self.path.glob(f"*{self.tag}.*"):
            solutions[sol.suffix] = sol
        return solutions

    @property
    def folder_name(self) -> str:
        return f"{str(self.number).zfill(5)}_{self.tag}"

    @property
    def link(self) -> str:
        return f"{QUESTION_BASE_URL}/{self.tag}/"


def move_question_directory():
    logging.info(f"Moving submitted solutions to {TARGET_DIRECTORY}...")
    for path in WORKDIR.glob('*'):
        if path.is_file():
            continue
        if path.name in EXCLUDED or path.name.startswith('.'):
            continue
        try:
            q = Question(path)
            q.move_to_target_directory()
        except Exception as error:
            logging.warning(f'Somthing went wrong when moving directory "{path}", error={error}')


def build_readme(questions: List[Question]) -> str:
    md = "| # | Title | Solutions | Difficulty |\n" + \
        "| - | - | - | - |\n"
    for q in questions:
        anchored_title = f"[{q.title}]({q.link})"
        solution_links = ""
        for ext, path in q.solutions_dict.items():
            solution_links += f'<a href="{path}"><img src="{ICONS[ext]}" width="20" height="20"></a>'
        md += f"| {q.number} | {anchored_title} " + \
            f"| {solution_links} | {q.difficulty} |\n"
    return md


if __name__ == "__main__":
    TARGET_DIRECTORY.mkdir(exist_ok=True)
    move_question_directory()

    questions = []
    level_count = {'easy': 0, 'medium': 0, 'hard': 0}
    total = 0
    for path in TARGET_DIRECTORY.glob('*'):
        q = Question(path)
        questions.append(q)
        if q.difficulty.lower() not in level_count:
            continue
        level_count[q.difficulty.lower()] += 1
        total += 1
    questions.sort(key=lambda q: q.number)
    logging.info(f"{total} questions are found ({level_count})")

    md_table = build_readme(questions)
    with open(SCRIPTS_DIRECTORY / 'README.md.tpl', 'r') as template, \
            open('README.md', 'w') as output:
        template_string = template.read()
        content = template_string.format(leetcode=md_table, total=total, **level_count)
        output.write(content)
    logging.info("Done updating README.md")
