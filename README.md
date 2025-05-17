## Environment Setup

1. Create repository on Github - Solar-Data-Discovery-optimization
2. Clone this repository:
   git clone https://github.com/Amdemichael/Solar-Data-Discovery-optimization.git
3. Create and activate virtual environment:
   -- python -m venv venv 
   -- .\venv\Scripts\activate
4. Install requirements:
  -- pip install -r requirements.txt

## Project Structure
1. data/: Contains raw data (ignored by git)

2. notebooks/: Jupyter notebooks for analysis

3. src/: Source code

4. scripts/: Utility scripts

5. tests/: Test cases

## Create Branch and Make commits
# Create and switch to new branch
git checkout -b setup-task

# Initial commit - .gitignore
git add .gitignore
git commit -m "init: add .gitignore"

# Second commit - environment setup
git add requirements.txt
git commit -m "chore: venv setup"

# Third commit - CI workflow
git add .github/workflows/ci.yml
git commit -m "ci: add GitHub Actions workflow"

# Fourth commit - project structure
git add README.md .vscode/settings.json notebooks/ tests/ scripts/
git commit -m "build: create project structure"


