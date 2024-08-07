import java.util.HashMap;

public class Q13 {
    public static void main(String []args) {
        HashMap<Character, Integer> values = new HashMap<Character, Integer>();
        values.put('I', 1);
        values.put('V', 5);
        values.put('X', 10);
        values.put('L', 50);
        values.put('C', 100);
        values.put('D', 500);
        values.put('M', 1000);
        String s = "MCMXCIV"; int length = s.length();
        int result = 0;
        for(int i=length-1; i>=0; i--) {
            char c = s.charAt(i);
            char right = i+1 == length?'\0':s.charAt(i+1);
            if((c == 'I' && (right == 'V' || right == 'X'))
            || (c == 'X' && (right == 'L' || right == 'C'))
            || (c == 'C' && (right == 'D' || right == 'M')))
                result -= values.get(c);
            else
                result += values.get(c);
        }
        System.out.println(result);
        return;
    }
}
