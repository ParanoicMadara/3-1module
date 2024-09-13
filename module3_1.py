calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]

# Пример вызова функций
info = string_info("Hello, World!")
print(info)

contains = is_contains("apple", ["Orange", "Banana", "Apple"])
print(contains)

print(calls)