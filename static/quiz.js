window.onload = function () {
    const quizContainer = document.getElementById('quiz');
    const resultsContainer = document.getElementById('results');
    const messagesContainer = document.getElementById('messages');
    const submitButton = document.getElementById('submit');
    const previousButton = document.getElementById("previous");
    const nextButton = document.getElementById("next");

    let number_30_sec = 4
    let total_seconds = 30 * number_30_sec;
    let c_minutes = parseInt(total_seconds / 60);
    let c_seconds = parseInt(total_seconds % 60);
    let timer;

    function CheckTime() {
        document.getElementById("quiz-time-left").innerHTML = 'Time Left: <br>' + c_minutes + ' minutes ' + c_seconds + ' seconds ';

        if (total_seconds <= 0) {
            showResults();
        } else {
            total_seconds = total_seconds - 1;
            c_minutes = parseInt(total_seconds / 60);
            c_seconds = parseInt(total_seconds % 60);
            timer = setTimeout(CheckTime, 1000);
        }
    }

    const myQuestions = [
        {
            question: "139 + 51 = ?",
            correctAnswer: "190"
        },
        {
            question: "141 + 59 = ?",
            correctAnswer: "200"
        },
        // {
        //     question: "97 + 75 = ?",
        //     correctAnswer: "172"
        // },
        // {
        //     question: "80 + 93 = ?",
        //     correctAnswer: "173"
        // }
    ];

    function buildQuiz() {
        // we'll need a place to store the HTML output
        const output = [];

        // for each question...
        myQuestions.forEach(
            (currentQuestion, questionNumber) => {

                // we'll want to store the list of answer choices
                const answers = [];

                // and for each available answer...
                // for (letter in currentQuestion.answers) {

                // ...add an HTML radio button
                answers.push(
                    `<label>
            <input type="text" name="question${questionNumber}" id="questions">
          </label>`
                );
                // }

                // add this question and its answers to the output
                output.push(
                    `<div class="slide">
                        <div class="question"> ${currentQuestion.question} </div>
                        <div class="answers"> ${answers.join('')} </div>
                    </div>`
                );
            }
        );

        // finally combine our output list into one string of HTML and put it on the page
        quizContainer.innerHTML = output.join('');

    }

    function showResults() {
        // gather answer containers from our quiz
        const answerContainers = quizContainer.querySelectorAll('.answers');

        // keep track of user's answers
        let numCorrect = 0;
        // document.getElementById('questions').disabled = true;

        // for each question...
        myQuestions.forEach((currentQuestion, questionNumber) => {

            // find selected answer
            const answerContainer = answerContainers[questionNumber];
            const selector = 'input[name=question' + questionNumber + ']';
            // if answer is correct

            const userAnswer = (answerContainer.querySelector(selector) || {}).value;
            (answerContainer.querySelector(selector) || {}).disabled = true;
            if (userAnswer === currentQuestion.correctAnswer) {

                // add to the number of correct answers
                numCorrect++;
                // color the answers green
                answerContainers[questionNumber].style.color = 'lightgreen';
            }
            // if answer is wrong or blank
            else {
                // color the answers red
                answerContainers[questionNumber].style.color = 'red';
            }
        });

        // show number of correct answers out of total
        resultsContainer.innerHTML = numCorrect + ' out of ' + myQuestions.length;
    }

    // display quiz right away
    buildQuiz();
    CheckTime();

    const slides = document.querySelectorAll(".slide");
    let currentSlide = 0;
    showSlide(0);

    // const slides = document.querySelectorAll(".slide");
    // let currentSlide = 0;

    function showSlide(n) {
        slides[currentSlide].classList.remove('active-slide');
        slides[n].classList.add('active-slide');
        currentSlide = n;
        if (currentSlide === 0) {
            previousButton.style.display = 'none';
        } else {
            previousButton.style.display = 'inline-block';
        }
        if (currentSlide === slides.length - 1) {
            nextButton.style.display = 'none';
            submitButton.style.display = 'inline-block';
        } else {
            nextButton.style.display = 'inline-block';
            submitButton.style.display = 'none';
        }
    }

    // showSlide(0);

    function showNextSlide() {
        // showSlide(currentSlide + 1);
        const answerContainers = quizContainer.querySelectorAll('.answers');
        const answerContainer = answerContainers[currentSlide];
        const selector = 'input[name=question' + currentSlide + ']';
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;

        if (myQuestions[currentSlide].correctAnswer === userAnswer) {
            if (currentSlide === slides.length - 1) {
                // showSlide(currentSlide);
                messagesContainer.innerHTML = ""
                showResults();
            } else {
                showSlide(currentSlide + 1);
                messagesContainer.innerHTML = ""
            }
        } else {
            messagesContainer.innerHTML = "Your answer is not correct, please try again";
            messagesContainer.style.color = 'red';
        }
    }

    function showPreviousSlide() {
        showSlide(currentSlide - 1);
        messagesContainer.innerHTML = ""
    }

    previousButton.addEventListener("click", showPreviousSlide);
    nextButton.addEventListener("click", showNextSlide);

    // on submit, show results
    // submitButton.addEventListener('click', showResults);
    submitButton.addEventListener('click', showNextSlide);
}