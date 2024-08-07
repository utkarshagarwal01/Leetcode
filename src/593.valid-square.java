/*
 * @lc app=leetcode id=593 lang=java
 *
 * [593] Valid Square
 */

// @lc code=start

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public double euclideanDistance(int x1, int y1, int x2, int y2) {
        double squaredSum = Math.pow(x1 - x2, 2) +  Math.pow(y1 - y2, 2);

        return squaredSum;
    }


    
    public boolean validSquare(int[] p1, int[] p2, int[] p3, int[] p4) {
        List<int[]> coordinates = new ArrayList<int[]>();
        coordinates.add(p1);
        coordinates.add(p2);
        coordinates.add(p3);
        coordinates.add(p4);
        
        List<Double> distances = new ArrayList<Double>(); 
        for (int i=0; i<4; i++) {
            for (int j=i+1; j<4; j++) {
                distances.add(euclideanDistance(coordinates.get(i)[0], coordinates.get(i)[1], coordinates.get(j)[0], coordinates.get(j)[1]));
            }
        }
        
        Collections.sort(distances);
        // for (Double double1 : distances) {
        //     System.out.println(double1);
        // }

        if (distances.get(0) == 0) {
            return false;
        } else if (Double.compare(distances.get(0), distances.get(1)) == 0 &&
                    Double.compare(distances.get(1), distances.get(2)) == 0 &&
                    Double.compare(distances.get(2), distances.get(3)) == 0 &&
                    Double.compare(distances.get(4), distances.get(5)) == 0) {
            return true;
        }

        return false;
    }

    // public static void main(String[] args) {
    //     Solution sol = new Solution();

    //     int[] p1 = {0, 0};
    //     int[] p2 = {1, 1};
    //     int[] p3 = {1, 0};
    //     int[] p4 = {0, 1};
    //     System.out.println(sol.validSquare(p1, p2, p3, p4));  // Output: true
    // }
}
// @lc code=end

