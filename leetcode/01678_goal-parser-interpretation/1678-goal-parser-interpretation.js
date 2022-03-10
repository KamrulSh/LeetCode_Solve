/**
 * @param {string} command
 * @return {string}
 */
var interpret = function(command) {
    let newCommand = "";
    for (let i = 0; i < command.length; i++) {
        if (command[i] == "G") {
            newCommand += command[i];
        } else if (command[i] == "(" && command[i + 1] == ")") {
            newCommand += "o";
            i++;
        } else if (command[i] == "(" && command[i + 1] == "a") {
            newCommand += "al";
            i += 3;
        }
    }
    return newCommand;
};