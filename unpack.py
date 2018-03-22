import pandas as pd


def unpack(cards):
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