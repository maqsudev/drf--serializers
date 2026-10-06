from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'descrioption'
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'description'
                ) THEN
                    ALTER TABLE api_product RENAME COLUMN descrioption TO description;
                END IF;

                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'catgory_id'
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'category_id'
                ) THEN
                    ALTER TABLE api_product RENAME COLUMN catgory_id TO category_id;
                END IF;

                IF EXISTS (
                    SELECT 1
                    FROM information_schema.tables
                    WHERE table_name = 'api_productimage'
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_productimage'
                    AND column_name = 'file'
                ) THEN
                    ALTER TABLE api_productimage ADD COLUMN file varchar(100) NOT NULL DEFAULT '';
                END IF;
            END $$;
            """,
            reverse_sql="""
            DO $$
            BEGIN
                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'description'
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'descrioption'
                ) THEN
                    ALTER TABLE api_product RENAME COLUMN description TO descrioption;
                END IF;

                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'category_id'
                )
                AND NOT EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_product'
                    AND column_name = 'catgory_id'
                ) THEN
                    ALTER TABLE api_product RENAME COLUMN category_id TO catgory_id;
                END IF;

                IF EXISTS (
                    SELECT 1
                    FROM information_schema.columns
                    WHERE table_name = 'api_productimage'
                    AND column_name = 'file'
                ) THEN
                    ALTER TABLE api_productimage DROP COLUMN IF EXISTS file;
                END IF;
            END $$;
            """,
        )
    ]
