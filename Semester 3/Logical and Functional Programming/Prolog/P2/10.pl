divisible(X,Y):- X mod Y =:= 0,!.
divisible(X,Y):- X>Y+1,
    Y1 is Y+1,
    divisible(X,Y1).

prime(2):-!.
prime(X):- X<2,!,
    false.
prime(X):-not(divisible(X,2)).


doublePrimes([],[]).
doublePrimes([H|T],[H,H|R]):-
    prime(H),
    !,
    doublePrimes(T,R).
doublePrimes([H|T],[H|R]):-
    doublePrimes(T,R).
