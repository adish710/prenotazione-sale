import unittest
from datetime import date

from prenotazioni import Agenda, Prenotazione, Sala


class TestSegnalazioni(unittest.TestCase):
    def setUp(self):
        self.oggi = date(2026, 11, 16)
        self.giorno = date(2026, 11, 17)
        self.agenda = Agenda()
        self.agenda.aggiungi_sala(Sala("A2", "Aula 2", 25, ["lavagna"]))
        self.agenda.aggiungi_sala(Sala("R1", "Sala riunioni", 10))

    def test_prenotazioni_contigue_non_si_sovrappongono(self):
        prenotazione_precedente = Prenotazione(
            "A2", self.giorno, "09:00", "10:00", "Mario Rossi", 20
        )
        prenotazione_contigua = Prenotazione(
            "A2", self.giorno, "10:00", "11:00", "Luigi Bianchi", 20
        )

        id_precedente = self.agenda.prenota(prenotazione_precedente, self.oggi)
        id_contigua = self.agenda.prenota(prenotazione_contigua, self.oggi)

        self.assertEqual(id_precedente, 1)
        self.assertEqual(id_contigua, 2)

    def test_partecipanti_esattamente_uguali_alla_capienza(self):
        prenotazione = Prenotazione(
            "R1", self.giorno, "09:00", "10:00", "Anna Verdi", 10
        )

        identificativo = self.agenda.prenota(prenotazione, self.oggi)

        self.assertEqual(identificativo, 1)
        self.assertIn(identificativo, self.agenda.prenotazioni)


if __name__ == "__main__":
    unittest.main()
