import os
import shutil
from pathlib import Path


def cleanUP():
    data_folder = os.path.join(Path(__file__).resolve().parent, 'connectmp', 'core', 'data')
    if os.path.exists(data_folder):
        shutil.rmtree(data_folder)
        print("Deleted data!")
        print("Cleanup Complete!")


if __name__ == '__main__':
    cleanUP()
