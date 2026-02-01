import argparse #Read CLI arguments
import json     #Read Config file
import logging  # Logging System
from pathlib import Path # File Handling

# READING CONFIG FILE

def load_config(config_path):
  """
    Reads JSON file and returns dictionary
  """
  path=Path(config_path) # Convert config path to path object
  config_text=path.read_text() # Reading content from path object
  return json.loads(config_text) # Convert json text to dictionary 

# Setup logging using config

def setup_logging(level):
  logging.basicConfig(
    level=getattr(logging,level),
    format="%(asctime)s - %(levelname)s - %(message)s"
  )

# Main Business Logic
def analyze_log(log_file,keyword):
  """ 
    Reads Log file and counts lines containing keyword.
  """
  text=Path(log_file).read_text()
  count=0
  for line in text.splitlines():
    if keyword in line:
      count+=1
  return count    

# main controller function
def main(config_path):
    """
    Controls the program using config file.
    """
    config = load_config(config_path)

    setup_logging(config["log_level"])

    logging.info("Starting log analysis")

    result = analyze_log(
        config["log_file"],
        config["keyword"]
    )

    logging.info(f"Total '{config['keyword']}' lines: {result}")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Config-driven Log Analyzer"
    )

    parser.add_argument(
        "--config",
        required=True,
        help="Path to config JSON file"
    )

    args = parser.parse_args()

    main(args.config)


