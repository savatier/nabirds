import pandas as pd

BOUNDING_BOX_FILE = 'bounding_boxes.txt'

def read_boxes(bird_dir):
    """Loads DataFrame of bounding box data for each image.
    """
    boxes = pd.read_table(f'{bird_dir}/{BOUNDING_BOX_FILE}', sep=' ',
                          header=None)
    boxes.columns = ['image', 'x', 'y', 'width', 'height']
    return boxes
