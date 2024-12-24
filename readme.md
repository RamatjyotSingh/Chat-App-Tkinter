# Chat Application with Performance Analysis

This repository contains a simple chat application built with a client-server architecture, alongside scripts and tools for performance testing and analysis. The client features a graphical user interface (GUI) built using Tkinter.

---

## Requirements

### Application

- **Python 3.x**
- **Tkinter** (usually included with Python)
- **Socket library** (usually included with Python)

### Performance Analysis

- **psutil** (for server metrics)
- **pandas** (for data analysis)
- **matplotlib** (for plotting)
- **seaborn** (for advanced plotting)

---

## Starting the Application

### Server

1. Navigate to the directory containing the `server.py` script.
2. Run the server script:

   ```bash
   python server.py
   ```

   By default, the server starts on `localhost` at port `50017`.

### Client

1. Navigate to the directory containing the `client.py` script.
2. Run the client script:

   ```bash
   python client.py
   ```

### Command-Line Arguments
You can specify the server host and port using command-line arguments:

```bash
python client.py --host <server_host> --port <server_port>
```

---

## Performance Testing

### Running the Tests

1. Navigate to the directory containing the performance test scripts.
2. Execute the test script:

   ```bash
   ./script.sh
   ```

   This script runs the client multiple times, collects performance data, and saves the results in `results.csv`.

### Analyzing the Results

1. Use the `analysis.py` script to analyze client-side performance:

   ```bash
   python analysis.py
   ```

2. Use the `server-analysis.py` script to visualize server performance metrics:

   ```bash
   python server-analysis.py
   ```

---

## Results

The results of the performance tests are saved in `results.csv`. Analysis scripts generate various plots to visualize key performance metrics, such as:

- **Messages Sent Per Second by Number of Clients**
- **Messages Received Per Second by Number of Clients**
- **Total Messages Sent and Received Per Second**
- **Messages Sent and Received Per Second by Number of Clients**

### Example Insights

1. **Performance Trends**: Running more clients increases the average number of messages sent per second.
2. **Server Load**: Performance degradation appears linear, suggesting the server can handle a moderate increase in clients without a significant drop in performance.
3. **Optimization**: Further optimization and scaling strategies may be needed to efficiently manage a larger number of clients.

---

## Graphs

Analysis scripts generate detailed visualizations, such as:

- **Messages Sent/Received Per Second**
- **Performance by Client Count**


---

## Author

**Ramatjyot Singh**

---

