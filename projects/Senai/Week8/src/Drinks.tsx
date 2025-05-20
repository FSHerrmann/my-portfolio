import React from 'react';

type Drink = {
  name: string;
  price: string;
};

type Category = {
  name: string;
  drinks: Drink[];
};

// Drink categories with their drinks and prices
const categories: Category[] = [
  {
    name: 'Water',
    drinks: [{ name: 'Water', price: 'R$ 5.00' }],
  },
  {
    name: 'Soda',
    drinks: [
      { name: 'Coca-Cola', price: 'R$ 7.00' },
      { name: 'Guarana', price: 'R$ 7.00' },
      { name: 'Sprite', price: 'R$ 7.00' },
    ],
  },
  {
    name: 'Juices',
    drinks: [
      { name: 'Strawberry', price: 'R$ 8.00' },
      { name: 'Orange', price: 'R$ 8.00' },
      { name: 'Grape', price: 'R$ 8.00' },
    ],
  },
];

// Drinks component displays drink categories and their items
const Drinks: React.FC = () => {
  return (
    <div>
      <h2>Drinks</h2>
      {categories.map(({ name, drinks }) => (
        <div key={name} className="drinks-category">
          <h3>{name}</h3>
          <ul>
            {drinks.map(({ name: drinkName, price }) => (
              <li key={drinkName}>
                {drinkName} - {price}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
};

export default Drinks;
