// src/Cardapio.tsx
import React, { useState } from 'react';
import Menu from './Menu.tsx';
import TelaApresentacao from './PresentationScreen';
import Gnocchi from './Gnocchi';
import Pastas from './Pastas';
import Bebidas from './Bebidas';
import Rodape from './Rodape';

const Cardapio: React.FC = () => {
  const [selected, setSelected] = useState('Início');

  let content: JSX.Element;

  switch (selected) {
    case 'Gnocchi':
      content = <Gnocchi />;
      break;
    case 'Pastas':
      content = <Pastas />;
      break;
    case 'Bebidas':
      content = <Bebidas />;
      break;
    case 'Início':
    default:
      content = <TelaApresentacao />;
      break;
  }

  return (
    <div style={{ maxWidth: 900, margin: '0 auto', padding: '1rem' }}>
      <Menu selected={selected} onSelect={setSelected} />
      <hr />
      {content}
      <Rodape />
    </div>
  );
};

export default Cardapio;
