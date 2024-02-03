insert([],_,_,[]).
insert([H|T], E, I, [H,E|R]):-
    (I=:=1;I=:=3;I=:=7;I=:=15),!,
    I1 is I+1,
    insert(T,E,I1,R).
insert([H|T],E,I,[H|R]):-
    I1 is I+1,
    insert(T,E,I1,R).
