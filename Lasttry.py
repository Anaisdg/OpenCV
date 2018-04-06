import cv2
import numpy as np


def preprocess(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)
    thresh = cv2.adaptiveThreshold(blur,255,1,1,11,1)
    return thresh

def imgdiff(img1,img2):
    img1 = cv2.GaussianBlur(img1,(5,5),5)
    img2 = cv2.GaussianBlur(img2,(5,5),5)
    diff = cv2.absdiff(img1,img2)
    diff = cv2.GaussianBlur(diff,(5,5),5)
    flag, diff = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY)
    return np.sum(diff)


def get_training(training_labels_filename,training_image_filename,num_training_cards,avoid_cards=None):
    training = {}

    labels ={}

    for line in open("train.txt",'r'):
        key, num, shape,fill = line.strip().split()
        labels[int(key)] = (num,shape,fill)
    

    print ("Training")

    im = cv2.imread(training_image_filename)
    for i,c in enumerate(getCards(im,num_training_cards)):
        if avoid_cards is None or (labels[i][0] not in avoid_cards[0] and labels[i][1] not in avoid_cards[1]):
            training[i] = (labels[i], preprocess(c))

    print ( training)
    return training


def newgetCards(im, numcards=12):
  gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray,(1,1),1000)
  flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY) 
       
  _,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  contours = sorted(contours, key=cv2.contourArea,reverse=True)[:numcards]  

  for card in contours:
    peri = 0.02*cv2.arcLength(card,True)
    approx = cv2.approxPolyDP(card,peri,True)
    #debug
    box = np.int0(approx)
    cv2.drawContours(im,[box],0,(255,255,0),6)
    imx = cv2.resize(im,(1000,600))
    cv2.imshow('a',imx)      
    
    h = np.float32([[0,0],[399,0],[399,399],[0,399]])

    transform = cv2.getPerspectiveTransform(approx,h)
    warp = cv2.warpPerspective(im,transform,(400,400))
    
    yield warp

def getCards(img,numcards,epsilon=0.02):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(1,1),1000)
    flag, thresh = cv2.threshold(blur, 120, 255, cv2.THRESH_BINARY)
    # Find contours
    image,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea,reverse=True) 
    # Select long perimeters only
    perimeters = [cv2.arcLength(contours[i],True) for i in range(len(contours))]
    listindex=[i for i in range(numcards) if perimeters[i]>perimeters[0]/2]
    # Show image
    imgcont = img.copy()
    [cv2.drawContours(imgcont, [contours[i]], 0, (0,255,0), 5) for i in listindex]
    imx = cv2.resize(imgcont,(1000,600))
    cv2.imshow('a',imx)    

    warp = list(range(numcards))
    
    for i in range(numcards):
        card = contours[i]
        peri = 0.02*cv2.arcLength(card,True)
        approx =  cv2.approxPolyDP(card,peri,True)
        rect = cv2.minAreaRect(contours[i])
        r = cv2.boxPoints(rect)

      
      
        h = np.float32([[0,0],[399,0],[399,399],[0,399]])
        approx = np.float32([item for sublist in approx for item in sublist])
        print(approx.shape)
        transform = cv2.getPerspectiveTransform(approx,h)
        warp[i] = cv2.warpPerspective(img,transform,(400,400))

    # Show perspective correction
    
    new_img_list = []
    for i in range(numcards):
        new_img = cv2.cvtColor(warp[i],cv2.COLOR_BGR2RGB)
        new_img_list.append(warp[i])
        
    
    
    return new_img_list



def find_closest_card(training,img):
    features = preprocess(img)
    return sorted(training.values(), key=lambda x:imgdiff(x[1],features))[0][0]

if __name__ == '__main__':
  
    filename = "train_original.jpg"
    num_cards = 12
    training_image_filename = "train_original.jpg"
    training_labels_filename = "train.txt"    
    num_training_cards = 12

    training = get_training(training_labels_filename,training_image_filename,num_training_cards)

    im = cv2.imread(filename)

    width = im.shape[0]
    height = im.shape[1]
    if width < height:
        im = cv2.transpose(im)
        im = cv2.flip(im,1)

    # for i,c in enumerate(getCards(im,num_cards)):
    #   card = find_closest_card(training,c,)
    #   cv2.imshow(str(card),c)
    # cv2.waitKey(0) 
    
    cards = [find_closest_card(training,c) for c in getCards(im,num_cards)]
    print (cards)
    
else:
    print (__doc__)