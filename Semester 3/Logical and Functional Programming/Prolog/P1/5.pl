%search(i,o)
search([H|_],EL):-
    H=:=EL,!.
search([_|T],EL):-
    search(T,EL).

setPairs([],[_|_],[]).
setPairs([H|T],AUX,R):-
    H = [A,B|_],
    search(A,AUX),
    !,
    R1 is [A|R],
    AUX1 is [A|AUX],
    search(B,AUX),
    !,
    R2 is [B|R1],
    AUX2 is [B|AUX1],
    setPairs(T,AUX2,R2).
setPairs([H|T],[H|AUX],R):-
    setPairs(T,AUX,R).


copy([],[]).
copy([H|T],[H|R]):-
    copy(T,R).

copyWithSearch([],[_|_],[]).
copyWithSearch([H|T],[H|AUX],[H|R]):-
    not(search(AUX,H)),
    !,
    copyWithSearch(T,AUX,R).


union([],[],[]).
union(A,[],A):-!.
union([],B,B):-!.
union(A,B,R):-
    copy(A,R),
    AUX = R,
    copyWithSearch(B,AUX,R).

