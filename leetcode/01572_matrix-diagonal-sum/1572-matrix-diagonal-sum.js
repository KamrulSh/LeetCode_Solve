/**
 * @param {number[][]} mat
 * @return {number}
 */
var diagonalSum = function (mat) {
    // 00 02
    // 11 11
    // 22 20
    let start = 0,
        end = mat.length - 1,
        mid = parseInt(mat.length / 2);
    sum = 0;
    for (let i = 0; i < mat.length; i++) {
        //console.log(mat[i][start], mat[i][end]);
        sum += mat[i][start] + mat[i][end];
        start++;
        end--;
        //console.log(sum);
    }
    if (mat.length % 2 != 0) {
        sum -= mat[mid][mid];
    }
    return sum;
};