const dashboard1 = document.querySelector("#dashboard-1")
const dashboard2 = document.querySelector("#dashboard-2")
const dashboard3 = document.querySelector("#dashboard-3")



document.getElementById("boton-dashboard-1").onclick = function() {
    dashboard1.style.display = "block"
    dashboard2.style.display = "none"
    dashboard3.style.display = "none"
}

document.getElementById("boton-dashboard-2").onclick = function() {
    dashboard1.style.display = "none"
    dashboard2.style.display = "block"
    dashboard3.style.display = "none"
}

document.getElementById("boton-dashboard-3").onclick = function() {
    dashboard1.style.display = "none"
    dashboard2.style.display = "none"
    dashboard3.style.display = "block"
}