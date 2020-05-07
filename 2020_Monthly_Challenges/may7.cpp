// In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
// Two nodes of a binary tree are cousins if they have the same depth, but have different parents.
// We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.
// Return true if and only if the nodes corresponding to the values x and y are cousins.
//  
// Note: 
// The number of nodes in the tree will be between 2 and 100.
// Each node has a unique integer value from 1 to 100.

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int x_depth = -1; 
    int y_depth = -1; 
    int x_parent = -1;
    int y_parent = -1;

    bool isCousins(TreeNode* root, int x, int y) {
        isCousinsHelper(root, -1, x, y, 0);
        return (x_depth == y_depth && x_parent != y_parent);
    }

    void isCousinsHelper(TreeNode* node, int parent, int x, int y, int k_depth){
        if(!node) return; 

        if(node->val == x){
            x_depth = k_depth;
            x_parent = parent;
        } else if(node->val == y){
            y_depth = k_depth;
            y_parent = parent;
        }

        isCousinsHelper(node->left, node->val, x, y, k_depth+1);
        isCousinsHelper(node->right, node->val, x, y, k_depth+1);
    }
};
