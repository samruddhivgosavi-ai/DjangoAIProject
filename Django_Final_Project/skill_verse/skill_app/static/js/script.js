function generatePlan() {

    const goal =
        document.getElementById("goal").value;

    const hours =
        document.getElementById("hours").value;

    const planBox =
        document.getElementById("plan-box");

    const planOutput =
        document.getElementById("plan-output");



    planBox.style.display = "block";



    planOutput.innerHTML = `

        <p>

            <strong>Career Goal:</strong>

            ${goal}

        </p>

        <p>

            <strong>Study Hours Per Day:</strong>

            ${hours} Hours

        </p>

        <hr>

        <h5>

            Daily Tasks

        </h5>

        <ul>

            <li>
                Study Core Concepts
            </li>

            <li>
                Practice Coding Problems
            </li>

            <li>
                Revise Previous Topics
            </li>

            <li>
                Build Mini Projects
            </li>

            <li>
                Practice Interview Questions
            </li>

        </ul>

    `;
}

function predictCareer() {

    const skill =
        document.getElementById("skill").value;

    const interest =
        document.getElementById("interest").value;

    const resultBox =
        document.getElementById("career-result");

    const output =
        document.getElementById("career-output");



    let career = "";



    if (
        skill === "Python"
        && interest === "Data Science"
    ) {

        career = "Data Scientist";

    }

    else if (
        skill === "JavaScript"
        && interest === "Web Development"
    ) {

        career = "Full Stack Developer";

    }

    else if (
        skill === "Machine Learning"
        && interest === "Artificial Intelligence"
    ) {

        career = "AI/ML Engineer";

    }

    else if (
        skill === "Machine Learning"
        && interest === "Data Science"
    ) {

        career = "Machine Learning Engineer";

    }

    else if (
        skill === "Power BI"
        && interest === "Analytics"
    ) {

        career = "Power BI Developer";

    }

    else {

        career = "Software Developer";

    }



    resultBox.style.display = "block";



    output.innerHTML = `

        <p>

            <strong>Main Skill:</strong>

            ${skill}

        </p>

        <p>

            <strong>Interest:</strong>

            ${interest}

        </p>

        <hr>

        <h4>

            Recommended Career:

        </h4>

        <h3 class="text-primary">

            ${career}

        </h3>

    `;
}