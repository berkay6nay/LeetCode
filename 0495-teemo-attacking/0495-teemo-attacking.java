class Solution {
    public int findPoisonedDuration(int[] timeSeries, int duration) {
        int total_dur = 0 ;
        for(int i = 0; i < timeSeries.length - 1; ++i){
            if(timeSeries[i] + duration <= timeSeries[i + 1]){
                total_dur += duration;
            }
            if(timeSeries[i] + duration > timeSeries[i + 1]){
                total_dur = total_dur + timeSeries[i + 1] - timeSeries[i]; 
            }
        }
        total_dur += duration;
        return total_dur;
        
            
    }
}