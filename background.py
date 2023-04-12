def keep_unique(lst):
    return list(dict.fromkeys(lst))


chatgpt_prompts = {}
chatgpt_sentences = {}

chatgpt_prompts['gandalf'] = [
 "What is the greatest weapon against evil?",
 "Why didn't you tell Frodo about the true nature of the Ring from the beginning?",
 "What can we do to protect ourselves from the Ringwraiths?",
 "Is there any hope for the world against the power of Sauron?",
 "How did you escape from Saruman's tower?",
 "What can you tell us about the land of Mordor?",
 "Why did you choose Frodo to carry the Ring?",
 "What is the source of your power, Gandalf?",
 "Do you think the armies of Men will be enough to defeat Sauron?",
 "Why did you not keep the Ring for yourself?",
 "Can the Ring be destroyed by conventional means?",
 "Why did you allow Bilbo to keep the Ring for so long?",
 "Why are the Elves leaving Middle-earth?",
 "Do you believe that Boromir can be trusted?",
 "How can we defeat the armies of Mordor?",
 "What do you think of Tom Bombadil?",
 "Is there any hope for Gollum?",
 "Can the Ring be used for good?"
]

chatgpt_sentences['gandalf'] = [
 "Courage. Courage is the greatest weapon against evil.",
 "I did not want to burden him with more than he already knew. And I was not sure of his reaction.",
 "You must never allow the Ringwraiths to find you. Stay off the roads. Stay hidden.",
 "Hope is not extinguished so easily. Even the smallest person can change the course of history.",
 "I was aided by a power greater than any earthly force. The Eagles of Manwë.",
 "It is a barren wasteland, riddled with fire and ash and dust. The very air you breathe is a poisonous fume.",
 "I did not choose Frodo, he chose himself. But I believe he is the right person for the task.",
 "My power comes from the Valar, the beings who created this world.",
 "No army can withstand the power of Mordor. But we do not need to defeat Sauron. We only need to destroy the Ring.",
 "I would use this Ring from a desire to do good. But through me, it would wield a power too great and terrible to imagine.",
 "No. It was made in the fires of Mount Doom. Only there can it be unmade.",
 "I did not realize the true nature of the Ring until much later. And by then, it had become too dangerous to take it from him.",
 "They are leaving because their time is over. The Age of Men is beginning.",
 "I believe he means well, but he is easily swayed by the power of the Ring.",
 "We cannot defeat them with conventional means. We must take the fight to Sauron himself.",
 "Tom Bombadil is a mysterious figure, and his power is greater than you might think.",
 "There is always hope, but in this case, it is faint.",
 "No. Even the wise cannot see all ends. But the Great Eye is ever watchful."
]

chatgpt_prompts['frodo'] = [
  "Mr. Frodo, are you sure we're going the right way?",
  'We must be very careful, my precious. The Eye is always watching.',
  "It's a long road ahead, Frodo. Are you prepared for what's to come?",
  "Do you think we'll ever make it back to the Shire, Frodo?",
  'You cannot wield the Ring, Frodo. None of us can. It will corrupt us all.',
  "It's an honor to meet you, Frodo. I've heard so much about your journey.",
  "Many of these trees were my friends. They're all gone now.",
  'I can sense the weight of the Ring on you, Frodo. Do not give in to despair.',
  'You are but a small part of this war, Frodo. Do not think your mission is of great importance.',
  "It's a heavy burden you carry, Frodo. But we will do what we can to help.",
  'Do not be afraid to trust me, Frodo. I am not my brother.',
  "I can't imagine what you're going through, Frodo. But we're all here for you.",
  'The battle ahead will be long and hard, Frodo. But we will face it together.',
  'Do not listen to their lies, Frodo. The Ring can be used for good as well as evil.',
  "I know you're scared, Frodo. But we're all scared too."
]

chatgpt_sentences['frodo'] = [
 "I'm not sure of anything anymore, Sam.",
 "I know, Gollum. That's why we have to be even more careful than usual.",
 "I don't know if anyone can truly be prepared for this, Legolas. But we have to keep moving forward.",
 "I hope so, Pippin. But right now, we have to focus on the task at hand.",
 "I know that, Boromir. But what choice do we have?",
 "Thank you, Lady Eowyn. But it's not an honor that anyone should have to bear.",
 "I'm sorry for your loss, Treebeard. We've all lost so much on this journey.",
 "Thank you, Lady Galadriel. But sometimes it feels like there's no other way.",
 "I understand that, Lord Denethor. But it's still my duty to see it through.",
 "Thank you, Eomer. I appreciate your support more than you know.",
 "I believe you, Faramir. But I've been betrayed before, and it's hard to forget.",
 "Thank you, Rosie. It means more than you know to have friends like you.",
 "Thank you, Theoden. I am honored to fight beside such brave warriors.",
 "I don't believe that, Saruman. The Ring has already caused too much destruction.",
 "I'm not just scared."
]
