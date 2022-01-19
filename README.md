O projeto está dividido em duas partes. 

o backend desenvolvido em python gera um endpoint para acessar os card cadastrados em uma base local. 

## 1. Inicie o backend com o comando 

python .\api\server.py run

##########################################

Na raiz do projeto existe um processo de importação de cards. 

## 2. para importar uma lista de cards no formato csv, basta executar o processo de importação

python .\import.py  

## 3. Em seguida digite o caminho completo de onde o arquivo está localizado na sua máquina.

##########################################

Por fim a pasta mu-app contém uma versão base de uma aplicação para consumir e cadastrar os dados de card. 

## 4. Para iniciar a aplicação frontend, basta executar o comando 

yarn start

##########################################
##########################################
##########################################

## Desafio

https://github.com/producao-conteudo/desafio

Precisamos desenvolver uma ferramenta para criação de Cards de conteúdo esportivos (Insights).

### 1. Interace HTTP REST API

Ações da API

- Criar card
- Ler card
- Remover card
- Atualizar card
- Listar card
  - Filtrar por tags

CREATE TABLE card (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  texto varchar NULL,
  data_criacao timestamp,
  data_modificacao timestamp NULL,
  UNIQUE(id)
);
CREATE TABLE card_tag (
	card_id int NOT NULL,
  tag_id int NOT NULL 
);
CREATE TABLE tag (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
  name varchar NOT NULL,
  UNIQUE(name)
);

Um card possui os campos: 
```
{
  "id": // identificador
  "texto" // texto do card
  "data_criacao" // data da criação do card
  "data_modificacao" // data da última alteração do card
  "tags" // tags vinculas ao card
}
```

- Criar Tag
- Ler Tag
- Remover Tag
- Atualizar Tag

```
Uma tag possui os campos:
{
  "id" // identificador
  "name" // nome da tag
}
```

Temos uma estimativa de milhares de criações de cards diariamente. A preocupação com performance será avaliada.

### 2. CLI para importação dos card

Necessitamos importar os conteúdos do nosso sistema de dados esportivos para gerar nossos cards e precisamos de uma ferramenta para auxiliar essa tarefa.


Dado um csv de "cards", faça um CLI (Command Line Interface) que importe os dados para o Insights.

CSV exemplo:

```
text,tag
Lorem ipsum dolor sit amet., tag1;tag2;tag3
Mauris fringilla non quam vel lacinia,tag3
Cras in tempus libero,
```
### 3. Interface WEB

Após termos nossa api desenvolvida, precisamos viabilizar uma interface frontend para nossos usuários interagirem.

Nosso time de UX desenhou as [telas](https://www.sketch.com/s/3f91077d-21c0-4040-8fae-b89d69809d9b) e disponibilizou para você!

Dê preferência aos frameworks como o Vuetify para aproveitar os componentes já prontos.

Clique no box com o botão de play para entrar no modo de navegação com os hotspots que indicam o fluxo.

Clique em cada uma das telas e utilize a funcionalidade de "Inspector" para ter acesso ao guia de css.

Os ícones utilizados no projeto são do [Material Design](https://material.io/resources/icons/?style=baseline)

Utilize o botão "Download Assets" para baixar a marca do produto Insights.


### Requerimentos:
- Linguagens de programação backend:
  - Python
  - NodeJs
  - C#
- Framework frontend
  - VueJS
  - ReactJS
  - Angular
- Fidelidade de layout
- Code Style
- Teste unitário
- Documentação
  - Descrição
  - Como rodar
  - API DOC (openapi/swagger)

