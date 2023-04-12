import pandas as pd
import os
import json
from tqdm import tqdm
import re
from background import chatgpt_prompts, chatgpt_sentences
import argparse


def change_file_extension(file_path, new_extension):
    file_name, ext = os.path.splitext(file_path)
    new_file_path = file_name + '.' + new_extension
    return new_file_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='data', help='directory where training data is stored')
    parser.add_argument('--file_name', type=str, default='lotr_scripts.csv', help='name of the training data')
    parser.add_argument('--char', nargs='+', default=['GANDALF'], help='list of characters to finetune the model')
    parser.add_argument('--separator', type=str, default='\n\n###\n\n',
                        help='string used to separate prompt and completion')
    parser.add_argument('--completion_end', type=str, default='###', help='completion end string')
    parser.add_argument('--completion_start', type=str, default=' ', help='completion start string')
    parser.add_argument('--add_chatgpt_dialogue', type=bool, default=True,
                        help='whether to add ChatGPT generated dialogues or not')
    parser.add_argument('--show_chars', type=bool, default=False,
                        help='show characters list')
    args = parser.parse_args()

    filter = args.char
    separator = args.separator
    completion_end = args.completion_end
    completion_start = args.completion_start

    data_path = os.path.join(args.dir, args.file_name)
    jsonl_path = change_file_extension(data_path, 'jsonl')
    jsonl_name, _ = os.path.splitext(jsonl_path)
    for f in filter:
        jsonl_name += '_' + f.lower()
    jsonl_path = jsonl_name + '.jsonl'

    df = pd.read_csv(data_path)
    df = df.dropna()

    if args.show_chars:
        chars = df['char'].value_counts()
        chars = chars[chars >= 30]
        print(chars)
        exit()

    c = 0

    with open(jsonl_path, 'w') as f:

        def write_data(pmt, cpt):
            cpt = re.sub(' +', ' ', cpt).replace('\u00a0', '').strip()
            pmt = re.sub(' +', ' ', pmt).replace('\u00a0', '').strip()
            if separator and not pmt.endswith(separator):
                pmt += separator
            if completion_end and not cpt.endswith(completion_end):
                cpt += completion_end
            if completion_start and not cpt.startswith(completion_start):
                cpt = completion_start + cpt
            data = {"prompt": pmt, "completion": cpt}
            json_data = json.dumps(data)
            f.write(json_data + '\n')

        for i in tqdm(range(len(df)-1)):
            if filter is not None and len(filter) > 0:
                if df.iloc[i+1]['char'] not in filter:
                    continue
            prompt = str(df.iloc[i]['dialog'])
            completion = str(df.iloc[i+1]['dialog'])
            write_data(prompt, completion)
            c += 1

        if args.add_chatgpt_dialogue and filter is not None:
            for character in filter:
                for p, s in zip(chatgpt_prompts[character.lower()], chatgpt_sentences[character.lower()]):
                    prompt = p
                    completion = s
                    write_data(prompt, completion)
                    c += 1

    print('JSONL data containing {} lines saved to:'.format(c), jsonl_path)
