import json, pyperclip, random
quotefile = './quotes.json'
with open(quotefile) as json_file:
    data = json.load(json_file)
quote = random.choice(data['quotes'])
pyperclip.copy(quote)
print(f'The following quote has been copied to your clipboard:\n\033[94m{quote}\033[0m')
