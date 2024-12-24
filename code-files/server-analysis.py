import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Combined data for visualization
data = {
    'Metric': ['Messages Sent', 'Messages Received', 'Messages Sent Per Second', 'Messages Received Per Second'],
    'Combined': [87255899, 3363203, 19630.17, 365.32]
}

df = pd.DataFrame(data)

# Set the style
sns.set(style="whitegrid")

# Bar chart for total messages sent and received
plt.figure(figsize=(12, 8))
bar_plot = sns.barplot(x='Metric', y='Combined', data=df, palette='viridis')
bar_plot.set_title('Total Messages Sent and Received', fontsize=16)
bar_plot.set_ylabel('Count', fontsize=14)
bar_plot.set_xlabel('Metric', fontsize=14)
bar_plot.set_xticklabels(bar_plot.get_xticklabels(), rotation=45, ha='right', fontsize=12)
for index, value in enumerate(df['Combined']):
    bar_plot.text(index, value + 0.05 * value, f'{value:,}', ha='center', fontsize=12)
plt.tight_layout()
plt.savefig('total_messages_sent_received_combined.png')
plt.show()

# Line plot for messages sent and received per second
plt.figure(figsize=(12, 8))
line_plot = sns.lineplot(x='Metric', y='Combined', data=df.loc[2:], marker='o', palette='viridis')
line_plot.set_title('Messages Sent and Received Per Second', fontsize=16)
line_plot.set_ylabel('Messages Per Second', fontsize=14)
line_plot.set_xlabel('Metric', fontsize=14)
line_plot.set_xticklabels(line_plot.get_xticklabels(), rotation=45, ha='right', fontsize=12)
for index, value in enumerate(df['Combined'][2:]):
    line_plot.text(index, value + 0.05 * value, f'{value:,.2f}', ha='center', fontsize=12)
plt.tight_layout()
plt.savefig('messages_per_second_combined.png')
plt.show()