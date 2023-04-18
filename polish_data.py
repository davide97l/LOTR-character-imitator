import openai
import os
import json
import re
from tqdm import tqdm
import time
import argparse

# example usage: python polish_data.py --top_n 50 --llm text-davinci-001 --file_name data/lotr_scripts_frodo.jsonl
parser = argparse.ArgumentParser()
parser.add_argument('--file_name', type=str, default='data/lotr_scripts_frodo.jsonl')
parser.add_argument('--top_n', type=int, default=50, help='Keep top N dialogues')
parser.add_argument('--llm', type=str, default='text-davinci-001', help='LLM to use for evaluating dialogues quality')
args = parser.parse_args()

file_name = args.file_name
new_file_name = file_name.split('.jsonl')[0] + '_polish.jsonl'
score_file_name = file_name.split('.jsonl')[0] + '_score.jsonl'
top_n = args.top_n
llm = args.llm
openai.api_key = os.environ["OPENAI_API_KEY"]


with open(file_name, 'r') as f:
    prompts = []
    completions = []
    for line in f:
        data = json.loads(line)
        prompts.append(data['prompt'])
        completions.append(data['completion'])

prompt = \
    'Given 2 sentences corresponding to a conversation between 2 characters, give it a score from 1 to 10.' \
    ' The score considers the correctness, logical coherence, usefulness, and the overall quality of the conversation.' \
    ' Only return the score without explanation.\n\n' \
    'Character 1: {}\nCharacter 2: {}\n'


def clean_str(s):
    return s.replace("###", "").replace("\n", "")


scores = []
for p, c in tqdm(zip(prompts, completions)):
    p, c = clean_str(p), clean_str(c)
    response = openai.Completion.create(
        engine=llm,
        prompt=prompt.format(p, c),
        max_tokens=10,
        n=1,
        stop=None,
        temperature=0.7,
    )
    response_text = response.choices[0].text.strip()
    score = float(re.findall(r'\d+', response_text)[0])
    scores.append(score)
    time.sleep(1)  # avoid overloading the system

# sort prompt and completions by score
idx = sorted(range(len(scores)), key=lambda k: scores[k], reverse=True)
scores = sorted(scores, reverse=True)
prompts = [prompts[i] for i in idx]
completions = [completions[i] for i in idx]

with open(new_file_name, 'w') as f:
    for p, c in zip(prompts[:top_n], completions[:top_n]):
        data = {"prompt": p, "completion": c}
        json_data = json.dumps(data)
        f.write(json_data + '\n')

with open(score_file_name, 'w') as f:
    for p, c, s in zip(prompts, completions, scores):
        data = {"prompt": p, "completion": c, "score": s}
        json_data = json.dumps(data)
        f.write(json_data + '\n')

print('JSONL data containing {} lines saved to:'.format(top_n), new_file_name)
print('JSONL data containing pairs score saved to:'.format(top_n), score_file_name)
