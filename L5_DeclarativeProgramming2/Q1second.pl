/* Write a predicate second(?List,?X) which succeeds when X is the second element of List. */

/*
The definition implies that the predicate should fail if the list has fewer than two elements.
The notation implies, either of the arguments can be instantiated (input) or unbound (output).
In some test cases, you see the symbol \+ which means negation. For example, the goal \+ second([1], X) will succeed if second([1], X) fails.
*/

second([H|[X|T]], X).