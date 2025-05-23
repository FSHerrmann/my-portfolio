import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles.css'; // Global styles

// React 18 root rendering
const root = ReactDOM.createRoot(document.getElementById('root')!);

root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
