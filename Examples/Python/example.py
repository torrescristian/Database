import couchdb

# Configuration for CouchDB server
COUCHDB_URL = 'https://admin:password@database-production.up.railway.app/'
DB_NAME = 'test'  # Change this to your database name

# Connect to the CouchDB server
server = couchdb.Server(COUCHDB_URL)

# Create or get a reference to the database
try:
    db = server[DB_NAME]
except couchdb.http.ResourceNotFound:
    db = server.create(DB_NAME)

# Sample document data
sample_doc = {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "age": 30
}

# Insert a document
doc_id, doc_rev = db.save(sample_doc)
print(f"Document inserted with ID: {doc_id}")

# Retrieve the inserted document
retrieved_doc = db.get(doc_id)
print("Retrieved Document:")
print(retrieved_doc)

# Update the document
retrieved_doc["age"] = 31
db.save(retrieved_doc)
print("Updated Document:")
print(db.get(doc_id))

# Delete the document
db.delete(retrieved_doc)
print("Document deleted.")
