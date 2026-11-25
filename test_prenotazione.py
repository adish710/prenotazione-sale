import unittest
from datetime import date

from prenotazioni import Prenotazione


class TestPrenotazione(unittest.TestCase):
    def setUp(self):
        self.giorno = date(2026, 11, 16)
        self.dati = ("A2", self.giorno, "09:00", "10:00", "Mario Rossi", 10)

    def test_orari_non_ammessi_solleva_value_error(self):
        casi = (
            ("09:15", "10:15", "inizio non multiplo"),
            ("07:30", "09:30", "inizio prima dell'apertura"),
            ("19:00", "20:30", "fine dopo la chiusura"),
            ("10:00", "10:00", "fine uguale all'inizio"),
            ("11:00", "10:00", "fine precedente all'inizio"),
        )
        for inizio, fine, motivo in casi:
            with self.subTest(motivo=motivo):
                with self.assertRaises(ValueError):
                    Prenotazione(
                        "A2",
                        self.giorno,
                        inizio,
                        fine,
                        "Mario Rossi",
                        10,
                    )

    def test_giorno_non_date_solleva_type_error(self):
        with self.assertRaises(TypeError):
            Prenotazione(
                "A2",
                "2026-11-16",
                "09:00",
                "10:00",
                "Mario Rossi",
                10,
            )

    def test_durata_minuti_restituisce_la_differenza(self):
        prenotazione = Prenotazione(*self.dati[:2], "09:00", "10:30", *self.dati[4:])

        durata = prenotazione.durata_minuti()

        self.assertEqual(durata, 90)


if __name__ == "__main__":
    unittest.main()