# Filters

1. **Logical operators.**
2. **Isin.**
3. **Multiple logical operators.**
4. **Str accessor.**
5. **Tilde (~).**
6. **Query.**
7. **Nlargest and nsmallest.**
8. **Loc and iloc.**

### Filter Rows using logical operators

#### **Syntaxis**
```python
# Filter rows by selecting certain 'string'
df2=df[df.column_name == 'string']

df2
```


#### Example 1
* Notebook: https://colab.research.google.com/drive/1PreIydqOEcwFpz9NFIYEObF1MHKNl-gU#scrollTo=drcuBTWAFzQW

Table

```cmd
Courses	Fee	Duration
1	PySpark	25000	50days
3	Java	24000	60days
4	PySpark	26000	35days
5	PHP	27000	30days
```


Code
```python
df2=technologies_df[technologies_df.Courses == 'PySpark']

# or
df2=technologies_df[technologies_df['Courses'] == 'PySpark']
df2=technologies_df[technologies_df['Courses'] != 'PySpark']
```

Output
```cmd
     Courses	Fee	   Duration
1	PySpark	   25000	50days
4	PySpark	   26000	35days
```


#### Example 2
* Example 2 - Select rows by multiple conditions
* https://note.nkmk.me/en/python-pandas-multiple-conditions/
### Filter Rows using "is in" method

**Syntaxis** 

```python
# Use the isin method to filter rows
filtered_df = df[df['Column1'].isin(target_strings)]
# or
filtered_df = df[df.Column1.isin(target_strings)]
```

**Example 1**

```python
import pandas as pd

# Sample DataFrame
data = {
    'Column1': ['apple', 'banana', 'orange', 'apple', 'grape'],
    'Column2': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Define the two string elements you want to filter
target_strings = ['apple', 'orange']

# Use the isin method to filter rows
filtered_df = df[df['Column1'].isin(target_strings)]

# Display the filtered DataFrame
print(filtered_df)

```

Example 2 - Select rows by multiple conditions
* https://note.nkmk.me/en/python-pandas-multiple-conditions/

### Query
https://www.listendata.com/2020/12/how-to-use-variable-in-query-in-pandas.html

### References
* https://builtin.com/data-science/pandas-filter
* https://towardsdatascience.com/8-ways-to-filter-a-pandas-dataframe-by-a-partial-string-or-pattern-49f43279c50f
* https://colab.research.google.com/corgiredirector?site=https%3A%2F%2Ftowardsdatascience.com%2F8-ways-to-filter-a-pandas-dataframe-by-a-partial-string-or-pattern-49f43279c50f
* Select rows by multiple conditions: https://note.nkmk.me/en/python-pandas-multiple-conditions/
* 10 ways to filter pandas dataframe: https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html
