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

##### Criar estrutura básica do projeto no index.html
* Criar uma página chamada css
> criar um arquivo dentro da página chamado styles.css

* Criar uma página chamada img
> Enviar uma foto sua

#### Código index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Portfólio Juvenal Culino</title>
	<!-- Google Fonts -->
	<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,700;0,900;1,300;1,700;1,900&display=swap" rel="stylesheet">
	<!-- Dev Icon Fonts -->
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@master/devicon.min.css">
	<!-- CSS do projeto -->

	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>
<body>
	<h1>Teste</h1>
	<ion-icon name="heart"></ion-icon>
	<i class="devicon-amazonwebservices-original"></i>
	<!-- Ion Icons -->
	<script src="https://unpkg.com/ionicons@5.1.2/dist/ionicons.js"></script>
</body>
</html>
```

#### Código styles.css
```
* {
font-family: 'Roboto', sans-serif;
}

h1 {
	color: red;
}
```

#### Links das fontes e dependências utilizadas

[Link Font](https://fonts.google.com)

[Link Ion Icon](https://ionicons.com)

[Link Language Fonts](https://devicon.dev)

###### OBS: Podemos testar o código utilizando nosso navegador


### Criando o HTML

> Criação do código html e adicionando icons


#### Código index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Portfólio Juvenal Culino</title>
	<!-- Google Fonts -->
	<link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,700;0,900;1,300;1,700;1,900&display=swap" rel="stylesheet">
	<!-- Dev Icon Fonts -->
	<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/devicons/devicon@master/devicon.min.css">
	<!-- CSS do projeto -->

	<link rel="stylesheet" type="text/css" href="css/styles.css">
</head>
<body>
	<main id="container">
		<aside id="bio-container">		
			<h2>Juvenal Culino</h2>
			<img id="bio-image" src="img/juvenal.jpg" alt="Juvenal Culino">
			<p>Olá, meu nome é juvenal culino e sou <span class="highlight"> Programador Python</span></p>
			<p id="Welcome-text">Seja bem-vindo(a)!</p>
			<ul id="social-container">
				<li><a href="#" target="_blank"><ion-icon name="logo-github"></ion-icon></a></li>
				<li><a href="#" target="_blank"><ion-icon name="logo-linkedin"></ion-icon></a></li>
				<li><a href="#" target="_blank"><ion-icon name="logo-facebook"></ion-icon></a></li>
			</ul>
			<div id="email-container">
				<ion-icon name="email-outline"></ion-icon><a href="mailto:b831381@gmail.com">b831381@gmail.com</a>
			</div>
		</aside>
		<section id="about-container">
			<h1 id="name">Juvenal Culino</h1>
			<p id="title"><span class="highlight">Programador Python</span></p>
			<p class="description"> Olá, sou um <span class="highlight">estudante de Python em específico, autodidata</span>, gosto muito da linguagem em si, e de desafios que complementem a minha aprendizagem, estou a cada dia tentando <span class="highlight">aprender o básico de outras linguagens como o C, JavaScript e Shell</span> para que posteriormente possa ter o domínio básico e <span class="highlight">engrandecer meu currículo para o mercado de trabalho..</span></p>
			<p class="description">Atuo tanto no <span class="highlight">Front</span> como no <span class="highlight">back-end</span>, e amo tecnologia, estudo todos os dias para me tornar cada vez melhor e escrever códigos que atendam os anseios do empregador e os meus claro....</p>
			<a href="#" id="btn-projects"><ion-icon name="share-social-outline"></ion-icon> <span>Ver Projetos</span></a>
			<h2 id="skills-section-title">Minhas Skills</h2>
			<p class="description">Conheça as tecnologias que domino:</p>
			<div id="skills-container">
				<div class="skills-box">
					<p class="skills-title"> Front-End</p>
					<i class="devicon-html5-plain colored"></i>
					<i class="devicon-css3-plain colored"></i>
					<i class="devicon-javascript-plain colored"></i>
				</div>
				<div class="skills-box">
					<p class="skills-title"> Back-End</p>
					<i class="devicon-php-plain colored"></i>
					<i class="devicon-python-plain colored"></i>
				</div><div class="skills-box">
					<p class="skills-title"> Database</p>
					<i class="devicon-mysql-plain colored"></i>
				</div><div class="skills-box">
					<p class="skills-title"> Front-End Frameworks</p>
					<i class="devicon-vuejs-plain colored"></i>
				</div><div class="skills-box">
					<p class="skills-title"> Back-End Framework</p>
					<i class="devicon-django-plain colored"></i>
				</div>
				<div class="skills-box">
					<p class="skills-title"> Front-End</p>
					<i class="devicon-linux-plain colored"></i>
				</div>
			</div>
		</section>
	</main>
	<!-- Ion Icons -->
	<script src="https://unpkg.com/ionicons@5.1.2/dist/ionicons.js"></script>
</body>
</html>
```

