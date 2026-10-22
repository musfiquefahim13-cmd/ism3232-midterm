
# Commands and Terminal Output

## 1. Environment Setup

Command:

```bash
python3 -m pip install -r requirements.txt
```

Output:

```text
[Insert actual installation output from the terminal]
```

## 2. Run the Program

Command:

```bash
python3 main.py
```

Output:

```text
Kettle Works: $1520.00 | sign-off: no | second chef: no
Lumen Labs: $1154.25 | sign-off: no | second chef: yes
Marlow Gala: $3325.00 | sign-off: yes | second chef: yes
Events: 8
Total booked: $14521.25
Average event total: $1815.16
Largest event total: Hilltop Gym
Sign-offs needed: 3
Second chefs needed: 4
```

## 3. Run Unit Tests

Command:

```bash
python3 -m pytest -v
```

Output:

```text
23 passed in 0.07s
```

## 4. Check Formatting

Command:

```bash
ruff format --check .
```

Output:

```text
6 files already formatted
```

## 5. Check Linting

Command:

```bash
ruff check .
```

Output:

```text
All checks passed!
```

## 6. Git Commit History

Command:

```bash
git log --oneline
```

Output:

```text
1e66d75 Document catering project in README
e65aa1d Expand unit tests to cover all business rules
24bc239 Add catering business rules and unit tests
a0cfa78 Implement catering calculations and event report
156dd11 Initialize catering project structure
```
