import pandas as pd

SIZE_FILE = 'sizes.txt'

def read_sizes(bird_dir):
    """Loads table of image sizes."""
    sizes = pd.read_table(f'{bird_dir}/{SIZE_FILE}', sep=' ',
                          header=None)
    sizes.columns = ['image', 'img_width', 'img_height']
    return sizes
