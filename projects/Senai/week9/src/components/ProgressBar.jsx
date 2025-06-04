function ProgressBar({ totalTasks, completedTasks }) {
  const progress = totalTasks === 0 ? 0 : (completedTasks / totalTasks) * 100;

  return (
    <div style={{ margin: '20px 0' }}>
      <p>Progress: {Math.round(progress)}%</p>
      <div style={{
        backgroundColor: '#eee',
        borderRadius: '5px',
        height: '20px',
        width: '100%',
      }}>
        <div style={{
          backgroundColor: '#4caf50',
          height: '100%',
          width: `${progress}%`,
          borderRadius: '5px',
          transition: 'width 0.3s ease',
        }}></div>
      </div>
    </div>
  );
}

export default ProgressBar;
