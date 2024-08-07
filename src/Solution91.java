class Solution91 {
    static int count = 0, n=0;
    public void recurse(String s, int i) {
        if(i==n)
            count++;
        else {
            if(i<n-1) {
                char first = s.charAt(i), second = s.charAt(i+1);
                int n = (first-'0')*10+(second-'0');
                if(n<=26 && first!='0') {
                    recurse(s, i+2);
                } 
            }
            if(i<n) {
                char first = s.charAt(i);
                if(first != '0')
                    recurse(s,i+1);
            }
        }
    }
    
    public int numDecodings(String s) {
        n = s.length();
        recurse(s,0);
        return count;
    }

    public int numDecodingsDP(String s) {
        int dp1=1, dp2=0, n=s.length();
        for(int i=n-1;i>=0;i--) {
            int dp=s.charAt(i)=='0'?0:dp1;
            if(i<n-1&&(s.charAt(i)=='1'||s.charAt(i)=='2'&&s.charAt(i+1)<'7'))
                dp+=dp2;
            dp2=dp1;
            dp1=dp;
        }
        return dp1;
    }
}