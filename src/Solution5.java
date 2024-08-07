class Solution5 {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean isPal[][] = new boolean[n][n];
        for(int i=0;i<n;i++) {
            isPal[i][i] = true;
        }
        for(int i=0;i<n-1;i++) {
            isPal[i][i+1] = s.charAt(i) == s.charAt(i+1);
        }
        for(int i=n-2;i>=0;i--) {
            for(int j=i+2;j<n;j++) {
                isPal[i][j] = isPal[i+1][j-1] && (s.charAt(i) == s.charAt(j));
                System.out.println(i + " " + j + " " + isPal[i][j]);
            }
        }
        for(int i=0;i<n;i++) {
            for(int j=0;j<n;j++) {
                System.out.print(isPal[i][j] + " ");
            }
            System.out.println();
        }
        int length = 0;
        int iPos = -1, jPos = -1;
        for(int i=0;i<n;i++) {
            for(int j=n-1;j>=i;j--) {
                if(isPal[i][j] && (j-i+1)>length) {
                    length = j-i+1;
                    iPos = i;
                    jPos = j;
                }
            }
        }
        return s.substring(iPos, jPos+1);
    }
}