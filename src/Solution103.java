// import java.util.ArrayList;
// import java.util.LinkedList;
// import java.util.List;
// import java.util.Queue;
// import javafx.util.Pair;
// /**
//  * Definition for a binary tree node.
//  * public class TreeNode {
//  *     int val;
//  *     TreeNode left;
//  *     TreeNode right;
//  *     TreeNode() {}
//  *     TreeNode(int val) { this.val = val; }
//  *     TreeNode(int val, TreeNode left, TreeNode right) {
//  *         this.val = val;
//  *         this.left = left;
//  *         this.right = right;
//  *     }
//  * }
//  */
// class Solution103 {
//     public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
//         Queue<Pair<TreeNode, Integer>> q = new LinkedList<Pair<TreeNode, Integer>>();
//         List<List<Integer>> finalList = new ArrayList<>();
//         if(root == null) return finalList;
//         q.add(new Pair<TreeNode, Integer>(root, 0));
//         while(q.peek() != null) {
//             Pair<TreeNode, Integer> current = q.remove();
//             TreeNode node = current.getKey();
//             int level = current.getValue();
//             System.out.println(node.val + " " + level);
//             if(finalList.size() == level) {
//                 ArrayList<Integer> newList = new ArrayList<Integer>(node.val);
//                 finalList.add(newList);
//             } else {
//                 finalList.get(level).add(node.val);
//             }
//             TreeNode first = level%2 == 0?node.right:node.left;
//             TreeNode second = level%2 == 1?node.right:node.left;
//             if(first != null)
//                 q.add(new Pair<>(first, level + 1));
//             if(second != null)
//                 q.add(new Pair<>(second, level + 1));

//         }
//         return finalList;
//     }
// }