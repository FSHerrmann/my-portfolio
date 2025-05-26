import React from 'react';
import './Menu.css';

function Menu() {
  return (
    <nav className="menu">
      {/* Restaurant name */}
      <h1 className="restaurant-name">Mamamia Massas</h1>

      {/* Menu items */}
      <ul className="menu-list">
        <li className="menu-item">
          <a href="#home">Início</a>
        </li>
        <li className="menu-item">
          <a href="#gnocchi">Gnocchi</a>
        </li>
        <li className="menu-item">
          <a href="#pastas">Pastas</a>
        </li>
        <li className="menu-item">
          <a href="#bedidas">Bedidas</a>
        </li>
      </ul>
    </nav>
  );
}

export default Menu;