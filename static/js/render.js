//table add rows as needed
var $tbody = document.querySelector("tbody");

Plotly.d3.json('/fakedata', function (error, response) {
    var tbl_body = document.createElement("tbody");
    
    renderTable(response);
})

function renderTable(board) {
   
   
   
    $tbody.innerHTML = "";
   
    for (var i = 0; i < board[0].length; i++) {
        var set = board[0][i];

        // console.log(set);
        
        var $row = $tbody.insertRow(i)
        for (var j = 0; j < set.length; j++) {
        
        var cards = set[j];
        console.log(cards);
        var $cell = $row.insertCell(j);
        $cell.innerText=cards;
        }
    }
}

//table with render base on the length of the data array
//