import re

def get_pattern_and_replacement(the_input, output):
    """
    Given the_input and output returns the pattern for matching more general case of the_input and a template string for generating the desired output.

    >>> get_pattern_and_replacement("You're not being nice to me.", "I want to be treated nicely.")
    ("You're not (?P<word0>\w+)ing (?P<word1>\w+) (?P<word2>\w+) me.", 'I want {{ word2 }} {{ word0 }} treated {{ word1 }}ly.')
    >>> get_pattern_and_replacement("You're not meeting my needs.", "I want my needs met.")
    ("You're not meeting (?P<word0>\w+) (?P<word1>\w+).", 'I want {{ word0 }} {{ word1 }} met.')
    """
    the_input_words = [i.strip('.?!') for i in the_input.split()]    
    output_words = [i.strip('.?!') for i in output.split()]
    input_set = set(the_input_words)
    output_set = set(output_words)
    
    intersection = input_set & output_set
    input_set_difference = list(input_set - output_set)
    output_set_difference = list(output_set - input_set)
    for i in input_set_difference:
        for j in output_set_difference:
            if i in j:
                intersection.add(i)
    for i in output_set_difference:
        for j in input_set_difference:
            if i in j:
                intersection.add(i)  
    if intersection:
        intersection = list(intersection)
        intersection = sorted(intersection, key=lambda x: len(x))[::-1]
        intersection = [i for i in intersection if len(i) > 1]
        # in order
        in_order = []
        for i in the_input_words:
            if i in intersection:
                in_order.append(i)
            else:
                for j in intersection:
                    if j in i:
                        in_order.append(j)
        intersection = in_order
        print intersection
        pattern = the_input
        replacement = output
        for i, word in enumerate(intersection):
            pattern = pattern.replace(word, '(?P<word%s>\w+)' % (i), 1)
            replacement = replacement.replace(word, '{{ word%s }}' % (i))
        return (pattern, replacement)
    else:
        return (the_input, output)
