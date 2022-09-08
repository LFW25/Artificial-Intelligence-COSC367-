/*
Write a predicate remove(+X, +ListIn, ?ListOut) that succeeds if ListOut can be obtained by removing all instances of X from ListIn. Note that the first two arguments will always be bound (given as input)
*/

remove(X, [], []).
remove(X, [X|List1], List2) :- remove(X, List1, List2). /* If the removable element heads the given list, remove it and recurse */
remove(X, [Y|List1], [Y|List2]) :- Y \= X, remove(X, List1, List2). /* If both lists start with the same element and that element is not the removable element, recurse without that shared head element */

