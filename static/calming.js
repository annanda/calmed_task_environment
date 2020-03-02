window.onload = function () {
    document.getElementById("breathing_click").onclick = function () {
        document.getElementById("calm_links").style.display = "none";
        document.getElementById("calm_video").style.display = "block";
        document.getElementById("calm_video_play").play()

    }
    document.getElementById("neutral_mood").onclick = function () {
        mood = 'neutral_mood';
        make_request(mood, task);
    }
    document.getElementById("unhappy_mood").onclick = function () {
        mood = 'unhappy_mood';
        make_request(mood, task);
    }
    document.getElementById("where_hidden_button").innerHTML = "<a class=\"hidden_button_link\" href=" + next_page + "><div class=\"hidden_button\">go on</div></a>"
}