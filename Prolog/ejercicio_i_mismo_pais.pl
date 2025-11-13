% Ejercicio i: Verificar entre dos personas si viven en el mismo país

% Base de datos de residencias
% vive_en(Persona, Pais)
vive_en(juan, colombia).
vive_en(maria, argentina).
vive_en(pedro, colombia).
vive_en(ana, brasil).
vive_en(luis, colombia).
vive_en(sofia, argentina).
vive_en(carlos, mexico).
vive_en(elena, brasil).

% Predicado que verifica si dos personas viven en el mismo país
mismo_pais(Persona1, Persona2) :-
    vive_en(Persona1, Pais),
    vive_en(Persona2, Pais),
    Persona1 \= Persona2.

% Predicado que encuentra el país donde viven ambas personas
pais_comun(Persona1, Persona2, Pais) :-
    vive_en(Persona1, Pais),
    vive_en(Persona2, Pais),
    Persona1 \= Persona2.

% Predicado que compara residencias
comparar_residencia(Persona1, Persona2, mismo_pais, Pais) :-
    vive_en(Persona1, Pais),
    vive_en(Persona2, Pais),
    Persona1 \= Persona2.

comparar_residencia(Persona1, Persona2, diferente_pais, [Pais1, Pais2]) :-
    vive_en(Persona1, Pais1),
    vive_en(Persona2, Pais2),
    Pais1 \= Pais2.

% Predicado que encuentra todos los compatriotas de una persona
compatriotas(Persona, Compatriota) :-
    vive_en(Persona, Pais),
    vive_en(Compatriota, Pais),
    Persona \= Compatriota.

% Predicado que cuenta cuántas personas viven en un país
habitantes_pais(Pais, Lista) :-
    findall(Persona, vive_en(Persona, Pais), Lista).

% Predicado que verifica si una persona es vecino (mismo país) de otra
son_vecinos(Persona1, Persona2) :-
    mismo_pais(Persona1, Persona2).

% Ejemplos de uso:
% ?- mismo_pais(juan, pedro).                  % true (ambos en colombia)
% ?- mismo_pais(maria, ana).                   % false (diferentes países)
% ?- pais_comun(juan, luis, X).                % X = colombia
% ?- comparar_residencia(sofia, maria, X, Y).  % X = mismo_pais, Y = argentina
% ?- compatriotas(juan, X).                    % X = pedro; X = luis
% ?- habitantes_pais(colombia, X).             % X = [juan, pedro, luis]