import pandas as pd


def unpack_df(cards):
    number = []
    shape = []
    color = []
    shading = []
    for card in cards:
        number.append(card[0])
        shape.append(card[1])
        color.append(card[2])
        shading.append(card[3])
    df = pd.DataFrame({'number':number,'shape':shape,'color':color,'shading':shading})
    return df

def unpack_dict(cards):
    board = {}
    for i in range(0,len(cards)):
        board[i] ={'number':cards[i][0],
                   'shape':cards[i][1],
                   'color':cards[i][2],
                   'shading':cards[i][3]}
   
    return board

    

def unpack_result(cards):
    predictions = []
    for card in cards:
        predictions.append(list(card[1]))
    
    board = {}
    for i in range(0,len(cards)):
        board[i] ={'number':predictions[i][0],
                   'shape':predictions[i][1],
                   'color':predictions[i][2],
                   'shading':predictions[i][3]}
   
    return board