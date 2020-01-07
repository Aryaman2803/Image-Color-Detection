import cv2
import pandas as pd

# Edit the imread function and put the name of the image in it
img = cv2.imread('colorpic.jpg')

clicked = False
r = g = b = xpos = ypos = 0

# Reading the csv file
index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)


# To calculate minimum distance of color
def getColorName(r, g, b):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(r - int(csv.loc[i, "R"])) + abs(g - int(csv.loc[i, "G"])) + abs(b - int(csv.loc[i, "B"]))
        if (d <= minimum):
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname


# function to get x,y coordinates of mouse double click
def on_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv2.imshow('image',img)
cv2.setMouseCallback('image', on_click)

while (1):

    cv2.imshow("image", img)
    if clicked:

        # cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv2.rectangle(img, (0, 0), (830, 50), (b, g, r), -1)

        font = cv2.FONT_ITALIC

        # Creating text string to display( Color name and RGB values )
        text = getColorName(r, g, b) + ' R='  + str(r) + ' G= ' + str(g) + ' B= ' + str(b)

        # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(img, text, (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        # For very light colours we will display text in black colour
        if r + g + b >= 600:
            cv2.putText(img, text, (10, 30),font, 1, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Break the loop when user hits 'esc' key
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
