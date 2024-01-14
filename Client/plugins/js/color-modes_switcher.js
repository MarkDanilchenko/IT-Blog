try {
  const colorMode = localStorage.getItem("colorMode");
  if (colorMode === null) {
    throw new Error("The color theme switched to light-mode as default");
  } else {
    $("html").attr("data-bs-theme", `${colorMode}`);
    if (colorMode == "dark") {
      $("#colorMode_switcher").attr("checked", true);
    } else {
      $("#colorMode_switcher").attr("checked", false);
    }
  }
} catch (e) {
  $("html").attr("data-bs-theme", `${"light"}`);
  $("#colorMode_switcher").attr("checked", false);
  localStorage.setItem("colorMode", "light");
}

// colorMode switcher button
if (document.getElementById("colorMode_switcher")) {
  document.getElementById("colorMode_switcher").addEventListener("click", () => {
    const colorMode = $("html").attr("data-bs-theme");
    if (colorMode == "dark") {
      $("html").attr("data-bs-theme", "light");
      //   $("header").css("background-color", "#fff");
      localStorage.setItem("colorMode", "light");
    } else if (colorMode == "light") {
      $("html").attr("data-bs-theme", "dark");
      //   $("header").css("background-color", "#212529");
      localStorage.setItem("colorMode", "dark");
    }
  });
}
