The Smith-Waterman algorithm is a dynamic programming algorithm used for local sequence alignment. Unlike global alignment algorithms (such as Needleman-Wunsch), which align entire sequences, Smith-Waterman finds the most similar subsequences within two sequences. This makes it particularly useful in bioinformatics for comparing DNA, RNA, or protein sequences where only portions of the sequences may be similar.

## How It Works

The algorithm builds a scoring matrix where each cell (i, j) represents the best alignment score ending at position i in the first sequence and position j in the second sequence. The key difference from global alignment is that negative scores are replaced with zero, allowing alignments to start fresh at any position.

### Scoring System

The algorithm uses three parameters:
- **Match score:** Points awarded when two characters match (typically positive, e.g., +2)
- **Mismatch penalty:** Points deducted when characters don't match (typically negative, e.g., -1)
- **Gap penalty:** Points deducted for introducing a gap in either sequence (typically negative, e.g., -1)

### Algorithm Steps

1. **Initialize the matrix:** Create an (n+1) × (m+1) matrix where n and m are the lengths of the two sequences. Initialize all cells to 0 (unlike global alignment where the first row and column have cumulative gap penalties).

2. **Fill the matrix:** For each cell (i, j), calculate four values:
   - Match/mismatch: `score[i-1][j-1] + (match_score if sequences match, else mismatch_penalty)`
   - Gap in sequence 1: `score[i-1][j] + gap_penalty`
   - Gap in sequence 2: `score[i][j-1] + gap_penalty`
   - Zero: Start a new alignment
   
   Take the maximum of these four values.

3. **Find the maximum score:** Track the highest score in the matrix and its position.

4. **Traceback:** Starting from the maximum score position, trace back through the matrix following the path that produced each score, until reaching a cell with score 0. This produces the optimal local alignment.

## Complexity

- **Time Complexity:** O(n × m) where n and m are the lengths of the two sequences
- **Space Complexity:** O(n × m) for storing the scoring matrix

## Applications

- **Bioinformatics:** Finding similar regions in DNA, RNA, or protein sequences
- **Database searching:** Identifying homologous sequences in biological databases
- **Evolutionary studies:** Detecting conserved regions across species
- **Pattern matching:** Finding similar substrings in text processing

## Input Format

The input must consist of two sequences (strings) on separate lines:

```
sequence1
sequence2
```

Example:
```
ACACACTA
AGCACACA
```

The algorithm will find the best local alignment between these two sequences, showing the scoring matrix construction and the optimal alignment with statistics.
