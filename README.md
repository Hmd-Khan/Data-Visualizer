# Data Mining Website

A simple web application built with Streamlit to perform basic data mining tasks on CSV files.

## Features

- **CSV File Upload:** Upload a CSV file to analyze.
- **Data Preview:** Display the first few rows of the CSV file.
- **Data Summary:** Generate descriptive statistics using Pandas.
- **Data Filtering:** Filter data based on a selected column and value.
- **Data Visualization:** Create scatter plots from the filtered data using Matplotlib.

## Dependencies

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Matplotlib](https://matplotlib.org/)

## Getting Started

1. **Install Dependencies:**

   Open your terminal and run:
   ```shell
   pip install streamlit pandas matplotlib
   ```

2. **Run the Application:**

   Navigate to the project directory and execute:
   ```shell
   streamlit run dmweb.py
   ```

3. **Upload a CSV File:**

   Once the app is running, use the file uploader to select a CSV file for analysis. Use the provided options to preview, filter, and visualize your data.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
