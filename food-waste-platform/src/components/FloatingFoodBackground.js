// src/components/FloatingFoodBackground.js
import React, { useEffect, useState } from "react";
import "./FloatingFoodBackground.css";

// Array of food emoji icons
const foodIcons = ["🍎", "🍌", "🍉", "🍇", "🍕", "🍟", "🍔", "🥑", "🍅"];

const FloatingFoodBackground = () => {
  const [positions, setPositions] = useState([]);

  useEffect(() => {
    const generatePositions = () => {
      // Generate equal spacing for each item based on index
      const newPositions = foodIcons.map((_, index) => ({
        // right: `${Math.random() + ((index*10) * Math.random())}vh`,
        // bottom: `${Math.random() + ((index*10) * Math.random())}vh`,
        left: `${20 + ( (index*10) * Math.random())}vh`, // Equally spaced in viewport width
        top: `${5 + ( (index*10) * Math.random())}vh`,  // Equally spaced in viewport height
      }));
      setPositions(newPositions);
    };

    // Update positions every 100 milliseconds for a smooth floating effect
    const interval = setInterval(() => {
      generatePositions();
    }, 10);

    // Cleanup interval on component unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="floating-food-background">
      {foodIcons.map((food, index) => (
        <div
          key={index}
          className="floating-food"
          style={{
            left: positions[index]?.left,
            top: positions[index]?.top,
            transform: `translate(${Math.random() * 10 - 5}px, ${Math.random() * 10 - 5}px)`,
          }}
        >
          {food}
        </div>
      ))}
    </div>
  );
};

export default FloatingFoodBackground;
