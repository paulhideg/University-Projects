

append2([],E,[E]).
append2([H|T],E,[H|R]):-
    append2(T,E,R).

appendList([],L,L).
appendList([H|T],L,[H|R]):-
    appendList(T,L,R).

subst([],_,[_|_],[]).
subst([H|T],E,L,R):-
    H=:=E,
    !,
    appendList(L,T,AUX),
    subst(AUX,E,L,R).
subst([H|T],E,L,[H|R]):-
    subst(T,E,L,R).
