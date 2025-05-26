import React from 'react';
import './Presentation.css';

function Presentation() {
  return (
    <section className="presentation-container">
      {/* Left side: headline + subhead */}
      <div className="presentation-text">
        <h2>Servindo massas à mais de 70 anos</h2>
        <p>qualidade passada por gerações</p>
      </div>

      {/* Right side: restaurant façade image */}
      <div className="presentation-image">
        <img
          src="https://via.placeholder.com/600x400?text=Fachada+do+Restaurante"
          alt="Fachada do Restaurante"
        />
      </div>
    </section>
  );
}

export default Presentation;
