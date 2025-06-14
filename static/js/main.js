$(document).ready(function () {
  const body = $("body");
  const toggleBtn = $("#theme-toggle");
  const icon = $("#theme-icon");

  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    body.attr("data-bs-theme", "dark");
    icon.removeClass("fa-moon").addClass("fa-sun");
  }

  toggleBtn.on("click", function () {
    const isDark = body.attr("data-bs-theme") === "dark";
    const newTheme = isDark ? "light" : "dark";

    body.attr("data-bs-theme", newTheme);
    localStorage.setItem("theme", newTheme);

    icon.toggleClass("fa-moon fa-sun");
  });
});
