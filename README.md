# API-Call-Similarity-Network-Graph

This project explores the similarity between malware samples by analyzing their API call sequences. Malware often exhibits similar behavior through sequences of API calls, making it possible to identify relationships between different samples. The project involves loading a dataset containing API call sequences per malware sample, extracting unique sequences, calculating the Jaccard Similarity between pairs of samples, and visualizing the connected samples as a graph. The resulting graph provides insights into clusters of similar malware samples based on their API call behavior.

## Key Features

- **Dataset Loading:** Load and preprocess the dataset containing API call sequences per malware sample.
- **Unique API Sequences:** Extract unique API call sequences from malware samples for analysis.
- **Jaccard Similarity:** Calculate the Jaccard Similarity between pairs of malware samples based on their unique API sequences.
- **Graph Visualization:** Visualize connected malware samples as a graph using NetworkX.
- **Export Graph:** Export the graph in DOT format for further analysis or visualization.

## Usage

1. Clone the repository: `git clone https://github.com/your_username/malware-similarity-analysis.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the script: `python malware_similarity_analysis.py`
4. Explore the generated DOT file to visualize connected malware samples.