/*
Write a predicate swap12(?List1, ?List2) which succeeds when List1 is identical to List2, except that the first two elements are exchanged. The predicate must fail on lists with fewer than two elements. Note that either of the arguments can be bound or unbound (input or output).
*/

swap12([A|[B|T]], [B|[A|T]]).