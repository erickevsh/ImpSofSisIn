def create_materia(self, conn, materia):
    try:
        sql = '''INSERT INTO
        materias (id, nombre, alumno, calificacion)
        VALUES (?, ?, ?, ?)'''
        cur = conn.cursor()
        cur.execute(sql, materia)
        conn.commit()
        msg = "Registered Succesfully"
    except:
        conn.rollback()
        msg = "Error occured"
    return msg