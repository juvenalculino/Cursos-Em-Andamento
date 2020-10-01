## Compartilhamentos e atualizações de repositório

## Encontrando branches
> Branches são criados o tempo todo e seu git pode não estar mapeando eles com o comando gti fetch você é atualizadode todos os branches e tags que ainda não estão reconhecidos por você.
* git fetch
* git fetch -a

## Recebendo atualizações
* git pull
> Utilizamos para atualizar a master do repo.

## Enviando alterações
* git push
> Este comando é o contrário do git pull

## Passos para enviar arquivos
* git staus 
* git add .
* git commit -a -m "msg"
* git push
> OBS: Não enviar código que é gerado automaticamente Ex: .node 

## Utilizando o remote
> Com o git remote podemos fazer algumas alterações como: Adicionar um repo para trackear ou remover,
* git remote
> Quando criamos um repo remoto adicionamos ele ao git com git remote add origin #link#.
* git remote add origin #link"

## Verificando origin

* git remote -v 

## Removendo origin

* git remote rm origin

## Adicionando 

* git remote add origin https:// # link.git " /

## Verificando 

* git remote -v 

## Trabalhando com submódulos

> Submódulos é a maneira que temos de possuir dois ou mais projetos em um repositório.
* git submodule  add # repo " 

## Verificar os submódulos 

* git submodule

## Atualizando submódulo

> Para atualizar precisamos commitar

###### Para enviar o repositório do submódulo
* git push --recurse-submodules=on-demand
> Este fluxo tem como funcionalidade atualizar o submódulo.

###### Ex:
* cd submosulo
* touch teste > teste.txt
* git status
* git add .
* git commit -a -m # msg #
* git push --recurse-submodules=on-demand
