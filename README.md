# Apron_SQL
Automating Data Aggregation Workflow on Brightics Platform

In this project, I developed a data aggregation workflow using Brightics — an internal data analytics platform. The goal was to automate the process of collecting and processing flight data, and then summarizing it for better decision-making. Here's a step-by-step breakdown of the process:

Data Retrieval
The data is pulled directly from an internal corporate database, referred to as BDPDPR (Brightics Database for Data Processing and Reporting). While I cannot share the database directly, the code can be executed within the Brightics platform, where it automatically connects to the database. In this GitHub example, I’ve replaced the direct database query with a mock dataset (a CSV file), which simulates the kind of data that Brightics would fetch.

Data Transformation
After retrieving the raw data, the next step is data transformation. In this example, I mapped flight terminal codes (like P01, P02, etc.) to a more user-friendly format, such as T1, T2, or CGO (for cargo terminals). This transformation is done using a simple Python function, which is applied to every row of data.

Aggregation
The transformed data is then grouped by terminal codes and counted. This means that for each terminal, the number of flights is calculated. After the initial count, I added an additional row that totals the number of flights across all terminals. This gives a summary of the data in a clean, aggregated format.

Data Presentation
Finally, the result is presented in a DataFrame (a table format) using Python's pandas library. The data can then be easily used for further analysis or visualized using tools like Power BI or Tableau.

How the Code Works

Here’s a high-level overview of the code and what it does:

Step 1: It reads a CSV file with flight data, simulating how Brightics would connect to and fetch data from the internal database (BDPDPR).

Step 2: A Python function (map_terminal_to_code) is used to transform terminal codes from raw data into more readable codes like T1 or CGO.

Step 3: The data is grouped by terminal code, and the number of flights per terminal is counted.

Step 4: The counts are aggregated, and a total row is added to summarize the data.

Step 5: Finally, the processed data is printed, showing the count of flights for each terminal and the total count.

How You Can Use It

Simulated Data: You can replace the mock dataset (mock_flight_data.csv) with your actual data from Brightics or any other database.

Customization: If you have different terminal codes or need to adjust the aggregation, you can modify the function that maps terminal codes or tweak how the data is grouped.

Automated Workflow: In a production environment, this same code can be run on the Brightics platform, where the data is automatically retrieved from the corporate database (BDPDPR), transformed, aggregated, and displayed.

Key Takeaways

No need for manual data entry: The workflow automates data aggregation, reducing the chance for human error and improving efficiency.

Data transformation: Mapping raw data to useful formats allows for better insights and clearer reporting.

Scalable: The workflow is scalable and can handle larger datasets, making it suitable for enterprise-level applications.

Conclusion

In this project, I’ve demonstrated how to automate the process of pulling, transforming, and aggregating flight data. Although the actual data comes from an internal database, this mock version simulates how you would use Brightics to handle such tasks. This saves time, ensures accuracy, and allows for more data-driven decision-making.
