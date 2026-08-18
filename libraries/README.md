# Python Libraries 

## Content
## Math & Data Analysis
* [NumPy](numpy)
* [Pandas](/pandas)

## Data visualization
* [Matplotlib](matplotlib)
* [Bokeh](bokeh)
* [Plotly](plotly)
* [Seaborn](seaborn)

## Machine Learning & Deep Learning
* [Scikit-learn](scikit-learn)
* [PyTorch](pytorch)
* [TensorFlow](tensorflow)

## Big Data Processing and Distributed Computing
* [PySpark](https://github.com/rosa-lpz/pyspark/tree/main)


Python’s extensive ecosystem is divided into **Core Standard Libraries** (built right into Python) and **Popular Third-Party Libraries** (installed via `pip` for specialized tasks like data science, web development, and AI).


## Essential Standard Libraries (Built-In)

These libraries come pre-installed with Python and don't require external installation.

| Library | Category | Description |
| --- | --- | --- |
| **os** / **sys** | System Operations | Provides tools to interact with the operating system, navigate directories, handle file paths, and manage system arguments. |
| **json** | Data Interoperability | Used to parse, read, write, and manipulate JSON data formats. |
| **datetime** | Time Management | Supplies classes for manipulating dates, times, and calculating time deltas. |
| **math** | Core Mathematics | Provides access to basic mathematical functions defined by the C standard (e.g., trigonometry, logs, factorials). |
| **re** | String Processing | Enables the use of Regular Expressions for advanced string matching, searching, and text parsing. |




## Data Science & Machine Learning (Third-Party)

These libraries form the backbone of modern data engineering, statistical analysis, and artificial intelligence.

| Library | Category | Description |
| --- | --- | --- |
| **NumPy** | Numerical Computing | Provides support for large, multi-dimensional arrays and matrices, along with a collection of high-level mathematical functions to operate on them. |
| **Pandas** | Data Manipulation | Offers powerful data structures like DataFrames to clean, filter, reshape, and analyze structured data (similar to Excel or SQL tables). |
| **SciPy** | Scientific Computing | Built on NumPy; used for advanced scientific and technical computing tasks like optimization, integration, and linear algebra. |
| **Scikit-learn** | Machine Learning | The go-to library for traditional machine learning algorithms (regression, classification, clustering) and data preprocessing. |
| **TensorFlow** | Deep Learning | An open-source framework developed by Google for building, training, and deploying deep neural networks. |
| **PyTorch** | Deep Learning | Developed by Meta; a highly flexible, Pythonic framework preferred by researchers for deep learning and AI prototyping. |

---

## Data Visualization (Third-Party)

Tools used to turn raw data into charts, graphs, and interactive dashboards.

| Library | Category | Description |
| --- | --- | --- |
| **Matplotlib** | Static Visualization | The foundational plotting library in Python. Highly customizable, used to create line graphs, bar charts, histograms, etc. |
| **Seaborn** | Statistical Plots | Built on top of Matplotlib; provides a high-level, cleaner interface for drawing attractive and informative statistical graphics. |
| **Plotly** | Interactive Charts | Used for creating dynamic, web-ready interactive plots, dashboards, and 3D visualizations. |

---

## Web Development & APIs (Third-Party)

Frameworks used to build backend servers, websites, and RESTful APIs.

| Library | Category | Description |
| --- | --- | --- |
| **Django** | Full-Stack Web Framework | A "batteries-included" framework for building large, robust web applications. Includes a built-in admin panel and ORM. |
| **Flask** | Micro-Web Framework | Lightweight and minimalist framework. Ideal for smaller applications, microservices, and rapid prototyping. |
| **FastAPI** | Modern API Framework | A modern, fast (high-performance) framework for building APIs with Python 3.8+ based on standard Python type hints. |

---



## Web Scraping & Automation (Third-Party)

Used for extracting data from websites and interacting with web services.

| Library | Category | Description |
| --- | --- | --- |
| **Requests** | HTTP Networking | Simplifies sending HTTP requests to interact with web pages and external APIs. "HTTP for Humans." |
| **BeautifulSoup** | HTML/XML Parsing | Parses HTML and XML documents to extract structured data from web pages during web scraping. |
| **Scrapy** | Web Crawling | An architectural framework used for large-scale web scraping and data extraction tasks. |

---



Here is an expanded list covering more specialized domains in Python, including Game Development, GUI Design, DevOps/Automation, and Natural Language Processing (NLP).

---

## Natural Language Processing & AI (Third-Party)

These libraries are dedicated to text processing, language modeling, and understanding human language.

| Library | Category | Description |
| --- | --- | --- |
| **Hugging Face (Transformers)** | Advanced AI / NLP | Provides thousands of pre-trained models to perform tasks on texts such as classification, information extraction, and summarization (includes access to LLMs). |
| **NLTK** (Natural Language Toolkit) | Traditional NLP | A foundational library for working with human language data, excellent for tokenization, stemming, tagging, and parsing text. |
| **SpaCy** | Industrial NLP | Built specifically for production use; incredibly fast and efficient at Named Entity Recognition (NER), part-of-speech tagging, and dependency parsing. |

---

## Game Development & GUI (Third-Party & Built-In)

Used for creating desktop applications, user interfaces, and 2D/3D video games.

| Library | Category | Description |
| --- | --- | --- |
| **Pygame** | Game Development | A set of Python modules designed for writing video games, handling graphics, sound, and physics. |
| **Tkinter** | GUI (Built-In) | Python's standard, built-in library for creating basic desktop Graphical User Interfaces (GUIs) quickly. |
| **PyQt** / **PySide** | Advanced GUI | Python bindings for the Qt framework, used to build highly professional, modern, and cross-platform desktop applications. |

---

## Devops, Automation & Cloud (Third-Party)

Tools designed for system administrators and developers to automate infrastructure, cloud services, and scripting.

| Library | Category | Description |
| --- | --- | --- |
| **Boto3** | Cloud (AWS) | The official Amazon Web Services (AWS) SDK for Python, allowing developers to write software that uses services like Amazon S3 and Amazon EC2. |
| **Paramiko** | Network Automation | A library that implements the SSHv2 protocol, allowing you to securely connect to remote servers and run commands. |
| **Fabric** | System Deployment | A high-level library designed to execute shell commands remotely over SSH, yielding a streamlined tool for application deployment or systems administration tasks. |

---

## Testing & Quality Assurance (Third-Party & Built-In)

Libraries used to write unit tests, functional tests, and ensure code reliability.

| Library | Category | Description |
| --- | --- | --- |
| **unittest** | Testing (Built-In) | Python's native unit testing framework, inspired by Java's JUnit, supporting test automation and aggregations of tests. |
| **pytest** | Testing | A highly popular, feature-rich alternative to `unittest` that makes it easy to write small, readable tests, yet scales to support complex functional testing. |
| **Selenium** | Browser Automation | Used to automate web browser interactions, widely adopted for testing web applications or automating repetitive browser tasks. |

---

## Advanced Utilities (Built-In)

Powerful modules hidden within Python's standard library that elevate data handling and performance.

| Library | Category | Description |
| --- | --- | --- |
| **collections** | Data Structures | Provides specialized container datatypes providing alternatives to Python’s general-purpose built-ins (e.g., `Counter`, `defaultdict`, `namedtuple`). |
| **itertools** | Performance | A collection of tools for handling iterators. Great for creating efficient loops, permutations, combinations, and infinite sequences. |
| **asyncio** | Concurrency | A library to write concurrent code using the `async`/`await` syntax, perfect for handling high-performance network and web servers. |