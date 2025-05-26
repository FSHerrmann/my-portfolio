// src/components/Sauces.js
import React from 'react';
import './Sauces.css';

const defaultSauces = [
  'Alla Puttanesca',
  'Al Pesto di Basilico',
  'Cacio e Pepe',
  'Alla Matriciana'
];

function Sauces({ list = defaultSauces, showTitle = true }) {
  return (
    <section className="sauces-container">
      {showTitle && <h2>Our Sauces</h2>}
      <ul className="sauces-list">
        {list.map(sauce => (
          <li key={sauce}>{sauce}</li>
        ))}
      </ul>
    </section>
  );
}

export default Sauces;
