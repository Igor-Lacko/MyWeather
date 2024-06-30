import PyQt6.QtWidgets as widgets
from PyQt6.QtCore import QObject
from PIL import Image
from sys import argv


def GetSiblings(widget : widgets.QWidget, type = widgets.QWidget) -> list[QObject] | None:
    """Finds all the siblings (have the same widget as parent) of the widget passed in as a parameter

    Args:
        widget (widgets.QWidget): Can be any valid QWidget
        type (type): Type of the sibling

    Returns:
        list[widgets.QObject] | None: Returns a list of all the siblings or None if the widget doesn't have a parent (so it's the Main Window)
    """

    #none check
    if (parent := widget.parentWidget()) is None:
        return None
    
    #return all children except of the parameter widget -> so all it's siblings
    return [child for child in parent.findChildren(type) if not (child is widget)]





def PNGColorSwap(src : str, mode : str, dst : str = None):
    """Swaps a black/white PNG's color to the other

    Args:
        src (str): the image source file
        mode (str): either dark or light 
        dst (str): the image destination file, by default the same as src
    """

    if dst is None:
        dst = src                                                   #default behaviour

    BLACK = (0,0,0)
    WHITE = (255,255,255)                                           #constants

    new_color = BLACK if mode == "light" else WHITE                 #get current color to be converted to
    old_color = WHITE if new_color == BLACK else BLACK              #get old color to  be converted from

    (image := Image.open(src)).convert("RGBA")                      #convert the image into rgb tuples

    image_data = list(image.getdata())

    modified = []

    for quadruple in image_data:
            
        if quadruple[:3] == old_color and quadruple[3] != 0:
            modified.append(new_color + (quadruple[3],))
        
        else:
            modified.append(quadruple)


    with open('modified.txt', 'w') as file:
        file.write(str(modified))

    image.putdata(modified)
    image.save(dst)


def main():
    if len(argv) != 3:
        print("kamo no tak")
        return
    
    PNGColorSwap(argv[1], "dark", argv[2])


if __name__ == "__main__":
    main()

