# Annotation Processor

标注文件处理器，支持 VOC XML 和 YOLO TXT 格式

## 核心功能

### VOCXMLProcessor
- **类别更新**：更新 XML 文件中的类别名称，支持批量处理
- **无标注检测**：提取无标注的图片
- **缺陷统计**：统计缺陷类别及其出现次数
- **类别过滤**：提取包含特定类别的图片
- **类别分组**：获取按类别分组的图片列表
- **详细统计**：获取详细的类别统计信息
- **批量处理**：批量处理多个 XML 文件，支持递归搜索
- **多线程处理**：使用多线程提高处理效率
- **完善的文档**：详细的参数说明和使用示例
- **错误处理**：优化的错误处理和日志记录

### YOLOTXTProcessor
- **类别更新**：更新 TXT 文件中的类别序号（YOLO 格式）
- **批量处理**：批量处理多个 TXT 文件，支持递归搜索
- **详细的文档**：详细的参数说明和使用示例
- **错误处理**：优化的错误处理和日志记录

## 使用示例

### 按类别分组获取图片

```python
from coreXAlgo.file_processing import VOCXMLProcessor

# 创建处理器实例
processor = VOCXMLProcessor()

# 获取按类别分组的图片列表
category_images = processor.get_images_by_category('annotations/')
for category, images in category_images.items():
    print(f"Category: {category}, Image count: {len(images)}")
```

### 获取详细的类别统计信息

```Python
from coreXAlgo.file_processing import VOCXMLProcessor

# 创建处理器实例
processor = VOCXMLProcessor()

# 获取详细的类别统计信息
stats = processor.get_category_statistics('annotations/')
print(f"Total categories: {stats['total_categories']}")
print(f"Total images: {stats['total_images']}")
print("\nCategory distribution:")
for category, count in stats['category_counts'].items():
    print(f"  {category}: {count} images")
```

### YOLO TXT 类别更新

```python
from coreXAlgo.file_processing import YOLOTXTProcessor

# 创建处理器实例
processor = YOLOTXTProcessor()

# 所有原始类别
all_categories = ['class1', 'class2', 'class3']

# 要替换的类别和目标类别
source_categories = ['class1', 'class3']
target_categories = ['class2', 'class1']

# 更新单个 TXT 文件
updated = processor.update_categories(
    'labels/image.txt',
    all_categories,
    source_categories,
    target_categories
)
print(f"Updated {updated} categories in the file")

# 更新目录中所有 TXT 文件
updated = processor.update_categories(
    'labels/',
    all_categories,
    source_categories,
    target_categories
)
print(f"Updated {updated} categories in the directory")
```

## API 参考

```{eval-rst}
.. automodule:: coreXAlgo.file_processing.annotation_processor
   :members:
   :undoc-members:
   :show-inheritance:
```

