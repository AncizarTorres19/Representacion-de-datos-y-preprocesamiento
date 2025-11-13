% Ejercicio a: Determinar si una persona es mayor que otra

% Base de datos de edades de personas
edad(juan, 25).
edad(maria, 30).
edad(pedro, 20).
edad(ana, 35).
edad(luis, 28).

% Predicado que determina si una persona es mayor que otra
es_mayor(Persona1, Persona2) :-
    edad(Persona1, Edad1),
    edad(Persona2, Edad2),
    Edad1 > Edad2.

% Ejemplos de uso:
% ?- es_mayor(maria, juan).     % true (30 > 25)
% ?- es_mayor(pedro, ana).      % false (20 < 35)
% ?- es_mayor(luis, pedro).     % true (28 > 20)