const deleteBtn = document.querySelector("#delete_btn");
const popup = document.querySelector(".popup");
const body = document.body;

deleteBtn.addEventListener("click", (e) => {
  popup.classList.toggle("show-popup");
  if (popup.classList.contains("show-popup")) {
    body.classList.add("scroll-hidden");
  } else {
    body.classList.remove("scroll-hidden");
  }
});

function ClosePopup() {
  popup.classList.remove("show-popup");
  body.classList.remove("scroll-hidden");
}
