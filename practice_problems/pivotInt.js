/**
 * @param {number} n
 * @return {number}
 */
var pivotInteger = function(n) {
    if( n === 1) return n
   let leftWindowIndex = 1
    let rightWindowIndex = leftWindowIndex + 1
    let rightWindowSum = 0
    let leftWindowSum = leftWindowIndex + rightWindowIndex
    for (let i = rightWindowIndex; i <= n; i++) {
        rightWindowSum += i

    }
    if (leftWindowSum === rightWindowSum) return rightWindowIndex
    while (rightWindowSum !== leftWindowSum && rightWindowIndex < n) {

        rightWindowIndex++
        rightWindowSum = 0
        for (let i = leftWindowIndex; i <= rightWindowIndex; i++) {
            rightWindowSum += i

        }
        leftWindowSum = 0
        for (let i = rightWindowIndex; i <= n; i++) {
            leftWindowSum += i

        }
        if(rightWindowSum === leftWindowSum) return rightWindowIndex

    }
    
    return -1

    
};

console.log(pivotInteger(8)) // 6
console.log(pivotInteger(4)) // -1