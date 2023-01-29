import os
img_src = 'C:\\Users\\lukas\\Desktop\\Neuer Ordner\\img-src\\0E8C9EC0-9AF6-4225-84BB-1C8EDB867BB0'

image_folder = 'img-src'
image_list = os.listdir(image_folder)

template = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Laurin Erdmann">
    <title>KUNSTGALERIE</title>
    <style>

    </style>
    </style>
    <link rel="stylesheet" type="text/css" href="style.css">
</head>

<body>
    <a class="center-bottom" href="./{value}.html"
        style="color: black; text-decoration: underline; font-family: Arial, Helvetica, sans-serif; text-decoration: none;">HORCH!</a>
<img src="{image1}" >
<img src="{image2}" >
</body>

</html>
"""

for i in range(0, len(image_list), 2):
    value = i // 2
    with open(f"{value}.html", "w") as file:
        file.write(template.format(value=value, image1=os.path.join(image_folder, image_list[i]), image2=os.path.join(image_folder, image_list[i + 1])))

