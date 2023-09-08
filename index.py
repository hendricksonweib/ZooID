
A = str(input('Escolha a classificação do animal: Vertebrado/Invertebrado: '))
vert = "Vertebrado"
Ave = "Ave"
Ins = "Inseto"
Carn = "Carnivoro"
Oni = "Onivoro"
Hem = "Hematofago"

if A == vert :
  B1 = str(input('escolha a classificação do animal: Ave/Mamifero: '))

  if B1 == Ave:
    C1 = str(input('Escolha a classificação alimentar: Carnivoro/Onivoro: '))

    if C1 == Carn:
      print('Aguia')

    else:
      print('Pombo')
  
  else:
    C2 = str(input('Escolha a classificação alimentar: Onivoro/Herbivoro: '))

    if C2 == Oni:
      print('Homem')

    else:
      print('Vaca')

else :
  B2 = str(input('escolha a classificação do animal: Inseto/Anelídio: '))

  if B2 == Ins:
    C3 = str(input('Escolha a classificação alimentar: Hematofago/Herbivoro: '))
  
    if C3 == Hem:
      print('Pulga')

    else:
      print('Largata')
  
  else:
    C4 = str(input('Escolha a classificação alimentar: Hematofago/Onivoro: '))

    if C4 == Oni:
      print("Sanguessuga")

    else:
      print("Minhoca")

