function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? match[2] : null;
}

function recordVisit() {
  if (!getCookie("visited") || !localStorage.getItem("visited")) {
    fetch("/visit")
      .then(res => res.json())
      .then(() => {
        document.cookie = "visited=true; max-age=" + 60*60*24 + "; path=/";
        localStorage.setItem("visited", "true");
      })
      .catch(err => console.error("Error recording visit:", err));
  } else {
    console.log("User already counted, skipping /visit call.");
  }
}

function updateVisitors() {
    fetch("/visCount")
        .then(response => response.json())
        .then(data => {
            // data is like { "visitors": 42 }
            const count = data.visitors;
            const span = document.getElementById("visitorCount");

            if (span) {
                span.textContent = count;
            }
        })
        .catch(err => console.error("Failed to fetch visitor count:", err));
}

// Trigger on page load
setInterval(updateVisitors, 5000); // refresh every 5 seconds
window.addEventListener("DOMContentLoaded", () => {
    recordVisit();
    updateVisitors();
});