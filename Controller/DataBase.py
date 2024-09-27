import sqlite3

class DataBase:
    def __init__(self, db_name='database.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS programas (
                    id INTEGER PRIMARY KEY,
                    nome_programa TEXT,
                    pnp_canal1_ton REAL,
                    pnp_canal1_toff REAL,
                    pnp_canal2_ton REAL,
                    pnp_canal2_toff REAL,
                    pnp_canal3_ton REAL,
                    pnp_canal3_toff REAL,
                    pnp_canal4_pwm REAL,
                    pnp_canal4_periodo_pwm REAL,
                    pnp_base_tempo REAL,
                    pnp_habilita_desabilita INTEGER,
                    pnp_qtd INTEGER,
                    npn_canal1_ton REAL,
                    npn_canal1_toff REAL,
                    npn_canal2_ton REAL,
                    npn_canal2_toff REAL,
                    npn_canal3_ton REAL,
                    npn_canal3_toff REAL,
                    npn_canal4_pwm REAL,
                    npn_canal4_periodo_pwm REAL,
                    npn_base_tempo REAL,
                    npn_habilita_desabilita INTEGER,
                    npn_qtd INTEGER,
                    rele_canal1_ton REAL,
                    rele_canal1_toff REAL,
                    rele_canal2_ton REAL,
                    rele_canal2_toff REAL,
                    rele_canal3_ton REAL,
                    rele_canal3_toff REAL,
                    rele_canal4_ton REAL,
                    rele_canal4_toff REAL,
                    rele_base_tempo REAL,
                    rele_habilita_desabilita INTEGER,
                    rele_qtd INTEGER
                )
            ''')
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar a tabela: {e}")

    def create(self, data):
        try:
            self.cursor.execute('''
                INSERT INTO programas (
                    nome_programa, pnp_canal1_ton, pnp_canal1_toff, pnp_canal2_ton, pnp_canal2_toff, 
                    pnp_canal3_ton, pnp_canal3_toff, pnp_canal4_pwm, pnp_canal4_periodo_pwm, pnp_base_tempo, 
                    pnp_habilita_desabilita, pnp_qtd, npn_canal1_ton, npn_canal1_toff, npn_canal2_ton, npn_canal2_toff, 
                    npn_canal3_ton, npn_canal3_toff, npn_canal4_pwm, npn_canal4_periodo_pwm, npn_base_tempo, 
                    npn_habilita_desabilita, npn_qtd, rele_canal1_ton, rele_canal1_toff, rele_canal2_ton, rele_canal2_toff, 
                    rele_canal3_ton, rele_canal3_toff, rele_canal4_ton, rele_canal4_toff, rele_base_tempo, 
                    rele_habilita_desabilita, rele_qtd
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', data)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao inserir dados: {e}")

    def read(self, program_name):
        try:
            self.cursor.execute('SELECT * FROM programas WHERE nome_programa = ?', (program_name,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
            return None
        
    def read_all(self):
        try:
            self.cursor.execute('SELECT * FROM programas')
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao ler dados: {e}")
            return None

    def update(self, program_name, data):
        try:
            self.cursor.execute('''
                UPDATE programas SET 
                    pnp_canal1_ton = ?, pnp_canal1_toff = ?, pnp_canal2_ton = ?, pnp_canal2_toff = ?, 
                    pnp_canal3_ton = ?, pnp_canal3_toff = ?, pnp_canal4_pwm = ?, pnp_canal4_periodo_pwm = ?, 
                    pnp_base_tempo = ?, pnp_habilita_desabilita = ?, pnp_qtd = ?, npn_canal1_ton = ?, npn_canal1_toff = ?, 
                    npn_canal2_ton = ?, npn_canal2_toff = ?, npn_canal3_ton = ?, npn_canal3_toff = ?, 
                    npn_canal4_pwm = ?, npn_canal4_periodo_pwm = ?, npn_base_tempo = ?, npn_habilita_desabilita = ?, 
                    npn_qtd = ?, rele_canal1_ton = ?, rele_canal1_toff = ?, rele_canal2_ton = ?, rele_canal2_toff = ?, 
                    rele_canal3_ton = ?, rele_canal3_toff = ?, rele_canal4_ton = ?, rele_canal4_toff = ?, 
                    rele_base_tempo = ?, rele_habilita_desabilita = ?, rele_qtd = ?
                WHERE nome_programa = ?
            ''', data + (program_name,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao atualizar dados: {e}")

    def delete(self, program_name):
        try:
            self.cursor.execute('DELETE FROM programas WHERE nome_programa = ?', (program_name,))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao deletar dados: {e}")

    def __del__(self):
        self.connection.close()

# Exemplo de uso
if __name__ == "__main__":
    db = DataBase()

    # Criar um novo registro
    data = (
        'Programa1', 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 1, 10, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 1, 20, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 1, 30
    )
    db.create(data)

    # Cria mais um registro
    data = (
        'Programa2', 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 0, 11, 10.1, 11.1, 12.1, 13.1, 14.1, 15.1, 16.1, 17.1, 18.1, 0, 21, 19.1, 20.1, 21.1, 22.1, 23.1, 24.1, 25.1, 26.1, 27.1, 0, 31
    )
    db.create(data)


    # Ler registros
    print(db.read('Programa1'))

    # Atualizar um registro
    updated_data = (
        1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1, 9.1, 0, 11, 10.1, 11.1, 12.1, 13.1, 14.1, 15.1, 16.1, 17.1, 18.1, 0, 21, 19.1, 20.1, 21.1, 22.1, 23.1, 24.1, 25.1, 26.1, 27.1, 0, 31
    )
    db.update('Programa1', updated_data)

    # Ler registros novamente para verificar a atualização
    print(db.read('Programa1'))

    # Ler todos os registros
    all = db.read_all()
    print(len(all))
    for row in all:
        print(row[1])

    # Deletar um registro
    db.delete('Programa1')
    db.delete('Programa2')

    # Ler registros novamente para verificar a exclusão
    print(db.read('Programa1'))
    print(db.read('Programa2'))