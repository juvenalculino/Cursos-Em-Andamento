-------------------------------------------
			DATABASE
-------------------------------------------


CRIANDO DATABASE

create database teste;

-------------------------------------------

MOSTRAR DATABASES

show databases;

-------------------------------------------

DELETANDO DATABASE

drop database teste;

-------------------------------------------

SELECIONANDO UMA DATABASE

use teste;


-------------------------------------------
			TABELAS
-------------------------------------------

VERIFICANDO TABELAS NO BANCO DE DADOS

show tables from teste;


-------------------------------------------

CRIANDO TABELA



create table usuarios
-> (id int primary key auto_increment,
-> login varchar(20) not null,
-> senha varchar(20) not null);

describe teste_um


-------------------------------------------
			INSERT - INSERIR
-------------------------------------------

insert into usuarios (id, nome, situacao) values (1,'admin','root');
OU
insert into usuarios values ('1','admin','admin');




-------------------------------------------
			SELECT
-------------------------------------------

Selecionar tudo de uma tabela

select * from usuarios;

Selecionando um nome em uma tabela

select * from usuarios where nome = 'ana';

Selecionando id e nome de uma tabela

select id, nome from usuarios;

Selecionando apenas certos usuários

select * from usuarios where id >= 2 and id <=6;

Selecionando todos os nomes com ana

select * from usuarios where nome = 'ana';



-------------------------------------------
			WHERE
-------------------------------------------
Clásula WHERE é usada para restringir os dados (tuplas) que
serão listados, ou seja, efetuar uma condição para que os dados
apareçam na listagem, para isso é necessário entender os seguintes

Operadores lógicos:

= igial a
> maior que
< menor que
>= maior ou igual a
<= menor que ou igual
and - E


Buscando tudo onde o id é 5

select * from usuarios where id = 5;

Buscando tudo onde o id é maior que 4 e menor que 7

mysql> select * from usuarios where id >= 4 and id <=7;



-------------------------------------------
			ORDER BY
-------------------------------------------

Clásula ORDER By altera a ordem de apresentação do resultadp
da pesquisa e possibilita colocar também em ordem ascendente
ou descrescente.

Selecionar tudo da tabela e ordenar pelo nome

select * from usuarios order by nome;

Selecionando e ordenando o id em ordem decrescente

select * from usuarios order by id desc;

Selecionando e ordenando o id, nome em ordem crescente

select id, nome from usuarios order by nome asc;

Selecionando id desc e nome anc

select id, nome from usuarios order by id desc, nome asc;




-------------------------------------------
			LIKE
-------------------------------------------

Comando LIKE - pode ser usado para buscar de acordo com a 
necessidade do conteúdo.

Carregar tudo da tabela que começa com a

select * from usuarios where nome like "%a";

Carregar tudo da tabela após a primeira ocorrência do a.

Selecionar tudo que contenham 'an'

select * from usuarios where nome like '%an%';



-------------------------------------------
			BETWEEN
-------------------------------------------

Comando BETWEEN é aplicado para diferenciar intervalos entre dados


Seleciona tudo entre 2 e o 5

select * from usuarios where id BETWEEN 2 and 5;



-------------------------------------------
			NOT BETWEEN - IN - NOT IN
-------------------------------------------

Seleciona tudo que não esta entre 2 e o 5

select * from usuarios where id not BETWEEN 2 and 5; 

Seleciona apenas os números passados

select * from usuarios where id in (1, 5, 8);

Seleciona os que não tem o 1 , 5, 8

select * from usuarios where id not in (1, 5, 8);


-------------------------------------------
			DESCRIBE
-------------------------------------------

Descreve a tabela usuários

describe usuarios 



-------------------------------------------
			DISTINCT
-------------------------------------------

Serve para eliminar a duplicidade | exclui repetição

select distinct nome from usuarios;




-------------------------------------------
			DROP
-------------------------------------------

EXCLUIR TABELA

show tables from teste

drop table usered;


-------------------------------------------
			ALTER ADD - ALTER DROP
-------------------------------------------


O comando ALTER ADD e ALTER DROP - funciona para alterar tabela  
adicionando coluna ou apagando.

Adicionando coluna

alter table usuarios add codigo_pessoa int;

Excluindo coluna

alter table usuarios drop codigo_pessoa;


-------------------------------------------
			UPDATE
-------------------------------------------

Atualiza determinado campo de um atributo

update usuarios set codigo_pessoa = 1;

Atualizando código especifico

update usuarios set codigo_pessoa = 2 where id = 4;



-------------------------------------------
			DELETE
-------------------------------------------

O delete é utilizado para apagar determinado registro

Apagando todos os registros

delete from usuarios;

Apagando determinado registro

delete from usuarios where id = 7;
delete from usuarios where nome = 'ana';


-------------------------------------------
			SUM
-------------------------------------------

Somando determinado registro ou todos os registros

Somando todos de id

select sum(id) as Media from usuarios;

Somando apenas um padrão

select sum(id) as Media from usuarios where codigo_pessoa = 1;



-------------------------------------------
			MIN - MAX - SUM
-------------------------------------------

Criando colona para inserirmos os dados

alter table usuarios add valor varchar(7);

adicionando valores

update usuarios set valor = '20,00' where id = 1;


Selecionando o menor valor

select min(valor) as ValorMinimo from usuarios;


Selecionando o maior valor

select max(valor) as ValorMaximo from usuarios;


Fazendo a soma dos valores

select sum(valor) as SomaValor from usuarios;


Calculando a média dos valores

select AVG(valor) as ValorMedia from usuarios;





<h1>			UPPER - LOWER</h1>


Tudo Maiúsculas

select id, upper(nome), upper(situacao), codigo_pessoa, valor from usuarios;




Tudo Minúsculas
select id, lower(nome), lower(situacao), codigo_pessoa, valor from usuarios;



-------------------------------------------
			PRIMARY KEY
-------------------------------------------

Chave primária - Serve para que não possa ter chave identica no banco de dados
Devemos adicionar ao criarmos a tabela.

Criar tabela

create table usered ( id int,  nome varchar(20), situacao varchar(20), valor varchar(8), primary key (id));

Inserir dados

insert into usered values (1,'ana','santos','30,00');

Ao inserirmos dados com o id igual ele volta com o erro:
ERROR 1062 (23000): Duplicate entry '1' for key 'usered.PRIMARY'




-------------------------------------------
			FORGEIN KEY
-------------------------------------------

No contexto dos banco de dados, o conceito de chave estrangeira ou chave externa 
se refere ao tipo de relacionamento entre distintas tabelas de dados do banco de dados. 
Uma chave estrangeira é chamada quando há o relacionamento entre duas tabelas

create table tbsql
(
	sql_codigo int not null,
	sql_nome varchar(60),
	primary KEY (sql_codigo)
);

create table alunos
(
	alu_codigo int not null,
	alu_nome varchar (80),
	alu_cod_curso int not null,
	foreign key (alu_cod_curso) references tbsql (sql_codigo)
);

Inserindo valores

insert into tbsql values (1, 'Curso Sql')

Inserindo valor alunos

insert into alunos values (1, 'João', 1)

Caso o código não exista pode dar problema


-------------------------------------------
			JOIN
-------------------------------------------

Buscando informações de varias tabelas com o comando join


select sql_codigo 'Código do Curso', sql_nome 'Nome do Curso', alu_nome 'Nome do Aluno' fro
m tbsql join alunos on alu_cod_curso = sql_codigo;






-------------------------------------------
			UNION
-------------------------------------------

Unindo informações de varias tabelas

select valor from usuarios union select alu_nome from alunos;
