window.onload = function () {
    document.getElementById("breathing_click").onclick = function () {
        document.getElementById("calm_links").style.display = "none";
        document.getElementById("calm_video").style.display = "block";
        document.getElementById('calm_video_play').src = 'static/videos/breathing.mp4';
        document.getElementById('calm_video_play').currentTime = 13;
        document.getElementById("calm_video_play").play()

    }
    document.getElementById("listening_click").onclick = function () {
        document.getElementById("calm_links").style.display = "none";
        document.getElementById("calm_video").style.display = "block";
        document.getElementById('calm_video_play').src = 'static/videos/listening_game.mp4';
        document.getElementById('calm_video_play').currentTime = 13;
        document.getElementById("calm_video_play").play()
    }
    document.getElementById("creatures_sea_click").onclick = function () {
        document.getElementById("calm_links").style.display = "none";
        document.getElementById("calm_video").style.display = "block";
        document.getElementById('calm_video_play').src = 'static/videos/sea_creatures.mp4';
        document.getElementById('calm_video_play').currentTime = 14;
        document.getElementById("calm_video_play").play()
    }
    document.getElementById("peace_out_click").onclick = function () {
        document.getElementById("calm_links").style.display = "none";
        document.getElementById("calm_video").style.display = "block";
        document.getElementById('calm_video_play').src = 'static/videos/peace_out.mp4';
        document.getElementById('calm_video_play').currentTime = 18;
        document.getElementById("calm_video_play").play()
    }
}