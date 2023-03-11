import os
import pymongo
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get MongoDB Atlas credentials from environment variables
mongo_username = os.getenv("MONGODB_ATLAS_USERNAME")
mongo_password = os.getenv("MONGODB_ATLAS_PASSWORD")
mongo_cluster_url = os.getenv("MONGODB_ATLAS_URL")

# Create a MongoClient and connect to the MongoDB Atlas cluster
client = pymongo.MongoClient(
    "mongodb+srv://" + mongo_username + ":" + mongo_password + "@" + mongo_cluster_url + "/test?retryWrites=true&w=majority"
)

# Get a reference to the database
db = client.test

# Print the number of documents in the "users" collection
print(db.users.count_documents({}))