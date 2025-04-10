import numpy as np
import os
import cv2


def read(image_folder,annotation_folder):

    # Read images and annotations

    color = (0, 255, 0)

    for filename in os.listdir(image_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(image_folder, filename)
            label_path = os.path.join(annotation_folder, os.path.splitext(filename)[0] + ".txt")

            if not os.path.exists(label_path):
                print(f"No annotation for {filename}")
                continue

            image =  cv2.imread(image_path)
            h, w, _ = image.shape

            with open(label_path, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    class_id = int(parts[0])
                    x_center, y_center, box_w, box_h = map(float, parts[1:])
                    
                    x1 = int((x_center - box_w / 2) * w)
                    y1 = int((y_center - box_h / 2) * h)
                    x2 = int((x_center + box_w / 2) * w)
                    y2 = int((y_center + box_h / 2) * h)
                       
                    cv2.rectangle(image, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(image, "car", (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        
            cv2.imshow("Image with BBoxes", image)
            key = cv2.waitKey(0)
            if key == 27:  # ESC key to exit
                break

        cv2.destroyAllWindows()


def main():
    image_folder = "data/scaled_images"
    annotation_folder = "data/annotations/"
    
    read(image_folder,annotation_folder)

main()
