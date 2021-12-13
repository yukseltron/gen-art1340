# Import all necessary libraries
from PIL import Image, ImageDraw, ImageChops
import PySimpleGUI as sg
import random
import colorsys
import os
import RNGHash as rng


random.seed = rng.getHash("Game.py")

def changeSeedWindow():
    sg.theme('Black')
    layout = [
        [sg.Text("Specify the file for generating the random seed for the enemy art.\nAny file can be used!")],
        [sg.Text("File", size =(15, 1)), sg.InputText(do_not_clear=False)],
        [sg.Text("", key = "-warning-", text_color = "red")],
        [sg.Submit()]
    ]
    window = sg.Window("Change Seed File", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            window.close()
            break
        file = values[0]
        try:
            random.seed = rng.getHash(file)
            window.close()
            break
        except:
            window['-warning-'].Update("File could not be found, please try inputting the path again.")
            continue

# Define a function to generate a random colour
def random_color():
    print(random.seed)
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
    image_bg_color = (0, 0, 0) # Set the background to black
    start_color = random_color()
    end_color = random_color()
    image = Image.new(
        "RGB", size=(image_size_px, image_size_px),
                color=image_bg_color)

    draw = ImageDraw.Draw(image)
    points = [] # Set "points" to be an empty list to be used later in the code

# The following lines of code determine the main constraints / conditions for the final image
    for line in range(lines):
        line2 = line
        random_point = (
            line + random.randint(padding_px, image_size_px - padding_px),
            line2 - random.randint(padding_px, image_size_px - padding_px))
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

# Turns set of images into a GIF
def createGIF(images):
    open_images = []
    for i in range(1,len(images)):
        img = Image.open(images[i]+".png")
        open_images.append(img)

    img = Image.open(images[0]+".png")
    img.save("out.gif", save_all=True, append_images=open_images, disposal=2, loop=0, duration=2000)

    for i in images:
        os.remove(i+".png")

# This line of code generates ten randomly generated images
def start_generator(num):
    images = []
    for i in range(num):
        path = "Test_Image_"+str(i)
        lines = (i + 2) * random.randrange(num,10)
        generate_art(path+".png", 250, 2, lines)
        images.append(path)

    createGIF(images)
