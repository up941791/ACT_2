import pandas as pd

def make_dataframe(split_path, split_name):
    return pd.DataFrame(split_path[split_name], columns=['img_path', 'label'])