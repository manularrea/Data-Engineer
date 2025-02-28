from prefect import flow, task
from prefect.server.schemas.schedules import CronSchedule
import subprocess

@task
def run_bronze():
    print(f"Triggering Bronze Processing 🥉")
    """Ingest historical batch data (hourly snapshot)."""
    subprocess.run(["python", "pipelines/batch/bronze_ingestion.py"], check=True)

@task
def run_silver():
    print(f"Triggering Silver Processing 🥈")
    """Clean and transform historical batch data."""
    subprocess.run(["python", "pipelines/batch/silver_processing.py"], check=True)

@task
def run_gold():
    print(f"Triggering Gold Aggregation 🥇")
    """Aggregate batch data and store in SQLite."""
    subprocess.run(["python", "pipelines/batch/gold_aggregation.py"], check=True)

@flow(name="Batch Pipeline")  # **Runs every hour**
def batch_pipeline():
    """Prefect Flow to orchestrate the batch pipeline (hourly)."""
    print("🚀 Running Batch Pipeline...")
    run_bronze()
    run_silver()
    run_gold()
    print("✅ Batch Pipeline Completed!")

if __name__ == "__main__":
    batch_pipeline()
