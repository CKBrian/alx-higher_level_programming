/* global $ */
/* adds a <li> element to a list when the user clicks on the tag DIV#add_item */
$('DIV#add_item').click(() => {
  const item = '<li>Item</li>';
  $('UL.my_list').append(item);
});
