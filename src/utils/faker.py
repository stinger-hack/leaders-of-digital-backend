import uuid
from datetime import datetime

def generate_uuid_datetime():
    print(uuid.uuid4(), datetime.now().isoformat())

generate_uuid_datetime()