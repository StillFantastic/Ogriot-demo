$("#meow").click(function() {
    var imgSrc = "meow.jpg";
    var obj = document.getElementById("pic");　　
    obj.src = imgSrc;
    $("#name").html("名稱 : 妞妞");
    $("#temperature").html("溫度 : 24度");
    $("#humidity").html("濕度 : 60%");
    $("#count").html("數量 : 3顆");
    $("#mature").html("成熟度：微熟")
});
$("#momo").click(function() {
    var imgSrc = "test_up.jpg";
    var obj = document.getElementById("pic");　　
    obj.src = imgSrc;
    $("#name").html("名稱 : 饅頭");
    $("#temperature").html("溫度 : 30度");
    $("#humidity").html("濕度 : 47%");
    $("#count").html("數量 : 20顆");
    $("#mature").html("成熟度：過熟")
});