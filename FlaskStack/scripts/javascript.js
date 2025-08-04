
/* Manage Dynamic Table for A values */
var counter = 0;

function addControlRow() {
  var table = document.getElementById("a_i_table").getElementsByTagName('tbody')[0];
  var row = table.insertRow();
  counter++;

  var a_number = row.insertCell(0);
  var begin = row.insertCell(1);
  var end = row.insertCell(2);
  var increment = row.insertCell(3);
  a_number.innerHTML = `a${counter}`;
  begin.innerHTML = "0";
  end.innerHTML = "1";
  increment.innerHTML = "1";
}

function removeControlRow() {
  var table = document.getElementById("a_i_table");
  if (counter > 0) {
    var row = table.deleteRow(-1);
    counter--;
  }
}