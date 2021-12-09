

function changeHref(mealid){


    var rate = document.getElementById("customRange12")
    var btn = document.getElementById("rateButton")
    var target = document.getElementById("favorite2");
    target.href = "/mealrecommend/favorite/"+ mealid.toString() + "/" +rate.value

}



