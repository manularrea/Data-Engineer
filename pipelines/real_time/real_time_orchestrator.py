from prefect import flow, task
import subprocess
import time

@task(retries=3, retry_delay_seconds=5)
def run_bronze():
    print(f"Triggering Bronze Processing 🥉")
    """Fetch real-time BTC/USD price and volume from multiple sources."""
    subprocess.run(["python", "pipelines/real_time/bronze_ingestion.py"], check=True)

@task(retries=3, retry_delay_seconds=5)
def run_silver():
    print(f"Triggering Silver Processing 🥈")
    """Clean and process real-time BTC/USD data."""
    subprocess.run(["python", "pipelines/real_time/silver_processing.py"], check=True)

@task(retries=3, retry_delay_seconds=5)
def run_gold():
    print(f"Triggering Gold Aggregation 🥇")
    """Compute moving averages and store data in SQLite."""
    subprocess.run(["python", "pipelines/real_time/gold_aggregation.py"], check=True)

@flow(name="Real-Time Pipeline")
def real_time_pipeline():
    """Prefect Flow to orchestrate the real-time pipeline."""
    print("🚀 Running Real-Time Pipeline...")
    run_bronze()
    run_silver()
    run_gold()
    print("✅ Real-Time Pipeline Completed!")

if __name__ == "__main__":
    real_time_pipeline()