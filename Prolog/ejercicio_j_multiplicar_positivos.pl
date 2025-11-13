% Ejercicio j: Si el número es positivo, multiplicarlo por 2, de lo contrario dejarlo igual

% Predicado que procesa un número según la regla
procesar_numero(Numero, Resultado) :-
    Numero > 0,
    Resultado is Numero * 2.

procesar_numero(Numero, Numero) :-
    Numero =< 0.

% Predicado que explica la operación realizada
procesar_con_explicacion(Numero, Resultado, multiplicado_por_2) :-
    Numero > 0,
    Resultado is Numero * 2.

procesar_con_explicacion(Numero, Numero, sin_cambio) :-
    Numero =< 0.

% Predicado que verifica si un número es positivo
es_positivo_num(Numero) :-
    Numero > 0.

% Predicado que aplica la regla con diferentes casos
aplicar_regla(Numero, Resultado, Caso) :-
    (   Numero > 0 ->
        Resultado is Numero * 2,
        Caso = positivo_multiplicado
    ;   Numero =:= 0 ->
        Resultado = 0,
        Caso = cero_sin_cambio
    ;   Numero < 0 ->
        Resultado = Numero,
        Caso = negativo_sin_cambio
    ).

% Predicado que procesa una lista de números
procesar_lista([], []).
procesar_lista([H|T], [H2|T2]) :-
    procesar_numero(H, H2),
    procesar_lista(T, T2).

% Predicado para mostrar el proceso paso a paso
mostrar_proceso(Numero, Original, Resultado, Operacion) :-
    Original = Numero,
    (   Numero > 0 ->
        Resultado is Numero * 2,
        Operacion = 'multiplicado por 2'
    ;   Resultado = Numero,
        Operacion = 'sin cambio'
    ).

% Ejemplos de uso:
% ?- procesar_numero(5, X).                    % X = 10 (positivo, se multiplica)
% ?- procesar_numero(-3, X).                   % X = -3 (negativo, sin cambio)
% ?- procesar_numero(0, X).                    % X = 0 (cero, sin cambio)
% ?- procesar_con_explicacion(7, X, Y).        % X = 14, Y = multiplicado_por_2
% ?- aplicar_regla(-5, X, Y).                  % X = -5, Y = negativo_sin_cambio
% ?- procesar_lista([3, -2, 0, 4], X).         % X = [6, -2, 0, 8]