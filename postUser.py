# Importa a Biblioteca requests para fazer requisições HTTP

import requests
url = "https://desafiopython.jogajuntoinstituto.org/api/users/"
urlLogin = "https://desafiopython.jogajuntoinstituto.org/api/users/login/"

# Cadastro de um novo usuário

newUser = {
        "username": "Null",
        "email": "Null@gmail.com",
        "phone": "66999936565",
        "address": "Rua Nula, 0, Centro, Nullandia, SP",
        "cpf": "000.000.000-00",
        "password": "Nulo123456789dez"
    }

envio = requests.post(url, json=newUser)

print(envio.status_code)
print(envio.json())


# Valida se o usuário foi cadastrado com sucesso
if envio.status_code == 201:
    print(f"Usuário {newUser['username']} cadastrado com sucesso!")
else:
    print(envio.login.status_code)
 

# Processo de Login

login = {
    "email": newUser['email'],
    "password": newUser['password']
}

envioLogin = requests.post(urlLogin, json=login)


# Valida se o usuário foi logado com sucesso

if envioLogin.status_code == 200:
    print(f"Login realizado com sucesso!")
else:
    print("Status code do login: ", envioLogin.status_code)
