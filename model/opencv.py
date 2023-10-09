import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)


model_path = "model.xml"
model = cv2.CascadeClassifier(model_path)


while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=8)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.Canny(img, 120, 120)

    cv2.imshow("Web Cam", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break