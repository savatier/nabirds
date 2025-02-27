import pandas as pd

TRAIN_TEST_SPLIT_FILE = 'train_test_split.txt'

def read_train_test(bird_dir):
    """Load train test split."""
    train_test = pd.read_table(f'{bird_dir}/{TRAIN_TEST_SPLIT_FILE}', sep=' ',
                               header=None)
    train_test.columns = ['image', 'is_train']
    return train_test
