FROM python:3.6
EXPOSE 5000
WORKDIR /future_transactions
RUN mkdir -p /future_transactions/future_transactions
COPY requirements.txt /future_transactions/future_transactions
RUN pip install -r /future_transactions/future_transactions/requirements.txt
COPY . /future_transactions/future_transactions
CMD python3 -m future_transactions.daily_summary_report_server