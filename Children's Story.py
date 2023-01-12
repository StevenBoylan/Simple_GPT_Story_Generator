# Import the openAI library
import openai

# Define the API key
openai.api_key = "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"

# Set variables for the Good Character, the Bad Character,
# the task the good character has to achieve and what the bad character has to to to stop this happening
main = input("Who is the main character in the story: ? (Type a person's name or a description: e.g. 'Anne' or 'an elephant')  ")
baddy = input("Who is the baddy in the story: ? (Type a person's name or a descriptions: e.g. 'Bob' or 'a witch') ")
task = input("What does the main character want/have to do: ? (Describe an action: e.g. 'Get back home' or 'Save a unicorn') ")
plot = input("What does the baddy want to do: ? (Describe an action: e.g. 'Stop Anne getting home' or 'steal the unicorn') ")
# Use these variables to create a seed phrase for GPT3
seed_phrase = str(("Write a children's story about " + main + " who wants to " + task +" " + "but " + baddy +" " + "wants to " + plot + "?"))

# Create the response for the API
response = openai.Completion.create(
engine="text-davinci-003",
prompt=seed_phrase,
temperature=0.7,
max_tokens=709,
top_p=1,
frequency_penalty=0.5,
presence_penalty=0
)

# Print the returned response
print(response.choices[0].text)
