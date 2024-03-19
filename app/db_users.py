
import os
from supabase import create_client, Client, ClientOptions
from .models import User, Health_Metrics
from db_client import create_supabase_client

# Create a Supabase client
supabase = create_supabase_client()

def get_user(user_name: str):
    """
    Retrieves the user information for a given user name from the 'users' table.

    Args:
        user_name (str): The user name to search for.

    Returns:
        dict: A dictionary containing the user information retrieved from the 'users' table.
    """
    try:
        response = supabase.table('users').select("*").eq('user_name', user_name).execute()
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def get_user_id(user_name: str):
    """
    Retrieves the user ID for a given user name from the 'users' table.

    Args:
        user_name (str): The user name to search for.

    Returns:
        Any: The response from the database query.
    """
    try:
        response = supabase.table('users').select("id").eq('user_name', user_name).execute()
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_user(user: User):
    """
    Creates a new user in the database.

    Args:
        user (User): The user object containing the user's information.

    Returns:
        dict: A dictionary containing the result of the insert operation.
    """
    try:
        data, count = supabase.table('users').insert({"user_name": user.user_name,"email": user.email}).execute()
        return {"data": data, "count": count}
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def delete_user(user_name: str):
    """
    Deletes a user from the database.

    Args:
        user_name (str): The user name to delete.

    Returns:
        dict: A dictionary containing the result of the delete operation.
    """
    try:
        data, count = supabase.table('users').delete().eq('user_name', user_name).execute()
        return {"data": data, "count": count}
    except Exception as e:
        print(f"An error occurred: {e}")
        return None 