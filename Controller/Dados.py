import threading
import time

class Dado:
    def __init__(self):
        self.full_scream = False
        self.mouse_pointer = False
        self.CANAL_NPN = 0
        self.CANAL_PNP = 1
        self.CANAL_RELAY = 2

        self.BASE_TEMPO_SEGUNDOS = 0
        self.BASE_TEMPO_MINUTOS = 1

        self.programa_salvo = None
        self.nome_programa = ''

        self.HABILITA_CANAL = 1
        self.DESABILITA_CANAL = 0
        self.salva_programa_tupla(self.reset_programa_tupla())

    def cria_programa_tupla(self, **kwargs):
        # Valores padrão
        default_values = {
            'nome_programa': '',  # Indice 0
            'pnp_canal1_ton': 1.0,
            'pnp_canal1_toff': 1.0,
            'pnp_canal1_qtd': 1,
            'pnp_canal2_ton': 1.0,
            'pnp_canal2_toff': 1.0,
            'pnp_canal2_qtd': 1,
            'pnp_canal3_ton': 1.0,
            'pnp_canal3_toff': 1.0,
            'pnp_canal3_qtd': 1,
            'pnp_canal4_pwm': 50.0,
            'pnp_canal4_periodo_pwm': 1.0,  # esse parametro é o periodo do pwm em segundos
            'pnp_canal4_ton': 1.0,
            'pnp_canal4_toff': 1.0,
            'pnp_canal4_qtd': 1,
            'pnp_base_tempo': self.BASE_TEMPO_SEGUNDOS,
            'pnp_habilita_desabilita': self.DESABILITA_CANAL,
            'npn_canal1_ton': 1.0,  # Indice 17
            'npn_canal1_toff': 1.0,
            'npn_canal1_qtd': 1,
            'npn_canal2_ton': 1.0,
            'npn_canal2_toff': 1.0,
            'npn_canal2_qtd': 1,
            'npn_canal3_ton': 1.0,
            'npn_canal3_toff': 1.0,
            'npn_canal3_qtd': 1,
            'npn_canal4_pwm': 50.0,
            'npn_canal4_periodo_pwm': 1.0,  # esse parametro é o periodo do pwm em segundos
            'npn_canal4_ton': 1.0,
            'npn_canal4_toff': 1.0,
            'npn_canal4_qtd': 1,
            'npn_base_tempo': self.BASE_TEMPO_SEGUNDOS,
            'npn_habilita_desabilita': self.DESABILITA_CANAL,
            'rele_canal1_ton': 1.0,  # Indice 33
            'rele_canal1_toff': 1.0,
            'rele_canal1_qtd': 1,
            'rele_canal2_ton': 1.0,
            'rele_canal2_toff': 1.0,
            'rele_canal2_qtd': 1,
            'rele_canal3_ton': 1.0,
            'rele_canal3_toff': 1.0,
            'rele_canal3_qtd': 1,
            'rele_canal4_ton': 1.0,
            'rele_canal4_toff': 1.0,
            'rele_canal4_qtd': 1,
            'rele_base_tempo': self.BASE_TEMPO_SEGUNDOS,
            'rele_habilita_desabilita': self.DESABILITA_CANAL
        }

        # Atualizar valores padrão com os fornecidos em kwargs
        default_values.update(kwargs)

        return (
            default_values['nome_programa'], default_values['pnp_canal1_ton'], default_values['pnp_canal1_toff'],
            default_values['pnp_canal1_qtd'], default_values['pnp_canal2_ton'], default_values['pnp_canal2_toff'],
            default_values['pnp_canal2_qtd'], default_values['pnp_canal3_ton'], default_values['pnp_canal3_toff'],
            default_values['pnp_canal3_qtd'], default_values['pnp_canal4_pwm'], default_values['pnp_canal4_periodo_pwm'],
            default_values['pnp_canal4_ton'], default_values['pnp_canal4_toff'], default_values['pnp_canal4_qtd'],
            default_values['pnp_base_tempo'], default_values['pnp_habilita_desabilita'], default_values['npn_canal1_ton'],
            default_values['npn_canal1_toff'], default_values['npn_canal1_qtd'], default_values['npn_canal2_ton'],
            default_values['npn_canal2_toff'], default_values['npn_canal2_qtd'], default_values['npn_canal3_ton'],
            default_values['npn_canal3_toff'], default_values['npn_canal3_qtd'], default_values['npn_canal4_pwm'],
            default_values['npn_canal4_periodo_pwm'], default_values['npn_canal4_ton'], default_values['npn_canal4_toff'],
            default_values['npn_canal4_qtd'], default_values['npn_base_tempo'], default_values['npn_habilita_desabilita'],
            default_values['rele_canal1_ton'], default_values['rele_canal1_toff'], default_values['rele_canal1_qtd'],
            default_values['rele_canal2_ton'], default_values['rele_canal2_toff'], default_values['rele_canal2_qtd'],
            default_values['rele_canal3_ton'], default_values['rele_canal3_toff'], default_values['rele_canal3_qtd'],
            default_values['rele_canal4_ton'], default_values['rele_canal4_toff'], default_values['rele_canal4_qtd'],
            default_values['rele_base_tempo'], default_values['rele_habilita_desabilita']
        )
    
    def salva_programa_tupla(self, tupla):
        self.programa_salvo = tupla

    def resgata_programa_tupla(self):
        self.programa_salvo = getattr(self, 'programa_salvo', None)
        return self.programa_salvo

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
            'pnp_canal1_qtd': row[4],
            'pnp_canal2_ton': row[5],
            'pnp_canal2_toff': row[6],
            'pnp_canal2_qtd': row[7],
            'pnp_canal3_ton': row[8],
            'pnp_canal3_toff': row[9],
            'pnp_canal3_qtd': row[10],
            'pnp_canal4_pwm': row[11],
            'pnp_canal4_periodo_pwm': row[12],
            'pnp_canal4_ton': row[13],
            'pnp_canal4_toff': row[14],
            'pnp_canal4_qtd': row[15],
            'pnp_base_tempo': row[16],
            'pnp_habilita_desabilita': row[17],
            'npn_canal1_ton': row[18],
            'npn_canal1_toff': row[19],
            'npn_canal1_qtd': row[20],
            'npn_canal2_ton': row[21],
            'npn_canal2_toff': row[22],
            'npn_canal2_qtd': row[23],
            'npn_canal3_ton': row[24],
            'npn_canal3_toff': row[25],
            'npn_canal3_qtd': row[26],
            'npn_canal4_pwm': row[27],
            'npn_canal4_periodo_pwm': row[28],
            'npn_canal4_ton': row[29],
            'npn_canal4_toff': row[30],
            'npn_canal4_qtd': row[31],
            'npn_base_tempo': row[32],
            'npn_habilita_desabilita': row[33],
            'rele_canal1_ton': row[34],
            'rele_canal1_toff': row[35],
            'rele_canal1_qtd': row[36],
            'rele_canal2_ton': row[37],
            'rele_canal2_toff': row[38],
            'rele_canal2_qtd': row[39],
            'rele_canal3_ton': row[40],
            'rele_canal3_toff': row[41],
            'rele_canal3_qtd': row[42],
            'rele_canal4_ton': row[43],
            'rele_canal4_toff': row[44],
            'rele_canal4_qtd': row[45],
            'rele_base_tempo': row[46],
            'rele_habilita_desabilita': row[47]
        }

        # Atualizar a tupla com os valores do banco de dados
        return self.cria_programa_tupla(**kwargs)
    
if __name__ == "__main__":
    # Exemplo de uso 1
    dado = Dado()
    data = dado.cria_programa_tupla(nome_programa='Programa1', pnp_canal1_ton=2.0, npn_canal2_toff=14.0)
    print(data)
    data = dado.reset_programa_tupla()  # reseta os valores padrão
    print(data)
    
    # Exemplo de uso 2
    from Controller.DataBase import DataBase

    db = DataBase()
    dado = Dado()

    # Atualizar a tupla com os valores do banco de dados
    updated_data = dado.atualiza_programa_tupla(db, 'Programa1')
    print(updated_data)