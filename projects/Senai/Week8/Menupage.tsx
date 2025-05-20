import React, { useState } from 'react';
import Menu from './Menu';
import PresentationScreen from './PresentationScreen';
import Gnocchi from './Gnocchi';
import Pastas from './Pastas';
import Drinks from './Drinks';
import Footer from './Footer';

// Main MenuPage component controls which section is displayed
const MenuPage: React.FC = () => {
  const [selected, setSelected] = useState('Home');

  let content: JSX.Element;

  switch (selected) {
    case 'Gnocchi':
      content = <Gnocchi />;
      break;
    case 'Pastas':
      content = <Pastas />;
      break;
    case 'Drinks':
      content = <Drinks />;
      break;
    case 'Home':
    default:
      content = <PresentationScreen />;
      break;
  }

  return (
    <div className="container">
      <Menu selected={selected} onSelect={setSelected} />
      <hr />
      {content}
      <Footer />
    </div>
  );
};

export default MenuPage;
