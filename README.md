# Penut

## Introduction
+ [GitHub](https://github.com/penut85420/penut)  
[![GitHub release](https://img.shields.io/github/v/release/penut85420/penut.svg)](https://github.com/penut85420/penut/releases)
[![GitHub release date](https://img.shields.io/github/release-date/penut85420/penut.svg)](https://github.com/penut85420/penut/releases)
[![GitHub issues](https://img.shields.io/github/issues/penut85420/penut.svg)](https://github.com/penut85420/penut/issues)
+ PyPI  
[![PyPI version](https://img.shields.io/pypi/v/penut.svg?maxAge=3600)](https://pypi.org/project/penut)
[![PyPI license](https://img.shields.io/pypi/l/penut.svg?maxAge=3600)](https://github.com/ckiplab/penut/blob/master/LICENSE)
[![PyPI python](https://img.shields.io/pypi/pyversions/penut.svg?maxAge=3600)](https://pypi.org/project/penut)
+ This package is a collection of my useful functions.
+ Including useful IO operation and NLP utils.

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
+ You can easily measure the execute time of code:
  ```python
  from penut.uitls import TimeCost

  with TimeCost('Sleep Time'):
    import time
    time.sleep(1)
  # Output: Sleep Time: 1.000262s
  ```