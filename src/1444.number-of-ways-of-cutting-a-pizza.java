/*
 * @lc app=leetcode id=1444 lang=java
 *
 * [1444] Number of Ways of Cutting a Pizza
 */

// @lc code=start
class Solution {
    int prefixSum[][];
    int M = 1000000000 + 7;
    int dp[][][];
    public boolean pieceHasApple(int row1, int col1, int row2, int col2) {
        row1 += 1;
        row2 += 1;
        col1 += 1;
        col2 += 1;
        return (prefixSum[row2][col2] - prefixSum[row1-1][col2] - prefixSum[row2][col1-1] + prefixSum[row1-1][col1-1]) > 0;         
    }

    public void generatePrefixSum(String[] pizza) {
        int rows = pizza.length, cols = pizza[0].length();
        prefixSum = new int[rows+1][cols+1];
        for(int i=1; i<=rows; i++) {
            for(int j=1; j<=cols; j++) {
                prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + (pizza[i-1].charAt(j-1) == 'A'?1:0);
            }
        }
    }

    public int ways(String[] pizza, int k) {
        int rows = pizza.length;
        int cols = pizza[0].length();
        this.generatePrefixSum(pizza);
        long [][][] dp = new long[rows][cols][k];
        int ways = (int)(solve(0, 0, rows , cols, k-1, dp) % M);

        return ways;
    }

    public long solve(int i, int j, int rows, int cols, int cuts, long [][][] dp) {
        boolean remainingPieceHasApple = pieceHasApple(i, j, rows-1, cols-1);
        if(cuts == 0 && remainingPieceHasApple) {
            return 1;
        }

        if(dp[i][j][cuts] != 0) {
            return dp[i][j][cuts];
        }

        long ways = 0;
        for(int k=i; k< rows-1; k++) {
            boolean cutPieceHasApple = pieceHasApple(i, j, k, cols-1);
            remainingPieceHasApple = pieceHasApple(k+1, j, rows-1, cols-1);
            if(cutPieceHasApple && remainingPieceHasApple) {
                ways = (ways + solve(k+1, j, rows, cols, cuts-1, dp)) % M; 
            }
        }

        for(int l=j; l< cols-1; l++) {
            boolean cutPieceHasApple = pieceHasApple(i, j, rows-1, l);
            remainingPieceHasApple = pieceHasApple(i, l+1, rows-1, cols-1);
            if(cutPieceHasApple && remainingPieceHasApple) {
                ways = (ways + solve(i, l+1, rows, cols, cuts-1, dp)) % M; 
            }
        }

        dp[i][j][cuts] = ways;

        // for( int )

        return ways;
    }
}
// @lc code=end

//641829390