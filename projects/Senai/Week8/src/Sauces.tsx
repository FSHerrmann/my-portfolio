import React from 'react';

type SaucesProps = {
  sauces: string[];
};

// Unordered list of sauces
const Sauces: React.FC<SaucesProps> = ({ sauces }) => {
  return (
    <ul className="sauces-list">
      {sauces.map(sauce => (
        <li key={sauce}>{sauce}</li>
      ))}
    </ul>
  );
};

export default Sauces;
