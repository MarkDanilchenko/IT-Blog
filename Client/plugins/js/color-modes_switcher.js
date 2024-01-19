/* `$("#colorMode_switcher").attr("checked", true);` is setting the `checked` attribute of the
element with the id `colorMode_switcher` to `true`. This is typically used for checkboxes or
radio buttons to indicate that the element is selected or checked. In this case, it is used to
set the switcher button to the "dark" color mode if the `colorMode` variable is equal to
"dark". */

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
  document
    .getElementById("colorMode_switcher")
    .addEventListener("click", () => {
      const colorMode = $("html").attr("data-bs-theme");
      if (colorMode == "dark") {
        $("html").attr("data-bs-theme", "light");
        // signout dots
        $(".dot").css("background", "#000000");
        localStorage.setItem("colorMode", "light");
      } else if (colorMode == "light") {
        $("html").attr("data-bs-theme", "dark");
        // signout dots
        $(".dot").css("background", "#ffffff");
        localStorage.setItem("colorMode", "dark");
      }
    });
}
