%len(i,o) (i,i)
%len(L:list, R:int)
len([],0).
len([_|T],R):- len(T,R1), R is R1+1.

%sumElems(i,o) (i,i)
%sumElems(L:list,R:int)
sumElems([],0).
sumElems([H|T],R):- sumElems(T,R1), R is R1+H.

%subsets(L:list,R:list)
%subsets(i,o)
subsets([],[]).
subsets([A|L],[A|S]):-subsets(L,S).
subsets([_|L],S):-subsets(L,S).


%checkCond(L:list)
%checkCond(i)
checkCond(L,N):-
    sumElems(L, S),
    S mod N =:=0.

%solve(i,o)
%solve(L:list,R:list)
solve(L,R):-
    subsets(L,R),
    len(L,N),
    checkCond(R,N).

%getAllSolutions(L:List,R:List)
%getAllSolutions(i,o)
getAllSolutions(L,R):-
    findall(AUX,solve(L,AUX),R).
