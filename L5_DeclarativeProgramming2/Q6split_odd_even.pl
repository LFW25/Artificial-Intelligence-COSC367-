/*
Write a predicate split_odd_even(+ListIn, ?ListA, ?ListB) whose first argument is a list, and whose second and third arguments are the odd and even indexed elements in that list respectively. Assume the first element of a list is indexed 1.
*/

split_odd_even([], [], []).
split_odd_even([X], [X], []).
split_odd_even([Y|[Z|ListIn]], [Y|ListA], [Z|ListB]) :- split_odd_even(ListIn, ListA, ListB).