

def multi_bracket_validation(input):
    """takes string argument and returns bool if brackets in string are balanced"""
    queue = []
    for i in input:
        if i in ['(', '[', '{']:
            queue.append(i)
        elif i in [')', ']', '}']:
            if queue == []:
                return False
            elif i == ')' and '(' not in queue:
                return False
            elif i == ']' and '[' not in queue:
                return False
            elif i == '}' and '{' not in queue:
                return False
            elif i == ')' and '(' in queue:
                queue.remove('(')
            elif i == ']' and '[' in queue:
                queue.remove('[')
            elif i == '}' and '{' in queue:
                queue.remove('{')
    if queue == []:
        return True
    else:
        return False
