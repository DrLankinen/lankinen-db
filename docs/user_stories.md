1. User can create a table with a name.
   `INSERT INTO "database" (date_created, date_modified, name, account_id) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)`
2. User can create tables for databases.
   `INSERT INTO "table" (date_created, date_modified, name, columns) VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)`
3. User can change database name.
   `UPDATE "database" SET date_modified=CURRENT_TIMESTAMP, name=? WHERE "database".id = ?`
4. User can delete database.
   `DELETE FROM "database" WHERE "database".id = ?`
