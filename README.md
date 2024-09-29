# R6 Siege Computing System - Data Processing

## Table of Contents

- [Background](#background)
- [Objective](#objective)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Author](#author)

## Background

Rainbow Six Siege (R6 Siege) is a first-person shooter game. We are receiving each day in a folder, a text file named `r6-matches-YYYYMMDD.log` that contains the logs of the whole matches made on R6 Siege at this date and in which the format is specified as follows.

`player_id, match_id, operator_id, nb_kills`

- `player_id`: Player unique identifier, a UUID. R6 Siege has more than 35M players.
- `match_id`: Match unique identifier, a UUID. R6 Siege currently have millions of matches, a number in constant increase.
- `operator_id`: Operator unique identifier, an integer. There are dozens of operators available in the game.
- `nb_kills`: Number of kills by the player, an integer.

## Objective

We need to suggest a system that computes:

- `Daily Operator Performance Analysis`: Compute and generate a text file (`operator_top100_YYYYMMDD.txt`) containing the top 100 operators based on the average number of kills over the last 7 days. Each row will follow the format: `operator_id|match_id1:avg_kills1,match_id2:avg_kills2,...,match_id100:avg_kills100`, where `avg_kills` is the average number of kills for the operator in the top 100 matches, listed in descending order.
- `Top Player Matches`: Generate a text file (`player_top10_YYYYMMDD.txt`) that ranks the top 10 players with the highest number of kills in individual matches over the past 7 days. Each row will follow the format:`player_id|match_id1:nb_kills1,match_id2:nb_kills2,...,match_id10:nb_kills10`, where `nb_kills` represents the number of kills for each player per match, in descending order.

## Installation

### Prerequisites

- Linux/MacOS
- Python 3.11.9
- Git, virtualenv

### Create a virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

## Project Structure

```plaintext
├── Makefile
├── README.md
├── compute_operator_stats.py
├── compute_player_stats.py
├── generate_matches.py
├── input
│   ├── r6-matches-20240922.log
│   ├── r6-matches-20240923.log
│   ├── r6-matches-20240924.log
│   ├── r6-matches-20240925.log
│   ├── r6-matches-20240926.log
│   ├── r6-matches-20240927.log
│   └── r6-matches-20240928.log
├── merge_logs.py
├── output
│   ├── operator_top100_20240928.txt
│   └── player_top10_20240928.txt
├── requirements.txt
├── utils.py
```

## Usage

### Run application in test mode

```bash
make test-all
```

The above make command will perform the following steps. See more details in Makefile.

- generate test log files in `input` folder
- merge all logs into `merged_matches.log` in the root folder of the project
- compute the top 100 average number of kills by operator on the last n(default to 7)days and write results into `output/operator_top100_YYYYMMDD.txt`.
  Each row has the following format:
  `operator_id|match_id1:avg_kills1,match_id2:avg_kills2,...,match_id100:avg_kills100`
- compute the top 10 matches in terms of number of kills by player on the last n(default to 7) days and write results into `output/player_top10_YYYYMMDD.txt`.
  Each row has the following format:
  `player_id|match_id1:nb_kills1,match_id2:nb_kills2,...,match_id10:nb_kills10`

### Run application with a cron job (ready to use for PROD env :D)

```bash
make schedule
```

The cron job will daily compute operator and player statistical results from `input` folder and persist results into `output` folder as the previous test mode.

## Author

- Lifeng Wan
- lifeng.wan.mtl@gmail.com
