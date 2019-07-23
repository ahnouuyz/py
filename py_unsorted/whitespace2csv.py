import argparse
from pathlib import Path
from time import strftime, localtime
from tqdm import tqdm

def main():
    args = get_inputs()
    whitespace_to_csv(args.file, args.o, args.delim, args.csv, args.pandas)
    args.file.close()
    args.o.close()
    report(args.o.name)

def get_inputs():
    default_filename = 'output ' + strftime('%Y%m%d_%H%M', localtime()) + '.csv'
    parser = argparse.ArgumentParser(description="""
        Convert variable whitespaces to a single delimiter in data files.
        Generates csv files by default.
    """)
    parser.add_argument('file', type=argparse.FileType('r'), help='file to convert')
    parser.add_argument('-o', type=argparse.FileType('w'), default=default_filename, help='file to store output')
    parser.add_argument('-d', '--delim', type=str, default=',', help='new delimiter (default ",")')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-c', '--csv', action='store_true', help='use csv library to write csv file')
    group.add_argument('-p', '--pandas', action='store_true', help='use pandas library to write csv file')
    return parser.parse_args()

def whitespace_to_csv(in_file, out_file, delimiter=',', csv_lib=False, pandas_lib=False):
    if pandas_lib:
        import pandas as pd
        df = pd.read_csv(in_file, delim_whitespace=True)
        df.to_csv(out_file, index=None, line_terminator='\n')
    elif csv_lib:
        import csv
        lines = [line.split() for line in tqdm(in_file)]
        writer = csv.writer(out_file, delimiter=delimiter, lineterminator='\n')
        writer.writerows(tqdm(lines))
    else:
        lines = [delimiter.join(line.split()) for line in tqdm(in_file)]
        out_file.write('\n'.join(tqdm(lines)))

def report(output_path):
    path = Path(output_path)
    print(f"""
        New file name = {path}
        New file size = {path.stat().st_size / 1024:.1f} kB
        Done!
    """)

if __name__ == '__main__':
    main()
