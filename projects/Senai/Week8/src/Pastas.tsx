import React from 'react';
import Sauces from './Sauces';

type Pasta = {
  name: string;
  price: string;
  image: string;
  sauces: string[];
};

// List of pasta options with their sauces
const pastaOptions: Pasta[] = [
  {
    name: 'Spaghetti',
    price: 'R$ 30.00',
    image: 'https://via.placeholder.com/150?text=Spaghetti',
    sauces: ['Alla Puttanesca', 'Al Pesto di Basilico', 'Cacio e Pepe', 'Alla Matriciana'],
  },
  {
    name: 'Tagliatelle',
    price: 'R$ 32.00',
    image: 'https://via.placeholder.com/150?text=Tagliatelle',
    sauces: ['Alla Puttanesca', 'Alla Matriciana'],
  },
  {
    name: 'Fettuccine',
    price: 'R$ 33.00',
    image: 'https://via.placeholder.com/150?text=Fettuccine',
    sauces: ['Alla Puttanesca', 'Al Pesto di Basilico', 'Cacio e Pepe'],
  },
  {
    name: 'Penne',
    price: 'R$ 29.00',
    image: 'https://via.placeholder.com/150?text=Penne',
    sauces: ['Alla Puttanesca', 'Cacio e Pepe'],
  },
  {
    name: 'Rigatoni',
    price: 'R$ 31.00',
    image: 'https://via.placeholder.com/150?text=Rigatoni',
    sauces: ['Alla Matriciana'],
  },
  {
    name: 'Pappardelle',
    price: 'R$ 34.00',
    image: 'https://via.placeholder.com/150?text=Pappardelle',
    sauces: ['Alla Puttanesca', 'Alla Matriciana'],
  },
];

// Pastas component displays pasta cards grouped 3 per row
const Pastas: React.FC = () => {
  // Split pastas into groups of 3 for rows
  const rows: Pasta[][] = [];
  for (let i = 0; i < pastaOptions.length; i += 3) {
    rows.push(pastaOptions.slice(i, i + 3));
  }

  return (
    <div>
      <h2>Pastas</h2>
      {rows.map((group, idx) => (
        <div className="cards-row" key={idx}>
          {group.map(({ name, price, image, sauces }) => (
            <div className="card" key={name}>
              <img src={image} alt={name} />
              <h3>{name}</h3>
              <p>{price}</p>
              <Sauces sauces={sauces} />
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Pastas;
