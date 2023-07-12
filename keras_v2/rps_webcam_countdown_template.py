import cv2
from keras.models import load_model
import numpy as np
model = load_model('keras_model.h5')
cap = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
timer = int(3)
data_collection_period = 30

while data_collection_period !=0:
    if timer != 0:
        while True:
            if timer > 0:
                ret, frame = cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(timer), (200, 250), font,7, (255, 255, 255),4, cv2.LINE_AA)
                cv2.imshow("Shaka",frame)
                cv2.waitKey(2000)
                timer -= 1

            else:
                ret, frame = cap.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str("GO!!"), (200, 250), font,7, (255, 255, 255),4, cv2.LINE_AA)
                cv2.imshow("Shaka",frame)
                cv2.waitKey(2000)
                cv2.destroyAllWindows()
                break

    ret, frame = cap.read()
    resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    image_np = np.array(resized_frame)
    normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    data[0] = normalized_image
    prediction = model.predict(data)
    cv2.imshow('frame', frame)
    cv2.waitKey(50)
    data_collection_period -= 1
    # Press q to close the window
    # print(prediction)
    # if cv2.waitKey(1) or 0xFF == ord('q'):
    #     break
print(prediction)          
# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()

