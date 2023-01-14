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

addBtn.addEventListener("click", () => {
  if (input.value.trim != 0) {
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
tasks.addEventListener('click', (e)=>{
    if(e.target.classList.contains('fa-xmark')){
        e.target.parentElement.parentElement.remove()
    }
})

//Marking a complete event
tasks.addEventListener('click', (e)=>{
    if(e/target.classList.contains('fa-pen-to-square')){
        e.target.parentElement.parentElement.classList.toggle('completed');
    }}
)

