# stepwise-code

A specification and formatter designed to organize code into clear, sequential steps

# Step comments 

Step comments are used to document specific portions of code, breaking down the logic into manageable, understandable sections. They serve as guidelines for developers to annotate their code effectively, highly improving code readability and flexibility. It drastically helps AI models to understand the code and its logic and to provide better suggestions and completions.

# Specification 

- A `step comment` is a single-line comment that starts with a number of dashes (splitted by space after each dashes) and followed by a space and a step title. Examples: `# - Step`, `# -- Sub-step`, `# --- Sub-sub-sub-step`, `# --- - Sub-sub-sub-sub step` and so on
- All steps MUST start with uppercase letters and do not contain trailing dots
- Before and after each step, there MUST be exactly one empty line, unless the superseding specification rules dictate otherwise
- Each block scope effectively resets the depth of the hierarchy and new step MUST start with a single dash
- If code block has any step comments, it MUST be covered fully step comments

## Why not enforce all steps to have an empty line before and after?

Many standard formatters contradict with that rule. For example, `black` formatter in Python removes empty line before comment if it is the first line of the block.

## Example

```python

from collections import Counter


def calculate_statistics(numbers: list[float]) -> dict:
    """Function to calculate statistics from a list of numbers"""

    # - Initialize statistics

    statistics = {
        "mean": 0,
        "median": 0,
        "mode": [],
        "variance": 0,
        "standard_deviation": 0,
    }

    # - Calculate mean

    statistics["mean"] = sum(numbers) / len(numbers)

    # - Calculate median

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 0:
        statistics["median"] = (sorted_numbers[n // 2 - 1] + sorted_numbers[n // 2]) / 2
    else:
        statistics["median"] = sorted_numbers[n // 2]

    # - Calculate mode

    num_counter = Counter(numbers)
    statistics["mode"] = [num for num, occ in num_counter.items() if occ == max(num_counter.values())]

    # - Calculate dispersion measures

    # -- Calculate variance

    squared_diffs = [(x - statistics["mean"]) ** 2 for x in numbers]
    statistics["variance"] = sum(squared_diffs) / len(numbers)

    # -- Calculate standard deviation

    statistics["standard_deviation"] = statistics["variance"] ** 0.5

    # - Return statistics

    return statistics


```

# Formatter 

- Makes first letter of step title upper case: `- step 1` -> `- Step 1`.
- Removes trailing dots from step title: `- Step 1...` -> `- Step 1`.
- Removes extra spaces around `-`: # -    step 1.` -> `# - step 1`
- Adds a space every three dashes: `# ---- Step` -> `# --- - Step`.
- Leaves exactly one empty line before and after each step.
- Skips lines wrapped in `fmt: off` and `fmt: on` comments and lines with `fmt: skip` comment.

Example: 
```python

# -    step 1.
a = 1
# -- sub-step 1.
b = 2
# -- sub-step 2...
c = 3
# --- sub-sub-step
d = 4
# ---- sub-sub-sub step

# fmt: off
# -    step 1.
a = 1
# fmt: on

# -    step 1. # fmt: skip

```

-> 

```python

# - Step 1

a = 1

# -- Sub-step 1

b = 2

# -- Sub-step 2

c = 3

# --- Sub-sub-step

d = 4

# --- - Sub-sub--sub step

# fmt: off
# -    step 1.
a = 1
# fmt: on

# -    step 1. # fmt: skip 

```
