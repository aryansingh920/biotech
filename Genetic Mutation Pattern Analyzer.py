import numpy as np
from itertools import product
import random
from collections import defaultdict

class GeneticSequenceAnalyzer:
    def __init__(self, sequence_length=1000):
        """
        Initialize the analyzer with a sequence length
        For demonstration we use 1000 base pairs - actual human genome has ~3 billion
        """
        self.sequence_length = sequence_length
        self.bases = ['A', 'T', 'G', 'C']
        self.known_cancer_mutations = {
            'p53': ['ATGCTA', 'GCTATG'],  # Example p53 tumor suppressor mutations
            'BRCA1': ['TACGTC', 'GCGCTA'], # Example breast cancer gene mutations
            'RAS': ['ATGGCG', 'GCGCTG']    # Example RAS oncogene mutations
        }
    
    def generate_random_sequence(self):
        """Generate a random DNA sequence of specified length"""
        return ''.join(np.random.choice(self.bases) for _ in range(self.sequence_length))
    
    def simulate_mutation(self, sequence):
        """
        Simulate random mutations in a sequence
        Types of mutations: substitution, insertion, deletion
        """
        mutation_types = ['substitution', 'insertion', 'deletion']
        mutation = random.choice(mutation_types)
        position = random.randint(0, len(sequence) - 1)
        mutated_sequence = list(sequence)
        
        if mutation == 'substitution':
            # Replace base with a different one
            available_bases = [b for b in self.bases if b != sequence[position]]
            mutated_sequence[position] = random.choice(available_bases)
        
        elif mutation == 'insertion':
            # Insert a random base
            mutated_sequence.insert(position, random.choice(self.bases))
        
        elif mutation == 'deletion':
            # Delete a base
            del mutated_sequence[position]
        
        return ''.join(mutated_sequence), mutation, position
    
    def generate_cancer_prone_sequences(self, num_sequences=100):
        """
        Generate sequences that contain known cancer-related mutations
        Returns both the sequence and the type of cancer mutation
        """
        cancer_sequences = []
        for _ in range(num_sequences):
            base_sequence = self.generate_random_sequence()
            # Randomly choose a known cancer mutation to insert
            cancer_type = random.choice(list(self.known_cancer_mutations.keys()))
            mutation_sequence = random.choice(self.known_cancer_mutations[cancer_type])
            
            # Insert the mutation at a random position
            position = random.randint(0, len(base_sequence) - len(mutation_sequence))
            mutated_sequence = (
                base_sequence[:position] + 
                mutation_sequence + 
                base_sequence[position + len(mutation_sequence):]
            )
            
            cancer_sequences.append({
                'sequence': mutated_sequence,
                'cancer_type': cancer_type,
                'mutation_position': position,
                'mutation_sequence': mutation_sequence
            })
            
        return cancer_sequences
    
    def analyze_mutation_patterns(self, sequences):
        """
        Analyze patterns in a list of sequences to identify common mutation characteristics
        """
        pattern_analysis = defaultdict(int)
        for seq in sequences:
            # Look for common patterns around mutation sites
            mutation_site = seq['sequence'][
                seq['mutation_position']:seq['mutation_position'] + 6
            ]
            pattern_analysis[mutation_site] += 1
        
        return pattern_analysis

# Example usage
analyzer = GeneticSequenceAnalyzer()

# Generate some example sequences with cancer-related mutations
print("Generating cancer-prone genetic sequences...")
cancer_sequences = analyzer.generate_cancer_prone_sequences(10)

# Analyze the first few sequences
print("\nExample cancer-prone sequences:")
for i, seq_data in enumerate(cancer_sequences[:3]):
    print(f"\nSequence {i+1}:")
    print(f"Cancer Type: {seq_data['cancer_type']}")
    print(f"Mutation Position: {seq_data['mutation_position']}")
    print(f"Mutation Sequence: {seq_data['mutation_sequence']}")
    print(f"First 50 bases: {seq_data['sequence'][:50]}...")

# Analyze patterns
patterns = analyzer.analyze_mutation_patterns(cancer_sequences)
print("\nCommon mutation patterns found:")
for pattern, count in sorted(patterns.items(), key=lambda x: x[1], reverse=True)[:5]:
    print(f"Pattern: {pattern}, Frequency: {count}")
