$(document).ready(function(){

  $(".pickup-hover").hide();
  $(".interview-hover").hide();
  $(".promotion-hover").hide();

  // Pitch Categories Hover Effect
  $(".pickup").hover(function(){
    $(".pickup-hover").toggle();
  });

  $(".interview").hover(function(){
    $(".interview-hover").toggle();
  });

  $(".promotion").hover(function(){
    $(".promotion-hover").toggle();
  });

  $("#like").click(function(){
    num = parseInt($(".like-num").text());
    $(".like-num").text(num+=1);
  });

  $("#dislike").click(function(){
    num = parseInt($(".dislike-num").text());
    $(".dislike-num").text(num+=1);
  });

});