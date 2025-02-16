import random
import string

def CreatePassWord(tamanho):
    characteres = string.ascii_letters + string.digits + string.punctuation
    PassWord = ''.join(random.choice(characteres) for i in range(tamanho))
    return PassWord

tamanho_senha = 10    #you can change
PassWord = CreatePassWord(tamanho_senha)
print(f"Your new secure password is: {PassWord}")

