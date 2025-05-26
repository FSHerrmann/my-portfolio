import React from 'react';
import './Drinks.css';

const drinksData = [
  {
    category: 'Água',
    items: [
      { name: 'Água Mineral', price: 'R$ 5,00' }
    ]
  },
  {
    category: 'Refrigerante',
    items: [
      { name: 'Coca-Cola', price: 'R$ 8,00' },
      { name: 'Guaraná',     price: 'R$ 7,50' },
      { name: 'Sprite',      price: 'R$ 7,00' }
    ]
  },
  {
    category: 'Sucos',
    items: [
      { name: 'Morango', price: 'R$ 10,00' },
      { name: 'Laranja', price: 'R$ 9,00' },
      { name: 'Uva',     price: 'R$ 11,00' }
    ]
  }
];

function Drinks() {
  return (
    <section className="drinks-container">
      <h2>Our Drinks</h2>

      {drinksData.map(section => (
        <div key={section.category} className="drinks-category">
          <h3>{section.category}</h3>
          <ul className="drinks-list">
            {section.items.map(item => (
              <li key={item.name} className="drinks-item">
                <span className="drink-name">{item.name}</span>
                <span className="drink-price">{item.price}</span>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </section>
  );
}

export default Drinks;
