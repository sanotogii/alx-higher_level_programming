$(document).ready(function () {
  $('DIV#toggle_header').on('click', function () {
    $('header').toggleClass(function () {
      if ($(this).hasClass('red')) {
        return 'green';
      } else {
        return 'red';
      }
    });
  });
});
