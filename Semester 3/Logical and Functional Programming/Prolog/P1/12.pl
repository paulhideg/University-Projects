removeNth([],_,_,[]).
removeNth([H|T],POS,N,[H|R]):-
    N=\=POS,
    !,
    POS1 is POS+1,
    removeNth(T,POS1,N,R).
removeNth([_|T],POS,N,R):-
    POS1 is POS+1,
    removeNth(T,POS1,N,R).


remove(A,N,R):-
    removeNth(A,1,N,R).

append(R,R,[]).
append([H|R],R2,[H|T]):-
    append(R,R2,T).

substitute([],_,[_|_],[]).
substitute([H|T],EL,L,R):-
    H=:=EL,
    append(R,R2,L),
    !,
    substitute(T,EL,L,R2).
substitute([H|T],EL,L,[H|R]):-
    substitute(T,EL,L,R).




