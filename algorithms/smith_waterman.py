from utils.markdown_utils import markdown_table


def smith_waterman(input_string: str) -> str:
    """
    Smith-Waterman algorithm for local sequence alignment.
    Finds the optimal local alignment between two sequences.

    :param input_string: Two sequences separated by newlines
    :return: Generator yielding strings and tables showing the algorithm steps
    """
    lines = input_string.strip().splitlines()
    sequence1 = lines[0].strip()
    sequence2 = lines[1].strip()

    n = len(sequence1)
    m = len(sequence2)

    # Scoring parameters
    match_score = 2
    mismatch_penalty = -1
    gap_penalty = -1

    # Initialize scoring matrix
    score_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Track the maximum score and its position for traceback
    max_score = 0
    max_pos = (0, 0)

    headers_rows = [""] + list(sequence2)
    headers_columns = [""] + list(sequence1)

    yield "## Smith-Waterman Algorithm Resolution"
    yield f"**Sequence 1:** {sequence1}"
    yield f"**Sequence 2:** {sequence2}"
    yield ""
    yield "**Scoring parameters:**"
    yield f"- Match score: +{match_score}"
    yield f"- Mismatch penalty: {mismatch_penalty}"
    yield f"- Gap penalty: {gap_penalty}"
    yield ""

    yield "### Initial State"
    yield (
        "The scoring matrix is initialized with zeros. Unlike global alignment (Needleman-Wunsch), "
        "the first row and column remain zero to allow local alignments to start anywhere."
    )
    yield markdown_table(score_matrix, headers_rows, headers_columns)
    yield ""

    yield "### Filling the Scoring Matrix"
    yield "For each cell (i, j), we calculate the score using:"
    yield "- **Match/Mismatch:** score[i-1][j-1] + (match_score if sequences match, else mismatch_penalty)"
    yield "- **Gap in sequence 1:** score[i-1][j] + gap_penalty"
    yield "- **Gap in sequence 2:** score[i][j-1] + gap_penalty"
    yield "- **Zero:** Start a new alignment"
    yield ""
    yield "We take the maximum of these four values."
    yield ""

    # Fill the scoring matrix
    for i in range(1, n + 1):
        yield f"### Step {i}: Processing row {i} (character '{sequence1[i - 1]}')"

        for j in range(1, m + 1):
            # Calculate match/mismatch score
            if sequence1[i - 1] == sequence2[j - 1]:
                diagonal_score = score_matrix[i - 1][j - 1] + match_score
                match_type = "match"
            else:
                diagonal_score = score_matrix[i - 1][j - 1] + mismatch_penalty
                match_type = "mismatch"

            # Calculate gap scores
            gap_up = score_matrix[i - 1][j] + gap_penalty
            gap_left = score_matrix[i][j - 1] + gap_penalty

            # Take maximum (including 0 for local alignment)
            score_matrix[i][j] = max(0, diagonal_score, gap_up, gap_left)

            # Track maximum score for traceback
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)

            # Explain the calculation for this cell
            if (
                j == 1
                or sequence1[i - 1] == sequence2[j - 1]
                or score_matrix[i][j] == max_score
            ):
                yield f"**Cell ({i}, {j}):** Comparing '{sequence1[i - 1]}' with '{sequence2[j - 1]}' ({match_type})"
                yield f"  - Diagonal: {score_matrix[i - 1][j - 1]} + {match_score if match_type == 'match' else mismatch_penalty} = {diagonal_score}"
                yield f"  - Up (gap): {score_matrix[i - 1][j]} + {gap_penalty} = {gap_up}"
                yield f"  - Left (gap): {score_matrix[i][j - 1]} + {gap_penalty} = {gap_left}"
                yield f"  - **Chosen:** {score_matrix[i][j]}"
                yield ""

        yield f"After processing row {i}:"
        yield markdown_table(score_matrix, headers_rows, headers_columns)
        yield ""

    yield "### Traceback"
    yield f"The maximum score is **{max_score}** at position ({max_pos[0]}, {max_pos[1]})"
    yield "We now traceback from this position to find the optimal local alignment."
    yield ""

    # Traceback to find the alignment
    aligned_seq1 = []
    aligned_seq2 = []
    alignment_symbols = []

    i, j = max_pos
    traceback_path = [(i, j)]

    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        current_score = score_matrix[i][j]
        diagonal_score = score_matrix[i - 1][j - 1]
        up_score = score_matrix[i - 1][j]

        # Determine which direction we came from
        if sequence1[i - 1] == sequence2[j - 1]:
            match_score_val = match_score
        else:
            match_score_val = mismatch_penalty

        if current_score == diagonal_score + match_score_val:
            # Diagonal move (match or mismatch)
            aligned_seq1.append(sequence1[i - 1])
            aligned_seq2.append(sequence2[j - 1])
            if sequence1[i - 1] == sequence2[j - 1]:
                alignment_symbols.append("|")
            else:
                alignment_symbols.append("x")
            i -= 1
            j -= 1
        elif current_score == up_score + gap_penalty:
            # Up move (gap in sequence 2)
            aligned_seq1.append(sequence1[i - 1])
            aligned_seq2.append("-")
            alignment_symbols.append(" ")
            i -= 1
        else:
            # Left move (gap in sequence 1)
            aligned_seq1.append("-")
            aligned_seq2.append(sequence2[j - 1])
            alignment_symbols.append(" ")
            j -= 1

        traceback_path.append((i, j))

    # Reverse the alignment (we built it backwards)
    aligned_seq1.reverse()
    aligned_seq2.reverse()
    alignment_symbols.reverse()
    traceback_path.reverse()

    yield f"**Traceback path:** {' → '.join([f'({i},{j})' for i, j in traceback_path])}"
    yield ""

    yield "### Final Result"
    yield f"**Optimal local alignment score:** {max_score}"
    yield ""
    yield "**Alignment:**"
    yield "```"
    yield f"Seq1: {''.join(aligned_seq1)}"
    yield f"      {''.join(alignment_symbols)}"
    yield f"Seq2: {''.join(aligned_seq2)}"
    yield "```"
    yield ""

    # Calculate alignment statistics
    matches = sum(
        1 for i in range(len(alignment_symbols)) if alignment_symbols[i] == "|"
    )
    mismatches = sum(
        1 for i in range(len(alignment_symbols)) if alignment_symbols[i] == "x"
    )
    gaps = sum(
        1
        for i in range(len(aligned_seq1))
        if aligned_seq1[i] == "-" or aligned_seq2[i] == "-"
    )
    alignment_length = len(aligned_seq1)
    identity = (matches / alignment_length * 100) if alignment_length > 0 else 0

    yield "**Alignment statistics:**"
    yield f"- Length: {alignment_length}"
    yield f"- Matches: {matches}"
    yield f"- Mismatches: {mismatches}"
    yield f"- Gaps: {gaps}"
    yield f"- Identity: {identity:.1f}%"
    yield ""

    yield "### Complete Scoring Matrix"
    yield markdown_table(score_matrix, headers_rows, headers_columns)
