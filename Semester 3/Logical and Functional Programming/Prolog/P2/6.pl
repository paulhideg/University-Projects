toNumber([],R,R).
toNumber([H|T],P,R):-
    P1 is P*10+H,
    toNumber(T,P1,R).

len([],0).
len([_|T],R):- len(T,R1), R is R1+1.

append2([],E,[E]).
append2([H|T],E,[H|R]):-
    append2(T,E,R).

rev_list([],[]).
rev_list([H|T],R):-
    rev_list(T,R1),
    append2(R1,H,R).

splitAux(0,[]):-!.
splitAux(N,[A|R]):-
    N1 is floor(N/10),
    A is N mod 10,
    splitAux(N1,R).

split(N,L):-
    splitAux(N,L1),
    rev_list(L1,L).

multiply([0],_,[0]):-!.
multiply(L,NR,R):-
    toNumber(L,0,AUX1),
    R1 is AUX1*NR,
    split(R1,R).

