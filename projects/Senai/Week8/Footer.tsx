import React from 'react';

// Footer component with social media icons and restaurant address
const Footer: React.FC = () => {
  return (
    <footer>
      <div className="social-icons">
        <a href="https://facebook.com" target="_blank" rel="noreferrer" aria-label="Facebook">
          <img src="https://cdn-icons-png.flaticon.com/24/733/733547.png" alt="Facebook Icon" />
        </a>
        <a href="https://instagram.com" target="_blank" rel="noreferrer" aria-label="Instagram">
          <img src="https://cdn-icons-png.flaticon.com/24/733/733558.png" alt="Instagram Icon" />
        </a>
        <a href="https://twitter.com" target="_blank" rel="noreferrer" aria-label="Twitter">
          <img src="https://cdn-icons-png.flaticon.com/24/733/733579.png" alt="Twitter Icon" />
        </a>
      </div>
      <p>Address: Rua das Massas, 123 - São Paulo, SP</p>
    </footer>
  );
};

export default Footer;
