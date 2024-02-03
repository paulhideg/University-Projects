% Decompose a list into a list following the structure:
% [[list of even numbers],[list of odd numbers], number of even numbers,
% number of odd numbers].

% decompose(L:list, R:list)
% decompose(i, o)

decompose([], [[], [], 0, 0]).
decompose([H|T], [[H|EVEN], ODD, EVENCOUNT, ODDCOUNT]) :-
    H mod 2 =:= 0, % in this case we perform a recursive call in which we increment the even no count, and also add to the head to the start of the    even list.
    decompose(T, [EVEN, ODD, EVENCOUNT1, ODDCOUNT]),
    EVENCOUNT is EVENCOUNT1 + 1.
decompose([H|T], [EVEN, [H|ODD], EVENCOUNT, ODDCOUNT]) :-
    H mod 2 =:= 1, % the same, but with odd.
    decompose(T, [EVEN, ODD, EVENCOUNT, ODDCOUNT1]),
    ODDCOUNT is ODDCOUNT1 + 1.

