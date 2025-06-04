import { useState } from 'react';

function TaskForm({ onAddTask }) {
  const [description, setDescription] = useState('');
  const [period, setPeriod] = useState('morning');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!description.trim()) return;

    const newTask = {
      id: Date.now(),
      description,
      period,
      completed: false,
    };

    onAddTask(newTask);
    setDescription('');
    setPeriod('morning');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Task description"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <select
        value={period}
        onChange={(e) => setPeriod(e.target.value)}
      >
        <option value="morning">Morning</option>
        <option value="afternoon">Afternoon</option>
        <option value="evening">Evening</option>
      </select>

      <button type="submit">Add Task</button>
    </form>
  );
}

export default TaskForm;
