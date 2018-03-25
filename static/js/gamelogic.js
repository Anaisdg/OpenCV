// -----------------------------
// Board Module

var boardModule = function (x) {
  // Variables to store board and deck

  // Filling the Board with Cards from the API

// Init Method
// ******************************
  function init() {
    var x;
    Plotly.d3.json('/fakedata', function (error, response) {
      x = callback(response);


    })
    console.log(x);
    return x;


  }

  function callback(data) {
    var board = [];
    for (i = 0; i < data.length; i++) {
      board[i] = {
        color: data[i].color,
        shape: data[i].shape,
        shading: data[i].shading,
        number: data[i].number
      }
    }

    return board;
  }

  //CheckSet Method
  //******************************************************************* */
  // Return true if three cards is a set

  function checkSet(card1, card2, card3) {
    //In case Cards are undefined
    if (card1 == undefined || card2 == undefined || card3 == undefined)
      throw new Error("Card is undefined");

    return isAllSameorDiff(card1.color, card2.color, card3.color) &&
      isAllSameorDiff(card1.shape, card2.shape, card3.shape) &&
      isAllSameorDiff(card1.shading, card2.shading, card3.shading) &&
      isAllSameorDiff(card1.number, card2.number, card3.number);
  }

  // isllSameorDiff Function
  /************************************************************************ */
  // Helpter function for CheckSet()
  // Return true if three attributes are all same or all different
  function isAllSameorDiff(a, b, c) {
    return (a == b && a == c && b == c) ||
      (a != b && a != c && b != c);
  }

// findSet Function
/************************************************************************ */
  // Find a set in the board. If no set is found, log the error
  var findSet = function () {
    // Cards that will be checked
    var c1, c2, c3,
      foundSet;
    for (var i = 0; i < board.length - 2; i++) {
      c1 = board[i];
      for (var j = i + 1; j < board.length - 1; j++) {
        c2 = board[j];
        for (var k = j + 1; k < board.length; k++) {
          c3 = board[k];
          if (checkSet(c1, c2, c3)) {
            removeSet(i, j, k);

            foundSet = [c1, c2, c3];
            console.log(foundSet);
            return foundSet;
          };
        }
      }
    };

    // Log if no set was found
    if (foundSet == undefined) {
      console.log("No Match Found");
    }
    console.log(foundSet);
    return foundSet;
  }

  // Remove three cards and shift the rest of the deck
  function removeSet(pos1, pos2, pos3) {
    board.splice(pos1, 1);
    board.splice(pos2, 1);
    board.splice(pos3, 1);
  }


  var checkRemainingBoard = function () {
    var tempSet = 0;
    while (tempSet != undefined) {
      try {
        tempSet = findSet();
      } catch (err) {
        console.log("No more set found in the board. \n");
        tempSet = undefined;
      }
    }
  }

  // boardModule public methods
  return {
    init: function (input) {
      return init(input);
    },

    findSet: findSet,

    checkRemainingBoard: checkRemainingBoard
  }
};

// gameModule

var gameModule = (function () {

  var startGame = function () {

    board = boardModule.init();

    console.log("Board is good to go!");
    console.log(board);
  }


  var playGame = function () {
    console.log("Starting the game!");
    // Run game until the deck is empty
    while (board.length != 0) {
      boardModule.findSet()
    }
    console.log("No more cards in the deck");

    // Check if there are any set left in the board
    boardModule.checkRemainingBoard();
    console.log("Finishing the game... \n");
  }

  // gameModule public methods
  return {

    init: startGame,
    playGame: playGame
  }
})()

//Run the Game simulation
function main() {


  gameModule.init();
  gameModule.playGame();

}
// Call main to simulate the game!
main();