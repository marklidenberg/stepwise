# stepwise-code

A specification and formatter designed to organize any code into clear, sequential steps

# Specification 

## Step comments 

Step comments are used to document specific portions of code, breaking down the logic into manageable, understandable sections. They serve as guidelines for developers to annotate their code effectively, highly improving code readability and flexibility. It drastically helps AI models to understand the code and its logic and to provide better suggestions and completions.

## Rules 

- A `step comment` is a single-line comment that starts with a number of dashes (splitted by space after each dashes) and followed by a space and a step title. Examples: `# - Step`, `# -- Sub-step`, `# --- Sub-sub-sub-step`, `# --- - Sub-sub-sub-sub step` and so on
- All steps MUST start with uppercase letters and do not contain trailing dots
- Before and after each step, there MUST be exactly one empty line, unless the superseding specification rules dictate otherwise
- Each block scope effectively resets the depth of the hierarchy and new step MUST start with a single dash
- If code block has any step comments, it MUST be covered fully step comments

### Why not enforce all steps to have an empty line before and after?

Many standard formatters contradict with that rule. For example, `black` formatter in Python removes empty line before comment if it is the first line of the block.

# Example

```python

```

## Example 

```python
# -    step 1.
a = 1
# -- sub-step 1.
b = 2
# -- sub-step 2...
c = 3
# --- sub-sub-step
# ---- sub-sub--sub step
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

# --- - Sub-sub--sub step
```
