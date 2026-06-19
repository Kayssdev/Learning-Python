# Tipos primitivos
#    A aula apresenta de forma prática os tipos primitivos em Python, como números inteiros, números de ponto flutuante, strings e booleanos. O código demonstra como realizar operações básicas, como soma, e como utilizar a função `input()` para receber dados do usuário. Além disso, o código mostra a importância de converter as entradas para o tipo correto (neste caso, `int`) para realizar cálculos matemáticos. A aula é fundamental para entender os fundamentos da programação em Python e como manipular diferentes tipos de dados.

# Exemplo de código para demonstrar tipos primitivos e operações básicas em Python
a, b = map(int, (input('Digite um número: '), input('Digite outro número: ')))
print(f'A soma entre {a} e {b} é igual a {a + b}.')

# Exercício: Mostre os tipos primitivos de cada variável
tex = input("Digite uma palavra para testar métodos de string e mostrar o tipo primitivo: ")
print(f'Tem letras maiúsculas: {tex.isupper()}')
print(f'Tem letras minúsculas: {tex.islower()}')
print(f'É alfabético: {tex.isalpha()}')
print(f'É numérico: {tex.isdigit()}')
print(f'É alfanuméricof: {tex.isalnum()}')