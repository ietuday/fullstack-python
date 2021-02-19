#  https://docs.python.org/2.0/ref/augassign.html
#augmented_assignment_stmt: target augop expression_list
#augop:           "+=" | "-=" | "*=" | "/=" | "%=" | "**="
#               | ">>=" | "<<=" | "&=" | "^=" | "|="
#target:          identifier | "(" target_list ")" | "[" target_list "]"
#              | attributeref | subscription | slicing



x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **=2
print(x)

x %= 60
print(x)

greeting = "Good "
print(greeting)
greeting += "morning "
print(greeting)

greeting *= 5
print(greeting)

# += -= *= /= %= **= <<= >>= &= ^= |=