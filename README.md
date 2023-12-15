The future_transactions project is developed using Flask, Angular, and Docker. There are two services:
  1. data-processing-server: Processes the fixed width Input.txt using pandas and generates output.csv
     (Note: This process is a job that exits once it finishes processing the data, and sample output.csv is available under /future_transactions/future/transactions/output.csv)
  2. daily-summary-report-server: A Flask app that serves user's requests with 3 endpoints:
     - http://localhost:5000/v1/report/getFile: downloads output.csv to the Downloads folder
     - http://localhost:5000/v1/report/getData: returns future transaction data in JSON format
     - http://localhost:5000: servers an HTML page with angular script to call the /v1/report/getData endpoint to fetch and display the future transaction data in a table

How to run the application with Docker?
  1. Clone the code to the local machine, and make sure the docker desktop is installed on the user's machine
  2. Make sure the user has write access to **/opt** folder as **/opt/log** and **/opt/data/future_transactions** are mounted into the containers
  3. Go to /future_transactions/future/transactions, and run **docker-compose up -d --build**
  4. Open a new tab in the browser, hit the endpoints provided

How to run the application without Docker?
  1. Clone the code to the local machine, and make sure **/opt/log** and **/opt/data/future_transactions** are created on the local machine
  2. Go to /future_transactions, and run the following commands in order:
     - **python -m future_transactions.data_processing_server**
     - **python -m future_transactions.daily_summary_report_server**
  3. Open a new tab in the browser, hit the endpoints provided
