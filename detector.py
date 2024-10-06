import cv2
import pytesseract
from utils import preprocess_image

# Load Haar Cascade for license plate detection
try:
    plate_cascade = cv2.CascadeClassifier('./model/haarcascade_russian_plate_number.xml')
    if plate_cascade.empty():
        raise Exception("Failed to load Haar Cascade for license plate detection.")
except Exception as e:
    print(f"Error loading Haar Cascade: {e}")

def detect_number_plate(image):
    """Detect number plates in the image and return the plate text."""
    try:
        # Preprocess the image
        gray_img = preprocess_image(image)
        if gray_img is None:
            return image, None

        # Detect plates
        plates = plate_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=4)

        if len(plates) == 0:
            print("No plates found.")
            return image, None

        for (x, y, w, h) in plates:
            # Draw rectangle around the number plate
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            plate_region = gray_img[y:y+h, x:x+w]

            # Extract text from the plate region using OCR
            plate_text = pytesseract.image_to_string(plate_region, config='--psm 8')

            if plate_text.strip():  # Ensure the detected text is not empty
                return image, plate_text.strip()

        return image, None

    except Exception as e:
        print(f"Error detecting number plate: {e}")
        return image, None
