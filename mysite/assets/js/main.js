// initialization of navbar 
$(document).ready(function(){
    $('.sidenav').sidenav();
  });
// initialization of Floating Action Button
$(document).ready(function(){
    $('.fixed-action-btn').floatingActionButton();
  });
// initialization of Tooltips
$(document).ready(function(){
    $('.tooltipped').tooltip();
  });
// initialization of Feature Discovery
$(document).ready(function(){
    $('.tap-target').tapTarget();
  });
// initialization of carousel
$('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true
  });
// initialization of carousel autoplay
autoplay();
function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 4500);
}
// intialization of Material Box
$(document).ready(function(){
    $('.materialboxed').materialbox();
  });
// initialization of Modal
 $(document).ready(function(){
    $('.modal').modal();
  });
// initialization of Text Counter
$(document).ready(function() {
    $('input#input_text, textarea#message').characterCounter();
  });
        