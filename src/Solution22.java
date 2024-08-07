import java.util.ArrayList;
import java.util.List;

class Solution22 {

    public void recurse(List<String> result, String s, int open, int close, int n) {
        if(s.length() == 2*n) {
            result.add(s);
        } else {
            if(open < n) {
                String s2 = s + "(";
                recurse(result, s2, open+1, close, n);
            }
            if(close<open) {
                String s1 = s+")";
                recurse(result, s1, open, close+1, n);
            }
        }
    }

    public List<String> generateParenthesis(int n) {
        List<String> result= new ArrayList<String>();

        recurse(result, "", 0, 0, n);

        // for(String s : result) {
        //     System.out.println(s);
        // }
        return result;
    }
}