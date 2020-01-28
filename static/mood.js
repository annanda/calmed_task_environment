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
            document.getElementById("answer_mood").innerHTML = 'Thanks!'
            // task_created = msg;
            // show_feedback_to_user(task_created.result_task_id);

        }
        // async: false
    });

}

window.onload = function () {
    document.getElementById("happy_mood").onclick = function () {
        let mood = 'happy_mood';
        let task = 'second_task'
        make_request(mood, task);
    }
    // var element = document.getElementById("div1");
}