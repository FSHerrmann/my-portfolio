import { useState, useEffect } from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import ProgressBar from './components/ProgressBar';
import Stopwatch from './components/Stopwatch';


function App() {
  const [tasks, setTasks] = useState(() => {
    const saved = localStorage.getItem('tasks');
    return saved ? JSON.parse(saved) : [];
  });

  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  const completedTasks = tasks.filter((task) => task.completed).length;

  const addTask = (newTask) => {
    setTasks((prevTasks) => [...prevTasks, newTask]);
  };

  const toggleTask = (id) => {
    setTasks((prevTasks) =>
      prevTasks.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  return (
    <div className="App">
      <h1>Week 9 – Task Manager</h1>
      <TaskForm onAddTask={addTask} />
      <ProgressBar totalTasks={tasks.length} completedTasks={completedTasks} />
      <TaskList tasks={tasks} onToggle={toggleTask} />
      <Stopwatch />

    </div>
  );
}

export default App;
