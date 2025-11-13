% Ejercicio f: Verificar si una persona es abuelo de otra

% Base de datos de relaciones familiares
% padre(Padre, Hijo)
padre(carlos, juan).
padre(carlos, maria).
padre(juan, pedro).
padre(juan, ana).
padre(luis, sofia).
padre(miguel, carlos).
padre(roberto, luis).

% madre(Madre, Hijo)
madre(elena, juan).
madre(elena, maria).
madre(carmen, pedro).
madre(carmen, ana).
madre(rosa, sofia).
madre(teresa, carlos).
madre(patricia, luis).

% Predicado que define la relación padre/madre (progenitor)
progenitor(X, Y) :- padre(X, Y).
progenitor(X, Y) :- madre(X, Y).

% Predicado que determina si X es abuelo de Z
abuelo(X, Z) :-
    padre(X, Y),
    progenitor(Y, Z).

% Predicado que determina si X es abuela de Z
abuela(X, Z) :-
    madre(X, Y),
    progenitor(Y, Z).

% Predicado general que determina si X es abuelo/a de Z
es_abuelo_de(X, Z) :-
    abuelo(X, Z).

es_abuelo_de(X, Z) :-
    abuela(X, Z).

% Predicado que encuentra todos los nietos de una persona
nietos(Abuelo, Nieto) :-
    es_abuelo_de(Abuelo, Nieto).

% Ejemplos de uso:
% ?- abuelo(miguel, juan).             % true (miguel es abuelo de juan)
% ?- abuelo(carlos, pedro).            % true (carlos es abuelo de pedro)
% ?- es_abuelo_de(teresa, ana).        % true (teresa es abuela de ana)
% ?- nietos(carlos, X).                % X = pedro; X = ana (nietos de carlos)
% ?- es_abuelo_de(X, pedro).           % X = carlos; X = teresa (abuelos de pedro)