/**
 * @param {string} s
 * @return {number}
 */
var maxDepth = function (s) {
    let maxVal = 0,
        count = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] == "(") {
            count++;
        } else if (s[i] == ")") {
            if (count > maxVal) {
                maxVal = count;
            }
            count--;
        }
    }
    return maxVal;
};