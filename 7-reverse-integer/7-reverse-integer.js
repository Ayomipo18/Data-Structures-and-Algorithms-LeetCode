/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    const sign = Math.sign(x)
   
    let num = Math.abs(x);
    
    let reversedNum = 0;
    while(num>0){
        const rightmostDigit = num % 10;
        num = Math.floor(num / 10);
        reversedNum *= 10;
        reversedNum += rightmostDigit;
        
        if(reversedNum > Math.pow(2,31)-1){
            return 0
        }
    }
    return reversedNum * sign
};