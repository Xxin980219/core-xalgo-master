# Basic

基础函数

## 核心功能

- **字符串处理**：输出带颜色和样式的字符串
- **文件序列化**：支持JSON、YAML和pickle格式的对象保存和加载
- **线程池**：使用线程池并行处理数据项，支持进度显示和错误处理

## 使用示例

### 字符串处理

```python
from coreXAlgo.utils import colorstr

# 基本用法
print(colorstr('red', 'bold', 'Error Message'))
print(colorstr('green', 'Success!'))
print(colorstr('hello world'))  # 默认蓝色粗体

# 组合使用
warning_msg = colorstr('yellow', 'underline', 'Warning:')
print(f"{warning_msg} This is a warning message")
```

### 文件序列化

```python
from coreXAlgo.utils import obj_to_json, obj_from_json, obj_to_yaml, obj_from_yaml, obj_to_pkl, obj_from_pkl

# JSON操作
config = {'lr': 0.01, 'batch_size': 32}
obj_to_json(config, 'config.json')
loaded_config = obj_from_json('config.json')

# YAML操作
obj_to_yaml(config, 'config.yaml')
loaded_config = obj_from_yaml('config.yaml')

# Pickle操作
obj_to_pkl(config, 'config.pkl')
loaded_config = obj_from_pkl('config.pkl')
```

### 线程池并行处理

```python
from coreXAlgo.utils import thread_pool

# 定义处理函数
def process_item(item):
    # 处理逻辑
    print(f"Processing: {item}")

# 要处理的数据项
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 使用线程池并行处理
failed_indices = thread_pool(process_item, items, workers=4)
print(f"Failed indices: {failed_indices}")
```

## API 参考

```{eval-rst}
.. automodule:: coreXAlgo.utils.basic
   :members:
   :undoc-members:
   :show-inheritance:
```