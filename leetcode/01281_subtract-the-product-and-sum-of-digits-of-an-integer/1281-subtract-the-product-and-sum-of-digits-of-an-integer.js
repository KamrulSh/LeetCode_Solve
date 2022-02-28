/**
 * @param {number} n
 * @return {number}
 */
var subtractProductAndSum = function (num) {
    let product = 1,
        sum = 0,
        digit = 0;
    while (num > 0) {
        digit = num % 10;
        product *= digit;
        sum += digit;
        num = parseInt(num / 10);
        //console.log(digit, num);
    }
    return product-sum;
};