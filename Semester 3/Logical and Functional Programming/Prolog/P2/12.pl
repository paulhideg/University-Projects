insert_div(N, _, L, L) :- N =< 2.
insert_div(N, N, L, L):-!,
insert_div(N, Div, L, [Div|R]) :- N mod Div =:= 0, !,
    NDiv is Div + 1,
    !,
    insert_div(N, NDiv, L, R).
insert_div(N, Div, L, R) :-
    NDiv is Div + 1,
    insert_div(N, NDiv, L, R).

divizori([], []).
divizori([H|T], [H|R]) :-
    divizori(T, RD),
    insert_div(H, 2, RD, R).
