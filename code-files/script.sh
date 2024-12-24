#!/bin/bash

clients=(  200000 )
repeats=3
TIMEOUT=300
OUTPUT_DIR="output_logs"
RESULTS_FILE="results.csv"

# Create the output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Create the results file and add the header
echo "clients,repeat,start_time,end_time,duration,messages_sent,messages_received" > $RESULTS_FILE

for c in "${clients[@]}"; do
    for ((i=1; i<=repeats; i++)); do
        echo "Running experiment with $c clients, repeat $i"
        start_time=$(date +%s)
        messages_sent=0
        messages_received=0

        for ((j=1; j<=c; j++)); do
            echo "Starting client $j for $c clients, repeat $i"
            python3 test_client2.py > "${OUTPUT_DIR}/output_${c}_clients_repeat_${i}_client_${j}.txt" 2>&1 &
        done

        sleep ${TIMEOUT}  # Run for the specified timeout
        wait

        end_time=$(date +%s)
        duration=$((end_time - start_time))

        # Collect messages sent and received from the logs
        for ((j=1; j<=c; j++)); do
            sent=$(grep -o "Messages sent: [0-9]*" "${OUTPUT_DIR}/output_${c}_clients_repeat_${i}_client_${j}.txt" | awk '{sum += $3} END {print sum}')
            received=$(grep -o "Messages received: [0-9]*" "${OUTPUT_DIR}/output_${c}_clients_repeat_${i}_client_${j}.txt" | awk '{sum += $3} END {print sum}')
            messages_sent=$((messages_sent + sent))
            messages_received=$((messages_received + received))
        done

        # Log the results to the CSV file
        echo "$c,$i,$start_time,$end_time,$duration,$messages_sent,$messages_received" >> $RESULTS_FILE
    done
done