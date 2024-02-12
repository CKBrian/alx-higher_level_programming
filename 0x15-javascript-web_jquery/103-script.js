/* global $ */
$(document).ready(() => {
  /* On keypress event */
  $('INPUT#language_code').on('keypress', (event) => {
    if (event.which === 13) {
      const lang = $('INPUT#language_code').val();
      $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
        $('DIV#hello').text(data.hello);
      });
    }
  });

  /* on button click event */
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang}`, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
