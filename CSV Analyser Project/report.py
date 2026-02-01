import json
import csv
from pathlib import Path
import datetime
import logging


def load_config(config_path):
  path=Path(config_path)
  text=path.read_text()
  return json.loads(text)

def logging_setup(logLevel):
  log_dir=Path("logs")
  log_dir.mkdir(exist_ok=True)
  logging.basicConfig(
  filename=log_dir/"app.log",
  filemode="a",
  level=getattr(logging,logLevel),
  format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def generate_report(csv_path,output_path):
 
  path=Path(csv_path)
  path2=Path(output_path)
  path2.parent.mkdir(parents=True, exist_ok=True)
  
  marks=[]
  
  if not path.exists():
    print("Missing csv file")
    logging.critical("Missing csv file")
    return
    
  logging.info("Reading CSV file...")
  with path.open(newline="") as f:
    reader=csv.DictReader(f)
    rows=list(reader)
    
    if not rows:
      print("No data Present")
      logging.warning("No data Present")
      return
   
    for i in rows:
      try:
        marks.append(int(i["marks"]))
      except ValueError:
         logging.error(
                    f"Invalid marks for {i.get('name', 'UNKNOWN')}: {i['marks']}"
                )
      
     
  if not marks:
    logging.warning("No valid marks found for calculation")
    return
  
  
  average=sum(marks)/len(marks)
  maxMarks=max(marks)
  minMarks=min(marks)
  
  
  logging.info("Writing report to output file")
  with path2.open("a") as f2:
    f2.write(f"Date: {datetime.date.today()}\n")
    f2.write(f"Average marks: {average:.2f}\n")
    f2.write(f"Max marks: {maxMarks}\n")
    f2.write(f"Min marks: {minMarks}\n")
    f2.write("----------------------------------\n\n")
  logging.info("Report generated successfully")
    
 

      
def main():
  
  config=load_config("config.json")
  try: 
   csv_path=config["input_file"]
   output_path=config["output_file"]
   logLevel=config["log_level"]
  
  except KeyError as e:
    print("Missing config key: ",e)
    return
   
  logging_setup(logLevel)
  logging.info("User logged in....")
  generate_report(csv_path,output_path)
  logging.info("Program Finished..") 

    
  
if __name__=="__main__":
  main()  