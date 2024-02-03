create(M,N,[]):-
    M>N,
    !.
create(M,N,[M|R]):-
    M1 is M+1,
    create(M1,N,R).


%search(i,o)
search([H|_],EL):-
    H=:=EL,!.
search([_|T],EL):-
    search(T,EL).

intersection([],[],[]).
intersection([],B,[]):-!.
intersection(A,[],[]):-!.
intersection([H|T],B,[H|R]):-
    search(B,H),
    !,
    intersection(T,B,R).
intersection([_|T],B,R):-
    intersection(T,B,R).

