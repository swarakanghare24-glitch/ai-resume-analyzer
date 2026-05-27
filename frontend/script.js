async function uploadResume() {
    const fileInput = document.getElementById("resumeFile");
    const resultDiv = document.getElementById("result");

    if (!fileInput.files.length) {
        alert("Please select a resume PDF");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/upload",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        resultDiv.innerHTML = `
            <h2>Analysis Result</h2>
            <p><strong>Predicted Role:</strong> ${data.predicted_role}</p>
            <p><strong>ATS Score:</strong> ${data.ats_score}</p>
            <p><strong>Skills Found:</strong> ${data.skills_found.join(", ")}</p>
            <p><strong>Missing Skills:</strong> ${data.missing_skills.join(", ")}</p>
        `;
    } catch (error) {
        resultDiv.innerHTML = "Error analyzing resume.";
        console.error(error);
    }
}