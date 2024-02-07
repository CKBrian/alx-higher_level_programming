/* global $ */
$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data, status) => {
  $('DIV#character').text((name, old) => {
    return data.name;
  });
});
