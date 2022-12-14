def removeOuterParentheses(s: str) -> str:
    stack, stack2 = [], []
    for i in s:
        if i == '(':  # проверяем явлется ли скобка открыващей для добавления в стек
            stack.append(i)
            if len(stack) > 1:
                stack2.append(i)
        elif i == ')' and len(stack) != 1:
            stack2.append(i)
            stack.pop()
        else:
            stack.clear()
    return ''.join(stack2)


print(f"'{removeOuterParentheses(input())}'")
