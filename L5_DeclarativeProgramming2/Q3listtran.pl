/*
Suppose we are given a knowledge base with facts about the translation of words between Language1 and Language2. The following is an example of translation of numbers between te reo Maori and English:

tran(tahi,one). 
tran(rua,two). 
tran(toru,three). 
tran(wha,four). 
tran(rima,five). 
tran(ono,six). 
tran(whitu,seven). 
tran(waru,eight). 
tran(iwa,nine).
Write a predicate listtran(?List1, ?List2) which translates a list of words in Language1 to/from the corresponding list of words in Language2. For example, for the facts given above:

listtran([tahi,iwa,rua],X).
should give:
X = [one, nine, two].
*/

listtran([], []).
listtran(L1, L2) :- [H1|T1] = L1, [H2|T2] = L2, tran(H1, H2), listtran(T1, T2).