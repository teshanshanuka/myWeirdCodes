import cv2, sys

if len(sys.argv) != 2:
    print('please specify filename to save image')
    sys.exit()

cap = cv2.VideoCapture(0) #VideoCapture('videofile name') for capture a video

ret, frame = cap.read()
while ret:
    ret, frame = cap.read()
    cv2.imshow('Press s to save and exit, q to exit', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(sys.argv[1], frame)
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
