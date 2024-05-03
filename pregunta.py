import os
import pandas as pd

def create_dataset_csv(base_path, output_filename):
    df = pd.DataFrame(columns=['phrase', 'sentiment'])
    for sentiment in ['negative', 'positive', 'neutral']:
        sentiment_path = os.path.join(base_path, sentiment)
        for filename in os.listdir(sentiment_path):
            file_path = os.path.join(sentiment_path, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    phrase = line.strip()
                    df = df._append({'phrase': phrase, 'sentiment': sentiment}, ignore_index=True)
    df = df[df.groupby('sentiment').cumcount() > 0]
    df.to_csv(output_filename, index=False)

create_dataset_csv('train', 'train_dataset.csv')
create_dataset_csv('test', 'test_dataset.csv')

