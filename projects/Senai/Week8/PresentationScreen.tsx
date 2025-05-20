import React from 'react';

// Presentation screen showing the tagline and restaurant facade image
const PresentationScreen: React.FC = () => {
  return (
    <div className="presentation-screen">
      <div className="text-section">
        <h2>Serving pasta for over 70 years</h2>
        <p>Quality passed down through generations</p>
      </div>
      <div>
        <img
          src="https://via.placeholder.com/300x200?text=Restaurant+Facade"
          alt="Restaurant Facade"
        />
      </div>
    </div>
  );
};

export default PresentationScreen;
