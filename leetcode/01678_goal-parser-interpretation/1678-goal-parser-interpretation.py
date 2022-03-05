class Solution:
    def interpret(self, command: str) -> str:
        newCommand = ""
        for i in range(len(command)):
            if command[i] == "G":
                newCommand += command[i]
            elif command[i] == "(" and command[i + 1] == ")":
                newCommand += "o"
                i += 1
            elif command[i] == "(" and command[i + 1] == "a":
                newCommand += "al"
                i += 3

        return newCommand
