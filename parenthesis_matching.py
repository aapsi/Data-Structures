from Stack import Stack

def is_match(p1,p2):
    if p1 == '(' and p2 == ')':
        return True
    elif p1 == '{' and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_paren_matching(string):
    s =Stack()
    index = 0
    is_balanced = True

    while index< len(string) and is_balanced:
        paren = string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced == False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced == False
        index+=1

    if is_balanced and s.is_empty():
        return True
    else:
        return False

print(is_paren_matching("((){})"))