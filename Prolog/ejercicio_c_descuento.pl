% Ejercicio c: Calcular precio final con descuento del 10% para compras mayores a 100

% Predicado que aplica descuento si la compra es mayor a 100
precio_final(PrecioOriginal, PrecioFinal) :-
    PrecioOriginal > 100,
    PrecioFinal is PrecioOriginal * 0.9.

% Predicado para cuando no se aplica descuento
precio_final(PrecioOriginal, PrecioOriginal) :-
    PrecioOriginal =< 100.

% Predicado que muestra si se aplica descuento o no
calcular_precio(PrecioOriginal, PrecioFinal, con_descuento) :-
    PrecioOriginal > 100,
    PrecioFinal is PrecioOriginal * 0.9.

calcular_precio(PrecioOriginal, PrecioOriginal, sin_descuento) :-
    PrecioOriginal =< 100.

% Ejemplos de uso:
% ?- precio_final(150, X).          % X = 135 (con descuento)
% ?- precio_final(80, X).           % X = 80 (sin descuento)
% ?- calcular_precio(200, X, Y).    % X = 180, Y = con_descuento
% ?- calcular_precio(50, X, Y).     % X = 50, Y = sin_descuento