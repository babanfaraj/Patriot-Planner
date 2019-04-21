window.onload =
    function () {
    var weekday = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    var today = new Date();
    var date = weekday[today.getDay()]+ " " + (today.getMonth()+1)+'/'+today.getDate()+'/'+today.getFullYear();
        document.getElementById("time-text").innerHTML=date;
    }

