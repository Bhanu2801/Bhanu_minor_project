var header= document.getElementById("header");
var navBar= document.getElementById("navbar");

var navbarHeight = navBar.offsetHeight;
var headerHeight = header.offsetHeight;

header.style.height = screen.height-navbarHeight;
