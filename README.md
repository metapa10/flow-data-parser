# Flow Data Parser

## Overview
The Flow Data Parser is a simple program designed to parse and analyze protocol numbers from a log file. This program is built to support the default log format and is compatible with version 2 only.

## Assumptions
- The program only supports the default log format and does not handle custom formats.
- The only version supported is version 2.
- The protocol numbers data has been sourced from the [IANA Protocol Numbers CSV](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.csv).
- The program does not utilize non-default libraries or packages, ensuring easy execution on a local machine.

## Features
- Parses protocol numbers from a log file.
- Provides summary statistics about the protocol usage.

## Running the Program

### Prerequisites
- Ensure you have Jupyter Notebook installed. You can install it via Anaconda or pip.

### Running in Jupyter Notebook
1. Launch Jupyter Notebook in your terminal:

   ```bash
   jupyter notebook
