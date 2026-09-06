1. Quais tabelas você definiu inicialmente?
Para o MVP do free music, foram definidas inicialmente as seguintes tabelas:

Users: armazena os usuários cadastrados na plataforma.
Tracks: armazena as informações das músicas (título, artista, álbum, gênero, duração, capa e link de download).
Favorites: armazena as músicas favoritas de cada usuário.
SearchHistory: armazena o histórico de buscas realizadas pelos usuários.
DownloadHistory: armazena o histórico de downloads realizados pelos usuários.
A tabela Users possui relação com Favorites, SearchHistory e DownloadHistory.
A tabela Tracks possui relação com Favorites e DownloadHistory.
O dashboard (ou área principal de resultados) não possui uma tabela própria, pois suas informações serão obtidas a partir dos dados das outras tabelas e de buscas externas (quando necessário).
A estrutura inicial pode ser representada da seguinte forma:
````
Users
  ├── Favorites
  ├── SearchHistory
  └── DownloadHistory
        └── Tracks
````
  
2. Você utilizou migrations? Se sim, quantas migrations? Descreva em uma frase o que cada uma faz.
   
No inicio será utilizada uma migration para criar a estrutura básica do banco de dados.
InitialCreate: cria as tabelas Users, Tracks, Favorites, SearchHistory e DownloadHistory, incluindo suas chaves primárias e relacionamentos.
Novas migrations poderão ser adicionadas posteriormente caso seja necessário alterar a estrutura do banco durante o desenvolvimento do projeto.

3. Qual o caminho do arquivo que gera a seed do seu banco?
A seed do banco ficará no seguinte caminho:
````
api/Data/Seed/DbInitializer.cs
````
Esse arquivo será responsável por inserir dados iniciais no banco de dados (músicas de exemplo, usuários de teste etc.), facilitando os testes e o desenvolvimento da aplicação

4. Quais os endpoints que você irá implementar inicialmente?
   
Inicialmente serão implementados os seguintes endpoints:

Autenticação:

POST /api/auth/register — realiza o cadastro de um novo usuário.
POST /api/auth/login — realiza o login do usuário.

Músicas:

GET /api/tracks — lista ou busca músicas (com suporte a filtros por gênero, artista e duração).
GET /api/tracks/{id} — retorna as informações detalhadas de uma música.

Favoritos:

GET /api/favorites — lista as músicas favoritas do usuário logado.
POST /api/favorites — adiciona uma música aos favoritos.
DELETE /api/favorites/{id} — remove uma música dos favoritos.

Histórico:

GET /api/history/searches — retorna o histórico de buscas do usuário.
GET /api/history/downloads — retorna o histórico de downloads do usuário.
POST /api/history/downloads — registra um novo download no histórico

Esses endpoints foram priorizados porque representam o fluxo principal do MVP. Primeiro, o usuário precisa conseguir se cadastrar e realizar o login. Depois, ele poderá buscar músicas, visualizar detalhes, adicionar favoritos e registrar downloads. Com esses dados disponíveis na API, será possível posteriormente desenvolver o player embutido, o feedback de progresso e a interface completa

5. Você está usando algum framework para escrever os endpoints da sua API? Se sim, qual?
   
Sim. A API será desenvolvida utilizando FastAPI (Python).
Para a comunicação com o banco de dados PostgreSQL será utilizado o SQLAlchemy, que também será responsável pelo gerenciamento das migrations.
O projeto será organizado em um monorepo, contendo a API e a aplicação Web:
````
free music/
├── api/       # FastAPI - Python
├── web/       # React - TypeScript
├── ativ1.md
└── README.md
````
