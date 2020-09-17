// navbar menu toggler
document.addEventListener('DOMContentLoaded', function () {
    var sideNav = document.querySelector('.sidenav');
    var instances = M.Sidenav.init(sideNav, {});
    

// initialization of select element
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});


// initialization of textareas
    var textNeedCount = document.querySelectorAll('#input-your-message, #input-word-meaning, #input-word-definition, #input-expression-meaning, #input-expression-definition');
    M.CharacterCounter.init(textNeedCount);


// initialization of datepicker
    var datePicker = document.querySelector('.datepicker');
    var instances = M.Datepicker.init(datePicker, {});


// initializing collapsible
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, {});
});