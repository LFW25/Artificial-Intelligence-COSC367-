/*
Write a predicate preorder(+Tree, Traversal) that determines the preorder traversal of a given binary tree. Each tree/subtree is either a leaf or of the form tree(root, left_subtree, right_subtree). A preorder traversal records the current node, then the left branch, then the right branch.
*/

preorder(leaf(X), [X]).
preorder(tree(Node, LeftBranch, RightBranch), [Node|GoRight]) :- append(Tree1, Tree2, GoRight), preorder(LeftBranch, Tree1), preorder(RightBranch, Tree2).