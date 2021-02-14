import React, {useState, useEffect} from 'react';
import './App.css';
import ArticleList from './components/ArticleList';


function App() {

  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/articles', {
      'method': 'GET',
      'headers': {
        'Content-Type': 'application/json',
        'Authorization': 'Token 3acdb8cab9d846743eeda8d933a8f80f01abf12b'
      }
    })
    .then(resp => resp.json())
    .then(resp => setArticles(resp))
    .catch(error => console.log(error))
  }, [])

  return (
    <div className="App">
        <h1>Django React Application</h1>
        <br/>
        <br/>
        <ArticleList articles={articles} />
    </div>
  );
}

export default App;
