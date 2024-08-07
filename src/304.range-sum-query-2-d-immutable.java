/*
 * @lc app=leetcode id=304 lang=java
 *
 * [304] Range Sum Query 2D - Immutable
 */

// @lc code=start
class NumMatrix {
    int prefixSum[][];

    public NumMatrix(int[][] matrix) {
        int rows = matrix.length;
        int cols = matrix[0].length;
        this.prefixSum = new int[rows+1][cols+1];
        for(int i=1; i<=rows; i++) {
            for(int j=1; j<=cols; j++) {
                this.prefixSum[i][j] = this.prefixSum[i-1][j] + this.prefixSum[i][j-1] + matrix[i-1][j-1] - this.prefixSum[i-1][j-1];
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        return this.prefixSum[row2+1][col2+1] - this.prefixSum[row1][col2+1] - this.prefixSum[row2+1][col1] + this.prefixSum[row1][col1];         
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */
// @lc code=end

