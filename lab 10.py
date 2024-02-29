def find_s(examples):
    # Initialize the most specific hypothesis
    h = ['ϕ'] * len(examples[0])  # Assuming all examples have the same number of attributes

    for example in examples:
        for i, attribute in enumerate(example):
            if h[i] == 'ϕ':
                h[i] = attribute  # Replace 'ϕ' with the observed attribute value
            elif h[i] != attribute:
                h[i] = '?'  # Generalize if there's a mismatch

    return h
# Define a dataset of positive examples ([Sky, AirTemp, Humidity, Wind, PlayTennis])
# Note: We omit the target concept 'PlayTennis' since we're focusing on positive examples.
positive_examples = [
    ['Sunny', 'Warm', 'Normal', 'Strong'],
    ['Sunny', 'Warm', 'High', 'Strong'],
    ['Sunny', 'Warm', 'High', 'Weak']
]

# Apply the Find-S algorithm
hypothesis = find_s(positive_examples)
print("The most specific hypothesis:", hypothesis)
