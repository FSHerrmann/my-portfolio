import React, { useState } from 'react';
import Menu from './Menu';
import TelaApresentacao from './PresentationScreen';
import Gnocchi from './Gnocchi';
import Pastas from './Pastas';
import Bebidas from './Bebidas';
import Rodape from './Rodape';

const Cardapio: React.FC = () => {
  const [selected, setSelected] = useState('Início');

  let componenteSelecionado: JSX.Element;

  switch (selected) {
    case 'Gnocchi':
      componenteSelecionado = <Gnocchi />;
      break;
    case 'Pastas':
      componenteSelecionado = <Pastas />;
      break;
    case 'Bebidas':
      componenteSelecionado = <Bebidas />;
      break;
    case 'Início':
    default:
      componenteSelecionado = <TelaApresentacao />;
      break;
  }

  return (
    <div style={{ maxWidth: 900, margin: '0 auto', padding: '1rem' }}>
      <Menu selected={selected} onSelect={setSelected} />
      <hr />
      {componenteSelecionado}
      <Rodape />
    </div>
  );
};

export default Cardapio;
