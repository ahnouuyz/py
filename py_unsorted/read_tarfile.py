import pandas as pd
import tarfile

def main():
    tarfilepath = 'T39_Whitespace-Delimiters_20190703.tar.gz'
    df = get_tar_table(tarfilepath, 2, sep=',')

def get_tar_table(tarfilepath, item_no, sep=r'\s+'):
    with tarfile.open(tarfilepath) as arc:
        members = [m for m in arc.getmembers() if m.isfile()]
        print(members[item_no].name)
        return pd.read_csv(arc.extractfile(members[item_no]), sep=sep)

if __name__ == '__main__':
    main()
