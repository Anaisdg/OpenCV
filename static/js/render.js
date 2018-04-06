//table add rows as needed
var $tbody = document.querySelector("tbody");

Plotly.d3.json('/fakedata', function (error, response) {
    var tbl_body = document.createElement("tbody");
    
    console.log(response);
    renderTable(response);
})

function renderTable(board) {
   
   
   
    $tbody.innerHTML = "";
   
    for (var i = 0; i < board[0].length; i++) {
        var set = board[0][i];

        console.log(set);
        
        var $row = $tbody.insertRow(i)
        
        // for (var j = 0; j < 2; j++) {
        
        // var cards =  set[j];
       
     
      
        var $cell1 = $row.insertCell(0);
        var $cell2 = $row.insertCell(1);
        var $cell3 = $row.insertCell(2);
        var $cell4 = $row.insertCell(3);
        
        $cell2.innerHTML = `<img src="../static/images/${set[0]}.gif"> `;
        $cell3.innerHTML = `<img src="../static/images/${set[1]}.gif"> `;
        $cell4.innerHTML =`<img src="../static/images/${set[2]}.gif">`;
       
    
        $cell1.innerText="Set " + (i+1);
        // }
    }
}

//table with render base on the length of the data array
//