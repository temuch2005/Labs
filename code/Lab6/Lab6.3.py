def modify_set_with_vowels(digit_set):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    try:
        result_set = digit_set.union(vowels)
    except AttributeError:
        print("Задана множина була перетворена на список.")
        result_set = set(list(digit_set) + list(vowels))
    return result_set

def main():
    digit_set = {'c', 'd'}

    updated_set = modify_set_with_vowels(digit_set)

    print("Результуюча множина:", updated_set)

if __name__ == "__main__":
    main()
