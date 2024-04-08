import java.util.*;

class Solution {
    public int solution(int[] nums) {
        HashMap<Integer, Integer> mon = new HashMap();
        
        for(int i=0; i<nums.length; i++) {
            if(mon.get(nums[i])==null) mon.put(nums[i], 1);
            else mon.put(nums[i], mon.get(nums[i])+1);
        }
        
        return Math.min(nums.length/2, mon.keySet().size());
    }
}