insert([],_,_,_,[]):-!.
insert([],POS,N,EL,[EL]):-
    POS>=N,
    !.
insert([H|T],POS,N,EL,[EL,H|R]):-
    POS=:=N,
    !,
    POS1 is POS+1,
    insert(T,POS1,N,EL,R).
insert([H|T],POS,N,EL,[H|R]):-
    POS1 is POS+1,
    insert(T,POS1,N,EL,R).

%(i,i,o)
gcd(A,0,A).
gcd(A,B,R):- A>B, gcd(B,A,R).
gcd(A,B,R):- M is B mod A, gcd(A,M,R).

%(i,i,o)
gcd2([],A,A).
gcd2([H|T],AUX,R):- gcd(H,AUX,R2), gcd2(T,R2,R).


