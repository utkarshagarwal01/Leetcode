import java.util.Arrays;

class Solution1013 {
    public boolean canThreePartsEqualSum(int[] arr) {
        int sum = Arrays.stream(arr).sum(), i=0, len = arr.length, count = 0, countNum = 0;
        if(sum%3!=0) return false;
        sum /=3;
        while(i<len) {
            count += arr[i++];
            if(count == sum) {
                countNum++;
                count = 0;
            }
        }
        return (countNum == 3 && count == 0) || (sum == 0 && countNum >3 && count == 0);
    }
}