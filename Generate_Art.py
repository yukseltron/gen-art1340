# Import all necessary libraries
from PIL import Image, ImageDraw, ImageChops
import random
import colorsys

# Define a function to generate a random colour
def random_color():
    h = random.random()
    s = 1
    v = 1

    float_rgb = colorsys.hsv_to_rgb(h, s, v)
    rgb = [int(x * 255) for x in float_rgb]

    return tuple(rgb)

# Define "interpolate" to be a function that blends all colours seamlessly in the final image
def interpolate(start_color, end_color, factor: float):
    recip = 1 - factor
    return(
        int(start_color[0] * recip + end_color[0] * factor),
        int(start_color[1] * recip + end_color[1] * factor),
        int(start_color[2] * recip + end_color[2] * factor)
        )

# Make image background transparent
def convertImage(path):
    img = Image.open(path)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []

    for item in datas:
        if item[0] == 0 and item[1] == 0 and item[2] == 0:
            newData.append((0, 0, 0, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(path, "PNG")

# Define the main function
def generate_art(path, target_size_px, scale_factor, lines):
    print("Generating Art!")  # This line of code clarifies that the function is active / has been executed properly
    image_size_px = target_size_px * scale_factor # Set image size
    padding_px = 16 * scale_factor # Pad the image
    image_bg_color = (0, 0, 0, 0) # Set the background to black
    start_color = random_color()
    end_color = random_color()
    image = Image.new(
        "RGB", size=(image_size_px, image_size_px),
                color=image_bg_color)

    draw = ImageDraw.Draw(image)
    points = [] # Set "points" to be an empty list to be used later in the code

# The following lines of code determine the main constraints / conditions for the final image
    for _ in range(lines):
        random_point = (
            random.randint(padding_px, image_size_px - padding_px),
            random.randint(padding_px, image_size_px - padding_px))
        points.append(random_point)

    min_x = min([p[0] for p in points])
    max_x = max([p[0] for p in points])
    min_y = min([p[1] for p in points])
    max_y = max([p[1] for p in points])

    delta_x = min_x - (image_size_px - max_x)
    delta_y = min_y - (image_size_px - max_y)

    for i, point in enumerate(points):
        points[i] = (point[0] - delta_x // 2, point[1] - delta_y // 2)

    thickness = 0
    n_points = len(points) - 1

    for i, point in enumerate(points):
        overlay_image = Image.new(
            "RGB", size=(image_size_px, image_size_px),
            color=image_bg_color)
        overlay_draw = ImageDraw.Draw((overlay_image))

        p1 = point

        if i == n_points:
            p2 = points[0]
        else:
            p2 = points [i + 1]
        line_xy = (p1, p2)
        color_factor = i / n_points
        line_color = interpolate(start_color, end_color, color_factor)
        thickness += scale_factor
        overlay_draw.line(line_xy, fill=line_color, width=thickness)
        image = ImageChops.add(image, overlay_image)

    image = image.resize((target_size_px, target_size_px))
    img = image.save(path, "PNG")
    img = convertImage(path)

# This line of code generates ten randomly generated images
def start_generator():
    for i in range(10):
        size = random.randint(120,150)
        scale = random.randint(1,5)
        lines = random.randint(15,50)
        generate_art("Test_Image_"+str(i)+".png", size, scale, lines)

start_generator()
