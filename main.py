# Python program to generate Wolfram code for a graph based on any base and number of digits

def next_state_any_base(number_list, base):
    # Calculate the differences between adjacent digits in the list, wrapping around
    diffs = [abs(number_list[i] - number_list[(i+1) % len(number_list)]) for i in range(len(number_list))]
    return diffs

def int_to_base_list(n, base, digits):
    # Convert integer n to a list of digits in the specified base, ensuring a fixed number of digits
    base_str = ""
    while n > 0:
        base_str = str(n % base) + base_str
        n //= base
    base_str = base_str.zfill(digits)  # Ensure it has the correct number of digits
    return [int(digit) for digit in base_str]

def base_list_to_int(base_list, base):
    # Convert a list of base-digits back to an integer
    return sum(d * (base ** i) for i, d in enumerate(reversed(base_list)))

def generate_wolfram_code(base, digits):
    # Calculate the total number of nodes based on base and digits
    num_nodes = base ** digits
    
    # Generate transitions for the specified base and number of digits
    transitions = []
    for n in range(num_nodes):
        original_number_list = int_to_base_list(n, base, digits)
        next_number_list = next_state_any_base(original_number_list, base)
        next_number = base_list_to_int(next_number_list, base)
        transitions.append((n, next_number))
    
    # Generate Wolfram code for the transitions in the specified base
    wolfram_code = "Graph[\n"
    wolfram_code += f"  Table[IntegerString[i, {base}, {digits}], {{i, 0, {num_nodes - 1}}}],\n"
    wolfram_code += "  DirectedEdge @@@ ({IntegerString[#1, " + str(base) + ", " + str(digits) + "], IntegerString[#2, " + str(base) + ", " + str(digits) + "]} & @@@ {\n"
    wolfram_code += ", ".join(f"{{{src}, {dest}}}" for src, dest in transitions)
    wolfram_code += "}),\n"
    wolfram_code += "  VertexLabels -> \"Name\"\n"
    wolfram_code += "]"
    
    return wolfram_code

# Example: Generate code for base 3 and 4 digits
base = 4
digits = 4
wolfram_code_output = generate_wolfram_code(base, digits)

# Display the generated Wolfram code
print(wolfram_code_output)
