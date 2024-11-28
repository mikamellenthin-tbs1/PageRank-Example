# Pagerank-Example

Dieses Projekt demonstriert den PageRank-Algorithmus in Python.

## Continuous Integration

Wir nutzen GitHub Actions für Continuous Integration, um die Kompatibilität über mehrere Python-Versionen und Betriebssysteme hinweg sicherzustellen.

### Workflow-Details

- **Pfad**: `.github/workflows/ci.yml`
- **Auslöser**: Bei Push oder Pull Request zum `main`-Branch.
- **Testmatrix**:
  - **Betriebssysteme**: Ubuntu, Windows, MacOS
  - **Python-Versionen**: 3.11, 3.12, 3.13(dev)

### Lokale Tests ausführen

Um Tests lokal auszuführen, verwende:

```bash
python -m unittest discover -s tests
