const deleteBtn = document.querySelector("#delete_btn");
const popup = document.querySelector(".popup");
const body = document.body;
const detail = document.querySelector("#detail");

deleteBtn.addEventListener("click", (e) => {
  popup.classList.toggle("show-popup");
  if (popup.classList.contains("show-popup")) {
    body.classList.add("scroll-hidden");
    detail.classList.add("blur");
  } else {
    body.classList.remove("scroll-hidden");
    detail.classList.remove("blur");
  }
});

function ClosePopup() {
  popup.classList.remove("show-popup");
  body.classList.remove("scroll-hidden");
  detail.classList.remove("blur");
}
