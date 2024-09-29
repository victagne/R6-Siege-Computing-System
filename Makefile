.PHONY: clean generate-data merge-data compute_operator compute_player schedule

# Clean input and output directories and the merged log file, use this command with caution in production environment
clean:
	rm -rf input output merged_matches.log

# Generating R6 matches data, passing necessary parameters
generate-data:
	python3.11 generate_matches.py --num_rows 1000000 --max_operator_id 36 --max_kills 1500 --days 7

# Merge recent log files
merge-data:
	python3.11 merge_logs.py

# Computing operator stats
compute_operator:
	python3.11 compute_operator_stats.py

# Computing player stats
compute_player:
	python3.11 compute_player_stats.py

# Execute all testing steps in sequence: clean, generate-data, merge-data, and compute operator and player stats
test-all: clean generate-data merge-data compute_operator compute_player

# Schedule a daily execution with crontab
current_dir := $(CURDIR)
schedule:
	@{ \
		echo "0 1 * * * (cd $(current_dir) && make merge-data && make compute_operator && make compute_player)" | crontab -; \
		echo "Cron job scheduled to run daily at 1 AM."; \
	}