class Solution {
    public boolean backspaceCompare(String s, String t) {
        /*
        - cmpare strings, keeping in mind deletion
        - we basiaclly use valid read position
        - backspace is not a valid position, letter before backspace is not a valid read position
        - compare out front and it doesn't work at some point
        - whow can this question be changed
             - maybe instead of just only #, they can have diff chars?
             - sub string that can be found in a string
        - what's the tech concept
            - Reverse string comparison while deleting chars
            - two pointers
            - backspacing

        - Works atm but since i am moving pointers, 1 pointer could be out of bounds
        - Two-Pointer Right-to-Left Traversal ($\mathcal{O}(1)$ Space)
        - Dynamic Skip Counter (Simulating Stack Pop)
        - Short-Circuit Guarding

        - Time - O(max(len(t), len(s)))
        - Space - O(1)
        */

        int l1 = s.length()-1;
        int l2 = t.length()-1;

        int l1_skip = 0;
        int l2_skip = 0;

        while(l1 >= 0 || l2 >= 0) {
            // check if it's a char, if char, then it's due for comparison.  Else, if it's a backspace, move until you see a char
            while (l1 >= 0) {
                if (s.charAt(l1) == '#') {
                    l1--;
                    l1_skip++;
                } else if(l1_skip > 0) {
                    l1--;
                    l1_skip--;
                } else {
                    break;
                }
            }

            while (l2 >= 0) {
                if (t.charAt(l2) == '#') {
                    l2--;
                    l2_skip++;
                } else if(l2_skip > 0) {
                    l2--;
                    l2_skip--;
                } else {
                    break;
                }
            }
            
            if(l1 >= 0 && l2 >= 0) {
                if(s.charAt(l1) != t.charAt(l2)) {
                    return false;
                }
            } else if((l1 >= 0 && l2 < 0) || (l1 < 0 && l2 >= 0)) {
                return false;
            }

            l1--;
            l2--;
        }

        return true;
    }
}