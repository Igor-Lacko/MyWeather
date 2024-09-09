import PyQt6.QtWidgets as widgets
from PyQt6.QtCore import QObject
from PIL import Image
from sys import argv
from datetime import date, datetime, timedelta


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



def GetDaylist(day_range : int, future : bool) -> list[str]:
    """Returns a list of the past days in the specigied range 

    Args:
        day_range (int): How many days in the past/future to return
        future (bool): If true, returns the future range days. If false, returns the past range days.

    Returns:
        list[str]: A list of strings of past/future dates in the format WEEKDAY, DD.MM.YYYY
    """
    dates = []

    for delta in range(day_range) if future else reversed(range(day_range * -1 + 1, 1)):
        dates.append((datetime.now() + timedelta(delta)).strftime("%A, %-d.%-m.%Y"))

    return dates





def main():
  #  dates = []
   # for i in range(int(argv[1])):
   #     dates.append((datetime.now() + timedelta(i)).strftime("%A, %-d.%-m.%Y"))

   # print(dates)
    PNGColorSwap('../../Assets/door-light.png', 'dark', '../../Assets/door-dark.png')


if __name__ == "__main__":
    main()

