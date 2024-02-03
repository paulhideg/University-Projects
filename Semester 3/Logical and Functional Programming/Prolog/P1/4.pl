addOne([],_,[]):-!.
addOne([H|T],E,[H,E|R]):-
    H mod 2 =:= 1,
    !,
    addOne(T,E,R).
addOne([H|T],E,[H|R]):-
    addOne(T,E,R).

%search(i,o)
search([H|_],EL):-
    H=:=EL,!.
search([_|T],EL):-
    search(T,EL).

%diference = all the elems that are in A but are not in B
diff([],[_|_],[]).
diff([H|T],B,[H|R]):-
    not(search(B,H)),
    !,
    diff(T,B,R).
diff([_|T],B,R):-
    diff(T,B,R).
