import React from 'react';
import Menu from './components/Menu';
import Presentation from './components/Presentation';
import Gnocchi from './components/Gnocchi';
import Sauces from './components/Sauces';
import Pastas from './components/Pastas';
import Drinks from './components/Drinks';
import Footer from './components/Footer';

const Cardapio: React.FC = () => (
  <div>
    <Menu />
    <Presentation />
    <Gnocchi />
    <Sauces />   {/* standalone sauces list */}
    <Pastas />
    <Drinks />
    <Footer />
  </div>
);

export default Cardapio;
