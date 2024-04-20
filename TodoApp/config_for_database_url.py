from dotenv import load_dotenv
load_dotenv()

import os

SQLALCHEMY_DATABASE_URL=os.getenv('SQLALCHEMY_DATABASE_URL')