# R6 Siege Computing System - Data Processing
> Rainbow Six Siege (R6 Siege) is a first-person shooter game, in which players use many different operators from the Rainbow team (composed of the world's leading counter- terrorism and special forces units). Different operators have different weapons and gadgets. Matches are conducted in a 5v5 manner, with each player only receiving one life per round. Players can pick any operator from any unit before a round starts, possibly the same.
Firstly, in order to improve game balance, we would like to analyze operators usage by checking the top 100 average number of kills they do in matches.
Secondly, in the context of a CRM campaign, we would like to send to each player the top 10 of their matches in terms of number of kills.

## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Contact](#contact)

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
  The above make command will
- generate test log files in `input` folder
- merge all logs into `merged_matches.log` in the root folder of the project
- compute the top 100 average number of kills by operator on the last 7 days and write results into `output/operator_top100_YYYYMMDD.txt`.
  Each row has the following format:
  `operator_id|match_id1:avg_kills1,match_id2:avg_kills2,...,match_id100:avg_kills100`
- compute the top 10 matches in terms of number of kills by player on the last 7 days and write results into `output/player_top10_YYYYMMDD.txt`.
  Each row has the following format: 
  `player_id|match_id1:nb_kills1,match_id2:nb_kills2,...,match_id10:nb_kills10`

### Run application with a cron job (ready to use in the product :D)
```bash
make schedule
```
  The cron job will daily compute operator and player statistical results from `input` folder and persist results into `output` as the previous test mode.

## Contact
- Lifeng Wan
- lifeng.wan.mtl@gmail.com