replace([],_,_,[]).
replace([H|T],OLD,NEW,[NEW|R]):-
    H=:=OLD,
    !,
    replace(T,OLD,NEW,R).
replace([H|T],OLD,NEW,[H|R]):-
    replace(T,OLD,NEW,R).
