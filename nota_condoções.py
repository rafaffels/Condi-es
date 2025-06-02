nota = int(input("Insira a nota:")) #Variavel com o nome Nota, onde vai receber um numero inteiro

if nota >= 7:# no if ele vera se a nota é maior ou igual a colocada na variavel nota, se o numero corresponder como verdadeiro sera impresso no print.
    print("Aprovado")
else: # caso a primeira condição não seja verdadeira vira para o else.
    if nota >= 5:
        print("recuperação") # no else apliquei mais de uma condição onde o programa vai identificar o melhor qual condição vai corresponder ao que foi atribuido.
    else:
        print("Reprovado")     