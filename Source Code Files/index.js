function hide() {
  let utilities = document.getElementById("utilities");
  let utiliesmenu = document.getElementById("utilitiesmenu");
  if (utiliesmenu.style.display != "flex") {
    utiliesmenu.style.display = "flex";
  } else {
    utiliesmenu.style.display = "none";
  }
}

function hide1() {
  let avt = document.getElementById("avt");
  let compavt = document.getElementById("compavt");
  if(compavt.style.display != "flex"){
    compavt.style.display = "flex";
  }
  else {
    compavt.style.display = "none";
  }
}
