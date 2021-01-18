window.onload = function () {
    const quizContainer = document.getElementById('quiz');
    const resultsContainer = document.getElementById('results');
    const messagesContainer = document.getElementById('messages');
    const submitButton = document.getElementById('submit');
    const previousButton = document.getElementById("previous");
    const nextButton = document.getElementById("next");
    const startButton = document.getElementById("start");

    let number_30_sec = 7;
    let total_seconds = 30 * number_30_sec;
    let c_minutes = parseInt(total_seconds / 60);
    let c_seconds = parseInt(total_seconds % 60);
    let timer;

    function CheckTime() {
        document.getElementById("quiz-time-left").innerHTML = 'Time Left: <br>' + c_minutes + ' minutes ' + c_seconds + ' seconds ';

        if (total_seconds <= 0) {
            showResults('true');
        } else {
            total_seconds = total_seconds - 1;
            c_minutes = parseInt(total_seconds / 60);
            c_seconds = parseInt(total_seconds % 60);
            timer = setTimeout(CheckTime, 1000);
        }
    }

    // where I put the questions
    const myQuestions = [

        {
            question: "141 + 59 = ?",
            correctAnswer: "200"
        },
        {
            question: "97 + 75 = ?",
            correctAnswer: "172"
        },
        {
            question: "If 21 x 25 = 525, then <br> <br> 525 ÷ _____ = 25",
            correctAnswer: "21"
        },
        {
            question: "Bill spent less money than Bryce but more money than Julia. Who spent more money, Julia or Bryce?",
            correctAnswer: "Bryce"
        },
        {
            question: "Nina earned less money than Ann but more money than Grace. Who earned the most money?",
            correctAnswer: "Ann"
        },
        {
            question: "Multiply: 12 x 3",
            correctAnswer: "36"
        },
        {
            question: "How would you write 15 as a Roman numeral?",
            correctAnswer: "XV"
        },
        {
            question: "What number does this Roman numeral represent? XXX",
            correctAnswer: "30"
        },
        {
            question: "What number does this Roman numeral represent? XVIII",
            correctAnswer: "28"
        },
        {
            question: "How would you write 31 as a Roman numeral?",
            correctAnswer: "XXXI"
        },
        {
            question: "6 tens corresponds to _____ units.",
            correctAnswer: "60"
        },
        {
            question: "_____ hundreds = 900 units",
            correctAnswer: "9"
        },
        //6th class
        {
            question: "Which integer represents this scenario? <br> Gain of 5 points: <br> -5 or 5?",
            correctAnswer: "5"
        },
        {
            question: "Which integer represents this scenario? <br> A lift goes down 4 floors: <br> -4 or 4?",
            correctAnswer: "-4"
        },
        {
            question: "Write an integer that represents this scenario: <br> 3 degrees colder today than yesterday:",
            correctAnswer: "-3"
        },
        {
            question: "A corn farm harvested corn for 7 days. They harvested 102 ears of corn each day. <br>How many ears of corn did the farm harvest?",
            correctAnswer: "714"
        },
        {
            question: "Marie picked 6 barrels of cherries. She put 52 cherries in each barrel. <br>How many cherries did Marie pick in all?",
            correctAnswer: "312"
        },

    ];

    function buildQuiz() {
        // we'll need a place to store the HTML output
        const output = [];

        // this is to create the initial slide - welcome slide
        output.push(`
            <div class="slide_wrapper">
                <p class="question"> Welcome to this Math test. <br>Please answer the questions before the timer is over.</p>
            </div>
        `);

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

    function showResults(timer_out) {
        // to stop the timer
        clearInterval(timer);
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
            let userAnswerTrim = userAnswer.trim();

            (answerContainer.querySelector(selector) || {}).disabled = true;
            // (answerContainer.querySelector(selector) || {}).style.backgroundColor = 'lightgray';
            if (userAnswerTrim.toLowerCase() === currentQuestion.correctAnswer.toLowerCase()) {

                // add to the number of correct answers
                numCorrect++;
                // color the answers green
                answerContainers[questionNumber].style.color = 'lightgreen';
                (answerContainer.querySelector(selector) || {}).style.backgroundColor = 'green';
                (answerContainer.querySelector(selector) || {}).style.color = 'white';
            }
            // if answer is wrong or blank
            else {
                // color the answers red
                (answerContainer.querySelector(selector) || {}).style.backgroundColor = 'red';
                (answerContainer.querySelector(selector) || {}).style.color = 'white';
                answerContainers[questionNumber].style.color = 'red';
            }
        });

        if (timer_out === 'true') {
            resultsContainer.innerHTML = 'Your time is over.<br>You got ' + numCorrect + ' out of ' + myQuestions.length + '.';
        } else {
            // show number of correct answers out of total
            resultsContainer.innerHTML = 'You got ' + numCorrect + ' out of ' + myQuestions.length + '. <br> Well done!!!';
        }
    }

    // display quiz right away
    buildQuiz();
    // CheckTime();

    // to show the welcome/ending slides instead of questions
    function showWrapperSlide(n) {
        if (currentSlideWrapper == 0) {
            slides[currentSlide].classList.remove('active-slide');
            slides_wrapper[n].classList.add('active-slide');
            currentSlideWrapper = n;
        }
    }

    function hideWrapperSlide() {
        slides_wrapper[currentSlideWrapper].classList.remove('active-slide');
    }

    const slides = document.querySelectorAll(".slide");
    const slides_wrapper = document.querySelectorAll(".slide_wrapper")

    let currentSlide = 0;
    let currentSlideWrapper = 0;
    showWrapperSlide(0);


    function showInitialSlide() {
        // to start the timer
        CheckTime();
        // to show the first question
        showSlide(0);
        // to hide the initial slide
        hideWrapperSlide();
    }

    function showSlide(n) {
        slides[currentSlide].classList.remove('active-slide');
        slides[n].classList.add('active-slide');
        currentSlide = n;
        startButton.style.display = 'none';
        if (currentSlide === 0) {
            previousButton.style.display = 'none';
        } else {
            previousButton.style.display = 'inline-block';
        }
        if (currentSlide === slides.length - 1) {
            nextButton.style.display = 'none';
            submitButton.style.display = 'block';
        } else {
            nextButton.style.display = 'inline-block';
            submitButton.style.display = 'none';
        }
    }

    function showNextSlide() {
        // showSlide(currentSlide + 1);
        const answerContainers = quizContainer.querySelectorAll('.answers');
        const answerContainer = answerContainers[currentSlide];
        const selector = 'input[name=question' + currentSlide + ']';
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
        let userAnswerTrim = userAnswer.trim();

        if (userAnswer === "") {
            // messagesContainer.innerHTML = "Your answer is empty, please write an answer";
            // messagesContainer.style.color = 'red';
            if (currentSlide === slides.length - 1) {
                    messagesContainer.innerHTML = "";
                    // show results if it is the last slide. This way I can delete the current message container content.
                    showResults('false');
                } else {
                    // (answerContainer.querySelector(selector) || {}).disabled = true;
                    (answerContainer.querySelector(selector) || {}).style.backgroundColor = 'white';
                    // (answerContainer.querySelector(selector) || {}).style.color = 'white';
                    showSlide(currentSlide + 1);
                    messagesContainer.innerHTML = ""
                }

        } else {
            if (myQuestions[currentSlide].correctAnswer.toLowerCase() === userAnswerTrim.toLowerCase()) {
                if (currentSlide === slides.length - 1) {
                    messagesContainer.innerHTML = "";
                    // show results if it is the last slide. This way I can delete the current message container content.
                    showResults('false');
                } else {
                    (answerContainer.querySelector(selector) || {}).disabled = true;
                    (answerContainer.querySelector(selector) || {}).style.backgroundColor = 'green';
                    (answerContainer.querySelector(selector) || {}).style.color = 'white';
                    showSlide(currentSlide + 1);
                    messagesContainer.innerHTML = ""
                }
            } else {
                (answerContainer.querySelector(selector) || {}).style.backgroundColor = 'red';
                (answerContainer.querySelector(selector) || {}).style.color = 'white';
                messagesContainer.innerHTML = "Your answer is not correct, please try again <br> or leave it empty to go to the next question.";
                messagesContainer.style.color = 'red';
            }
        }


    }

    function showPreviousSlide() {
        showSlide(currentSlide - 1);
        messagesContainer.innerHTML = ""
    }

    previousButton.addEventListener("click", showPreviousSlide);
    nextButton.addEventListener("click", showNextSlide);


    // submitButton.addEventListener('click', showResults);
    // on submit, still call showNextSlide, there I handle if it is the last slide
    submitButton.addEventListener('click', showNextSlide);
    startButton.addEventListener('click', showInitialSlide);
}