# Projeto: Portfólio com github pages

### O que é um github pages?
> É Uma forma de criar uma página estática nos servidores do github.

> Muito mais simples de colocar no ar, e não precisa de domínio e nem servidor.

> Muitas empresas utilizam para apresentar seus projetos ou a prórpia documentação.

### Como criar uma página?

* Você deve segiur alguns passos simples, veja:

1. Criar o repositório com o nome do usuário do github.
2. Clonar o repositório do nosso computador.
3. Adicionar o código do projeto no branch master.
4. Enviar o código por meio de push.
5. Pronto. Você tem um site em https://seu_nome_usuario.github.io

### Criando

* New
* Create Repository
* Colocar: seu_nome_usuario.github.io
* Create repository

##### Abrir o terminal no seu windows ou linux
> Passar os comandos que aparecerão no github

```
echo "# juvenalculino.github.io" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/juvenalculino/juvenalculino.github.io.git
git push -u origin main
```
###### Agora vamos criar um arquivo index.html e subir para o github
> Se preferir pode criar o arquivo no github
* touch index.html
* nano touch.html
> Escrever os comandos:
```
   <h1> Seu_nome </h1>
--> Salvar e subir.
```
* git add .
* git commit -a -m "Adicionando o index.html"
* git push

[>>> Tutorial de Criação da página <<<](http://blog.triadworks.com.br/aprenda-a-usar-o-github-como-seu-portfolio)

### Configurações iniciais do projeto

