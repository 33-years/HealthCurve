from datetime import date
import os
from db_client import create_supabase_client
from models import User, Insert_Metrics, Upsert_Metrics
from typing import List


# Create a Supabase client
supabase = create_supabase_client()

def Create_User_Metrics(metrics: List[Insert_Metrics]):
    """
    Inserts a set of health metric data into the database.

    Args:
    metrics (List[Insert_Metrics]): The list of health metric data to insert.

    Returns:
    The number of data inserted.

    Raises:
    ValueError: If metrics is empty.
    Exception: If the database operation fails or returns an error.
    """

    # Validate input: if metrics is empty, raise ValueError
    if not metrics:
        raise ValueError("No data provided")

    # Prepare the data to insert
    data_to_insert = [
        {"user_id": metric.user_id, "metric_date": metric.metric_date,"metric_type": metric.metric_type, "metric_value": metric.metric_value}
        for metric in metrics
    ]

    # Try to insert the data into the database
    try:
        result = supabase.table('health_metrics').insert(data_to_insert).execute()
    except Exception as e:
        # If the database operation fails, raise an exception
        raise Exception("Database operation failed") from e
    #print(result)
    return result

from typing import List

def Upsert_User_Metrics(upsert_metrics: List[Upsert_Metrics]):
    """
    Upserts user metrics into the 'health_metrics' table in the database.

    Args:
        upsert_metrics (List[Upsert_Metrics]): A list of Upsert_Metrics objects containing the metrics to be upserted.

    Returns:
        The result of the upsert operation.

    Raises:
        ValueError: If no data is provided.
        Exception: If the database operation fails.
    """
    if not upsert_metrics:
        raise ValueError("No data provided")
    
    date_to_insert = [
        {"id": metric.id, "user_id": metric.user_id, "metric_date": metric.metric_date, "metric_type": metric.metric_type, "metric_value": metric.metric_value} 
        for metric in upsert_metrics
    ]

    try:
        result = supabase.table('health_metrics').upsert(date_to_insert).execute()
    except Exception as e:
        raise Exception("Database operation failed") from e
    #print(result)
    return result


def Delete_User_Metrics(id:str):
    """
    Deletes a user's health metrics from the database.

    Args:
        id (str): The ID of the  metric that should be deleted.

    Returns:
        dict: The result of the delete operation.

    Raises:
        Exception: If the database operation fails.
    """
    try:
        result = supabase.table('health_metrics').delete().eq('id', id).execute()
    except Exception as e:
        raise Exception("Database operation failed") from e
    #print(result)
    return result

# if __name__ == "__main__":
    # Test Code block to be executed when the script is run as the main module
    # testuser_metrics = [
    #     Insert_Metrics(user_id="5b0bba2d-d9d4-49ec-bb64-db5c0134543d", metric_date="2022-01-01", metric_type="weight", metric_value=70.0),
    #     Insert_Metrics(user_id="5b0bba2d-d9d4-49ec-bb64-db5c0134543d", metric_date="2022-01-02", metric_type="height", metric_value=180.0),
    #     Insert_Metrics(user_id="5b0bba2d-d9d4-49ec-bb64-db5c0134543d", metric_date="2022-01-03", metric_type="steps", metric_value=10000.0)
    # ]
    # Create_User_Metrics(testuser_metrics)

    # testuser_metrics2 = [
    #     Upsert_Metrics(id="1316f3d5-cd83-42dc-a8e2-9a475be6da54", user_id="5b0bba2d-d9d4-49ec-bb64-db5c0134543d",metric_date="2023-01-01", metric_type="weight", metric_value=72.0),
    #     Upsert_Metrics(id="fdd3bd77-465a-40fc-8963-12f1f42ef70b", user_id="5b0bba2d-d9d4-49ec-bb64-db5c0134543d",metric_date="2022-01-02", metric_type="height", metric_value=181.0),
    #     Upsert_Metrics(id="488054be-0ee0-4cdb-9c06-9a3f64afd9a5", user_id="5b0bba2d-d9d4-49ec-bb64-db5c0134543d",metric_date="2023-01-03", metric_type="miles", metric_value=10000.0)
    # ]
    # Upsert_User_Metrics(testuser_metrics2)

    # test_id = "3adeacef-bad1-4f91-9916-f489fd227e4c"
    # Delete_User_Metrics(test_id)
