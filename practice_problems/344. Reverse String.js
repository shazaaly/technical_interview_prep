/**
*  Note : String immutability: In JavaScript, strings are immutable, which means you can't 
*  change their characters directly. 
*  You need to convert the string to an array, 
*  swap the characters in the array, and then convert the array back to a string.
*  @return {void} Do not return anything, modify s in-place instead.
*/
var reverseString = function(s) {
    let left = 0;
    let right = s.length - 1;

    while(left < right){
       [s[left], s[right]] =[s[right], s[left]]
 
        left++
        right--
    }
    
};
