public class Solution {
    public int EvalRPN(string[] tokens) {
        Stack<int> stack = new();
        for(int i = 0; i < tokens.Length; i++) {
            bool isNumeric = int.TryParse(tokens[i], out int num);
            if(!isNumeric) {
                int secondNumber = stack.Pop();
                int firstNumber = stack.Pop();
                int calValue = calc(tokens[i], firstNumber, secondNumber);
                stack.Push(calValue);
            } else {
                stack.Push(num);
            }
        }
        return stack.Pop();
    }
    
    private int calc(string op, int firstNumber, int secondNumber) {
        if(op == "+") {
            return firstNumber + secondNumber;
        } else if(op == "-") {
            return firstNumber - secondNumber;
        } else if(op == "/") {
            return firstNumber / secondNumber;
        }
        return firstNumber * secondNumber;;
    }
}

//use a stack, add every element in the token
//if we see a value that is not a number, pop the top two values from the stack to do the operation with
//17 5
//9 + 3 = 12
//12 * -11 = -132
//6 / -132 = 0
//10 * 0 = 0
//0 + 17 = 17
//17 + 5 = 22

//9
//2 + 1= 3
//3 * 3 = 9