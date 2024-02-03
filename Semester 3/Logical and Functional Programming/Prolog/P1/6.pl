count([],_,0).
count([H|T],EL,CNT):-
    H=:=EL,
    !,
    count(T,EL,CNT1),
    CNT is CNT1+1.
count([_|T],EL,CNT):-
    count(T,EL,CNT).


isSet([],[_|_]).
isSet([H|T],AUX):-
    count(AUX,H,CNT),
    CNT=:=1,
    !,
    isSet(T,AUX).

remove3Occurences([],_,_,[]).
remove3Occurences([H|T],EL,CNT,[H|R]):-
    H=:=EL,
    CNT>2,
    !,
    CNT1 is CNT+1,
    remove3Occurences(T,EL,CNT1,R).
remove3Occurences([H|T],EL,CNT,[H|R]):-
    H=\=EL,
    !,
    remove3Occurences(T,EL,CNT,R).
remove3Occurences([H|T],EL,CNT,R):-
    CNT1 is CNT+1,
    remove3Occurences(T,EL,CNT1,R).
