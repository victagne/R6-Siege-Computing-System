import os
import logging
from datetime import datetime
from collections import defaultdict
from typing import Optional
from utils import sort_file_by_operator_id, prepare_folder

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_operator_avg_kills(log_path: str, output_dir: Optional[str] = 'output') -> None:
    """
    Calculate the average number of kills for each operator from a log file
    and write the result into output/operator_top100_YYYYMMDD.txt.

    Args:
        log_path (str): log file containing player's match data
        output_dir (Optional[str]): output dictory, default to 'output'

    Returns:
        None
    """

    prepare_folder(output_dir)

    # {operator1: {match1: [kill1, kill2], match2: [], ...}, ...}
    operator_match_kills = defaultdict(lambda: defaultdict(list))

    with open(log_path, 'r') as f:
        for line in f:
            try:
                player_id, match_id, operator_id, nb_kills = line.strip().split(',')
                operator_id = int(operator_id)
                match_id = match_id.strip()
                nb_kills = int(nb_kills)
                operator_match_kills[operator_id][match_id].append(nb_kills)
            except ValueError as e:
                logging.error(f"Skipping malformed line: {line.strip()}, {e}")
                continue

    today_str = datetime.now().strftime('%Y%m%d')
    output_file = os.path.join(output_dir, f'operator_top100_{today_str}.txt')

    with open(output_file, 'w') as outfile:
        for operator_id, matches in operator_match_kills.items():
            match_avg_kills = []
            for match_id, kills in matches.items():
                avg_kills = int(sum(kills) / len(kills))  # Only keep integers, not decimals
                match_avg_kills.append((match_id, avg_kills))

            # sort in descending order by avg_kills
            match_avg_kills.sort(key=lambda x: x[1], reverse=True)
            top_100_matches = match_avg_kills[:100]

            formatted_kills = ','.join([f"{match_id}:{avg_kills}" for match_id, avg_kills in top_100_matches])
            outfile.write(f"{operator_id}|{formatted_kills}\n")

    # sort output by operator id
    sort_file_by_operator_id(output_file)
    logging.info(f"Top 100 average kills by operator written to {output_file}.")


if __name__ == "__main__":
    log_file = 'merged_matches.log'

    if os.path.exists(log_file):
        calculate_operator_avg_kills(log_path=log_file)
    else:
        logging.warning(f"Merged file {log_file} does not exist. Try 'make merge-data' first.")
