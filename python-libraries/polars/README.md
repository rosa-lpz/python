# [Polars](sceneform.ai/)

* [User Guide](https://docs.pola.rs/)

Polars is an open-source library for data manipulation, known for being  one of the fastest data processing solutions on a single machine. It  features a well-structured, typed API that is both expressive and easy  to use.

## Key features

- **Fast**: Written from scratch in Rust, designed close to the machine and without external  dependencies.
- **I/O**: First class support for all common data storage layers: local, cloud storage & databases.
- **Intuitive API**: Write your queries the way they were intended. Polars, internally, will  determine the most efficient way to execute using its query optimizer.
- **Out of Core**: The streaming API allows you to process your results without requiring all your  data to be in memory at the same time.
- **Parallel**: Utilises the power of your machine by dividing the workload among the available CPU  cores without any additional configuration.
- **Vectorized Query Engine**
- **GPU Support**: Optionally run queries on NVIDIA GPUs for maximum performance for in-memory or  streaming workloads.
- **[Apache Arrow support](https://arrow.apache.org/)**: Polars can consume and produce Arrow data  often with zero-copy operations. Note that Polars is not built on a Pyarrow/Arrow implementation.  Instead, Polars has its own compute and buffer implementations.

