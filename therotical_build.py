import sys
import numpy as np
import cv2

def rectify(h):

def preprocess(img):
    blur = cv2.GaussianBlur(img,(5,5),2)


def imgdiff(img1,img2):

    return np.sum(diff)

def find_closest_card(training,img):
    features = preprocess(img)
    return sorted(training.values(),key = Lambda x :imgdiff(x[1].features))[0][0]

def getCards(im,numcards=4):
    pass

def get_training(training_label_filename,training_image_filename,num_training_cards,avoid_cards=None):
    return training
    


if __name__ == '__main__':
  if len(sys.argv) == 6:
    filename = sys.argv[1]
    num_cards = int(sys.argv[2])
    training_image_filename = sys.argv[3]
    training_labels_filename = sys.argv[4]
    num_training_cards = int(sys.argv[5])
    print(sys.argv)

    training = get_training(training_labels_filename,training_image_filename,num_training_cards)

    im = cv2.imread("/Users/anais/Desktop/Playing-Card-Recognition/test.jpg")
    preprocess(im)

    width = im.shape[0]
    height = im.shape[1]
    if width < height:
      im = cv2.transpose(im)
      im = cv2.flip(im,1)

    # Debug: uncomment to see registered images
    for i,c in enumerate(getCards(im,num_cards)):
      card = find_closest_card(training,c,)
      cv2.imshow(str(card),c)
      cv2.waitKey(0)

    cards = [find_closest_card(training,c) for c in getCards(im,num_cards)]
    print (cards)

  else:
    print (__doc__)
