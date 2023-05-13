const accDetails = document.getElementById("account-details");
const account = document.getElementById("account");
const account_icon = document.getElementById("acc-person");

if (account != null && account_icon != null) {
  account.addEventListener("click", (event) => {
    if (accDetails.style.display != "block") {
      accDetails.style.display = "block";
    } else {
      accDetails.style.display = "none";
    }
  });

  window.addEventListener("click", (event) => {
    if (event.target != account && event.target != account_icon) {
      accDetails.style.display = "none";
    }
  });
}

const nav_section = document.getElementById("nav_section");
const menu_bar = document.getElementById("menu-bar");

if (window.innerWidth <= 500) {
  menu_bar.addEventListener("click", (event) => {
    if (nav_section.style.display != "block") {
      nav_section.style.display = "block";
    } else {
      nav_section.style.display = "none";
    }
  });
}
