let getId = document.querySelectorAll('.buy')
// console.log(getId)
// getId.addEventListener('click', getDataID)
// function getDataID() {
    
// }
getId.forEach( (item) => {
    item.addEventListener('click', function() {
        console.log(item.getAttribute('data-id'))
    })
})


function loadDoc() {
    var xhttp = new XMLHttpRequest();
    
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        console.log(this.responseText)
    //    document.getElementById("demo").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "http://127.0.0.1:8000/admin/orders/gig", true);
    xhttp.send();
}