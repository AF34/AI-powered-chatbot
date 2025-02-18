import faiss
import numpy as np
import json

# Provide the full path to the seo_data.json file
file_path = r"C:\Users\BASKER\seo_crawler\my_project\faiss\seo_data.json"

with open(file_path, "r") as f:
    seo_data = json.load(f)

# Convert SEO meta descriptions into vectors
def create_vector(text):
    vector = np.zeros(100)  # Simple vector representation of fixed 100 dimensions
    for word in text.split():
        vector[hash(word) % 100] += 1  # Map words to vector positions based on hash
    return vector

# Create a FAISS index to store the vectors (100 dimensions)
index = faiss.IndexFlatL2(100)  # FAISS index for L2 distance in a 100-dimensional space

vectors = np.array([create_vector(item['meta_description'] or '') for item in seo_data], dtype='float32')

# Add the vectors to the FAISS index
index.add(vectors)


faiss.write_index(index, "seo_data.index")

# Print confirmation message
print("FAISS index saved!")
