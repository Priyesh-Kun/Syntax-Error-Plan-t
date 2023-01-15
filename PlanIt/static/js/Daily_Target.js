let input = document.querySelector(".text ");
let addBtn = document.querySelector(".Add ");
let tasks = document.querySelector(".tasks ");

input.addEventListener("keyup", () => {
  if (input.value.trim() != 0) {
    addBtn.classList.add("active");
  } else {
    addBtn.classList.remove("active");
  }
});
function hide() {
  let utilities = document.getElementById("utilities");
  let utiliesmenu = document.getElementById("utilitiesmenu");
  if (utiliesmenu.style.display != "flex") {
    utiliesmenu.style.display = "flex";
  } else {
    utiliesmenu.style.display = "none";
  }
}

addBtn.addEventListener("click", () => {
  if (input.value.trim() != 0) {
    let newItem = document.createElement("div");
    newItem.classList.add("item");
    newItem.innerHTML = `
    <p> ${input.value}</p><div class="item-btn">
        <i class="fa-solid fa-pen-to-square"></i>
        <i class="fa-solid fa-xmark"></i>
      </div>`;
    tasks.appendChild(newItem);
    input.value = " ";
  } else {
    alert("Please Enter A  Task");
  }
});

//Deleting an event
tasks.addEventListener("click", (e) => {
  if (e.target.classList.contains("fa-xmark")) {
    e.target.parentElement.parentElement.remove();
  }
});

//Marking a complete event
tasks.addEventListener("click", (e) => {
  if (e.target.classList.contains("fa-pen-to-square")) {
    e.target.parentElement.parentElement.classList.toggle("completed");
    let audio = new Audio("/static/sound/taskcompletion.mp3");
    audio.play();
  }
});

function voice() {
  var recognition = new webkitSpeechRecognition();
  recognition.lang = "en-GB";
  recognition.onresult = function (event) {
    console.log(event);
    document.getElementById("text").value = event.results[0][0].transcript;
  };
  recognition.start();
}
