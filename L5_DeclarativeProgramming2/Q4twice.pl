/*
Write a predicate twice(?In, ?Out) whose left argument is a list, and whose right argument is a list consisting of every element in the left list repeated twice.
For example, the query:
    twice([a,4,buggle],X).
gives
    X = [a,a,4,4,buggle,buggle].
and the query
    twice(X, [1, 1, 2, 2]).
gives
    X = [1,2].
and the query
    twice(X, [a, a, b, b, c]).
fails.
*/

twice([], []).
twice(Input, Output) :- [H1|InTail] = Input, [H1|T] = Output, [H1|OutTail] = T, twice(InTail, OutTail).