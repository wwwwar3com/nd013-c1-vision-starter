import argparse
import os
import shutil

from utils import get_module_logger


def split(source, destination):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - source [str]: source data directory, contains the processed tf records
        - destination [str]: destination data directory, contains 3 sub folders: train / val / test
    """
    for idx, f_name in enumerate(os.listdir(source)):
        if not f_name.endswith('tfrecord'):
            continue
        if idx % 100 < 15:
            shutil.move(source + '/' + f_name, destination+'/test/'+f_name)
        elif idx % 100 < 30:
            shutil.move(source + '/' + f_name, destination+'/train/'+f_name)
        else:
            shutil.move(source + '/' + f_name, destination+'/val/'+f_name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--source', default='./data/waymo/training_and_validation',
                        help='source data directory')
    parser.add_argument('--destination', default='./data/waymo/',
                        help='destination data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.source, args.destination)
