def calculate_powerOfStrings(s):
    # Checking whether the string is a palindrome
    is_palindrome = s == s[::-1]

    # Calculating X based on palindrome condition
    X = 5 if is_palindrome else 1

    # Calculating the power using the given formula
    power = len(s) // 2 + X
    print("String: ", s, " power: ", power)
    return power


def max_power_difference(strings):
    if not strings or len(strings) == 1:
        return 0

    # Calculating powers for each string and store them in a list
    powers = [calculate_powerOfStrings(s) for s in strings]

    # Finding the maximum and minimum powers in the string list
    max_power = max(powers)
    min_power = min(powers)

    # Calculating the maximum difference in power
    max_difference = max_power - min_power

    return max_difference


if __name__ == '__main__':
    strings_list = ['abc', 'acca', 'loki']
    result = max_power_difference(strings_list)
    print("Maximum difference in power:", result)
