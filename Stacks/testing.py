from Stacks import Stack1


new_stack=Stack1()

print(new_stack.is_empty()) #should return true because the stack is empty
new_stack.push(4)
new_stack.push('Red')
new_stack.push('Burger')
new_stack.push('kebab')


print(new_stack)