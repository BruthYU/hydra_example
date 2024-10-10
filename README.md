# hydra_example

### 1. Install hydra
```shell
pip install hydra-core
```


### 2. Run Example
```shell
python run.py
```


**Note that** `# @package _global_` could move the config to the global namespace
```python
# try
print(config.model.college)
# and
print(config.college)
```