#### Código CSS

```
* {
font-family: 'Roboto', sans-serif;
}
```

## CSS do container da bio


#### Código css
```
/* Reset */
* {
	padding: 0;
	margin: 0;
	font-family: 'Roboto', sans-serif;
	box-sizing: border-box;
}

/* Variables */

:root {
	--main-color: #54B689;
	--main-text-color: #FFF;
	--border-color: # 999;
	--bio-bg-color: #1E2A3A;
	--bio-border-color: #293544;
	--about-bt-color: #111821;
}

/* General */
.highlight {
	color: var(--main-color);
}

/* Containers */
#container {
	display: flex;
	flex-direction: row;
	color: var(--main-text-color);
}

#bio-container {
	flex: 1 1 20%;
	min-height: 100vh;
	background-color: var(--bio-bg-color);
	text-align: center;
	padding: 30px 12px;
	border-right: 5px solid var(--bio-border-color);
}

#about-container {
	flex: 1 1 80%;
	min-height: 100vh;
	background-color: var(--about-bt-color);
	padding: 50px;
}



/* Bio Container */

#bio-container h2 {
	margin-bottom: 20px;
}


#bio-container p {
	margin-bottom: 20px;
}

#bio-container #welcome-text {
	font-weight: bold; 
}


#bio-image {
	width: 175px;
	height: 175px;
	border-radius: 50%;
	margin-bottom: 25px;
}


#social-container {
	display: flex;
	justify-content: center;
	list-style: none;
	border-bottom: 1px solid var(--border-color);
	margin-bottom: 25px,
	padding-bottom: 25px;
}

#social-container li {
	flex: 1 1 0;
	max-width: 60px;
}

#social-container li a{
	color: var(--main-color);
	font-size: 30px;
}

#email-container {
	display: flex;
	justify-content: center;
}

#email-container ion-icon,
#email-container a {
	flex: 1 1 0;
}

#email-container a {
	color: var(--main-text-color);
	text-decoration: none;
	max-width: 225px;
}

#email-container ion-icon {
	color: var(main-color);
	font-size: 20px;
	margin-right: 5px;
	max-width: 20px;
}

/* about container */

#name {
	font-size: 42px;
	margin-bottom: 15px;
}

#title {
	font-size: 24px;
	margin-bottom: 15px;
	font-weight: bold;
}

#description {
	max-width: 75%;
	margin-bottom: 10px;
}

#btn-projects {
	font-weight: bold;
	font-size: 16px;
	color: var(--main-text-color);
	background-color: var(--main-color);
	border: 2px solid var(--main-color);
	border-radius: 5px;
	text-decoration: none;
	transition: .5s;
	margin: 25px 0;
	padding: 12px 10px;
	width: 150px;
	text-align: center;
	display: flex;
}

#btn-projects ion-icon,
#btn-projects span {
	flex: 1 1 0;
}

#btn-projects ion-icon {
	font-size: 20px;
	max-width: 20px;
}

#btn-projects:hover {
	background-color: transparent;
}

#skills-section-title {
	border-top: 1px solid var(--border-color);
	padding-top: 20px;
	margin-bottom: 20px;
	font-size: 32px;
}

#skills-container {
	display: flex;
	flex-wrap: wrap;
	margin-top: 25px;
}

.skills-box {
	flex: 1 1 33%;
	max-width: 33%;
	margin-bottom: 35px;
}

.skills-title {
	font-size: 24px;
	margin-bottom: 25px;
	font-weight: bold;
	padding-left: 10px;
	border-left: 5px solid var(--main-color);
}

.skills-box i {
	font-size: 45px;
	margin-right: 10px;
}
```


### Deixando o Projeto responsivo (para android)


##### Código css

