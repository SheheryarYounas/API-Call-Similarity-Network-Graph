import pandas as pd
import networkx as nx
import pydot

while True: 

    #Step 1: Load the dataset

    dataset_file = 'dynamic_api_call_sequence_per_malware_100_0_306.csv'

    dataset = pd.read_csv(dataset_file)

    print(f"Enter 1 for Malware Similarity Analysis")
    print(f"Enter 2 for Goodware Similarity Analysis ")
    print(f"Enter 3 to Exit")

    choice = int(input())

    #print(dataset.head())

    #Step 2: Filter the dataset to include only malware samples

    if choice == 1:
        print("Please select how many malware samples you want to analyze (10 is recommended):")
        num_malware_samples = int(input())

        malware_dataset = dataset[dataset['malware'] == 1].head(num_malware_samples)

    elif choice == 2:
        print("Please select how many goodware samples you want to analyze (10 is recommended):")
        num_goodware_samples = int(input())

        malware_dataset = dataset[dataset['malware'] == 0].head(num_goodware_samples)

    elif choice == 3:
        break

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
    print("Please enter a threshold value for Jaccard Similarity (between 0 and 1):")
    threshold = float(input())

    if threshold < 0 or threshold > 1:
        print("Invalid threshold value. Please enter a value between 0 and 1.")
        continue

    print(f"Threshold value: {threshold}")

    for i in range(len(unique_api_sequences)):

        for j in range(i + 1, len(unique_api_sequences)):

            intersection = set(unique_api_sequences[i]).intersection(set(unique_api_sequences[j]))
            union = set(unique_api_sequences[i]).union(set(unique_api_sequences[j]))

            jaccard_similarity = len(intersection) / len(union)

            #print(f"Jaccard Similarity between malware {i} and malware {j}: {jaccard_similarity}")

            if jaccard_similarity > threshold:
                connected_pairs.append((i, j))

            
    if choice == 1:
        print(f"Number of connected malware samples: {len(connected_pairs)}")
    elif choice == 2:
        print(f"Number of connected goodware samples: {len(connected_pairs)}")

    #Step 5: Create a graph to visualize the connected malware samples

    G = nx.Graph()

    number_of_nodes = len(unique_api_sequences)

    for i in range(number_of_nodes):
        G.add_node(i)

    for pair in connected_pairs:
        G.add_edge(pair[0], pair[1])

    if choice == 1:
        nx.drawing.nx_pydot.write_dot(G, 'malware_graph.dot')
    elif choice == 2:
        nx.drawing.nx_pydot.write_dot(G, 'goodware_graph.dot')



