# Annotation_convert

标注文件转换，LabelMe ↔ VOC ↔ YOLO 标注格式互转

## 核心功能

- **格式互转**：支持 LabelMe、VOC 和 YOLO 三种标注格式的相互转换
- **标签映射**：支持将原始标签映射到目标标签，通过 `label_mapping` 参数实现
- **批量处理**：支持批量处理多个标注文件
- **图像尺寸缓存**：优化性能，避免重复读取图像尺寸

## 使用示例

### 标签映射功能

```python
from coreXAlgo.file_processing import AnnotationConverter

# 定义类别名称和标签映射
class_names = ["A", "B", "C"]
label_mapping = {"A": "B", "C": "B"}  # 将 A 和 C 映射到 B

# 创建转换器实例
converter = AnnotationConverter(class_names, label_mapping)

# LabelMe → YOLO目标检测格式
converter.labelme_to_yolo_obj('labelme/001.json')

# LabelMe → YOLO分割格式
converter.labelme_to_yolo_seg('labelme/001.json')

# YOLO分割 → LabelMe格式
converter.yolo_seg_to_labelme('yolo/001.txt', 'images/001.jpg')
```

## API 参考

```{eval-rst}
.. automodule:: coreXAlgo.file_processing.annotation_convert
   :members:
   :exclude-members: AnnotationError, FormatError, FileError, ValidationError, PolygonPoint, BBox
   :show-inheritance:
```