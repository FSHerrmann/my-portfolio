import React from 'react';
import './Gnocchi.css';

const gnocchiData = [
  {
    name: 'Gnocchi de Batata',
    price: 'R$ 25,00',
    image: 'https://via.placeholder.com/150?text=Batata'
  },
  {
    name: 'Gnocchi de Espinafre',
    price: 'R$ 27,00',
    image: 'https://via.placeholder.com/150?text=Espinafre'
  },
  {
    name: 'Gnocchi de Cenoura',
    price: 'R$ 26,00',
    image: 'https://via.placeholder.com/150?text=Cenoura'
  },
  {
    name: 'Gnocchi de Beterraba',
    price: 'R$ 28,00',
    image: 'https://via.placeholder.com/150?text=Beterraba'
  }
];

function Gnocchi() {
  return (
    <section className="gnocchi-container">
      <h2>Our Gnocchi Selection</h2>
      <div className="gnocchi-grid">
        {gnocchiData.map(item => (
          <div key={item.name} className="gnocchi-card">
            <img src={item.image} alt={item.name} />
            <h3>{item.name}</h3>
            <p className="price">{item.price}</p>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Gnocchi;
