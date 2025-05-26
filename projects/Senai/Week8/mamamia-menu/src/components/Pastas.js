// src/components/Pastas.js
import React from 'react';
import Sauces from './Sauces';
import './Pastas.css';

const pastasData = [
  {
    name: 'Espaguete',
    price: 'R$ 30,00',
    image: 'https://via.placeholder.com/150?text=Espaguete',
    sauces: [
      'Alla Puttanesca',
      'Al Pesto di Basilico',
      'Cacio e Pepe',
      'Alla Matriciana'
    ]
  },
  {
    name: 'Tagliatelle',
    price: 'R$ 32,00',
    image: 'https://via.placeholder.com/150?text=Tagliatelle',
    sauces: [
      'Alla Puttanesca',
      'Alla Matriciana'
    ]
  },
  {
    name: 'Fettuccine',
    price: 'R$ 31,00',
    image: 'https://via.placeholder.com/150?text=Fettuccine',
    sauces: [
      'Alla Puttanesca',
      'Al Pesto di Basilico',
      'Cacio e Pepe'
    ]
  },
  {
    name: 'Penne',
    price: 'R$ 29,00',
    image: 'https://via.placeholder.com/150?text=Penne',
    sauces: [
      'Alla Puttanesca',
      'Cacio e Pepe'
    ]
  },
  {
    name: 'Rigatoni',
    price: 'R$ 28,00',
    image: 'https://via.placeholder.com/150?text=Rigatoni',
    sauces: [
      'Alla Matriciana'
    ]
  },
  {
    name: 'Pappardelle',
    price: 'R$ 33,00',
    image: 'https://via.placeholder.com/150?text=Pappardelle',
    sauces: [
      'Alla Puttanesca',
      'Alla Matriciana'
    ]
  }
];

function Pastas() {
  return (
    <section className="pastas-container">
      <h2>Our Pastas</h2>
      <div className="pastas-grid">
        {pastasData.map(item => (
          <div key={item.name} className="pasta-card">
            <img src={item.image} alt={item.name} />
            <h3>{item.name}</h3>
            <p className="price">{item.price}</p>
            {/* embed the Sauces component, passing only the allowed sauces and hiding its title */}
            <Sauces list={item.sauces} showTitle={false} />
          </div>
        ))}
      </div>
    </section>
  );
}

export default Pastas;
