import pandas as pd

CLASS_FILE = 'classes.txt'

def read_classes(bird_dir, terminal_levels):
    """Loads DataFrame with class labels. Returns full class table
    and table containing lowest level classes.
    """
    def make_annotation(s):
        try:
            return s.split('(')[1].split(')')[0]
        except Exception as e:
            return None

    classes = pd.read_table(f'{bird_dir}/{CLASS_FILE}', header=None)
    classes['id'] = classes[0].apply(lambda s: int(s.split(' ')[0]))
    classes['label_name'] = classes[0].apply(lambda s: ' '.join(s.split(' ')[1:]))
    classes.drop(0, inplace=True, axis=1)
    classes['annotation'] = classes['label_name'].apply(make_annotation)
    classes['name'] = classes['label_name'].apply(lambda s: s.split('(')[0].strip())

    terminal_classes = classes[classes['id'].isin(terminal_levels)].reset_index(drop=True)
    return classes, terminal_classes
