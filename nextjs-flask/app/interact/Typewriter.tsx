import { useEffect, useState } from 'react';

interface TypewriterProps {
  text: string; // The text to typewrite
  speed?: number; // Time delay between characters (in milliseconds)
}

const Typewriter: React.FC<TypewriterProps> = ({ text, speed = 50 }) => {
  const [displayText, setDisplayText] = useState('');
  const [currentIndex, setCurrentIndex] = useState(0);

  useEffect(() => {
    if (currentIndex < text.length) {
      const timer = setTimeout(() => {
        setDisplayText((prev) => prev + text[currentIndex]);
        setCurrentIndex(currentIndex + 1);
      }, speed);

      return () => clearTimeout(timer);
    }
  }, [currentIndex, text, speed]);
  
  return <span>{displayText}</span>;
};

export default Typewriter;
