class Solution {
    public boolean isPalindrome(int x) {
        String num = Integer.toString(x);
        String empty = "";
        for(int i = num.length() - 1; i >= 0 ; --i ){
            Character chur_char = num.charAt(i);
            empty += chur_char;
        }
        if(num.equals(empty)) return true;
        else return false;
    }
}