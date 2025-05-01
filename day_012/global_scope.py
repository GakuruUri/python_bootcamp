enemies = 1

def increase_enemies():
    global_enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")


enemies = 1
def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemy + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")