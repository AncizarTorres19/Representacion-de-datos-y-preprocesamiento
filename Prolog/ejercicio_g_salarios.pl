% Ejercicio g: Determinar entre dos personas quién gana más

% Base de datos de salarios
salario(juan, 2500000).
salario(maria, 3200000).
salario(pedro, 1800000).
salario(ana, 4500000).
salario(luis, 2800000).
salario(sofia, 3700000).

% Predicado que determina si una persona gana más que otra
gana_mas(Persona1, Persona2) :-
    salario(Persona1, Salario1),
    salario(Persona2, Salario2),
    Salario1 > Salario2.

% Predicado que encuentra quién gana más entre dos personas
quien_gana_mas(Persona1, Persona2, Persona1) :-
    gana_mas(Persona1, Persona2).

quien_gana_mas(Persona1, Persona2, Persona2) :-
    gana_mas(Persona2, Persona1).

% Predicado que compara salarios y da resultado detallado
comparar_salarios(Persona1, Persona2, Persona1, gana_mas, Diferencia) :-
    salario(Persona1, Salario1),
    salario(Persona2, Salario2),
    Salario1 > Salario2,
    Diferencia is Salario1 - Salario2.

comparar_salarios(Persona1, Persona2, Persona2, gana_mas, Diferencia) :-
    salario(Persona1, Salario1),
    salario(Persona2, Salario2),
    Salario2 > Salario1,
    Diferencia is Salario2 - Salario1.

comparar_salarios(Persona1, Persona2, igual, mismo_salario, 0) :-
    salario(Persona1, Salario),
    salario(Persona2, Salario).

% Predicado que encuentra la persona con mayor salario
mayor_salario(Persona) :-
    salario(Persona, Salario),
    \+ (salario(_, OtroSalario), OtroSalario > Salario).

% Ejemplos de uso:
% ?- gana_mas(maria, juan).                    % true (3200000 > 2500000)
% ?- quien_gana_mas(pedro, luis, X).           % X = luis
% ?- comparar_salarios(ana, sofia, X, Y, Z).   % X = ana, Y = gana_mas, Z = 800000
% ?- mayor_salario(X).                         % X = ana (mayor salario)