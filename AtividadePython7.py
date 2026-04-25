import random


def lancar_dados():
    dado1 = random.randint(1, 6)  
    dado2 = random.randint(1, 6)  
    
    total = dado1 + dado2
    return total


print("Soma dos dados:", lancar_dados())