/**
 * @param {number[][]} accounts
 * @return {number}
 */
var maximumWealth = function(accounts) {
    let newArr = [];
    for (let i = 0; i < accounts.length; i++) {
        let sum = 0;
        for (let j = 0; j < accounts[i].length; j++) {
            sum += accounts[i][j];
        }
        newArr.push(sum);
    }
    let maxValue = Math.max(...newArr);
    //console.log(newArr, maxValue);
    return maxValue;
};