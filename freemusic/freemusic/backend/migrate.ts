import { Client } from "pg";
import { readdirSync, readFileSync } from "fs";
import { join } from "path";
import "dotenv/config";

async function migrate() {
  const databaseUrl = process.env.DATABASE_URL;
  if (!databaseUrl) {
    console.error("DATABASE_URL não definida");
    process.exit(1);
  }

  const client = new Client({ connectionString: databaseUrl });
  await client.connect();

  const migrationsDir = join(__dirname, "migrations");
  const files = readdirSync(migrationsDir)
    .filter((f) => f.endsWith(".sql"))
    .sort();

  for (const file of files) {
    console.log(`Executando: ${file}`);
    const sql = readFileSync(join(migrationsDir, file), "utf-8");
    await client.query(sql);
  }

  console.log("Migrations concluídas.");
  await client.end();
}

migrate().catch((err) => {
  console.error(err);
  process.exit(1);
});
