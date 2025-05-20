// src/Menu.tsx
import React from 'react';

type MenuProps = {
  selected: string;
  onSelect: (option: string) => void;
};

const Menu: React.FC<MenuProps> = ({ selected, onSelect }) => {
  const options = ['Início', 'Gnocchi', 'Pastas', 'Bebidas'];
  return (
    <nav>
      <h1>Mamamia Massas</h1>
      <ul>
        {options.map(opt => (
          <li
            key={opt}
            style={{ fontWeight: selected === opt ? 'bold' : 'normal', cursor: 'pointer' }}
            onClick={() => onSelect(opt)}
          >
            {opt}
          </li>
        ))}
      </ul>
    </nav>
  );
};

export default Menu;
