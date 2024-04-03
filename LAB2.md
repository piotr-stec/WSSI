### ZAD 1.1
- A) X jest rodzeństwem Y
- B) X jest kuzynem Y
- C) swat/swatka
- D) y jest ojczymem/macochą dla x
- E) rodzeństwo przyrodnie
- F) szwagier/szwagierka
- G) rodzeństwo przyrodnie
### ZAD 1.2
- A) rodzeństwo
  ```
  relacjarodzenstwo(X,Y) :-
    rodzic(X,Z),
    rodzic(X,H),
    rodzic(Y,H),
    rodzic(Y,Z),
    X\=Y.
  ```
- B) kuzynostwo
  ```
  kuzyn(X,Y) :-
    rodzic(X,Z),
    rodzic(Z,H),
    rodzic(Y,D),
    rodzic(D,H).
  ```
- C) swat/swatka
  ```
  swat(X,Y) :-
    rodzic(H,B),
    rodzic(H,C),
    rodzic(B,X),
    rodzic(C,Y).
  ```

- D) macocha
  ```
  macocha(X,Y) :-
    rodzic(X,D),
    rodzic(H,D),
    rodzic(H,Y).
  ```

- E) przyrodnie rodzeństwo
  ```
  przyrodnierodzenstwo(X,Y) :-
    rodzic(X,H),
    rodzic(X,I),
    rodzic(Y,I),
    rodzic(Y,J).
  ```
  
- F) szwagier/szwagierka
    ```
    szwagier(X,Y) :-
      rodzic(H,X),
      rodzic(H,B),
      rodzic(B,J),
      rodzic(Y,J).
    ```

- G) przyrodnie rodzeństwo(możliwe kazirodztwo)
    ```
    przyrodnierodzenstwoG(X,Y) :-
      rodzic(Y,H),
      rodzic(Y,I),
      rodzic(X,I),
      rodzic(X,J),
      rodzic(H,J).
    ```
### ZAD 2
```
kobieta(X) :-
    \+mezczyzna(X).

ojciec(X,Y) :-
    rodzic(Y,X),
    mezczyzna(X).

matka(X,Y) :-
    rodzic(Y,X),
    kobieta(X).

corka(X,Y) :-
    rodzic(X,Y),
    kobieta(X).

brat_rodzony(X,Y) :-
    rodzic(X,H),
    rodzic(X,J),
    rodzic(Y,H),
    rodzic(Y,J),
    mezczyzna(X).

brat_przyrodni(X,Y) :-
    rodzic(X,H),
    rodzic(X,J),
    rodzic(Y,H),
    rodzic(Y,I),
    mezczyzna(X).

kuzyn(X,Y) :-
    rodzic(X,H),
    rodzic(H,J),
    rodzic(Y,I),
    rodzic(I,J).

dziadek_od_strony_ojca(X,Y) :-
    ojciec(H,Y),
    ojciec(X,H).

dziadek_od_strony_matki(X,Y) :-
	matka(H,Y),
    ojciec(Y,H).

dziadek(X,Y) :-
    rodzic(Y,H),
    ojciec(X,H).

babcia(X,Y) :-
    rodzic(Y,H),
    matka(X,H).

wnuczka(X,Y) :-
    rodzic(Y,H),
    rodzic(H,X),
    kobieta(Y).
   
przodek_do2pokolenia_wstecz(X,Y) :-
    rodzic(Y,H),
    rodzic(H,X).

przodek_do3pokolenia_wstecz(X,Y) :-
    rodzic(Y,H),
    rodzic(J,H),
    rodzic(H,X).
```

  
  
