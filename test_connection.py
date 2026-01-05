import MySQLdb

DB_HOST = 'localhost'
DB_USER = 'root'        
DB_PASS = '1868Salam@'

try:
    # 1. Connect to the MySQL SERVER (Note: we are not specifying a db yet)
    print(f"Attempting to connect to MySQL as {DB_USER}...")
    connection = MySQLdb.connect(
        host=DB_HOST, 
        user=DB_USER, 
        passwd=DB_PASS
    )
    print("✅ Connection to MySQL Server successful!")

    # 2. Create a Cursor (This is like a pointer to send commands)
    cursor = connection.cursor()

    # 3. Create the Database
    # This fixes the error you were getting in Django
    db_name = "product_db"
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    print(f"✅ Database '{db_name}' created successfully.")

    # 4. Close the connection
    cursor.close()
    connection.close()

except MySQLdb.Error as e:
    print(f"❌ Error connecting to MySQL: {e}")