def solution(string, markers):
    s = [line for line in string.splitlines()]
    for m in markers:
        s = [elem[:elem.find(m)].rstrip() if m in elem else elem for elem in s]
    return '\\n'.join(s)


result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ['#', '!'])
print(result)


######## best practice solution from kata user957258
def solution2(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
