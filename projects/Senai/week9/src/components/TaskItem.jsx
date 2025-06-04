function TaskItem({ task, onToggle }) {
  return (
    <li>
      <label style={{
        color: task.completed ? '#999' : '#000',
        textDecoration: task.completed ? 'line-through' : 'none',
      }}>
        <input
          type="checkbox"
          checked={task.completed}
          onChange={() => onToggle(task.id)}
        />
        {' '}
        {task.description}
      </label>
    </li>
  );
}

export default TaskItem;
