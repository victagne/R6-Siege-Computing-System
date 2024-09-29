import os
import logging
from collections import defaultdict
from datetime import datetime
from typing import Optional
from utils import prepare_folder

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def calculate_player_top_matches(log_path: str, output_dir: Optional[str] = 'output', n=10) -> None:
    """
    Calculate top n matches in terms of number of kills by player from a log file
    and write the result into output/player_top10_YYYYMMDD.txt.

    Args:
        log_path (str): log file containing players' match data
        output_dir (Optional[str]): output dictory, default to output

    Returns:
        None
    """

    prepare_folder(output_dir)

    # {player1: {match1: 2, match2: 5, ...}, ...}
    player_kills = defaultdict(lambda: defaultdict(int))

    with open(log_path, 'r') as file:
        for line in file:
            player_id, match_id, operator_id, nb_kills = line.strip().split(',')
            nb_kills = int(nb_kills)
            player_kills[player_id][match_id] += nb_kills

    current_date = datetime.now().strftime('%Y%m%d')
    output_file = os.path.join(output_dir, f'player_top10_{current_date}.txt')

    with open(output_file, 'w') as file:
        for player_id, matches in player_kills.items():
            # sort in descending order by kills and take top n
            top_matches = sorted(matches.items(), key=lambda item: item[1], reverse=True)[:n]
            match_results = ','.join([f"{match_id}:{kills}" for match_id, kills in top_matches])
            file.write(f"{player_id}|{match_results}\n")

    logging.info(f"Top 10 matches in terms of kills by player written to {output_file}.")


if __name__ == '__main__':
    log_file = 'merged_matches.log'
    if os.path.exists(log_file):
        calculate_player_top_matches(log_path=log_file)
    else:
        logging.warning(f"Merged file {log_file} does not exist. Try 'make merge-data' first.")
