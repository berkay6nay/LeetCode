class Solution {
    public int strStr(String haystack, String needle) {
        Integer needle_length = needle.length();
        for(int i = 0 ; i < haystack.length() - needle_length + 1 ; ++i){
            if(needle.charAt(0) == haystack.charAt(i)){
                String cur_string = haystack.substring(i , i + needle_length);
                if(cur_string.equals(needle)) return i;
            }
        }
        return -1;
    }
}