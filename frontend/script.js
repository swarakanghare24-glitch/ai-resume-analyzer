async function uploadResume() {

const fileInput = document.getElementById("resumeFile");

const result = document.getElementById("result");

if (!fileInput.files[0]) {

result.innerHTML = "Please upload a resume first.";

return;

}

const formData = new FormData();

formData.append(
"file",
fileInput.files[0]
);

result.innerHTML = "Analyzing Resume...";

try {

const response = await fetch(
"http://127.0.0.1:8000/upload",
{
method: "POST",
body: formData
}
);

const data = await response.json();

result.innerHTML = `

<div class="result-card">

<h3>Predicted Role</h3>

<p>${data.predicted_role}</p>

</div>

<div class="result-card">

<h3>ATS Score</h3>

<p>${data.ats_score}%</p>

</div>

<div class="result-card">

<h3>Skills Found</h3>

<p>${data.skills_found.join(", ")}</p>

</div>

<div class="result-card">

<h3>Missing Skills</h3>

<p>${data.missing_skills.join(", ")}</p>

</div>

`;

}

catch(error){

console.log(error);

result.innerHTML =
"Error analyzing resume";

}

}