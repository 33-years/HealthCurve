
import os
from dotenv import load_dotenv
from supabase import create_client, Client, ClientOptions

def create_supabase_client():
    # Load environment variables from the .env file
    if os.path.exists(".env"):
        load_dotenv(dotenv_path=".env")

    # Get the Supabase URL and key from environment variables
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")

    # Create a Supabase client
    supabase: Client = create_client(url, key,
        options=ClientOptions(
            postgrest_client_timeout=10,
            storage_client_timeout=10
        ))
    return supabase
