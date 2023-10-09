def get_nested_value(data, key):
    keys = key.split('/')
    result = data
    for k in keys:
        if isinstance(result, dict) and k in result:
            result = result[k]
        else:
            return None
    return result

def main():
    object1 = {"a": {"b": {"c": "d"}}}
    key1 = "a/b/c"
    value1 = get_nested_value(object1, key1)
    print(f"Value 1: {value1}")  # Output: "d"

    object2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y/z"
    value2 = get_nested_value(object2, key2)
    print(f"Value 2: {value2}")  # Output: "a"

if __name__ == "__main__":
    main()
