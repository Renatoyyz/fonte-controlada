import threading
import time

class Dado:
    def __init__(self):
        self.full_scream = False
        self.CANAL_NPN = 0
        self.CANAL_PNP = 1
        self.CANAL_RELAY = 2

        self.BASE_TEMPO_SEGUNDOS = 0
        self.BASE_TEMPO_MINUTOS = 1

        self.HABILITA_CANAL = 1
        self.DESABILITA_CANAL = 0

    def cria_programa_tupla(self, **kwargs):
        # Valores padrão
        default_values = {
            'nome_programa': '',
            'pnp_canal1_ton': 1.0,
            'pnp_canal1_toff': 1.0,
            'pnp_canal2_ton': 1.0,
            'pnp_canal2_toff': 1.0,
            'pnp_canal3_ton': 1.0,
            'pnp_canal3_toff': 1.0,
            'pnp_canal4_pwm': 50.0,
            'pnp_canal4_periodo_pwm': 1.0,# esse parametro é o periodo do pwm em segundos
            'pnp_base_tempo': self.BASE_TEMPO_SEGUNDOS,
            'pnp_habilita_desabilita': self.DESABILITA_CANAL,
            'pnp_qtd': 1,# esse é a quantidade de ciclos do canal pnp
            'npn_canal1_ton': 1.0,
            'npn_canal1_toff': 1.0,
            'npn_canal2_ton': 1.0,
            'npn_canal2_toff': 1.0,
            'npn_canal3_ton': 1.0,
            'npn_canal3_toff': 1.0,
            'npn_canal4_pwm': 50.0,
            'npn_canal4_periodo_pwm': 17.0,# esse parametro é o periodo do pwm em segundos
            'npn_base_tempo': self.BASE_TEMPO_SEGUNDOS,
            'npn_habilita_desabilita': self.DESABILITA_CANAL,
            'npn_qtd': 1,# esse é a quantidade de ciclos do canal npn
            'rele_canal1_ton':  1.0,
            'rele_canal1_toff': 1.0,
            'rele_canal2_ton': 1.0,
            'rele_canal2_toff': 1.0,
            'rele_canal3_ton': 1.0,
            'rele_canal3_toff': 1.0,
            'rele_canal4_ton': 1.0,
            'rele_canal4_toff': 1.0,
            'rele_base_tempo': self.BASE_TEMPO_SEGUNDOS,
            'rele_habilita_desabilita': self.DESABILITA_CANAL,
            'rele_qtd': 1# esse é a quantidade de ciclos do canal rele
        }

        # Atualizar valores padrão com os fornecidos em kwargs
        default_values.update(kwargs)

        return (
            default_values['nome_programa'], default_values['pnp_canal1_ton'], default_values['pnp_canal1_toff'],
            default_values['pnp_canal2_ton'], default_values['pnp_canal2_toff'], default_values['pnp_canal3_ton'],
            default_values['pnp_canal3_toff'], default_values['pnp_canal4_pwm'], default_values['pnp_canal4_periodo_pwm'],
            default_values['pnp_base_tempo'], default_values['pnp_habilita_desabilita'], default_values['pnp_qtd'],
            default_values['npn_canal1_ton'], default_values['npn_canal1_toff'], default_values['npn_canal2_ton'],
            default_values['npn_canal2_toff'], default_values['npn_canal3_ton'], default_values['npn_canal3_toff'],
            default_values['npn_canal4_pwm'], default_values['npn_canal4_periodo_pwm'], default_values['npn_base_tempo'],
            default_values['npn_habilita_desabilita'], default_values['npn_qtd'], default_values['rele_canal1_ton'],
            default_values['rele_canal1_toff'], default_values['rele_canal2_ton'], default_values['rele_canal2_toff'],
            default_values['rele_canal3_ton'], default_values['rele_canal3_toff'], default_values['rele_canal4_ton'],
            default_values['rele_canal4_toff'], default_values['rele_base_tempo'], default_values['rele_habilita_desabilita'],
            default_values['rele_qtd']
        )
    
    def reset_programa_tupla(self):
        return self.cria_programa_tupla()
    
    def atualiza_programa_tupla(self, db, program_name):
        # Obter os valores do banco de dados
        result = db.read(program_name)
        if not result:
            print(f"Programa {program_name} não encontrado.")
            return None

        # Mapear os valores retornados para os parâmetros correspondentes
        row = result[0]
        kwargs = {
            'nome_programa': row[1],
            'pnp_canal1_ton': row[2],
            'pnp_canal1_toff': row[3],
            'pnp_canal2_ton': row[4],
            'pnp_canal2_toff': row[5],
            'pnp_canal3_ton': row[6],
            'pnp_canal3_toff': row[7],
            'pnp_canal4_pwm': row[8],
            'pnp_canal4_periodo_pwm': row[9],
            'pnp_base_tempo': row[10],
            'pnp_habilita_desabilita': row[11],
            'pnp_qtd': row[12],
            'npn_canal1_ton': row[13],
            'npn_canal1_toff': row[14],
            'npn_canal2_ton': row[15],
            'npn_canal2_toff': row[16],
            'npn_canal3_ton': row[17],
            'npn_canal3_toff': row[18],
            'npn_canal4_pwm': row[19],
            'npn_canal4_periodo_pwm': row[20],
            'npn_base_tempo': row[21],
            'npn_habilita_desabilita': row[22],
            'npn_qtd': row[23],
            'rele_canal1_ton': row[24],
            'rele_canal1_toff': row[25],
            'rele_canal2_ton': row[26],
            'rele_canal2_toff': row[27],
            'rele_canal3_ton': row[28],
            'rele_canal3_toff': row[29],
            'rele_canal4_ton': row[30],
            'rele_canal4_toff': row[31],
            'rele_base_tempo': row[32],
            'rele_habilita_desabilita': row[33],
            'rele_qtd': row[34]
        }

        # Atualizar a tupla com os valores do banco de dados
        return self.cria_programa_tupla(**kwargs)
    
if __name__ == "__main__":
    # Exemplo de uso 1
    dado = Dado()
    data = dado.cria_programa_tupla(nome_programa='Programa1', pnp_canal1_ton=2.0, npn_canal2_toff=14.0)
    print(data)
    data = dado.reset_programa_tupla()# reseta os valores padrão
    print(data)
#****************************************************************************************
    # Exemplo de uso 2
    from Controller.DataBase import DataBase

    db = DataBase()
    dado = Dado()

    # Atualizar a tupla com os valores do banco de dados
    updated_data = dado.atualiza_programa_tupla(db, 'Programa1')
    print(updated_data)