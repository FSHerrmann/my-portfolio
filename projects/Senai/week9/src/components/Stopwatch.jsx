import { useState, useEffect, useRef } from 'react';

function Stopwatch() {
  const [seconds, setSeconds] = useState(0);
  const [running, setRunning] = useState(false);
  const intervalRef = useRef(null);

  useEffect(() => {
    if (running) {
      intervalRef.current = setInterval(() => {
        setSeconds((prev) => prev + 1);
      }, 1000);
    } else if (intervalRef.current) {
      clearInterval(intervalRef.current);
    }

    return () => clearInterval(intervalRef.current);
  }, [running]);

  const handleReset = () => {
    setRunning(false);
    setSeconds(0);
  };

  return (
    <div style={{ marginTop: '30px' }}>
      <h2>⏱️ Stopwatch</h2>
      <p style={{ fontSize: '1.5rem' }}>{seconds}s</p>
      <button onClick={() => setRunning(true)} disabled={running}>Start</button>
      <button onClick={() => setRunning(false)} disabled={!running}>Pause</button>
      <button onClick={handleReset}>Reset</button>
    </div>
  );
}

export default Stopwatch;
