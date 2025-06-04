import TaskItem from './TaskItem';

function TaskColumn({ title, tasks, onToggle }) {
  return (
    <div className="task-column">
      <h3>{title}</h3>
      <ul>
        {tasks.map((task) => (
          <TaskItem key={task.id} task={task} onToggle={onToggle} />
        ))}
      </ul>
    </div>
  );
}

export default TaskColumn;
