// Predefined users with their codes and passwords for validation
const users = {
  commercial: { userCode: "CMCL12", password: "Com&c1@l;" },
  hr: { userCode: "98HR", password: "RH!@2025" },
  it: { userCode: "DEV4567TI", password: "IT&&||==2025" }
};

// Get references to important DOM elements
const form = document.getElementById('login-form');
const errorDiv = document.getElementById('error-message');
const postLoginDiv = document.getElementById('post-login-content');

// Listen for form submission
form.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent default form submit (page reload)

  // Clear previous messages and content
  errorDiv.textContent = "";
  postLoginDiv.innerHTML = "";

  // Get input values trimmed
  const userCode = form['user-code'].value.trim();
  const department = form['department'].value;
  const password = form['password'].value;

  // Validate selected department
  if (!users[department]) {
    errorDiv.textContent = "Please select a valid department.";
    return;
  }

  const userData = users[department];

  // Validate user code and password
  if (userCode !== userData.userCode || password !== userData.password) {
    errorDiv.textContent = "Invalid user code or password for the selected department.";
    return;
  }

  // Credentials are valid - hide login form and show department-specific content
  form.style.display = 'none';
  showDepartmentContent(department);
});

// Function to show content based on department after login
function showDepartmentContent(department) {
  switch(department) {
    case 'commercial':
      showCommercialContent();
      break;
    case 'hr':
      showHRContent();
      break;
    case 'it':
      showITContent();
      break;
  }
}

// Commercial department content
function showCommercialContent() {
  const productName = "Super Widget";
  const productPrice = "$49.99";
  const productImageUrl = "https://via.placeholder.com/300x200?text=Product+Image";

  postLoginDiv.innerHTML = `
    <h2>Welcome to Commercial Department</h2>
    <img src="${productImageUrl}" alt="Product Image" class="product-image" />
    <p><strong>Product:</strong> ${productName}</p>
    <p><strong>Price:</strong> ${productPrice}</p>
  `;
}

// HR department content
function showHRContent() {
  postLoginDiv.innerHTML = `
    <h2>Welcome to HR Department</h2>
    <button id="show-positions-btn">View Positions and Salaries</button>
    <div id="positions-table-container"></div>
  `;

  document.getElementById('show-positions-btn').addEventListener('click', showPositionsTable);
}

// Function to display HR positions and salaries table
function showPositionsTable() {
  const employees = [
    { name: "Alice Johnson", department: "HR", position: "Recruiter", salary: "$3,500" },
    { name: "Bob Smith", department: "HR", position: "HR Manager", salary: "$5,200" },
    { name: "Carol White", department: "HR", position: "Payroll Specialist", salary: "$3,800" }
  ];

  let tableHTML = `
    <table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Department</th>
          <th>Position</th>
          <th>Salary</th>
        </tr>
      </thead>
      <tbody>
  `;

  employees.forEach(emp => {
    tableHTML += `
      <tr>
        <td>${emp.name}</td>
        <td>${emp.department}</td>
        <td>${emp.position}</td>
        <td>${emp.salary}</td>
      </tr>
    `;
  });

  tableHTML += `
      </tbody>
    </table>
  `;

  document.getElementById('positions-table-container').innerHTML = tableHTML;
}

// IT department content
function showITContent() {
  postLoginDiv.innerHTML = `
    <h2>Welcome to IT Department</h2>
    <label for="number-input">Enter a number to convert to binary:</label>
    <input type="number" id="number-input" min="0" placeholder="Enter a number" />
    <button id="convert-btn">Convert to Binary</button>
    <p id="binary-result" style="margin-top: 15px; font-weight: bold;"></p>
  `;

  document.getElementById('convert-btn').addEventListener('click', () => {
    const numInput = document.getElementById('number-input').value.trim();
    const resultP = document.getElementById('binary-result');

    if (numInput === "" || isNaN(numInput)) {
      resultP.textContent = "Please enter a valid number.";
      resultP.style.color = "red";
      return;
    }

    const num = parseInt(numInput, 10);
    const binary = num.toString(2); // Convert number to binary string

    resultP.textContent = `Binary representation: ${binary}`;
    resultP.style.color = "green";
  });
}
