class Solution {
    public List<String> fizzBuzz(int n) {
        
    List<String> empty_list = new ArrayList<>();
    
    for(int i = 1 ; i <= n ; ++i){
        String flag = "";
        if(i % 3 == 0) flag += "Fizz";
        if(i % 5 == 0) flag += "Buzz";
        if(i % 5 != 0 && i % 3 != 0) flag += String.valueOf(i);
        empty_list.add(flag);
    }
        
        return empty_list;
        
        
        
    }
}