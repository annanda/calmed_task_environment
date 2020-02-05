function make_request(text, task, method = "post") {
    $.ajax({
        url: '/store_mood',
        type: 'POST',
        data: JSON.stringify({
            mood: text,
            task: task
        }),
        contentType: 'application/json',
        processData: false,
        success: function (msg) {
            document.getElementById("answer_mood").innerHTML = 'Thanks!';
            document.getElementById("mood_buttons").style.display = 'None'

        }
        // async: false
    });

}

function get_url_vars() {
    let vars = {};
    let parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}

let next_page = '';
let task = ''
window.onload = function () {
    task = get_url_vars()["task"];
    let mood = ''
    if (task == 'first_task') {
        next_page = 'calming_content';
    }
    if (task == 'second_task') {
        next_page = 'calming_content_2';
    }
    if (task == 'third_task') {
        next_page = 'calming_content_3';
    }
    if (task == 'forth_task') {
        next_page = 'calming_content_4';
    }
    document.getElementById("happy_mood").onclick = function () {
        mood = 'happy_mood';
        make_request(mood, task);
    }
    document.getElementById("neutral_mood").onclick = function () {
        mood = 'neutral_mood';
        make_request(mood, task);
    }
    document.getElementById("unhappy_mood").onclick = function () {
        mood = 'unhappy_mood';
        make_request(mood, task);
    }
}

let time_to_move = get_url_vars()["time_next"];
setTimeout(function () {
    window.location.href = next_page;
}, time_to_move);