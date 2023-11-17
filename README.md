# CRS-R index

This repository contains the code for the CRS-R index, a tool to assess the level of consciousness of patients with 
disorders of consciousness. The CRS-R index is a single number that summarizes the CRS-R[1] behavioral assessment. 
This number has shown to be a good predictor of the level of consciousness of patients with disorders of consciousness 
see [2] for more details.


### Usage
The repository contains both and R and a Python implementation of the CRS-R index. The R implementation can be used as 
follows:

```R
# Load the data
mydata = read.csv("/path/to/mydata.csv")

# Execute the R-script
# This will create a new column in the data frame called CRS_R_index
```

The Python implementation can be used as follows:
```Python
# Import dependencies
import pandas as pd
# load the CRS_R_index function from the CRS_R_index.py file
from CRS_R_index import CRS_R_index

# load the data
mydata = pd.read_csv("/path/to/mydata.csv")

# Execute the function
crs_r_index = CRS_R_index(mydata, 1)

# Note: this will calculate the CRS-R index for the first 
# CRS-R assessment in the dataframe. See function for details
```

### References
[1] Giacino, J. T., Kalmar, K., & Whyte, J. (2004). The JFK Coma Recovery Scale-Revised: measurement characteristics
and diagnostic utility. Archives of physical medicine and rehabilitation, 85(12), 2020-2029.

[2] Annen, J., Heine, L., Ziegler, E., Rabe, S., & Bender, A. (2018). The CRS-R Index: A Simple and Robust Outcome
Measure for Disorders of Consciousness. Frontiers in neurology, 9, 1115.


### Code Authors
Jitka Annen, Glenn van der Lande