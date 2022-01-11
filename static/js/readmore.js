const readMoreBtn = document.querySelector(".read-more-btn");
const storyline = document.querySelector(".storyline");

readMoreBtn.addEventListener("click", (e) => {
  storyline.classList.toggle("show-more");
  if (readMoreBtn.innerText === "Read more") {
    readMoreBtn.innerText = "Read less";
  } else {
    readMoreBtn.innerText = "Read more";
  }
});
