import React from 'react';
import Sauces from './Sauces';

type GnocchiOption = {
  name: string;
  price: string;
  image: string;
};

// List of Gnocchi options with their images and prices
const gnocchiOptions: GnocchiOption[] = [
  {
    name: 'Potato Gnocchi',
    price: 'R$ 25.00',
    image: 'https://via.placeholder.com/150?text=Potato+Gnocchi',
  },
  {
    name: 'Spinach Gnocchi',
    price: 'R$ 27.00',
    image: 'https://via.placeholder.com/150?text=Spinach+Gnocchi',
  },
  {
    name: 'Carrot Gnocchi',
    price: 'R$ 26.00',
    image: 'https://via.placeholder.com/150?text=Carrot+Gnocchi',
  },
  {
    name: 'Beetroot Gnocchi',
    price: 'R$ 28.00',
    image: 'https://via.placeholder.com/150?text=Beetroot+Gnocchi',
  },
];

// List of sauces for gnocchi
const gnocchiSauces = [
  'Alla Puttanesca',
  'Al Pesto di Basilico',
  'Cacio e Pepe',
  'Alla Matriciana',
];

// Gnocchi component displays gnocchi cards and their sauces
const Gnocchi: React.FC = () => {
  return (
    <div>
      <h2>Gnocchi</h2>
      {/* Grid with 2 columns for gnocchi cards */}
      <div className="cards-grid cards-grid-2" style={{ marginBottom: '1rem' }}>
        {gnocchiOptions.map(({ name, price, image }) => (
          <div className="card" key={name}>
            <img src={image} alt={name} />
            <h3>{name}</h3>
            <p>{price}</p>
          </div>
        ))}
      </div>
      <h3>Sauces</h3>
      <Sauces sauces={gnocchiSauces} />
    </div>
  );
};

export default Gnocchi;
