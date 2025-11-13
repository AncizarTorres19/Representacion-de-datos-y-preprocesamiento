% Ejercicio b: Determinar si un número es par o impar

% Predicado que determina si un número es par
es_par(Numero) :-
    0 is Numero mod 2.

% Predicado que determina si un número es impar
es_impar(Numero) :-
    1 is Numero mod 2.

% Predicado general que clasifica un número
clasificar_numero(Numero, par) :-
    es_par(Numero).

clasificar_numero(Numero, impar) :-
    es_impar(Numero).

% Ejemplos de uso:
% ?- es_par(4).                    % true
% ?- es_par(7).                    % false
% ?- es_impar(3).                  % true
% ?- es_impar(8).                  % false
% ?- clasificar_numero(10, X).     % X = par
% ?- clasificar_numero(15, X).     % X = impar