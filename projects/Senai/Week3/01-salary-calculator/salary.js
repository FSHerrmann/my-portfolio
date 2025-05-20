let employeeName;
let department;
let workedHours;
let hourlyRate;
let monthlySalary;
const regularHoursLimit = 220;

function adjustHourlyRateByDepartment(department, baseRate) {
  if (department === "AD") {
    return baseRate * 1.1; // 10% increase for Administrative
  } else if (department === "GE") {
    return baseRate * 1.25; // 25% increase for Management
  }
  return baseRate; // No change for Operational
}

function calculateMonthlySalary(department, workedHours, hourlyRate) {
  hourlyRate = adjustHourlyRateByDepartment(department, hourlyRate);

  if (department === "GE") {
    return workedHours * hourlyRate; // No overtime for Management
  }

  if (workedHours > regularHoursLimit) {
    let overtimeHours = workedHours - regularHoursLimit;
    return (regularHoursLimit * hourlyRate) + (overtimeHours * hourlyRate * 2);
  } else {
    return workedHours * hourlyRate;
  }
}

// Example values:
employeeName = "John";
department = "AD"; // "OP", "AD", or "GE"
workedHours = 240;
hourlyRate = 10;

monthlySalary = calculateMonthlySalary(department, workedHours, hourlyRate);

let overtimeHours = department === "GE" ? 0 : Math.max(0, workedHours - regularHoursLimit);

console.log(`The employee from the ${department} department, ${employeeName}, worked ${workedHours} hours and had ${overtimeHours} overtime hours. Their monthly salary was $${monthlySalary.toFixed(2)}.`);
