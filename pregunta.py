import os
import csv

def create_dataset_csv(base_path, output_filename):
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['phrase', 'sentiment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for sentiment in ['negative', 'positive', 'neutral']:
            sentiment_path = os.path.join(base_path, sentiment)
            for entry in os.scandir(sentiment_path):
                if entry.is_file():
                    file_path = entry.path
                    with open(file_path, 'r', encoding='utf-8') as file:
                        phrase = file.read().strip()
                    writer.writerow({'phrase': phrase, 'sentiment': sentiment})

create_dataset_csv('train', 'train_dataset.csv')
create_dataset_csv('test', 'test_dataset.csv')
