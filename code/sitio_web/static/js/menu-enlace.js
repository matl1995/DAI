$(document).ready(function(){
    $("#botones").hover(function(){
        $("#botones1").show("slow", function(){
            //Animación completa
        });
    }, function(){
        $("#botones1").hide("slow", function(){
            //Animación completa
        });
    });
});