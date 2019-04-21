window.onload =
    function () {
    var today = new Date();
    var date = (today.getMonth()+1)+'/'+today.getDate()+'/'+today.getFullYear();
        document.getElementById("time-text").innerHTML=date;
    }

