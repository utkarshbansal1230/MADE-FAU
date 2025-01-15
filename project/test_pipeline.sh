#!/bin/bash

# Exit on any command failure
set -e

echo "Running the test"

# Define the expected output database file
DB_FILE="../data/air_quality.db"

# Clean up previous output
if [ -f "$DB_FILE" ]; then
    echo "Removing previous database file..."
    rm "$DB_FILE"
fi

# Execute the pipeline
echo "Executing the data pipeline..."
python3 pipeline.py

# Validate the output
if [ -f "$DB_FILE" ]; then
    echo "System test passed: Database file created at $DB_FILE"
else
    echo "System test failed: Database file not created!"
    exit 1
fi
