import unittest
from pagerank.pagerank_example import Page, Graph

class TestPageRank(unittest.TestCase):
    def setUp(self):
        # Graphen und Beispielseiten initialisieren
        self.graph = Graph()
        self.page_a1 = Page("A1")
        self.page_b1 = Page("B1")
        self.page_a2 = Page("A2")
        self.page_b2 = Page("B2")
        self.page_c2 = Page("C2")

        # Seiten zum Graphen hinzufügen
        for page in [self.page_a1, self.page_b1, self.page_a2, self.page_b2, self.page_c2]:
            self.graph.add_page(page)

        # Verbindungen hinzufügen
        self.graph.add_link(self.page_a1, self.page_b1)
        self.graph.add_link(self.page_b1, self.page_a1)
        self.graph.add_link(self.page_a2, self.page_c2)
        self.graph.add_link(self.page_c2, self.page_b2)
        self.graph.add_link(self.page_b2, self.page_a2)

    def test_page_initialization(self):
        # Testet die Initialisierung der Page-Objekte
        self.assertEqual(self.page_a1.id, "A1")
        self.assertEqual(self.page_a1.pagerank, 1.0)
        self.assertEqual(len(self.page_a1.outgoing_links), 1)
        self.assertEqual(len(self.page_a1.incoming_links), 1)

    def test_add_link(self):
        # Überprüft, ob Links korrekt hinzugefügt wurden
        self.assertIn(self.page_b1, self.page_a1.outgoing_links)
        self.assertIn(self.page_a1, self.page_b1.incoming_links)

    def test_pagerank_calculation(self):
        # Berechnet den PageRank und überprüft die Ergebnisse
        self.graph.calculate_pagerank(damping_factor=0.85, tolerance=0.0001)
        
        # Summe des PageRanks überprüfen (sollte ungefähr 1.0 sein)
        total_rank = sum(page.pagerank for page in [self.page_a1, self.page_b1, self.page_a2, self.page_b2, self.page_c2])
        self.assertAlmostEqual(total_rank, 1.0, places=2)

        # Überprüfen, dass die PageRank-Werte zwischen 0 und 1 liegen
        for page in [self.page_a1, self.page_b1, self.page_a2, self.page_b2, self.page_c2]:
            self.assertGreaterEqual(page.pagerank, 0)
            self.assertLessEqual(page.pagerank, 1)

    def test_no_links(self):
        # Testet den Fall, wenn eine Seite ohne Links vorhanden ist
        isolated_page = Page("D")
        self.graph.add_page(isolated_page)
        self.graph.calculate_pagerank()
        
        # Der PageRank-Wert für eine isolierte Seite kann niedrig sein
        self.assertGreaterEqual(isolated_page.pagerank, 0.01)

    def test_damping_factor_variation(self):
        # Testet die Auswirkungen des Dämpfungsfaktors auf das Ergebnis
        self.graph.calculate_pagerank(damping_factor=0.85)
        rank_with_85 = self.page_a1.pagerank
        
        # Füge mehr Knoten hinzu, um den Dämpfungsfaktor-Effekt zu verdeutlichen
        additional_page = Page("Extra")
        self.graph.add_page(additional_page)
        self.graph.add_link(additional_page, self.page_a1)
        
        self.graph.calculate_pagerank(damping_factor=0.5)
        rank_with_50 = self.page_a1.pagerank
        
        # Die PageRank-Werte sollten unterschiedlich sein
        self.assertNotEqual(rank_with_85, rank_with_50)

    def test_tolerance_effect(self):
        # Testet die Auswirkungen unterschiedlicher Toleranzwerte
        self.graph.calculate_pagerank(tolerance=0.001)
        rank_with_001 = self.page_a1.pagerank
        
        self.graph.calculate_pagerank(tolerance=0.00001)
        rank_with_00001 = self.page_a1.pagerank
        
        # Die PageRank-Werte bei strengerer Toleranz sollten stabil bleiben
        self.assertAlmostEqual(rank_with_001, rank_with_00001, places=4)

if __name__ == '__main__':
    unittest.main()