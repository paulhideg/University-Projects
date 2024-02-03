removeConsec([],[]).
removeConsec([A],[A]):-!.
removeConsec([A,B],[]):- B =:= A + 1,!.
removeConsec([A,B],[A,B]):- B =\= A + 1,!.
removeConsec([A,B,C|T],R):-
    B =:= A + 1,
    C =:= B+1,
    !,
    removeConsec([B,C|T],R).
removeConsec([A,B,C|T],R):-
    B =:= A + 1,
    C =\= B + 1,
    !,
    removeConsec([C|T],R).
removeConsec([A,B,C|T],[A|R]):-
    B =\= A+1,
    removeConsec([B,C|T],R).
