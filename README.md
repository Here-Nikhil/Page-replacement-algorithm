A modern, interactive GUI application built with PyQt5 and Matplotlib to simulate and analyze various page replacement algorithms used in operating systems. This tool allows users to input reference strings and frame sizes, visualize algorithm performance, and identify the most efficient scheduling strategy.

Features
Supported Algorithms: FIFO, LRU, Optimal, Second Chance, and Clock
Interactive GUI: Clean interface with real-time input validation
Theme Support: Toggle between light and dark modes
Visualization: Bar graph comparing page faults across algorithms
Detailed Results: Tabular output with reference string and frame size information
Progress Tracking: Visual progress bar during simulation
Error Handling: User-friendly error messages for invalid inputs
Prerequisites
Python 3.7+
Required Python packages:
PyQt5
NumPy
Matplotlib

Input Data:

Reference String: Enter space-separated integers (e.g., 1 2 3 4 2 1 5)
Frame Size: Enter a positive integer (default is 3 if left blank)
Algorithm Selection: Choose "All Algorithms" or a specific algorithm from the dropdown
Run Simulation: Click "Run Simulation" to process the input and view results.

View Results:

Detailed output appears in the text area
Bar graph visualizes page faults for each algorithm
Most efficient algorithm is highlighted

Toggle Theme: Check/uncheck "Dark Mode" to switch between light and dark themes.

Example
Input:

Reference String: 7 0 1 2 0 3 0 4 2 1 0 3
Frame Size: 3
Algorithm: All Algorithms
Output:

Table showing page faults for each algorithm
Graph with bars colored according to the theme
Highlighted "Optimal" algorithm as most efficient (if implemented)
