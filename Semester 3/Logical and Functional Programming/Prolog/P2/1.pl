append2([],R,[R]).
append2([H|R],R2,[H|T]):-
    append2(R,R2,T).

len([],0).
len([_|T],R):- len(T,R1), R is R1+1.

merge(A,[],A):-!.
merge([],B,B):-!.
merge([A|T1],[B|T2],[A|R]):-
    A<B,
    !,
    merge(T1,[B|T2],R).
merge([A|T1],[B|T2],[B|R]):-
    A>B,
    !,
    merge([A|T1],T2,R).
merge([A|T1],[B|T2],R):-
    A=:=B,
    merge([A|T1],T2,R).


merge_sort([],[]).
merge_sort([A],[A]).
merge_sort(L,R):-
    split(L,Left,Right),
    merge_sort(Left,RL),
    merge_sort(Right,RR),
    merge(RL,RR,R).

split(L, LC, LC, L) :-
    len(L, RL),
    len(LC, RLC),
    Diff is RLC - RL,
    abs(Diff, AUX),
    AUX =< 1.
split([H|T], LC, Left, Right) :-
    append2(LC, H, RA),
    split(T, RA, Left, Right).

split(L, Left, Right):- split(L,[], Left, Right).

sortNoKeep(L,R):-
    merge_sort(L,R).
