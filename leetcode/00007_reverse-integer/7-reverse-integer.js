/**
 * @param {number} x
 * @return {number}
 */
var reverse = function (x) {
    let num = 0,
        digit = 0;
    let absX = Math.abs(x);
    while (absX) {
        digit = absX % 10;
        absX = parseInt(absX / 10);
        num = num * 10 + digit;
    }
    let limit = Math.pow(2, 31) - 1;
    if (num > limit) {
        return 0;
    }
    return x < 0 ? num * -1 : num;
};