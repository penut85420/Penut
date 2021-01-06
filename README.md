# Penut

## Introduction
+ This package is a collection of my useful functions, including some useful IO operations.

## Installation
+ You can install this package through pip:
  ```
  pip install penut
  ```

## Usage
+ You can easily load or dump and json/pkl/csv/npy file:
  ```python
  import penut.io as pio

  data = pio.load('./data.json')
  data = pio.load('./data.pkl')
  data = pio.load('./data.csv')
  data = pio.load('./data.npy')

  pio.dump(data, './data.json')
  pio.dump(data, './data.pkl')
  pio.dump(data, './data.csv')
  pio.dump(data, './data.npy')
  ```
+ You can easily measure the execution time of code:
  ```python
  from penut.uitls import TimeCost

  with TimeCost('Sleep Time'):
    import time
    time.sleep(1)
  # Output: Sleep Time: 1.000262s
  ```