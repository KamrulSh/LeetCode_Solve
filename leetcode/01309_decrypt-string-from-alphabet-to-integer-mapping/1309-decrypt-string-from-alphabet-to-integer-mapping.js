/**
 * @param {string} s
 * @return {string}
 */
var freqAlphabets = function (str) {
    let newStr = "",
        char;
    for (let i = 0; i < str.length; i++) {
        let code = "";
        if (str[i + 2] == "#") {
            code += str[i] + str[i + 1];
            i += 2;
        } else code += str[i];
        //console.log(code);
        char = String.fromCodePoint(parseInt(code) + 96);
        newStr += char;
    }
    return newStr;
};