# Created by Mika Mellenthin - 05.11.2024
# Pagerank example (LF11a)

class Page:
    def __init__(self, id):
        self.id = id
        self.pagerank = 1.0
        self.outgoing_links = []
        self.incoming_links = []

    def add_outgoing_link(self, page):
        """Verbindet diese Seite mit einer anderen Seite (ausgehender Link)."""
        if page not in self.outgoing_links:  # Vermeidet doppelte Links
            self.outgoing_links.append(page)
            page.incoming_links.append(self)  # Verknüpft die eingehenden Links auf die Zielseite


class Graph:
    def __init__(self):
        self.pages = []

    def add_page(self, page):
        """Fügt eine Seite zum Graphen hinzu."""
        if page not in self.pages:
            self.pages.append(page)

    def calculate_pagerank(self, damping_factor=0.85, tolerance=0.0001):
        """Berechnet den PageRank für jede Seite im Graphen bis zur Konvergenz."""
        num_pages = len(self.pages)
        if num_pages == 0:
            return

        # Initialisiert alle PageRank-Werte gleichmäßig
        for page in self.pages:
            page.pagerank = 1.0 / num_pages

        while True:
            new_ranks = {}
            max_change = 0  # Verfolgt die größte Änderung in einer Iteration

            for page in self.pages:
                # Berechnet den PageRank basierend auf eingehenden Links
                rank_sum = sum(
                    incoming_page.pagerank / len(incoming_page.outgoing_links)
                    for incoming_page in page.incoming_links
                )
                # Aktualisiert den PageRank-Wert unter Berücksichtigung des Dämpfungsfaktors
                new_ranks[page.id] = (1 - damping_factor) / num_pages + damping_factor * rank_sum

            # Aktualisiert alle PageRank-Werte und prüft die Konvergenz
            for page in self.pages:
                change = abs(new_ranks[page.id] - page.pagerank)
                max_change = max(max_change, change)
                page.pagerank = new_ranks[page.id]

            # Prüft, ob die Änderung kleiner als der Toleranzwert ist
            if max_change < tolerance:
                break  # Beendet die Iteration, wenn alle Änderungen klein genug sind

    def add_link(self, page_from, page_to):
        """Fügt einen Link von einer Seite zur anderen hinzu."""
        page_from.add_outgoing_link(page_to)


# Neues Objekt vom Typ 'Graph' erstellen
graph = Graph()

# Knoten erstellen
page_a1 = Page("A1")
page_b1 = Page("B1")
page_a2 = Page("A2")
page_b2 = Page("B2")
page_c2 = Page("C2")
page_a3 = Page("A3")
page_b3 = Page("B3")
page_c3 = Page("C3")
page_a4 = Page("A4")
page_b4 = Page("B4")
page_c4 = Page("C4")

# Knoten zum Graphen hinzufügen
graph.add_page(page_a1)
graph.add_page(page_b1)
graph.add_page(page_a2)
graph.add_page(page_b2)
graph.add_page(page_c2)
graph.add_page(page_a3)
graph.add_page(page_b3)
graph.add_page(page_c3)
graph.add_page(page_a4)
graph.add_page(page_b4)
graph.add_page(page_c4)

# Verbindungen hinzufügen
graph.add_link(page_a1, page_b1)
graph.add_link(page_b1, page_a1)

graph.add_link(page_a2, page_c2)
graph.add_link(page_c2, page_b2)
graph.add_link(page_b2, page_a2)

graph.add_link(page_a3, page_b3)
graph.add_link(page_b3, page_a3)
graph.add_link(page_b3, page_c3)
graph.add_link(page_c3, page_a3)

graph.add_link(page_a4, page_b4)
graph.add_link(page_b4, page_c4)

# Berechnung des PageRanks
graph.calculate_pagerank()

# Ausgabe der PageRank-Werte
print("Untergraph 1:")
for page in [page_a1, page_b1]:
    print(f"Page {page.id}: PageRank = {page.pagerank:.4f}")

print("\nUntergraph 2:")
for page in [page_a2, page_b2, page_c2]:
    print(f"Page {page.id}: PageRank = {page.pagerank:.4f}")

print("\nUntergraph 3:")
for page in [page_a3, page_b3, page_c3]:
    print(f"Page {page.id}: PageRank = {page.pagerank:.4f}")

print("\nUntergraph 4:")
for page in [page_a4, page_b4, page_c4]:
    print(f"Page {page.id}: PageRank = {page.pagerank:.4f}")