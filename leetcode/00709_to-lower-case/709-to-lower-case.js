/**
 * @param {string} str
 * @return {string}
 */
var toLowerCase = function (str) {
    let newStr = "", value = 0;
    for (let i = 0; i < str.length; i++) {
        if (str.charCodeAt(i) < 91 && str.charCodeAt(i) > 64) {
            value = str.charCodeAt(i) + 32;
            newStr += String.fromCodePoint(value);
        } else newStr += str[i];
        //console.log(newStr);
    }
    return newStr;
};