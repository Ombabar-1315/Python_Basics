import random

def generate_agent_id():
    id = random.randint(1000, 9999)
    return id

def generate_agent_code():
    code = random.randint(10000, 99999)
    return code



def genrate_agent(*skills,**details):
    print("Agent Skills :",skills)
    print("Agent Details :",details)

