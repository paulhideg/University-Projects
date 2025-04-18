successor([], _, []) :- !.
successor([0], 1, [1]) :- !.
successor([N], 0, [NR]) :- NR is N + 1, !.
successor([9|T], 1, [0|R]) :-
    successor(T, 1, R), !.
successor([H|T], 0, [HR|R]) :-
    successor(T, C, R),
    HR is H + C.

