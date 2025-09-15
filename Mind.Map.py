# mindmap.py
# Generate a mind map (graph) from text input using spaCy + NetworkX

import spacy
import networkx as nx
import matplotlib.pyplot as plt

# Load English NLP model (first run: python -m spacy download en_core_web_sm)
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    """
    Extracts multi-word noun phrases as key concepts.
    """
    doc = nlp(text)
    keywords = [chunk.text.strip() for chunk in doc.noun_chunks if len(chunk.text.split()) > 1]
    return keywords

def build_graph(keywords):
    """
    Builds a simple undirected graph where words inside phrases are linked.
    """
    G = nx.Graph()
    for kw in keywords:
        words = kw.split()
        for i in range(len(words)-1):
            G.add_edge(words[i], words[i+1])
    return G

def draw_graph(G, title="Mind Map"):
    """
    Visualizes the graph using matplotlib.
    """
    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(G, seed=42)  # reproducible layout
    nx.draw(
        G, pos,
        with_labels=True,
        node_color="lightblue",
        node_size=2000,
        font_size=10,
        edge_color="gray",
        linewidths=1,
        font_weight="bold"
    )
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    # Example text — replace this with any notes, article, or essay
    text = """
    Artificial intelligence is a branch of computer science that aims to
    create intelligent machines. It has applications in robotics, natural
    language processing, computer vision, and machine learning.
    """
    keywords = extract_keywords(text)
    print("Extracted keywords:", keywords)
    G = build_graph(keywords)
    draw_graph(G, title="AI Concepts Mind Map")
