import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution15 {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> set = new ArrayList<List<Integer>>();
        int i=0;
        while(i< nums.length-2) {
            set.addAll(twoSum(nums, i+1, -1* nums[i]));
            do{
                i++;
            }while(i< nums.length-2 && nums[i] == nums[i-1]);
        }
        return set;
    }
    //{-1,0,1,2,-1,-4}
    //{-4,-1,-1,0,1,2}
    public ArrayList<ArrayList<Integer>> twoSum(int[] nums, int l, int target) {
        ArrayList<ArrayList<Integer>> a = new ArrayList<ArrayList<Integer>>();
        int r = nums.length -1;
        while(l<r) {
            int sum = nums[l] + nums[r];
            if(sum == target) {
                ArrayList<Integer> n = new ArrayList<Integer>();
                n.add(nums[l]); n.add(nums[r]);  n.add(-1*target);
                a.add(n);
                // System.out.println(target + " " + nums[l] + " " + nums[r]);
                do {
                    l++;   
                }while(l< r && nums[l]==nums[l-1]);
            } else if(sum < target) {
                do {
                    l++;   
                }while(l< r && nums[l]==nums[l-1]);
            } else {
                do {
                    r--;   
                }while(l< r && nums[r]==nums[r+1]);
            }
        }
        return a;
    }
    
    // public int[] twoSum(int[] nums, int start, int target) {
    //     HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    //     int a[] = new int[2];
    //     a[0] = -1; a[1] = -1;
    //     for(int i=start ; i<nums.length; i++)
    //         if(map.containsKey(target-nums[i])) {
    //             a[0] = i; a[1] = map.get(target-nums[i]);
    //         }
    //         else
    //             map.put(nums[i], i);
    //     return a;
    // }
}