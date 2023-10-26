void reverseString(char* s, int sSize){

    
    int start = 0;
    int end = sSize - 1;
    int middle = (start + end)/2;
    
    while(start <= middle){
        char s_char = s[start];
        char e_char = s[end];
        
        s[start] = e_char;
        s[end] = s_char;
        
        ++start;
        --end;
        
    }
    
    
}