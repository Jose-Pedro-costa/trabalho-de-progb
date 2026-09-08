# Atividade 1 – Capítulo 5

## 1. Quais tabelas você definiu inicialmente?

Defini inicialmente apenas a tabela `songs`, que representa o recurso central da aplicação Free Music. Ela armazena as informações básicas de cada música: título, artista, álbum, gênero, duração em segundos, URL da capa e URL de prévia do áudio.

## 2. Você utilizou migrations? Se sim, quantas migrations? Descreva em uma frase o que cada uma faz.

Sim, utilizei migrations. Criei **1 migration**:

- `001_create_songs.sql` — Cria a tabela `songs` com suas colunas, restrições, índices para melhorar a performance das buscas por títulos, artista e gênero.

## 3. Qual o caminho do arquivo que gera a seed do seu banco?

O arquivo de seed está em:

`backend/seed.sql`

## 4. Quais os endpoints que você irá implementar inicialmente? Cada endpoint deve ser um método e um path. Explique em um parágrafo por que você resolveu priorizar a implementação desses endpoints.

Endpoint inicial:

- `GET /api/songs`

Priorizei a implementação deste endpoint porque a listagem e a busca de músicas são a funcionalidade central do Free Music. Sem ela, o restante da aplicação (filtros, detalhes, favoritos, player e download) não faz sentido. Começar pelo `GET /api/songs` (com suporte a query params de filtro) permite validar rapidamente o fluxo completo banco → API → frontend, seguindo a abordagem de fatias verticais do livro. Os endpoints de detalhe (`GET /api/songs/:id`), autenticação e favoritos serão adicionados nas próximas fatias, quando a necessidade deles aparecer de forma natural.

## 5. Você está usando algum framework para escrever os endpoints da sua API? Se sim, qual?

Sim. Estou utilizando o **Express**, um framework minimalista para Node.js.
