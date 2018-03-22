/*
  RULES GIVEN:
  "Set" is a card game where a group of players try to identify a "set" of c
  ards from those placed face-up on a table.
  Each card has an image on it with 4 orthogonal attributes:
   - Color (red, green, or purple)
   - Shape (diamond, squiggle, or oval)
   - Shading (solid, empty, or striped)
   - Number (one, two, or three)

  Three cards are a part of a set if, for each property, the values are
  all the same or all different.

  For example:
  - The cards "two red solid squiggles", "one green solid diamond",
    "three purple solid ovals" would make up a set. (number, shape, and color
    are different, shading is the same)

  - The cards "two red solid squiggles", "one green solid squiggles",
    "three purple solid ovals" would not make up a set, because shape is the
     same on two cards, but different on the third.

   - A game of Set starts by dealing 12 cards, face-up. When a player sees
     three cards that make up a set, they yell "Set!" and grab the cards.
     New cards are dealt from the deck to replace them.

  - If no player can find a set, three more cards are dealt
    (to make 15, then 18, then 21...)

  - The game is over when there are no cards left in the deck, and no
    sets left on the table. The player with the most sets wins.
*/


/*
  Seach for TODO to locate the required methods!
  There are three Todos:
  - "A method that takes three cards, and determines whether
    the three cards make a set"
  - "A method that given a "board" of cards, will either find a set,
     or determine if there are no sets on the table"
  - "A method that will play an entire game of Set, from beginning to end,
    and return a list of each valid sets you removed from the board."
*/

/*
  Set Game assumptions:
  - This game is played in the terminal w/ "node set.js"
  - There are four players in the game
  - Players keep the cards when they find a set
  - Players do not have a turn, so the fastest get the set (random)
  - When there's a tie at the end, player added later to the game wins
  - Sets that players grabbed will be printed at the end for each player
*/

/*
  There are 5 modules in this program:
    - cardModule
    - deckModule
    - boardModule
    - playerModule
    - gameModule
*/

// -------------------------------
// Card Module
var cardModule = (function() {
  // Card attributes
  var colorSet   = ["red", "green", "purple"],
      shapeSet   = ["diamond", "squiggle", "oval"],
      shadingSet = ["solid", "empty", "striped"],
      numberSet  = ["one", "two", "three"];

  // Card object
  function Card(color, shape, shading, number) {
    this.color = color;
    this.shape = shape;
    this.shading = shading;
    this.number = number;
  }

  // cardModule public methods
  return {
    // Create new Card with random attributes
    getNewCard: function () {
      var newCard = new Card(colorSet[Math.floor(Math.random() * 3)],
                              shapeSet[Math.floor(Math.random() * 3)],
                              shadingSet[Math.floor(Math.random() * 3)],
                              numberSet[Math.floor(Math.random() * 3)]);
      return newCard;
    }
  };
})();

// ----------------------------------
// Deck Module

var deckModule = (function() {
  // Deck variable that hold the current deck
  var deck;

  // How many cards can be in the deck
  var DECK_SIZE = 60;

  // Check if DECK_SIZE is more than 12 && divisible by 3
  function checkDeckSize() {
      if (DECK_SIZE < 12) throw new Error("DECK_SIZE needs to be over 12");
      if (DECK_SIZE % 3 != 0) throw new Error("DECK_SIZE need to be divisible by 3");
  }

  // Return a new deck with random cards
  function generateDeck() {
    checkDeckSize();
    deck = [];
    for (var i = 0; i < DECK_SIZE; i++) {
      deck.push(cardModule.getNewCard());
    }
    return deck;
  }

  // deckModule public methods
  return {
    init: function() {
      return generateDeck();
    }
  };
})();

// -----------------------------
// Board Module
var boardModule = (function() {
  // Variables to store board and deck
  var board,
      deck;

  // Initializes the board;
  function init(input) {
    board = [];
    deck = input;
    addTwelveCards();
    return board;
  }

  // Add twelve cards to the board for initialization
  function addTwelveCards() {
    for (var i = 0; i < 12; i++) {
      board.push(deck.pop());
    }
  }

  // TODO 1
  // Return true if three cards is a set
  function checkSet(card1, card2, card3) {
    if (card1 == undefined || card2 == undefined || card3 == undefined)
      throw new Error("Card is undefined");

    return isAllSameorDiff(card1.color, card2.color, card3.color) &&
           isAllSameorDiff(card1.shape, card2.shape, card3.shape) &&
           isAllSameorDiff(card1.shading, card2.shading, card3.shading) &&
           isAllSameorDiff(card1.number, card2.number, card3.number);
  }

  // Helpter function for CheckSet()
  // Return true if three attributes are all same or all different
  function isAllSameorDiff(a, b, c) {
    return (a == b && a == c && b == c) ||
           (a != b && a != c && b != c);
  }

  // TODO 2
  // Find a set in the board. If no set is found, log the error
  var findSet = function() {
    // Cards that will be checked
    var c1, c2, c3,
        foundSet;
    for (var i = 0; i < board.length-2; i++) {
      c1 = board[i];
      for (var j = i + 1; j < board.length-1; j++) {
        c2 = board[j];
        for (var k = j + 1; k < board.length; k++) {
          c3 = board[k];
          if (checkSet(c1, c2, c3)) {
            removeSet(i, j, k);
            playerModule.givePointToRandPlayer(c1, c2, c3);
            foundSet = [c1, c2, c3];
            addThreeCards();
            return foundSet;
          };
        }
      }
    };

    // Log if no set was found
    if (foundSet == undefined) {
      console.log("No Match Found");
    }
    addThreeCards()
    return foundSet;
  }

  // Remove three cards and shift the rest of the deck
  function removeSet(pos1, pos2, pos3) {
    board.splice(pos1,1);
    board.splice(pos2,1);
    board.splice(pos3,1);
  }

  // Add three cards to the board
  function addThreeCards() {
    var numCardToReplace = 3;
    // Check if the deck is empty
    if (deck.size < 3) {
      throw new Error("not enough cards left in the deck");
    };

    for (var i = 0; i < numCardToReplace; i++) {
      board.push(deck.pop());
    }
  }

  var checkRemainingBoard = function() {
    var tempSet = 0;
    while (tempSet != undefined) {
      try {
        tempSet = findSet();
      }
      catch(err) {
        console.log("No more set found in the board. \n");
        tempSet = undefined;
      }
    }
  }

  // boardModule public methods
  return {
    init: function(input) {
        return init(input);
    },

    findSet: findSet,

    checkRemainingBoard: checkRemainingBoard
  }
})();


// Call main to simulate the game!
main();
