## O que é um branche?

* Branche é a forma que o git separa as versões do projeto.
* Quando um branche é criado ele inicia na master, estamos trabalhando nele no momento;
* Geralmente cada nova feature fica em um branche separado;
* Após a finalização os branches são unidos formando o código-fonte final.

## Criando e visualizando branche

###### Visualizar :
* git branch
###### Criar:
* git branch #nome#
  
> Essas opções são utilizadas no dia a dia de um desenvolvedor.

###### Clonar projeto e criar outra pasta
* mkdir branch
* git clone https://#repo# . Ou git init
  
###### Ver o Branch
* git branch

###### Criando branch
* git branch #nome#
  > git branch

###### OBS: Sempre que criarmos um branch devemos partir da master.

## Deletando branches

###### Podemos deletar utilizando a flag -d ou --delete
> Não é comum deletar um branch.

> Geralmente se usa o --delete

* git branch --delete #nome#
  
## Mudando de branch

###### Podemos mudar para outro branch utilizando:
* git checkout -b #nome#
  > Este comando é utilizado para diversas mudanças de um arquivo.
  
  > Alterando um branch podemis levar as alterações que não foram commitadas junto, tome cuidado!!!

## Escolher branch

* git checkout master OU #nome#
  
###### Mudar e escolher branch com novo nome
* git checkout -b #novo_nome#
> Devemos comitar os códigos.

> Ao criarmos uma copia que não seja da master, copiamos o código que não é original.

## Unindo branches

* git merge #nome# 
  > normalmente recebemos atualizações de outros desenvolvedores.

###### Caso esteja na master
* git merge #segundo_branch#
* git push

## Criando outro branch

* git checkout -b #novo_branch#
* git status
* git commit -a -m "Mensagem"
* git checkout novo_nome
* git merge #novo_nome#

## Utilizando a stash

> Podemos salvar as modificações para prosseguir com uma outra abordagem de solução  e não perder o código.

> Após o comando o branch será resetado para a sua versão de acordo com o repo.

* git stash
* git status

## Recuperando stash

* git stash list

###### Também podemos recuperar
* git stash #nome#
* git stash apply
 
###### Salvar
* git stash

## Removendo stash

###### Para limpar totalmente as stash de um branch

* git stash clear

###### Deletar satash específico
* git stash drop #nome#
  > git stash list
  
  > git stash drop 5
  
  
## Utilizando tags

###### Podemos criar tags nos branches
* git tag -a #nome# -m "Msg"
  > A tag é diferente do stash, serve como um checkpoint de um branch.
  
  > É utilizada para demarcar estágios de desenvolvimento de algúm recurso.
  
* git tag -a V1.0 -m "Versão 1.0"

## Verificando e alterando tags

###### Verificando
* git show #nome#
* git tag
  
###### Trocando de tags
* git checkout #nome#
* git show V1.0
  
## Enviando tag ao repositório

* git psuh origin #nome#
  
###### Enviando varias tags
* git push origin --tags

## Enviando e compartilhando tags

* git push origin V1.0
* git push origin --tags
