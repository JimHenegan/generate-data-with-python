# Generate Data with Python

This repository contains code to generate data with Python.

## Main Ideas

- Begin with a CSV file of metadata.
   - See the file `example-metadata.csv` to see an example.

- Define some parameters.
   - `seed`: the seed number for a random generator
   - `sample_size`: the number of observations in the generated data

- Set up a random number generator with numpy.
   - Example: `rng = np.random.default_rng(seed)`

- Call some helper functions (from `helpers`) to generate the data.

   - See the `Demo.ipynb` notebook for a full example.
  
