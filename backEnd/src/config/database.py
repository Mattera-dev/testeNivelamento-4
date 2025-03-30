import mysql.connector
from src.config.env import getConfig

config = getConfig()

class Database:
    def __init__(self):
        ok, conn = self.__connect()
        if ok:
            self.conn = conn
    
    def __connect(self):
        try:
            conn = mysql.connector.connect(
                host=config["database"]["host"],
                user=config["database"]["user"],
                password=config["database"]["password"],
                database=config["database"]["dbname"],
                port=config["database"]["port"],
                charset='utf8mb3'
            )
            
            if conn.is_connected():
                return (True, conn)
        except Exception as e:
            raise e
        
        
    def query(self, **kwargs):
        if not self.conn.is_connected():
            return (False, "Database not connected")
        ofset = 20
        try:
            query = "SELECT * FROM `operadora` WHERE 1=1"
            if "name" in kwargs:
                query += f" AND Razao_Social like '{kwargs['name']}%' OR Nome_Fantasia like '{kwargs['name']}%'"
            query += " LIMIT 20"
            if "offset" in kwargs and kwargs["offset"] > 0:
                query += f" OFFSET {kwargs["offset"] * ofset}"
            cursor = self.conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            if len(results) != 0:
                return (True, results)
            return (False, [])
        except Exception as e:
            raise e
        finally:
            cursor.close()
