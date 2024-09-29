import os
import uuid
import random
import argparse
from datetime import datetime, timedelta
from utils import clear_directory, prepare_folder
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_and_write_data(num_rows: int, max_operator_id: int, max_kills: int, days: int) -> None:

    """
    Generate testing data.

    Args:
        num_rows (int): the total number of rows to generate
        max_operator_id (int): max operator id
        max_kills (int): max number of kills
        days (int): the number of the recent days to generate

    Returns:
        None
    """

    output_dir = "input"
    prepare_folder(output_dir)

    for i in range(days):
        # Calculate date with delta
        current_date = (datetime.now() - timedelta(days=i)).strftime("%Y%m%d")
        filename = os.path.join(output_dir, f"r6-matches-{current_date}.log")

        # Generate rows and write file
        with open(filename, "w") as file:
            for _ in range(num_rows):
                # If we use uuid.uuid4(), play_ids and match_ids are almost unique, but in real case, they can be same.
                # So here we only keep the first 4 bits of UUID to make some duplications intentionally.
                player_id = str(uuid.uuid4())[:4]
                match_id = str(uuid.uuid4())[:4]
                operator_id = random.randint(1, max_operator_id)
                nb_kills = random.randint(0, max_kills)

                row = f"{player_id}, {match_id}, {operator_id}, {nb_kills}"
                file.write(row + "\n")

        logging.info(f"File {filename} is created.")


def main():
    parser = argparse.ArgumentParser(description="Generate R6 match data and save to output folder.")
    parser.add_argument('--num_rows', type=int, default=1000000,  # in real case, it should greater than 30M
                        help='Number of rows of data to generate (default: 1000000)')
    parser.add_argument('--max_operator_id', type=int, default=36,
                        help='Maximum value for operator_id (default: 36)')
    parser.add_argument('--max_kills', type=int, default=1500,
                        help='Maximum number of kills (nb_kills) (default: 1500)')
    parser.add_argument('--days', type=int, default=7,
                        help='Number of recent days (default: 7)')
    args = parser.parse_args()

    # Clean input and output folders
    clear_directory('input')
    clear_directory('output')

    # Generate and write data
    generate_and_write_data(args.num_rows, args.max_operator_id, args.max_kills, args.days)


if __name__ == "__main__":
    main()
