class Solution {
    public:
        string interpret(string command) {
            string newCommand= "";
            for(int i=0; i<command.size(); i++)
            {
                if (command[i] == 'G') {
                    newCommand += command[i];
                } else if (command[i] == '(' && command[i + 1] == ')') {
                    newCommand += "o";
                    i++;
                } else if (command[i] == '(' && command[i + 1] == 'a') {
                    newCommand += "al";
                    i += 3;
                }
            }
            return newCommand;
        }
    };