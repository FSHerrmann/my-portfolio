// src/App.js
import React from 'react';
import Menu from './components/Menu';
import Presentation from './components/Presentation';
import Gnocchi from './components/Gnocchi';
import Sauces from './components/Sauces';
import Pastas from './components/Pastas';
import Drinks from './components/Drinks';

function App() {
  return (
    <div>
      <Menu />
      <Presentation />
      <Gnocchi />
      <Sauces />
      <Pastas />
      <Drinks />

      <main style={{ padding: '2rem' }}>
        {/* any extra content */}
      </main>
    </div>
  );
}

export default App;
