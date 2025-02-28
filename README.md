# PortScan
Yan Vieira Romano

## 1. Criar e Ativar o Ambiente Virtual
Para isolar as dependências do projeto, crie e ative um ambiente virtual:

```
# Criar o ambiente virtual
python3 -m venv venv

# Ativar o ambiente virtual
source venv/bin/activate  # No Linux/Mac
# Ou no Windows:
# venv\Scripts\activate
```

------
## 2. Instalar as Dependências
Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt:

```
pip install --upgrade pip  # Atualizar o pip para evitar problemas
pip install -r requirements.txt
```
-----

## 3. Verificar o Nmap
O programa usa o Nmap para descobrir hosts ativos na rede. Certifique-se de que o Nmap está instalado no sistema:
```
sudo apt update
sudo apt install nmap
```
Verifique a instalação com 
```
nmap --version
```


## 4. Rodando

Para utilizar basta executar main.py no terminal
```
python3 main.py
```

O programa mostra todas as opções que o usuário pode realizar diretamente em menus user frendly C: