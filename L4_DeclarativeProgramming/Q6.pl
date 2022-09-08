directlyIn(irina, natasha).
directlyIn(natasha, olga).
directlyIn(olga, katarina).

contains(Y, X) :- directlyIn(X, Y).
contains(Y, X) :- directlyIn(X, Z), contains(Y, Z).