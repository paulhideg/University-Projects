%arangements of k from a given list

elim(E,[E|L],L).
elim(E,[A|X],[A|Y]):-
    elim(E,X,Y).

perm([],[]).
perm([E|L],T):-
    perm(L,R),
    elim(E,T,R).


