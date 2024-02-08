/* global $ */
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data, status) => {
  const objs = data.results;
  objs.forEach((item) => {
    const item1 = $('<li>' + item.title + '</li>');
    $('UL#list_movies').append(item1);
  });
});
