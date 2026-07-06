# Python environment variables



## Dotenv

```python
# Import the necessary module
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')

# Example usage
print(f'SECRET_KEY: {SECRET_KEY}')
print(f'DATABASE_URL: {DATABASE_URL}')
```



# References

* https://www.geeksforgeeks.org/python/using-python-environment-variables-with-python-dotenv/

## Videos

* How to Use Python Environment Variables: https://youtu.be/sOwG0bw0RNU

