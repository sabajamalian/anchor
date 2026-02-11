# Database Migrations

This directory contains SQL migration scripts for the database schema.

## Running Migrations

Migrations should be run in numerical order. Each migration file is prefixed with a number (e.g., `001_`, `002_`) to ensure proper execution order.

### Manual Execution

Connect to your Azure SQL database and execute each migration script:

```bash
sqlcmd -S <server>.database.windows.net -d <database> -U <username> -P <password> -i 001_create_items_table.sql
sqlcmd -S <server>.database.windows.net -d <database> -U <username> -P <password> -i 002_seed_sample_data.sql
```

### Using Azure Data Studio or SQL Server Management Studio

1. Connect to your Azure SQL database
2. Open each migration file in order
3. Execute the script

## Migration Naming Convention

Format: `XXX_description.sql`

- `XXX`: Three-digit sequential number (001, 002, etc.)
- `description`: Brief description of what the migration does (use underscores for spaces)

## Creating New Migrations

1. Determine the next sequential number
2. Create a new `.sql` file with the appropriate name
3. Add a header comment with migration details:
   ```sql
   -- Migration: XXX - Title
   -- Description: Detailed description
   -- Date: YYYY-MM-DD
   ```
4. Write your SQL statements
5. Test the migration on a development database first
