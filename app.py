import faiss
import numpy as np
import json
import openai
from flask import Flask, request, jsonify

# Load OpenAI API Key
openai.api_key = "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"

# Define the create_vector function
def create_vector(text):
    vector = np.zeros(100)  # Simple vector representation
    for word in text.split():
        vector[hash(word) % 100] += 1
    return vector

# Load FAISS index
index = faiss.read_index("seo_data.index")
file_path = r"C:\Users\BASKER\seo_crawler\my_project\faiss\seo_data.json"

# Load SEO Data
with open(file_path, "r") as f:
    seo_data = json.load(f)

# Convert query to vector
def create_query_vector(query):
    return np.array([create_vector(query)], dtype='float32')

# Function to get GPT response
def query_gpt(query, seo_info):
    prompt = f"SEO Analysis: {seo_info}. Question: {query}"
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=100)
    return response.choices[0].text.strip()

# Initialize Flask app
app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_query = data.get('query')

    # Search FAISS index
    query_vector = create_query_vector(user_query)
    _, I = index.search(query_vector, k=1)
    closest_data = seo_data[I[0][0]]

    # Get GPT-based SEO response
    answer = query_gpt(user_query, closest_data)

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
