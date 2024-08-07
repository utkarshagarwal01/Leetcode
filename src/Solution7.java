class Solution7 {
    public int reverse(int x) {
        int max = Integer.MAX_VALUE;
        max++;
        System.out.println(max);
        max++;
        System.out.println(max);
        max++;
        System.out.println(max);

        boolean negative = x<0;
        if(negative) x*=-1;
        int n = x, s = 0;
        while(n != 0) {
            int a = n%10;
            if (s > Integer.MAX_VALUE/10 || (s == Integer.MAX_VALUE / 10 && a > 7)) return 0;
            if (s < Integer.MIN_VALUE/10 || (s == Integer.MIN_VALUE / 10 && a < -8)) return 0;
            s = s*10 + a;
            n = n/10;
        }
        if(negative) s *= -1;
        return s;
    }
}