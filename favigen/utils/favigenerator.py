import asyncio
import os
from favicons import Favicons

fav = "static/media/Group 442.png"
loc = "static/media/favs"
color = "#F15A24"

if not os.path.exists(loc):
    os.makedirs(loc)


def generate_favicon(source, location, color='#000000'):
    with Favicons(source=source, output_directory=location, background_color=color) as favicons:
        favicons.generate()
        html = favicons.html_gen()
        html = favicons.html()
    return html

# generate_favicon(source=fav, location=loc, color='#FFFFFF')



# async def generate_favicon_async(source, location, color='#000000'):
#     async with Favicons(source=source, output_directory=location, background_color=color) as favicons:
#         await favicons.generate()
#         for icon in favicons.filenames():
#             print(icon)

# asyncio.run(generate_favicon_async(source=fav, location=loc, color=color))



# with open("image-predictions.tsv", "wb") as file:
#         file.write(image_pred_response.content)