# Free Music

Plataforma web e mobile para pesquisa, pré-visualização e download de músicas.

## Problema

Encontrar músicas de forma rápida, com filtros úteis (gênero, artista, duração), pré-ouvir antes de baixar e guardar favoritos/histórico.

## Componentes

- `backend/` — API HTTP + PostgreSQL
- `web/` — Frontend web (React + TypeScript)
- `mobile/` — Frontend mobile (React Native / Expo)

## Stack

- TypeScript
- Express + pg
- PostgreSQL
- React / React Native

## Como rodar (desenvolvimento)

```bash

cd backend
cp .env.example .env   
npm install
npx tsx migrate.ts
psql $DATABASE_URL -f seed.sql
npm run dev


cd web
npm install
npm run dev
```

