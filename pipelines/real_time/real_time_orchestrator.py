from prefect import flow, task
import subprocess
import time

@task
def run_bronze():
    print(f"Triggering Bronze Processing 🥉")
    """Fetch real-time BTC/USD price and volume from multiple sources."""
    subprocess.run(["python", "pipelines/real_time/bronze_ingestion.py"], check=True)

@task
def run_silver():
    print(f"Triggering Silver Processing 🥈")
    """Clean and process real-time BTC/USD data."""
    subprocess.run(["python", "pipelines/real_time/silver_processing.py"], check=True)

@task
def run_gold():
    print(f"Triggering Gold Aggregation 🥇")
    """Compute moving averages and store data in SQLite."""
    subprocess.run(["python", "pipelines/real_time/gold_aggregation.py"], check=True)

@flow
def real_time_pipeline():
    """Prefect Flow to orchestrate the real-time pipeline."""
    while True:
        print("🚀 Running Real-Time Pipeline...")
        run_bronze()
        run_silver()
        run_gold()

        # **Modify timing to fetch data multiple times per minute**
        time.sleep(120)  # **Run every 2 minutes instead of 30 seconds**
        
if __name__ == "__main__":
    real_time_pipeline()
