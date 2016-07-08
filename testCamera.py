import numpy as np
import cv2
import urllib.request
import base64

# MAKE SURE THIS WORKS FIRST
# USES BUILT IN LAPTOP WEBCAM
"""
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


# Option 1
# TODO change URL. It Must End in .mjpg
"""

stream = urllib.request.urlopen('http://50.89.131.216:8080/?action=stream')
bytes = ''
print("hello")
while True:
    print("hello1")
    bytes = bytes + str(stream.read(1024))
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a!=-1 and b!=-1:
        print("hello1232")

        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.COLOR_BGR2GRAY)
        cv2.imshow('i',i)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit(0)

"""
#stream = urllib.request.urlopen('http://50.89.131.216:80/')
stream = urllib.request.urlopen('https://upload.wikimedia.org/wikipedia/commons/4/4d/Cat_March_2010-1.jpg')

print("hello")
while True:
    print("hello1")
    image = np.asarray(bytearray(stream.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    cv2.imshow('i', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)
"""


# Option 2
# TODO CHANGE URL username and password. DOESNT NEED TO END IN .mjpg
# TODO Might not need the whole header section
"""
url = ""
user = ""
password = ""
auth_encoded = base64.encodestring('%s:%s' % (user, password))[:-1]

req = urllib.Request(url)
req.add_header('Authorization', 'Basic %s' % auth_encoded)

while True:
    response = urllib.urlopen(req)
    img_array = np.asarray(bytearray(response.read()), dtype=np.uint8)
    frame = cv2.imdecode(img_array, 1)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        exit(0)

"""

# Option 3
# TODO change url, can remover user and password if needed. must have .cgi at end of url like in example below
"""
capture = cv2.VideoCapture()
#frame = cv2.Mat()
ip = "50.89.131.216"
port = 80
username = ""
password = ""
capture.open("http://%s:%d/html" % (ip, port))

if capture.isOpened():
    while True:
        capture >> frame
        if frame.empty():
            print("EMPTY FRAME BREAKING LOOP")
            break
        cv2.imshow('i', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            exit(0)

"""