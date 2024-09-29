import os
import logging
from datetime import datetime, timedelta

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def merge_logs(output_dir: str, merged_file: str, n: int) -> None:

    """
    Merge log files of the recent n days.

    Args:
        output_dir (str): the directory where the log file will be saved
        merged_file (str): the merged file
        n (int): max number of log files to be merged

    Returns:
        None
    """

    # Log files of the last n days
    log_files = []

    current_date = datetime.now()
    for i in range(n):
        date_str = (current_date - timedelta(days=i)).strftime('%Y%m%d')
        log_file = f'r6-matches-{date_str}.log'
        log_path = os.path.join(output_dir, log_file)

        # Add log file
        if os.path.exists(log_path):
            log_files.append(log_path)

    if not log_files:
        logging.warning(f'There is no log files for the recent {n} days.')
        return

    # Merge logs
    with open(merged_file, 'w') as outfile:
        for f in log_files:
            with open(f, 'r') as infile:
                outfile.write(infile.read())

    logging.info(f'Merged {len(log_files)} log files into {merged_file}.')


if __name__ == "__main__":
    # Merge logs of the recent days
    merge_logs(output_dir='input', merged_file='merged_matches.log', n=7)
