import pandas as pd
import networkx as nx
import pydot

#Step 1: Load the dataset

dataset_file = 'dynamic_api_call_sequence_per_malware_100_0_306.csv'

dataset = pd.read_csv(dataset_file)

#print(dataset.head())

#Step 2: Filter the dataset to include only malware samples

malware_dataset = dataset[dataset['malware'] == 1].head(100)

#print(malware_dataset.head())

#Step 3: Extract the unique API calls from malware samples

unique_api_sequences = []
for _, row in malware_dataset.iterrows():
  api_sequence = tuple(row[1:101].unique())  # Extract and convert to tuple
  unique_api_sequences.append(api_sequence)

print(f"Number of unique API sequences: {len(unique_api_sequences)}")

#print(unique_api_calls)

#Step 4: Compare each pair of malware samples and calculate the Jaccard Similarity

connected_pairs = []
threshold = 0.7

print(f"Threshold value: {threshold}")

for i in range(len(unique_api_sequences)):

    for j in range(i + 1, len(unique_api_sequences)):

        intersection = set(unique_api_sequences[i]).intersection(set(unique_api_sequences[j]))
        union = set(unique_api_sequences[i]).union(set(unique_api_sequences[j]))

        jaccard_similarity = len(intersection) / len(union)

        #print(f"Jaccard Similarity between malware {i} and malware {j}: {jaccard_similarity}")

        if jaccard_similarity > threshold:
            connected_pairs.append((i, j))

        
print(f"Number of connected malware samples: {len(connected_pairs)}")

#Step 5: Create a graph to visualize the connected malware samples

G = nx.Graph()

for i in range(100):
    G.add_node(i)

for pair in connected_pairs:
    G.add_edge(pair[0], pair[1])

nx.drawing.nx_pydot.write_dot(G, 'malware_graph.dot')



