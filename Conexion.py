from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    _DATABASE = 'mydb'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CONEXIONES=1
    _MAX_CONEXIONES=5
    _pool=None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool=pool.SimpleConnectionPool(cls._MIN_CONEXIONES,cls._MAX_CONEXIONES,
                                                    host=cls._HOST,
                                                    user=cls._USERNAME,
                                                    password=cls._PASSWORD,
                                                    port=cls._DB_PORT,
                                                    database=cls._DATABASE)
                log.debug(f'pool exitoso: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'error pool: {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion=cls.obtenerPool().getconn()
        log.debug(f'conexion obtenida: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'regresamos la conexion al pool {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()

if __name__ == '__main__':
    conexion1= Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    conexion2= Conexion.obtenerConexion()
    # conexion3= Conexion.obtenerConexion()
    # conexion4= Conexion.obtenerConexion()
    # conexion5= Conexion.obtenerConexion()


