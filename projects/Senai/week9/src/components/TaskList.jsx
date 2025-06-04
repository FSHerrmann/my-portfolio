import TaskColumn from './TaskColumn';

function TaskList({ tasks, onToggle }) {
  const morningTasks = tasks.filter((t) => t.period === 'morning');
  const afternoonTasks = tasks.filter((t) => t.period === 'afternoon');
  const eveningTasks = tasks.filter((t) => t.period === 'evening');

  return (
    <div className="task-list" style={{ display: 'flex', gap: '2rem' }}>
      <TaskColumn title="🌅 Morning" tasks={morningTasks} onToggle={onToggle} />
      <TaskColumn title="🌇 Afternoon" tasks={afternoonTasks} onToggle={onToggle} />
      <TaskColumn title="🌃 Evening" tasks={eveningTasks} onToggle={onToggle} />
    </div>
  );
}

export default TaskList;
