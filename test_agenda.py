import unittest
from datetime import date

from prenotazioni import (
    Agenda,
    Sala,
    SalaNonTrovata
)


class TestAgenda(unittest.TestCase):
    def setUp(self):
        self.oggi = date(2026, 11, 16)
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A2", "Aula 2", 25))

    def test_aggiungi_sala_rifiuta_codice_duplicato(self):
        duplicata = Sala("A2", "Seconda aula", 30)

        with self.assertRaises(ValueError):
            self.agenda.aggiungi_sala(duplicata)
    
    def test_sala_rifiuta_codice_inesistente(self):
        with self.assertRaises(SalaNonTrovata):
            self.agenda.sala("INESISTENTE")