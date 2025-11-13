% EJERCICIOS DE PROLOG - REPRESENTACIÓN DE DATOS Y PREPROCESAMIENTO
% Autor: Ancizar Torres
% Fecha: Noviembre 2024

% =================================================================
% EJERCICIO A: Determinar si una persona es mayor que otra
% =================================================================

% Base de datos de edades
edad(juan, 25).
edad(maria, 30).
edad(pedro, 20).
edad(ana, 35).
edad(luis, 28).

es_mayor(Persona1, Persona2) :-
    edad(Persona1, Edad1),
    edad(Persona2, Edad2),
    Edad1 > Edad2.

% =================================================================
% EJERCICIO B: Determinar si un número es par o impar
% =================================================================

es_par(Numero) :-
    0 is Numero mod 2.

es_impar(Numero) :-
    1 is Numero mod 2.

clasificar_numero(Numero, par) :- es_par(Numero).
clasificar_numero(Numero, impar) :- es_impar(Numero).

% =================================================================
% EJERCICIO C: Precio final con descuento del 10% para compras > 100
% =================================================================

precio_final(PrecioOriginal, PrecioFinal) :-
    PrecioOriginal > 100,
    PrecioFinal is PrecioOriginal * 0.9.

precio_final(PrecioOriginal, PrecioOriginal) :-
    PrecioOriginal =< 100.

% =================================================================
% EJERCICIO D: Clasificar una nota como aprobada o reprobada
% =================================================================

clasificar_nota(Nota, aprobada) :- Nota >= 3.0.
clasificar_nota(Nota, reprobada) :- Nota < 3.0.

% =================================================================
% EJERCICIO E: Determinar peso ideal según IMC (18.5 - 24.9)
% =================================================================

% Base de datos de personas (peso en kg, altura en metros)
persona(juan, 70, 1.75).
persona(maria, 60, 1.65).
persona(pedro, 85, 1.80).

calcular_imc(Peso, Altura, IMC) :-
    IMC is Peso / (Altura * Altura).

tiene_peso_ideal(Persona) :-
    persona(Persona, Peso, Altura),
    calcular_imc(Peso, Altura, IMC),
    IMC >= 18.5,
    IMC =< 24.9.

% =================================================================
% EJERCICIO F: Verificar si una persona es abuelo de otra
% =================================================================

% Base de datos familiar
padre(carlos, juan_f).
padre(juan_f, pedro_f).
madre(elena, juan_f).
madre(carmen, pedro_f).

progenitor(X, Y) :- padre(X, Y).
progenitor(X, Y) :- madre(X, Y).

abuelo(X, Z) :-
    padre(X, Y),
    progenitor(Y, Z).

% =================================================================
% EJERCICIO G: Determinar quién gana más entre dos personas
% =================================================================

% Base de datos de salarios
salario(juan_s, 2500000).
salario(maria_s, 3200000).
salario(pedro_s, 1800000).

gana_mas(Persona1, Persona2) :-
    salario(Persona1, Salario1),
    salario(Persona2, Salario2),
    Salario1 > Salario2.

% =================================================================
% EJERCICIO H: Calcular área de rectángulo con lados positivos
% =================================================================

area_rectangulo(Largo, Ancho, Area) :-
    Largo > 0,
    Ancho > 0,
    Area is Largo * Ancho.

% =================================================================
% EJERCICIO I: Verificar si dos personas viven en el mismo país
% =================================================================

% Base de datos de residencias
vive_en(juan_p, colombia).
vive_en(pedro_p, colombia).
vive_en(maria_p, argentina).

mismo_pais(Persona1, Persona2) :-
    vive_en(Persona1, Pais),
    vive_en(Persona2, Pais),
    Persona1 \= Persona2.

% =================================================================
% EJERCICIO J: Multiplicar por 2 si es positivo, sino dejar igual
% =================================================================

procesar_numero(Numero, Resultado) :-
    Numero > 0,
    Resultado is Numero * 2.

procesar_numero(Numero, Numero) :-
    Numero =< 0.

% =================================================================
% EJEMPLOS DE USO Y CONSULTAS
% =================================================================

% Ejercicio A: ?- es_mayor(maria, juan).
% Ejercicio B: ?- clasificar_numero(8, X).
% Ejercicio C: ?- precio_final(150, X).
% Ejercicio D: ?- clasificar_nota(3.5, X).
% Ejercicio E: ?- tiene_peso_ideal(maria).
% Ejercicio F: ?- abuelo(carlos, pedro_f).
% Ejercicio G: ?- gana_mas(maria_s, pedro_s).
% Ejercicio H: ?- area_rectangulo(5, 3, X).
% Ejercicio I: ?- mismo_pais(juan_p, pedro_p).
% Ejercicio J: ?- procesar_numero(-5, X).