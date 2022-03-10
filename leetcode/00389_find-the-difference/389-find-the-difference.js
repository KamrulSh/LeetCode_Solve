/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function (s, t) {
    let len = t.length;
    let last2 = t.charCodeAt(len - 1);
    let last1 = 0;
    // counting the ascii code value
    for (let i in s) {
        last1 += s.charCodeAt(i);
        last2 += t.charCodeAt(i);
    }
    return String.fromCharCode(last2 - last1);
};