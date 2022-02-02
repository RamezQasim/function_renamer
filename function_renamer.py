def function_renamer(code="def Hello_world()"):
    """
    input your code as a multi-line string

    the output code is a string with camel case function names.

    Assumptions:
    1) functions' words are separated by underscores only; no other separators used.
    2) a given function name which is not in camel case will not appear in camel case elsewhere
    """

    import re

    # This function converts function names into camel case
    def camel_maker(names):
        start = re.findall(r'^_*', names)  # stores the leading underscores if they exist
        words = list(filter(None, re.split(r'_', names)))  # stores words within the function name in a list without '_'

        if len(words) == 1 and "".join(words)[0].isupper():  # case: function name is already in camel case
            words = ''.join(words)
        else:
            words = [camel.capitalize() for camel in words]  # capitalise first letter while decapitalising others
            words = ''.join(words)

        start = "".join(start)
        result = start + words
        return result

    # Defining variables
    newcode = code  # store the new code after renaming the functions
    codeline = code.split('\n')
    funk = []  # will store function names within the code
    d = {}

    # Extract functions' names from code and store them in 'funk'
    for line in codeline:
        if line.startswith('def'):
            ppos = line.find('(')
            funk.append(line[4:ppos])  # get the string between 'def ' and the arguments '(...)'

    # output variables
    for function_name in funk:
        d[function_name] = {'hash': hash(function_name),
                            'camelcase': camel_maker(function_name),
                            'allcaps': function_name.upper()}
        newcode = newcode.replace(function_name, camel_maker(function_name))
    return d, newcode
