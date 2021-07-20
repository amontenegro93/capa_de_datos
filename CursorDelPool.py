from Conexion import Conexion
from logger_base import log

class CursorDelPool:
    def __init__(self):
        self._conexion=None
        self._cursor=None

    def __enter__(self):
        log.debug('inicio enter')
        self._conexion=Conexion.obtenerConexion()
        self._cursor=self._conexion.cursor()
        return self._cursor

    def __exit__(self,tipo_exepcion,valor_exepcion,detalle_exepcion):
        log.debug('inicio exit')
        if valor_exepcion:
            self._conexion.rollback()
            log.error(f'error: {valor_exepcion}{tipo_exepcion}{detalle_exepcion}')
        else:
            self._conexion.commit()
            log.debug(f'commit')
        self._cursor.close()
        Conexion.liberarConexion(self._conexion)

if __name__ == '__main__':
    with CursorDelPool() as cursor:
        log.debug('adentro')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
