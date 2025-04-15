import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await axios.post(`http://localhost:8000/ask?query=${message}`, { message });
    setResponse(res.data.response);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>Make a question about Marcus Aurelius´s Meditations: </label>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <button type="submit">Send</button>
      </form>
        {response && (
            <div>
                <label>The response it is:</label>
                <p>{response}</p>
            </div>
        )}

    </div>
  );
}

export default App;