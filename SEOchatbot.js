import { useState } from "react";
import axios from "axios";

const SEOChatbot = () => {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("");

  const handleAsk = async () => {
    const res = await axios.post("http://localhost:5000/ask", { query });
    setResponse(res.data.answer);
  };

  return (
    <div className="container">
      <h1>SEO Chatbot</h1>
      <input type="text" value={query} onChange={(e) => setQuery(e.target.value)} placeholder="Ask an SEO question" />
      <button onClick={handleAsk}>Ask</button>
      <div>
        <h2>Answer:</h2>
        <p>{response}</p>
      </div>
    </div>
  );
};