```
/* Reset */
* {
	padding: 0;
	margin: 0;
	font-family: 'Roboto', sans-serif;
	box-sizing: border-box;
}

/* Variables */

:root {
	--main-color: #54B689;
	--main-text-color: #FFF;
	--border-color: # 999;
	--bio-bg-color: #1E2A3A;
	--bio-border-color: #293544;
	--about-bt-color: #111821;
}

/* General */
.highlight {
	color: var(--main-color);
}

/* Containers */
#container {
	display: flex;
	flex-direction: row;
	color: var(--main-text-color);
}

#bio-container {
	flex: 1 1 20%;
	min-height: 100vh;
	background-color: var(--bio-bg-color);
	text-align: center;
	padding: 30px 12px;
	border-right: 5px solid var(--bio-border-color);
}

#about-container {
	flex: 1 1 80%;
	min-height: 100vh;
	background-color: var(--about-bt-color);
	padding: 50px;
}



/* Bio Container */

#bio-container h2 {
	margin-bottom: 20px;
}


#bio-container p {
	margin-bottom: 20px;
}

#bio-container #welcome-text {
	font-weight: bold; 
}


#bio-image {
	width: 175px;
	height: 175px;
	border-radius: 50%;
	margin-bottom: 25px;
}


#social-container {
	display: flex;
	justify-content: center;
	list-style: none;
	border-bottom: 1px solid var(--border-color);
	margin-bottom: 25px,
	padding-bottom: 25px;
}

#social-container li {
	flex: 1 1 0;
	max-width: 60px;
}

#social-container li a{
	color: var(--main-color);
	font-size: 30px;
}

#email-container {
	display: flex;
	justify-content: center;
}

#email-container ion-icon,
#email-container a {
	flex: 1 1 0;
}

#email-container a {
	color: var(--main-text-color);
	text-decoration: none;
	max-width: 225px;
}

#email-container ion-icon {
	color: var(main-color);
	font-size: 20px;
	margin-right: 5px;
	max-width: 20px;
}

/* about container */

#name {
	font-size: 42px;
	margin-bottom: 15px;
}

#title {
	font-size: 24px;
	margin-bottom: 15px;
	font-weight: bold;
}

#description {
	max-width: 75%;
	margin-bottom: 10px;
}

#btn-projects {
	font-weight: bold;
	font-size: 16px;
	color: var(--main-text-color);
	background-color: var(--main-color);
	border: 2px solid var(--main-color);
	border-radius: 5px;
	text-decoration: none;
	transition: .5s;
	margin: 25px 0;
	padding: 12px 10px;
	width: 150px;
	text-align: center;
	display: flex;
}

#btn-projects ion-icon,
#btn-projects span {
	flex: 1 1 0;
}

#btn-projects ion-icon {
	font-size: 20px;
	max-width: 20px;
}

#btn-projects:hover {
	background-color: transparent;
}

#skills-section-title {
	border-top: 1px solid var(--border-color);
	padding-top: 20px;
	margin-bottom: 20px;
	font-size: 32px;
}

#skills-container {
	display: flex;
	flex-wrap: wrap;
	margin-top: 25px;
}

.skills-box {
	flex: 1 1 33%;
	max-width: 33%;
	margin-bottom: 35px;
}

.skills-title {
	font-size: 24px;
	margin-bottom: 25px;
	font-weight: bold;
	padding-left: 10px;
	border-left: 5px solid var(--main-color);
}

.skills-box i {
	font-size: 45px;
	margin-right: 10px;
}

/* Mobile */
@media(max-width: 450px) {

	#container {
		flex-direction: column;
	}

	#bio-container {
		min-height: auto;
		border-right: none;
		border-bottom: 5px solid var(--bio-border-color);
	}

	#bio-container h2 {
		display: none;
	}

	#bio-container p {
		max-width: 60%
		margin: 10px auto;
	}

	#about-container {
		text-align: center;
		padding: 30px;
	}

	#about-container .descripton {
		margin: 10px auto;
		max-width: 100%;
		line-height: 26px;
	}

	#btn-projects {
		margin: 20px auto;
	}

	.skills-box {
		flex: 1 1 100%;
		max-width: 100%;
		margin-bottom: 40%;
		text-align: left;
	}

	.skills-box i {
		font-size: 60px;
	}
}
```


## Enviando o protfólio para o repositório


* git status
* git add .
* git commit -a -m "msg"
* git push


