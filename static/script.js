const form = document.getElementById("driver-form");

form.addEventListener("submit", function(event) {
  event.preventDefault();
  
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const license = document.getElementById("license").value;
  const dob = document.getElementById("dob").value;
  
  const output = document.getElementById("output");
  output.innerHTML += `
    <h3>Driver Details:</h3>
    <p>Name: ${name}</p>
    <p>Email: ${email}</p>
    <p>Driver's License Number: ${license}</p>
    <p>Date of Birth: ${dob}</p>
  `;
  
  // Clear form fields
  form.reset();
});

function startDetection() {
  fetch('/start')
    .then(response => response.json())
    .then(data => {
      console.log(data);
      document.getElementById('start').disabled = true;
      document.getElementById('stop').disabled = false;
      document.getElementById('output').innerHTML = 'Detection loop started successfully!';
    })
    .catch(error => console.error(error));
}

