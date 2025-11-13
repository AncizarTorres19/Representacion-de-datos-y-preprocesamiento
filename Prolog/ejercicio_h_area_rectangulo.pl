% Ejercicio h: Calcular el área de un rectángulo si ambos lados son positivos

% Predicado que verifica si un número es positivo
es_positivo(Numero) :-
    Numero > 0.

% Predicado que calcula el área de un rectángulo si ambos lados son positivos
area_rectangulo(Largo, Ancho, Area) :-
    es_positivo(Largo),
    es_positivo(Ancho),
    Area is Largo * Ancho.

% Predicado que valida y calcula el área con mensaje de error
calcular_area_segura(Largo, Ancho, Area, valido) :-
    es_positivo(Largo),
    es_positivo(Ancho),
    Area is Largo * Ancho.

calcular_area_segura(Largo, _, 0, error_largo_no_positivo) :-
    \+ es_positivo(Largo).

calcular_area_segura(Largo, Ancho, 0, error_ancho_no_positivo) :-
    es_positivo(Largo),
    \+ es_positivo(Ancho).

% Predicado que verifica si se puede calcular el área
puede_calcular_area(Largo, Ancho) :-
    es_positivo(Largo),
    es_positivo(Ancho).

% Predicado para calcular perímetro también (si ambos lados son positivos)
perimetro_rectangulo(Largo, Ancho, Perimetro) :-
    es_positivo(Largo),
    es_positivo(Ancho),
    Perimetro is 2 * (Largo + Ancho).

% Predicado que calcula tanto área como perímetro
rectangulo_completo(Largo, Ancho, Area, Perimetro) :-
    es_positivo(Largo),
    es_positivo(Ancho),
    Area is Largo * Ancho,
    Perimetro is 2 * (Largo + Ancho).

% Ejemplos de uso:
% ?- area_rectangulo(5, 3, X).                 % X = 15
% ?- area_rectangulo(-2, 4, X).                % false (lado negativo)
% ?- calcular_area_segura(6, 2, X, Y).         % X = 12, Y = valido
% ?- calcular_area_segura(-1, 3, X, Y).        % X = 0, Y = error_largo_no_positivo
% ?- rectangulo_completo(4, 7, A, P).          % A = 28, P = 22