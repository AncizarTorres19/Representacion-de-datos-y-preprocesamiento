% Ejercicio e: Determinar peso ideal según IMC (18.5 - 24.9)

% Base de datos de personas con peso y altura
persona(juan, 70, 1.75).    % peso en kg, altura en metros
persona(maria, 60, 1.65).
persona(pedro, 85, 1.80).
persona(ana, 55, 1.60).
persona(luis, 90, 1.70).

% Predicado que calcula el IMC
calcular_imc(Peso, Altura, IMC) :-
    IMC is Peso / (Altura * Altura).

% Predicado que determina si el IMC está en rango normal (peso ideal)
peso_ideal_imc(IMC) :-
    IMC >= 18.5,
    IMC =< 24.9.

% Predicado que determina si una persona tiene peso ideal
tiene_peso_ideal(Persona) :-
    persona(Persona, Peso, Altura),
    calcular_imc(Peso, Altura, IMC),
    peso_ideal_imc(IMC).

% Predicado que calcula y clasifica el IMC
clasificar_imc(Persona, IMC, Clasificacion) :-
    persona(Persona, Peso, Altura),
    calcular_imc(Peso, Altura, IMC),
    determinar_clasificacion(IMC, Clasificacion).

% Clasificaciones del IMC
determinar_clasificacion(IMC, bajo_peso) :-
    IMC < 18.5.

determinar_clasificacion(IMC, peso_ideal) :-
    IMC >= 18.5,
    IMC =< 24.9.

determinar_clasificacion(IMC, sobrepeso) :-
    IMC > 24.9,
    IMC =< 29.9.

determinar_clasificacion(IMC, obesidad) :-
    IMC > 29.9.

% Ejemplos de uso:
% ?- tiene_peso_ideal(maria).          % Verificar si María tiene peso ideal
% ?- clasificar_imc(juan, X, Y).       % X = IMC, Y = clasificación
% ?- calcular_imc(70, 1.75, X).        % X = IMC calculado