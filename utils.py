import cv2

def preprocess_image(image):
    """Convert image to grayscale for easier detection."""
    try:
        if image is None:
            raise ValueError("Input image is None")

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray

    except Exception as e:
        print(f"Error in preprocessing image: {e}")
        return None
