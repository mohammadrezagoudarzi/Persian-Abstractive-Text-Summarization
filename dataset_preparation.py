import pandas as pd

# Paths to your dataset files
train_path = "AIR_Project/pn_summary/train.csv"
val_path = "AIR_Project/pn_summary/dev.csv"
test_path = "AIR_Project/pn_summary/test.csv"

columns = ['id', 'title', 'article', 'summary', 'category', 'categories', 'network', 'link']

# Load the datasets
train_data: pd.DataFrame = pd.read_csv(train_path, names=columns, header=None, sep='\t')[['article', 'summary']].iloc[1:]
val_data: pd.DataFrame = pd.read_csv(val_path, names=columns, header=None, sep='\t')[['article', 'summary']].iloc[1:]
test_data: pd.DataFrame = pd.read_csv(test_path, names=columns, header=None, sep='\t')[['article', 'summary']].iloc[1:]

# Check for required columns
required_columns = ['article', 'summary']
for dataset, name in [(train_data, "Train"), (val_data, "Val"), (test_data, "Test")]:
    if not all(col in dataset.columns for col in required_columns):
        raise ValueError(f"{name} dataset must contain the columns: {required_columns}")
    print(f"{name} dataset loaded successfully with {len(dataset)} records.")


def get_train_dataset():
    return train_data

def get_val_dataset():
    return val_data

def get_test_dataset():
    return test_data