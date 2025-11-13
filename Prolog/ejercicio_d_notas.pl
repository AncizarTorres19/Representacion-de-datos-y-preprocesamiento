% Ejercicio d: Clasificar una nota como aprobada o reprobada

% Predicado que determina si una nota está aprobada (>= 3.0)
aprobada(Nota) :-
    Nota >= 3.0.

% Predicado que determina si una nota está reprobada (< 3.0)
reprobada(Nota) :-
    Nota < 3.0.

% Predicado general que clasifica la nota
clasificar_nota(Nota, aprobada) :-
    Nota >= 3.0.

clasificar_nota(Nota, reprobada) :-
    Nota < 3.0.

% Predicado con clasificación más detallada
clasificacion_detallada(Nota, excelente) :-
    Nota >= 4.5.

clasificacion_detallada(Nota, buena) :-
    Nota >= 4.0,
    Nota < 4.5.

clasificacion_detallada(Nota, aceptable) :-
    Nota >= 3.0,
    Nota < 4.0.

clasificacion_detallada(Nota, reprobada) :-
    Nota < 3.0.

% Ejemplos de uso:
% ?- aprobada(3.5).                    % true
% ?- reprobada(2.8).                   % true
% ?- clasificar_nota(4.2, X).          % X = aprobada
% ?- clasificar_nota(2.5, X).          % X = reprobada
% ?- clasificacion_detallada(4.8, X).  % X = excelente
% ?- clasificacion_detallada(3.7, X).  % X = aceptable