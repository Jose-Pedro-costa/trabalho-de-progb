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
# 1. Backend
cd backend
cp .env.example .env   # ajuste DATABASE_URL se necessário
npm install
npx tsx migrate.ts
psql $DATABASE_URL -f seed.sql
npm run dev

# 2. Web (em outro terminal, depois)
cd web
npm install
npm run dev
```

## Licença das músicas

Usamos apenas músicas de domínio público ou Creative Commons para fins educacionais.
