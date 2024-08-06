import psycopg2
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.engine import reflection

# Database connection details
products_db_config = {
    'dbname': 'tradepoint_fresh',
    'user': 'tradepoint',
    'password': 'qg5fyzjs08o2k9gk',
    'host': 'db-postgresql-cluster-do-user-7089764-0-347d.b.db.ondigitalocean.com',
    'port': '25060'
}

staging_db_config = {
    'dbname': 'tradepoint_staging_pool',
    'user': 'tradepoint',
    'password': 'qg5fyzjs08o2k9gk',
    'host': 'db-postgresql-cluster-do-user-7089764-0-347d.b.db.ondigitalocean.com',
    'port': '25061'
}

def get_engine(db_config):
    connection_str = f"postgresql+psycopg2://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}"
    return create_engine(connection_str)

def get_table_schemas(engine):
    inspector = reflection.Inspector.from_engine(engine)
    table_schemas = {}
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        table_schemas[table_name] = columns
    return table_schemas

def compare_schemas(schema1, schema2):
    differences = []
    tables1 = set(schema1.keys())
    tables2 = set(schema2.keys())

    for table in tables1.union(tables2):
        if table not in schema1:
            differences.append(f"Table {table} is missing in schema1")
        elif table not in schema2:
            differences.append(f"Table {table} is missing in schema2")
        else:
            columns1 = {col['name']: col for col in schema1[table]}
            columns2 = {col['name']: col for col in schema2[table]}
            all_columns = set(columns1.keys()).union(columns2.keys())
            for column in all_columns:
                if column not in columns1:
                    differences.append(f"Column {column} in table {table} is missing in schema1")
                elif column not in columns2:
                    differences.append(f"Column {column} in table {table} is missing in schema2")
                else:
                    col1 = columns1[column]
                    col2 = columns2[column]
                    if col1 != col2:
                        differences.append(f"Column {column} in table {table} differs: {col1} vs {col2}")
    return differences

def main():
    products_engine = get_engine(products_db_config)
    staging_engine = get_engine(staging_db_config)

    products_schema = get_table_schemas(products_engine)
    staging_schema = get_table_schemas(staging_engine)

    differences = compare_schemas(products_schema, staging_schema)

    if differences:
        print("Differences found:")
        for diff in differences:
            print(diff)
    else:
        print("No differences found.")

if __name__ == "__main__":
    main()
