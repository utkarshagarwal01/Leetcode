class SolutionDEShaw {
    public int compute(int leafs) {
        if(leafs == 1)
            return 1;
        int sum = 0;
        for (int i=1;i<=leafs/2;i++) {
            sum += compute(leafs-i)*compute(i);
        }
        return sum;
    }
}