import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from itertools import product

def generate_rna_combinations():
    """
    Generates all possible RNA codon combinations using the four bases:
    A (Adenine), U (Uracil), G (Guanine), C (Cytosine)
    """
    bases = ['A', 'U', 'G', 'C']
    # Using itertools.product to generate all possible combinations
    codons = [''.join(p) for p in product(bases, repeat=3)]
    return codons

def create_codon_matrix():
    """
    Creates a 4x16 matrix representing all 64 possible codons,
    organized by their first and second bases
    """
    bases = ['A', 'U', 'G', 'C']
    codons = generate_rna_combinations()
    
    # Create a matrix to store the counts
    matrix = np.zeros((4, 16))
    
    # Fill the matrix based on the first two bases
    for i, first_base in enumerate(bases):
        for j, (second_base, third_base) in enumerate(product(bases, bases)):
            codon = first_base + second_base + third_base
            matrix[i, j] = codons.index(codon)
            
    return matrix, bases

def visualize_rna_evolution():
    """
    Creates two visualizations:
    1. Historical understanding (simpler grouping)
    2. Current understanding (complete codon table)
    """
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 12))
    
    # Historical visualization (circa 1960s)
    historical_data = np.random.rand(4, 4)  # Simplified 4x4 understanding
    sns.heatmap(historical_data, ax=ax1, cmap='viridis',
                xticklabels=['A', 'U', 'G', 'C'],
                yticklabels=['A', 'U', 'G', 'C'])
    ax1.set_title('Historical Understanding of RNA Codons (1960s)\n'
                 'Simple Base Pairing Model')
    
    # Current complete visualization
    matrix, bases = create_codon_matrix()
    second_third_labels = [f"{b1}{b2}" for b1, b2 in product(bases, bases)]
    sns.heatmap(matrix, ax=ax2, cmap='viridis',
                xticklabels=second_third_labels,
                yticklabels=bases)
    ax2.set_title('Current Understanding of RNA Codons\n'
                 'Complete 64 Codon Model')
    
    # Add explanatory text
    plt.figtext(0.02, 0.98, 'Evolution of RNA Codon Understanding:', 
                fontsize=12, weight='bold')
    plt.figtext(0.02, 0.95, 
                'Historical: Scientists initially thought the genetic code was a simple '
                'base-pairing system.\nModern: We now know there are 64 possible codons '
                'coding for 20 amino acids plus stop signals.', 
                fontsize=10)
    
    plt.tight_layout()
    return plt.gcf()

# Generate and store all possible codons
all_codons = generate_rna_combinations()
print(f"Total number of possible RNA codons: {len(all_codons)}")
print("\nFirst 10 codons as example:")
for i, codon in enumerate(all_codons[:10]):
    print(f"Codon {i+1}: {codon}")

# Create visualization
fig = visualize_rna_evolution()
plt.show()

# Additional analysis of codon patterns
def analyze_codon_patterns():
    """
    Analyzes patterns in codon distribution
    """
    patterns = {}
    for codon in all_codons:
        first_base = codon[0]
        if first_base not in patterns:
            patterns[first_base] = []
        patterns[first_base].append(codon)
    
    return patterns

patterns = analyze_codon_patterns()
print("\nDistribution of codons by first base:")
for base, codons in patterns.items():
    print(f"\nBase {base} starts {len(codons)} codons:")
    print(", ".join(codons[:5]) + "...")
