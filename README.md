# LOTR Character Imitator 🧝‍♂️

Have you ever wanted to talk like your favorite characters from "The Lord of the Rings"? 🤔

With this project, you can! We have fine-tuned an OpenAI language model to imitate the speech patterns and language of various characters from the iconic movie franchise. 🤖📝📚

Our model has been trained on a vast amount of text data, including the original books and scripts from the movies, to capture the unique voices of characters such as Gandalf, Frodo, and Aragorn. Simply input your desired character and prompt, and watch as our model generates text that sounds like it was written by J.R.R. Tolkien himself! 🤩🎬📜

## Dataset

### Kaggle data

The Lord of the Rings characters dialogue data is available on [Kaggle](https://www.kaggle.com/datasets/paultimothymooney/lord-of-the-rings-data).

### ChatGPT-generated data

We can ask ChatGPT to generate some prompt-completion pairs using the following prompt:
> I want you to generate dialogue pair sentences. The first sentence of each pair is a random character talking to {name} and the second sentence is {name}'s response. I want you to generate sentences like {name} using the tone, manner, values and vocabulary {name} would use. Do not write any explanations. Only talk like {name}.

## Data preprocessing

Preprocess the data by running the `format_data.py` script.
Make sure the `lotr_scripts.csv` file is in the directory `data`. If not, you can download it from [here](https://www.kaggle.com/datasets/paultimothymooney/lord-of-the-rings-data).
```
python format_data.py --dir data --char {name}
```
Where `{name}` should be replaced with the name of the character you want the model to imitate.

You can use the following command to visualize a list of all supported characters and their respective number of dialogue lines.
```
python format_data.py --show_chars True
```

**BONUS**: use ChatGPT generated data to augment the dataset. 
- Open ChatGPT and input the prompt defined in the previous section to generate prompt-completion pairs. Replace `{name}` with the name of your character.
- You can use another prompt to create 2 python lists: one for the prompts and one for the completions.
    > Given the previous text, generate 2 Python lists of string: the first list contains the sentences spoken by the random character and the second list contains the responses of {name}
- Add the resulted lists in the file `background.py` respecting the predefined format.
- An example for the character Gandalf is already provided as a reference.

## Fine-tuning
Add your OpanAI key.
```
export OPENAI_API_KEY="<OPENAI_API_KEY>"
```
**Optional**: check the data is in the right format. 
```
openai tools fine_tunes.prepare_data -f lotr_scripts_{name}.jsonl
```
Start a fine-tuning job.
```
openai api fine_tunes.create -t lotr_scripts_{name}.jsonl -m <BASE_MODEL>
```
`<BASE_MODEL>` can be any OpenAI LLM that supports fine-tuning. For example, you can choose `curie` or `davinci`.

Finally, you can check the status of your fine-tuning run with the next command.
```
openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>
```

## Talk with your character

Open [OpenAI Playground](https://platform.openai.com/playground/) and select your fine-tuned model to start chatting.

For best results make sure `Stop sequences` is `###` and `Inject start text` is set as `↵↵###↵↵`. 
To test the models I fine-tuned a `curie` model and generated sentences with a `temperature` parameter of 0.7.

## Chat examples

### Gandalf

>**USER**: How many orcs have you killed?
>
>**GANDALF**: I do not know. Hundreds? Thousands? I've lost count.
> 
>**USER**: Who is Frodo?
>
>**GANDALF**: He is the ring bearer. We should never have left him.
> 
>**USER**: Where can the ring of be destroyed?
> 
>**GANDALF**: In the fire of Mount Doom.
> 
>**USER**: Where does your power come from?
>
>**GANDALF**: My power is derived from the will of the Valar.
> 
>**USER**: What are the Valar?
>
>**GANDALF**: The Valar are the rulers of all things in the world.
> 
>**USER**: What do you think about Gollum? Does he have any hope?
>
>**GANDALF**: No. He is beyond hope.

### Frodo

>**USER**: Who is Gollum?
>
>**FRODO**: Release him!
>
>**USER**: Do you trust Gollum?
>
>**FRODO**: Yes. Then release him.
>
>**USER**: Gollum will betray you
>
>**FRODO**: I know. But it's all I have left to trust.
> 
>**USER**: Do you have the ring?
> 
>**FRODO**: I have the Ring Sam.
>
>**USER**: Give the ring to me!
>
>**FRODO**: No!
>
>**USER**: Then I will take it from you
>
>**FRODO**: Give me the Ring Sam!
>
>**USER**: Frodo, you are tired, I can help you to share the weight
>
>**FRODO**: No!
>
>**USER**: Where are you going?
>
>**FRODO**: I must leave the Shire.

### Gandalf when asked Frodo's questions

>**USER**: Who is Gollum?
>
>**GANDALF**: He is a creature of the deeps. A creature of the past.
> 
>**USER**: Do you trust Gollum?
>
>**GANDALF**: No.
> 
>**USER**: Gollum will betray you
>
>**GANDALF**: Yes he will
>
>**USER**: Do you have the ring?
>
>**GANDALF**: No. No, I do not.
> 
>**USER**: Give the ring to me!
>
>**GANDALF**: No!
>
>**USER**: Then I will take it from you
>
>**GANDALF**: You wouldn't harm an old man, would you?