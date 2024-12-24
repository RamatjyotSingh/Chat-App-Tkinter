import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV data
results2 = pd.read_csv('results2.csv')
results3 = pd.read_csv('results3.csv')

# Combine the results
all_results = pd.concat([ results2, results3])

# Calculate messages per second
all_results['messages_sent_per_sec'] = all_results['messages_sent'] / all_results['duration']
all_results['messages_received_per_sec'] = all_results['messages_received'] / all_results['duration']

# Boxplot for messages sent per second
plt.figure(figsize=(12, 6))
sns.boxplot(x='clients', y='messages_sent_per_sec', data=all_results)
plt.title('Messages Sent Per Second by Number of Clients')
plt.xlabel('Number of Clients')
plt.ylabel('Messages Sent Per Second')
plt.savefig('messages_sent_per_second_boxplot.png')
plt.show()

# Boxplot for messages received per second
plt.figure(figsize=(12, 6))
sns.boxplot(x='clients', y='messages_received_per_sec', data=all_results)
plt.title('Messages Received Per Second by Number of Clients')
plt.xlabel('Number of Clients')
plt.ylabel('Messages Received Per Second')
plt.savefig('messages_received_per_second_boxplot.png')
plt.show()

# Line plot for messages sent and received per second
plt.figure(figsize=(12, 6))
sns.lineplot(x='clients', y='messages_sent_per_sec', data=all_results, marker='o', label='Messages Sent Per Second')
sns.lineplot(x='clients', y='messages_received_per_sec', data=all_results, marker='o', label='Messages Received Per Second')
plt.title('Messages Sent and Received Per Second by Number of Clients')
plt.xlabel('Number of Clients')
plt.ylabel('Messages Per Second')
plt.legend()
plt.savefig('messages_per_second_lineplot.png')
plt.show()