const closeDiv = document.getElementById("close");
const cancelDiv = document.getElementById("closeError");
const success = document.getElementById("success_message");
const error = document.getElementById("error_message");

if (cancelDiv != null) {

  //   closeDiv.addEventListener("click", (event) => {
  //     if (success.style.display != "flex") {
  //       success.style.display == "flex";
  //     } else {
  //       success.style.display == "none";
  //     }
  //   });

  cancelDiv.addEventListener("click", (event) => {
    if (error.style.display != "flex") {
      error.style.display == "flex";
    } else {
      error.style.display == "none";
    }
  });
}
