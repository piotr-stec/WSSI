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

  
  
