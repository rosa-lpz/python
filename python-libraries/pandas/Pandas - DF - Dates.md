## Dates and times
* **Google Colaboratory Notebook:** https://colab.research.google.com/drive/1O9D-MECDx33e23tWX0ES0ckxgHcrM6af


# Convert columns to datetime objects

This line uses the `pd.to_datetime()` function from the `pandas` library to convert the `datetime` column in the DataFrame `df` to actual `datetime` objects.
```python
df["datetime"] = pd.to_datetime(df["datetime"], format="%Y-%m-%d %H:%M:%S")
```

- `df["datetime"]`: Refers to the `datetime` column in the current DataFrame.
  
- `pd.to_datetime()`: Converts the string or object in the `datetime` column into a `datetime64` object (which allows for easier manipulation and sorting of date and time).
  
- `format="%Y-%m-%d %H:%M:%S"`: Specifies the exact format of the date and time in the column. It tells `pandas` how to interpret the strings in that column. Here's what the format means:
  
    - `%Y`: 4-digit year (e.g., `2023`)
    - `%m`: 2-digit month (e.g., `08` for August)
    - `%d`: 2-digit day (e.g., `05` for the 5th day)
    - `%H`: 2-digit hour in 24-hour format (e.g., `14` for 2 PM)
    - `%M`: 2-digit minute (e.g., `30` for 30 minutes past the hour)
    - `%S`: 2-digit second (e.g., `45` for 45 seconds past the minute)
# Extract
### Extract year

```python
# Use Datetime.strftime() Method to extract year
df['Year'] = df['InsertedDate'].dt.strftime('%Y')

# Using pandas.Series.dt.year()
df['Year'] = df['InsertedDate'].dt.year  

# Using pandas.DatetimeIndex() to extract year
df['year'] = pd.DatetimeIndex(df['InsertedDate']).year

# Use datetime.to_period() method to extract year
df['Month_Year'] = df['InsertedDate'].dt.to_period('y')

# Use DataFrame.apply() with lambda function and strftime()
df['Year'] = df['InsertedDate'].apply(lambda x: x.strftime('%Y')) 

# Use Pandas.to_datetime() and datetime.strftime() method
df['yyyy'] = pd.to_datetime(df['InsertedDate']).dt.strftime('%Y')


```

#### Using strftime()
```python
# Use DataFrame.apply() with lambda function and strftime()
df['Year'] = df['InsertedDate'].apply(lambda x: x.strftime('%Y')) 
```

#### Using dt.year
```python
# Using pandas.Series.dt.year()
df['Year'] = df['InsertedDate'].dt.year  

# This result in error
FB_Cont1['Anio'] = FB_Cont1['Fecha de publicación'].dt.year
```

### Extract month

```python
# Using pandas.Series.dt.year()
df['Mes'] = df['InsertedDate'].dt.month_name() 

```

Example 1
```python
FB_Cont_YM_Prom['Mes'] = FB_Cont_YM_Prom['Fecha_publicacion'].dt.month_name()

```




# **Reference**s

- [https://stackoverflow.com/questions/29370057/select-dataframe-rows-between-two-dates](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F29370057%2Fselect-dataframe-rows-between-two-dates)
- Data school: [https://youtu.be/yCgJGsg0Xa4](https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Fyoutu.be%2FyCgJGsg0Xa4)
- https://sparkbyexamples.com/pandas/pandas-extract-year-from-datetime/#:~:text=Pandas%20Extract%20Year%20using%20Datetime.&text=strftime()%20method%20takes%20the,to%20convert%20String%20to%20Datetime.
