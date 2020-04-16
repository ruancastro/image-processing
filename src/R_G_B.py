import cv2
# separando nas cores R G B e exibindo
def exibe_rgb(image):

    (B, G, R) = cv2.split(image)
    cv2.imshow("Red", R)
    cv2.imshow("Green", G)
    cv2.imshow("Blue", B)
    k = cv2.waitKey(0)

    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('output/Only_B.png',B)
        cv2.imwrite('output/Only_G.png',G)
        cv2.imwrite('output/Only_R.png',R)
        cv2.destroyAllWindows()


    merged = cv2.merge([B, G, R])
    cv2.imshow("Merged", merged)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
