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

# Evaluation

To evaluate character responses, it has been used ChatGPT with the following prompt.
Replace `{user_prompt_N}` with your prompt and `{name_response_N}` with the corresponding reply for the parts of dialogue you want to evaluate.

> Given a conversation between {name} from the Lord of the Rings and a random user, I want you to score the quality of the responses of {name} from 1 to 10 according to the degree of how much they resemble the talking style, tone, background, and personality of {name}. Also, consider the coherence and correctness of the responses with respect to the prompt. Responses should also reflect the environment and facts that happened in the character's world. Give and show the score for each response and output the average score.
>
> User: {user_prompt_1}
> 
> Character: {name_response_1}
> 
> User: {user_prompt_2}
> 
> ...

<details>
<summary>Evaluation of Gandalf</summary>


- "How many orcs have you killed?" - Score: 8/10. Gandalf's response of "I do not know. Hundreds? Thousands? I've lost count" is a reflection of his long history of fighting against the armies of darkness. The tone of his response is serious and contemplative, which fits with his role as a powerful wizard who has seen many battles.
- "Who is Frodo?" - Score: 9/10. Gandalf's response of "He is the ring bearer. We should never have left him" accurately reflects the urgency and gravity of the situation facing Middle-earth. His tone is concerned and regretful, which reflects his deep care for Frodo and the fate of the world.
- "Where can the ring of be destroyed?" - Score: 9/10. Gandalf's answer of "In the fire of Mount Doom" is a concise and accurate reflection of the central quest of the Lord of the Rings. His tone is serious and focused, which reflects the seriousness of the task at hand.
- "Where does your power come from?" - Score: 9/10. Gandalf's response of "My power is derived from the will of the Valar" is consistent with his character's background as a Maiar and reflects his understanding of the complex mythology of Middle-earth. His tone is matter-of-fact, which reflects his confidence and authority.
- "What are the Valar?" - Score: 8/10. Gandalf's response of "The Valar are the rulers of all things in the world" accurately reflects the hierarchy of beings in Tolkien's mythology. His tone is informative and patient, which reflects his role as a guide and mentor.
- "What do you think about Gollum? Does he have any hope?" - Score: 7/10. Gandalf's response of "No. He is beyond hope" accurately reflects his understanding of the nature of Gollum and his role in the quest. However, his tone is somewhat dismissive and lacks the empathy and complexity that Gandalf exhibits in other parts of the story.

Overall, the average score for Gandalf's responses is: 8.17.

</details>

<details>
<summary>Evaluation of Frodo</summary>


- "Who is Gollum?" - Frodo's response of "Release him!" is not a direct answer to the question, but it is consistent with his character's compassion and empathy for even the most unlikely creatures. However, the response doesn't reflect the context of Gollum's identity or backstory. I would give this response a score of 6 out of 10.
- "Do you trust Gollum?" - Frodo's response of "Yes. Then release him." is consistent with his tendency to see the good in people and his desire to give everyone a chance. However, it doesn't reflect the reality of Gollum's past actions, which Frodo is aware of. I would give this response a score of 7 out of 10.
- "Gollum will betray you" - Frodo's response of "I know. But it's all I have left to trust." is consistent with his conflicted nature, as he struggles with the task of carrying the Ring and the weight of responsibility that comes with it. He is aware of the risks but is willing to take them for the greater good. The response is also accurate with respect to Gollum's true nature. I would give this response a score of 9 out of 10.
- "Do you have the ring?" - Frodo's response of "I have the Ring Sam." is accurate and concise, reflecting his seriousness about the task he has been entrusted with. The response also shows his willingness to confide in Sam. I would give this response a score of 8 out of 10.
- "Give the ring to me!" - Frodo's response of "No!" is consistent with his understanding of the danger that the Ring poses and his determination to complete his mission. It's also consistent with his reluctance to burden others with the task, even those he trusts. The response also shows his awareness of the responsibility that comes with holding the Ring. I would give this response a score of 9 out of 10.
- "Then I will take it from you" - Frodo's response of "Give me the Ring Sam!" is consistent with his urgency and the gravity of the situation. It's also a reflection of his desire to protect Sam from the burden of carrying the Ring. The response is not directly answering the user's statement but is consistent with Frodo's character. I would give this response a score of 7 out of 10.
- "Frodo, you are tired, I can help you to share the weight" - Frodo's response of "No!" is consistent with his reluctance to burden others with the task and his awareness of the danger that the Ring poses. The response also shows his determination to complete the mission on his own. I would give this response a score of 8 out of 10.
- "Where are you going?" - Frodo's response of "I must leave the Shire." is accurate and reflects his understanding of the task at hand. The response also shows his awareness of the danger that the Ring poses and his urgency to leave as soon as possible. I would give this response a score of 9 out of 10.

Overall, the average score for Frodo's responses is: 7.88.

</details>
