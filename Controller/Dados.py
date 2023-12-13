import threading
import time

class Dado:
    def __init__(self):
        self._nome_prog = ""

    @property
    def nome_prog(self):
        return self._nome_prog
    def set_nome_prog(self, nome):
        self._nome_prog = nome