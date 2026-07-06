# Python Environments

## Python environments with venv

### Windows

```cmd
python get-pip.py
python -m pip --version
py -m ensurepip --default-pip

python -m pip install

[notice] A new release of pip is available: 23.2.1 -> 25.3
[notice] To update, run: C:\<directory_path>\Python\Python312\python.exe -m pip install --upgrade pip

```



````cmd
python -m pip install --upgrade pip
python -m pip --version
````



For install packages 

```
python -m pip install requests
```

Create the environment
```cmd
py -m venv venv
```


### Linux

Install venv
````
sudo apt install python3-venv python3-pip
````

Check
````bash
python3 -m ensurepip --default-pip
````

Create the environment
````bash
python3 -m venv venv
source venv/bin/activate
````


## Python environments with Anaconda

Conda allows you to create separate environments, each containing  their own files, packages, and package dependencies. The contents of  each environment do not interact with each other.

The most basic way to create a new environment is with the following command:

```
conda create --name <env-name>
```

To add packages while creating an environment, specify them after the environment name:

```
conda create --name <env_name> python numpy pandas
conda create --name <env_name> python==3.11 pandas==2.2.2 seaborn==0.13.2 matplotlib==3.8.4
conda activate <env_name>

conda create --name envpython311 python==3.11 pandas==2.2.2 seaborn==0.13.2 matplotlib==3.8.4
conda activate envpython311

```

For more information on working with environments, see [Managing environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).



### List of conda environments

```
conda info --envs
```

output

````bash
conda environments:

   base           /home/username/Anaconda3
   myenvironment   * /home/username/Anaconda3/envs/myenvironment
````

# References
* https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/
