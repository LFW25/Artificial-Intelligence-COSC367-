/*
Binary trees are trees where all internal nodes have exactly two children. The mirror of a binary tree is obtained by exchange all the left and right children.
The smallest binary trees consist of only one leaf node.

We will represent leaf nodes as leaf(Label) . For instance, leaf(1) and leaf(3) are leaf nodes, and therefore small binary trees.

Given two binary trees B1 and B2 we combine them into one binary tree by tree(B1,B2).So, from the leaves leaf(2) and leaf(3) we can build the binary tree tree(leaf(2),leaf(3)) . And from the binary trees leaf(1) and tree(leaf(2),leaf(3)) we can build the binary tree tree(leaf(1), tree(leaf(2), leaf(3))).

Define a predicate mirror/2 that succeeds when the two arguments are binary trees and are the mirror of each other.
*/

mirror(nil,nil).
mirror(t(_,L1,R1),t(_,L2,R2)) :- mirror(L1,R2), mirror(R1,L2).