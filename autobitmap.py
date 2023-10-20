import cv2
import numpy as np

# Open the image
img = cv2.imread('D:\Code Stuff\Robocup\check\Background.bmp')

# Convert the image to RGB format
img_rgb_t = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb_nt = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Define a dictionary with colors to replace and their respective replacements
color_replacements_t = {
    (0, 176, 240): (255, 255, 255),  # Replace with white
    (255, 153, 0): (255, 255, 255),  # Replace with white
    (112, 48, 160): (255, 255, 255),  # Replace with white
    (112, 173, 71): (255, 255, 255),  # Replace with white
    (166, 166, 166): (255, 255, 255),  # Replace with white
    (255, 206, 133): (255, 255, 255),  # Replace with white
    (255, 146, 0): (255, 255, 255),  # Replace with white
    (27, 184, 241): (255, 255, 255),  # Replace with white
    (221, 186, 151): (0, 0, 0),  # Replace with black
    (68, 114, 196): (0, 0, 0),  # Replace with black
    (255, 255, 0): (0, 0, 0),  # Replace with black
}

color_replacements_nt = {
    (0, 176, 240): (255, 255, 255),  # Replace with white
    (255, 153, 0): (255, 255, 255),  # Replace with white
    (112, 48, 160): (255, 255, 255),  # Replace with white
    (112, 173, 71): (255, 255, 255),  # Replace with white
    (166, 166, 166): (255, 255, 255),  # Replace with white
    (255, 206, 133): (255, 255, 255),  # Replace with white
    (255, 146, 0): (255, 255, 255),  # Replace with white
    (27, 184, 241): (255, 255, 255),  # Replace with white
    (221, 186, 151): (0, 0, 0),  # Replace with black
    (68, 114, 196): (255, 255, 255),  # Replace with black
    (255, 255, 0): (255, 255, 255),  # Replace with black
}


tolerance = 33

for target_color, replacement_color in color_replacements_t.items():
    lower_bound = np.array([max(0, target_color[0] - tolerance),
                            max(0, target_color[1] - tolerance),
                            max(0, target_color[2] - tolerance)])
    upper_bound = np.array([min(255, target_color[0] + tolerance),
                            min(255, target_color[1] + tolerance),
                            min(255, target_color[2] + tolerance)])
    mask = cv2.inRange(img_rgb_t, lower_bound, upper_bound)

    # Replace the matched colors with the respective replacement color
    img_rgb_t[mask > 0] = replacement_color

for target_color, replacement_color in color_replacements_nt.items():
    lower_bound = np.array([max(0, target_color[0] - tolerance),
                            max(0, target_color[1] - tolerance),
                            max(0, target_color[2] - tolerance)])
    upper_bound = np.array([min(255, target_color[0] + tolerance),
                            min(255, target_color[1] + tolerance),
                            min(255, target_color[2] + tolerance)])
    mask = cv2.inRange(img_rgb_nt, lower_bound, upper_bound)

    # Replace the matched colors with the respective replacement color
    img_rgb_nt[mask > 0] = replacement_color

# Add a black border to the image
border_width = 10  # Adjust the border width as needed
bordered_img_t = cv2.copyMakeBorder(cv2.cvtColor(img_rgb_t, cv2.COLOR_RGB2BGR), border_width, border_width, border_width, border_width, cv2.BORDER_CONSTANT, value=(0, 0, 0))    
bordered_img_nt = cv2.copyMakeBorder(cv2.cvtColor(img_rgb_nt, cv2.COLOR_RGB2BGR), border_width, border_width, border_width, border_width, cv2.BORDER_CONSTANT, value=(0, 0, 0)) 

# Resize the modified image to 7200x5400
new_width = 7200
new_height = 5400
resized_img_t = cv2.resize(cv2.cvtColor(bordered_img_t, cv2.COLOR_RGB2BGR), (new_width, new_height))
resized_img_nt = cv2.resize(cv2.cvtColor(bordered_img_nt, cv2.COLOR_RGB2BGR), (new_width, new_height))
print("resized!")

# Flip the image vertically
flipped_img_t = cv2.flip(resized_img_t, 0)
flipped_img_nt = cv2.flip(resized_img_nt, 0)

# Rotate the flipped image 90 degrees to the left (counter-clockwise)
rotated_img_t = cv2.rotate(flipped_img_t, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated_img_nt = cv2.rotate(flipped_img_nt, cv2.ROTATE_90_COUNTERCLOCKWISE)

# Save the modified image
cv2.imwrite('D:\Code Stuff\Robocup\check\Trap.bmp', cv2.cvtColor(rotated_img_t, cv2.COLOR_RGB2BGR))
cv2.imwrite('D:\Code Stuff\Robocup\check\Trapless.bmp', cv2.cvtColor(rotated_img_nt, cv2.COLOR_RGB2BGR))



