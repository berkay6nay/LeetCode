int maxProfit(int* prices, int pricesSize){
    
    int l = 0;
    int r = 1;
    int profit = 0;
    
    while(r < pricesSize){
        if(prices[l] < prices[r]){
            if(prices[r] - prices[l] > profit) profit = prices[r] - prices[l];
        }
        else{
            l = r;
        }
        r = r + 1;
    }
    
    return profit;
    

}