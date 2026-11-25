import unittest
from datetime import date

from prenotazioni import (
    Agenda,
    Sala,
    SalaNonTrovata,
    timedelta,
    Prenotazione,
    DataNonAmmessa,
    PrenotazioneNonTrovata
    
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

    def test_prenota_rifiuta_date_non_ammesse(self):
        date_non_ammesse = (
            (self.oggi - timedelta(days=1), "data passata"),
            (date(2026, 11, 22), "domenica"),
            (self.oggi + timedelta(days=61), "oltre l'orizzonte"),
        )
        for giorno, motivo in date_non_ammesse:
            with self.subTest(motivo=motivo):
                prenotazione = Prenotazione(
                    "A2", giorno, "09:00", "10:00", "Mario Rossi", 10
                )
                with self.assertRaises(DataNonAmmessa):
                    self.agenda.prenota(prenotazione, self.oggi)
    
    def test_prenota_accetta_la_data_di_oggi(self):
        prenotazione = Prenotazione(
            "A2", self.oggi, "09:00", "10:00", "Mario Rossi", 10
        )

        identificativo = self.agenda.prenota(prenotazione, self.oggi)

        self.assertEqual(identificativo, 1)

    def test_cancella_rifiuta_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.cancella(999)

    def test_prenotazione_rifiuta_id_inesistente(self):
        with self.assertRaises(PrenotazioneNonTrovata):
            self.agenda.prenotazione(999)


if __name__ == "__main__":
    unittest.main()