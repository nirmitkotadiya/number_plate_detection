import cv2
from datetime import datetime
import os
from detector import detect_number_plate

def main():
    """Main function to process the image and log results."""
    image_path = 'images/car_5.jpeg'
    output_image_path = "detected_image/detected_plate.jpg"

    try:
        # Load the image
        img = cv2.imread(image_path)
        if img is None:
            raise FileNotFoundError(f"Could not load image at {image_path}. Please check the path.")

        # Detect the number plate
        detected_img, plate = detect_number_plate(img)

        

        if plate:
            # Create timestamp for logging
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp}: Number Plate Detected. Image successfully saved at {os.path.abspath(output_image_path)} \n"

            # Save log to a file
            with open("number_plate_log.txt", "a") as log_file:
                log_file.write(log_entry)

            # Save the detected image with the plate
            # output_image_path = "detected_image/detected_plate.jpg"
            cv2.imwrite(output_image_path, detected_img)
            print(f"Detected image saved at: {output_image_path}")

            # Show the detected image with the plate
            cv2.imshow("Detected Plate", detected_img)
            cv2.waitKey(0)  # Wait for any key press to close the window
            cv2.destroyAllWindows()

        else:
            print("No plate detected.")

    except Exception as e:
        print(f"Error in main: {e}")

if __name__ == "__main__":
    main()
