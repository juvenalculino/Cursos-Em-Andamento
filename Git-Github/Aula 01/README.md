## Criando Repositórios com Git
  
* git status -> Verificar se tem algo criado.
* No github:
* Repositories
* New
* Repository Name -> <nome>
* Description -> Adicionar descrição.
* Create repository 

## Iniciando um .git e adicionando o README.md

* git init
* git add README.md 
* git status
* git commit -a -m "Testando"
* git branch -M master
* git remote add origin "https://o-repositorio-que-voce-criou.git/"
* git push -u origin master

## Ver origem do repositório

* git remote -v

## Remover origem

* git remote rm origin

## Verificando alterações:

###### Criar um arquivo index.html na pasta que você criou o .git
* git status
###### Se ficar vermelho pricisara adicionar ao repositório remoto.
* git add

## Adicionando arquivos ao projeto

* git add

## Adicionando diversos arquivos

* git add .

## Adicionando arquivos específicos

* git add index.html

## salvando alterações

* git commit

## Salvando arquivos específicos com mensagens

* git commit -m "Mensagem"

## Enviando vários arquivos para salvar e passar mensagem

* git commit -a -m "Mensagem"

## Enviando código para o repositório

* git push

## Recebendo as mudanças

É comum sincronizar as mudanças efetuadas localmente com as mudanças do remoto.

* git pull

## Clonando repositório

* git clone <Nome do repo>

## Removendo arquivos

* git rm
* git rm index.html
* git commit -a -m "Deletando arquivos"
* git push

Temos que passar estes comandos

## Verificando alterações por meio de logs

* git log

## Renomeando arquivos | mover arquivos

* git mv
Caso o arquivo esteja na pasta errada
##### git mv indx.html html/index.html

## Desfazendo alterações

* git checkout
* git checkout index.html

## Ignorando arquivos ao projeto

* Devemos adicionar uma chave chamada .gitignore na raiz do projeto
* No arquivo passamos as regras para que sejam ignoradas.
* touch .gitignore
* Depois salvar e sincronizar com o repo.
* git add .
* git commit -a -m "Mensagem"
* git push

## Resetando um Branche

* git reset
Geralmente utilizada com a flag --hard
* git reset --hard origin/master
