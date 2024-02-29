# Candidate Elimination Algorithm Implementation

# Step 1: Initialize specific and general hypotheses
def initialize_hypotheses(attributes):
    specific_hypothesis = ['0'] * len(attributes)
    general_hypothesis = ['?'] * len(attributes)
    return specific_hypothesis, general_hypothesis

# Step 2: Update hypotheses based on example
def update_hypotheses(specific_hypothesis, general_hypothesis, example):
    for i in range(len(specific_hypothesis)):
        if example[i] == '1':
            specific_hypothesis[i] = example[i]
            general_hypothesis[i] = '?' if specific_hypothesis[i] != general_hypothesis[i] else general_hypothesis[i]
        elif example[i] == '0':
            general_hypothesis[i] = specific_hypothesis[i] if specific_hypothesis[i] != general_hypothesis[i] else general_hypothesis[i]
    return specific_hypothesis, general_hypothesis

# Step 3: Candidate Elimination Algorithm
def candidate_elimination_algorithm(training_examples):
    attributes = training_examples[0][0:-1]
    specific_hypothesis, general_hypothesis = initialize_hypotheses(attributes)

    for example in training_examples:
        label = example[-1]
        if label == '1':  # Positive example
            specific_hypothesis, general_hypothesis = update_hypotheses(specific_hypothesis, general_hypothesis, example)
        elif label == '0':  # Negative example
            general_hypothesis = update_negative_example(specific_hypothesis, general_hypothesis, example)

    return specific_hypothesis, general_hypothesis

# Step 4: Update hypotheses based on negative example
def update_negative_example(specific_hypothesis, general_hypothesis, example):
    for i in range(len(specific_hypothesis)):
        if example[i] == '0':
            general_hypothesis[i] = specific_hypothesis[i]
            specific_hypothesis[i] = '?' if specific_hypothesis[i] != general_hypothesis[i] else specific_hypothesis[i]
    return general_hypothesis

# Step 5: Test the Candidate Elimination Algorithm
def test_candidate_elimination_algorithm():
    # Training examples
    training_examples = [
        ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', '1'],
        ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', '1'],
        ['Rainy', 'Cold', 'High', 'Weak', 'Warm', 'Change', '0'],
        ['Sunny', 'Cold', 'High', 'Strong', 'Cool', 'Change', '1']
    ]

    # Run Candidate Elimination algorithm
    specific_hypothesis, general_hypothesis = candidate_elimination_algorithm(training_examples)

    # Display results
    print("\nCandidate Elimination Algorithm Results:")
    print("Specific Hypothesis:", specific_hypothesis)
    print("General Hypothesis:", general_hypothesis)

if __name__ == "__main__":
    # Run the test
    test_candidate_elimination_algorithm()
