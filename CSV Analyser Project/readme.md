# ---------------------------------- ✅

# WHAT EXACTLY TO DO ❤️

# ---------------------------------- ✅

1. A command-line tool written in Python
2. Takes a CSV file as input
3. Automatically:
   a) Reads the data
   b) Analyzes it
   c) Generates a report (text / CSV / summary file)
4. No hard-coding
5. Reusable
6. Config-driven

👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾👾

# -----------------------------------✅

3️⃣ WHAT “AUTOMATED REPORT” MEANS

# -----------------------------------✅

- Automated report means:

-- No manual calculation
-- No manual formatting
-- No Excel clicking

- The program automatically generates:

-- Total rows
-- Column-wise statistics
-- Errors / missing values
-- Summaries
-- Clean output file

# ------------------------------------✅

--- ----------------------------------------------->

###### FILES USAGE

- File_1: report.py
    - The entry point of your application
    - Contains the Python code that:
      -- Reads input
      -- Processes data
      -- Generates report

- FILE_2:config.json
  -- A control file that defines:
  -- Input CSV path
  -- Output report path
  -- Columns to analyze
  -- Report type
  -- Logging level

- File_2: data/input.csv
  -- Raw CSV data
  -- Source of truth
  -- Program reads from here
  -- No modification should happen here

- FILE_3: output/report.txt
  -- Final output produced by program
  -- Human-readable summary
  -- This is the goal of the project
  -- User cares about this file

- FILE_4: logs/app.log
  -- Record of everything program does
  -- Debug errors later
  -- Analyze failures
  -- Professional standard

--- ----------------------------------------->

### HOW ALL FILES WORK TOGETHER (FLOW)

User runs command
→ report.py starts
→ reads config.json
→ reads data/input.csv
→ processes data
→ writes output/report.txt
→ logs everything to logs/app.log
