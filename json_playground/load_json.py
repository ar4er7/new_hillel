import json

# with open('json_playground/sw_templates.json') as f:
#     templates = json.load(f)

# print(type(templates))

# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))


with open("json_playground/sw_templates.json") as f:
    file_content = f.read()
    templates = json.loads(file_content)

print(templates.items())

# for section, commands in templates.items():
#     print(section)
#     print('\n'.join(commands))
