# coreXAlgo Documentation

<div class="hero-section">
  <div class="hero-content">
    <div class="hero-badge">🚀 v0.5.7</div>
    <h1 class="hero-title">coreXAlgo</h1>
    <p class="hero-subtitle">算法开发工具库</p>
    <p class="hero-description">为算法工程师打造的综合性工具集合，提供高效、可靠的技术支持，显著提升开发效率</p>
    <div class="hero-buttons">
      <a href="#quick-start" class="btn btn-primary">开始使用</a>
      <a href="https://github.com/Xxin980219/coreXAlgo" class="btn btn-secondary" target="_blank">GitHub</a>
    </div>
  </div>
  <div class="hero-pattern"></div>
</div>

<style>
  /* Hero Section */
  .hero-section {
    position: relative;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    padding: 4rem 2rem;
    border-radius: 16px;
    margin-bottom: 3rem;
    color: white;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
  }
  
  .hero-pattern {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: 
      radial-gradient(circle at 20% 50%, rgba(255,255,255,0.1) 0%, transparent 50%),
      radial-gradient(circle at 80% 80%, rgba(255,255,255,0.1) 0%, transparent 50%),
      radial-gradient(circle at 40% 20%, rgba(255,255,255,0.05) 0%, transparent 30%);
    pointer-events: none;
  }
  
  .hero-content {
    position: relative;
    z-index: 1;
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }
  
  .hero-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(10px);
    padding: 0.4rem 1rem;
    border-radius: 20px;
    font-size: 0.85rem;
    font-weight: 600;
    margin-bottom: 1.5rem;
    border: 1px solid rgba(255, 255, 255, 0.3);
  }
  
  .hero-title {
    font-size: 3.5rem;
    margin-bottom: 0.5rem;
    font-weight: 800;
    background: linear-gradient(to right, #ffffff, #e0e7ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    text-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  }
  
  .hero-subtitle {
    font-size: 1.5rem;
    margin-bottom: 1rem;
    opacity: 0.95;
    font-weight: 500;
  }
  
  .hero-description {
    font-size: 1.1rem;
    margin-bottom: 2rem;
    opacity: 0.85;
    line-height: 1.6;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .hero-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .btn {
    display: inline-flex;
    align-items: center;
    padding: 0.8rem 2rem;
    border-radius: 8px;
    font-weight: 600;
    text-decoration: none;
    transition: all 0.3s ease;
    font-size: 1rem;
  }
  
  .btn-primary {
    background: white;
    color: #667eea;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
  }
  
  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.3);
  }
  
  .btn-secondary {
    background: rgba(255, 255, 255, 0.1);
    color: white;
    border: 2px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
  }
  
  .btn-secondary:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: translateY(-2px);
  }
  
  /* Feature Cards */
  .feature-card {
    border-radius: 12px;
    padding: 1.5rem;
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    border: 1px solid #e2e8f0;
    transition: all 0.3s ease;
    height: 100%;
  }
  
  .feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 12px 40px rgba(0, 0, 0, 0.1);
    border-color: #667eea;
  }
  
  .feature-icon {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    display: block;
  }
  
  .feature-card h3 {
    color: #1e293b;
    font-size: 1.25rem;
    margin-bottom: 0.75rem;
    font-weight: 700;
  }
  
  .feature-card ul {
    margin: 0;
    padding-left: 1.2rem;
    color: #64748b;
  }
  
  .feature-card li {
    margin-bottom: 0.4rem;
    line-height: 1.5;
  }
  
  /* Sub Features Grid */
  .sub-features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1rem;
  }
  
  .sub-feature-card {
    background: white;
    border-radius: 8px;
    padding: 1rem;
    border: 1px solid #e2e8f0;
    transition: all 0.3s ease;
  }
  
  .sub-feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
    border-color: #667eea;
  }
  
  .sub-feature-card h4 {
    color: #1e293b;
    font-size: 1rem;
    margin-bottom: 0.75rem;
    font-weight: 600;
  }
  
  .sub-feature-card ul {
    margin: 0;
    padding-left: 1.2rem;
    color: #64748b;
  }
  
  .sub-feature-card li {
    margin-bottom: 0.4rem;
    line-height: 1.5;
    font-size: 0.9rem;
  }
  
  /* Module Cards */
  .module-card {
    border-radius: 12px;
    padding: 2rem;
    background: white;
    border: 2px solid #e2e8f0;
    transition: all 0.3s ease;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  
  .module-link {
    text-decoration: none;
    color: inherit;
    display: block;
    height: 100%;
  }
  
  .module-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, #667eea, #764ba2);
    transform: scaleX(0);
    transition: transform 0.3s ease;
  }
  
  .module-card:hover::before {
    transform: scaleX(1);
  }
  
  .module-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 50px rgba(102, 126, 234, 0.15);
    border-color: #667eea;
  }
  
  .module-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
  }
  
  .module-card h3 {
    color: #1e293b;
    font-size: 1.3rem;
    margin-bottom: 0.75rem;
    font-weight: 700;
  }
  
  .module-card p {
    color: #64748b;
    margin: 0;
    line-height: 1.6;
  }
  
  /* Info Section */
  .info-section {
    background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
  }
  
  .info-item {
    display: flex;
    align-items: center;
    margin-bottom: 1rem;
    padding: 0.75rem;
    background: white;
    border-radius: 8px;
    border-left: 4px solid #667eea;
  }
  
  .info-item:last-child {
    margin-bottom: 0;
  }
  
  .info-label {
    font-weight: 700;
    color: #1e293b;
    margin-right: 0.75rem;
    min-width: 120px;
  }
  
  .info-value {
    color: #64748b;
    font-weight: 500;
  }
  
  /* Quick Start Section */
  .quick-start-section {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    padding: 2.5rem;
    border-radius: 12px;
    color: white;
    margin: 2rem 0;
  }
  
  .quick-start-section h3 {
    color: white;
    margin-top: 0;
    margin-bottom: 1.5rem;
    font-size: 1.5rem;
  }
  
  .quick-start-section pre {
    background: rgba(255, 255, 255, 0.1);
    border-radius: 8px;
    padding: 1rem;
    overflow-x: auto;
  }
  
  .quick-start-section code {
    color: #a5b4fc;
    font-family: 'Consolas', 'Monaco', monospace;
  }
  
  /* Features Grid */
  .features-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 1.5rem;
    margin: 2rem 0;
  }
  
  .feature-item {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
    padding: 1rem;
    background: #f8fafc;
    border-radius: 8px;
    border: 1px solid #e2e8f0;
  }
  
  .feature-check {
    color: #10b981;
    font-size: 1.2rem;
    flex-shrink: 0;
  }
  
  .feature-text {
    color: #334155;
    font-weight: 500;
  }
  
  /* Changelog */
  .changelog-item {
    padding: 1.5rem;
    background: #f8fafc;
    border-radius: 8px;
    margin-bottom: 1rem;
    border-left: 4px solid #667eea;
  }
  
  .changelog-version {
    font-weight: 700;
    color: #1e293b;
    font-size: 1.1rem;
    margin-bottom: 0.5rem;
  }
  
  .changelog-list {
    margin: 0;
    padding-left: 1.2rem;
    color: #64748b;
  }
  
  .changelog-list li {
    margin-bottom: 0.3rem;
  }
</style>

CoreXAlgo 是一个综合性的算法库，提供了多种实用工具和算法，主要涵盖文件处理、高级计算机视觉和通用工具函数等领域。该项目设计模块化，结构清晰，便于扩展和维护。

本库整合了算法开发过程中常用的核心功能模块，通过模块化的设计，为算法研发提供高效、可靠的技术支持，显著提升开发效率，减少重复性工作，确保代码质量和可维护性。

## 📋 项目概览

<div class="features-grid">
  <div class="feature-card">
    <h3>🎯 核心功能</h3>
    <div class="sub-features-grid">
      <div class="sub-feature-card">
        <h4>计算机视觉</h4>
        <ul>
          <li>图像处理与变换（CLAHE增强）</li>
          <li>标注工具与格式转换（YOLO、VOC、LabelMe）</li>
          <li>目标检测与可视化</li>
          <li>归一化互相关计算</li>
        </ul>
      </div>
      <div class="sub-feature-card">
        <h4>文件处理</h4>
        <ul>
          <li>批量文件操作与管理</li>
          <li>标注格式转换与验证</li>
          <li>数据预处理与增强</li>
          <li>压缩文件管理</li>
          <li>图像裁剪与分割</li>
        </ul>
      </div>
      <div class="sub-feature-card">
        <h4>基础工具</h4>
        <ul>
          <li>日志管理与配置</li>
          <li>FTP/SFTP客户端</li>
          <li>数据库客户端</li>
          <li>多线程文件传输</li>
          <li>边界框处理工具</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="feature-card">
    <h3>🚀 技术特点</h3>
    <div class="sub-features-grid">
      <div class="sub-feature-card">
        <h4>架构设计</h4>
        <ul>
          <li>模块化代码结构</li>
          <li>低耦合高内聚设计</li>
          <li>统一的接口和命名规范</li>
          <li>易于扩展和维护</li>
        </ul>
      </div>
      <div class="sub-feature-card">
        <h4>性能优化</h4>
        <ul>
          <li>多线程并发支持</li>
          <li>批量处理能力</li>
          <li>内存效率优化</li>
          <li>并行处理架构</li>
        </ul>
      </div>
      <div class="sub-feature-card">
        <h4>质量保证</h4>
        <ul>
          <li>完善的异常处理机制</li>
          <li>详细的文档和注释</li>
          <li>跨平台兼容性</li>
          <li>生产级代码质量</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="feature-card">
    <h3>💡 应用场景</h3>
    <div class="sub-features-grid">
      <div class="sub-feature-card">
        <h4>数据获取与管理</h4>
        <ul>
          <li>批量从FTP/SFTP服务器下载数据</li>
          <li>服务器端文件整理和备份</li>
          <li>批量文件操作和管理</li>
        </ul>
      </div>
      <div class="sub-feature-card">
        <h4>数据预处理</h4>
        <ul>
          <li>标注格式转换与验证</li>
          <li>图像裁剪和增强</li>
          <li>数据验证和清理</li>
          <li>YOLO数据预处理</li>
        </ul>
      </div>
      <div class="sub-feature-card">
        <h4>图像处理</h4>
        <ul>
          <li>图像增强（CLAHE）</li>
          <li>特征匹配（NCC）</li>
          <li>边界框处理和可视化</li>
          <li>多边形处理和掩码操作</li>
        </ul>
      </div>
    </div>
  </div>
</div>

## 📁 项目架构

:::{dropdown} {octicon}`repo;1em`&nbsp; 目录结构
:animate: fade-in-slide-down
:open:

```
coreXAlgo/
├── 📄 __init__.py              # 主入口文件
├── 📄 version.py               # 版本管理
├── 📄 coreXAlgo_分析报告.md    # 项目分析报告
│
├── 📁 utils/                   # 基础工具模块
│   ├── 📄 basic.py            # 基础工具函数（日志、序列化、线程池等）
│   ├── 📄 bbox_util.py        # 边界框处理工具（转换、绘制等）
│   ├── 📄 constants.py        # 常量定义
│   ├── 📄 ftp_client.py       # FTP协议文件传输客户端
│   ├── 📄 sftp_client.py      # SFTP协议文件传输客户端
│   ├── 📄 mt_db_client.py     # 多线程数据库客户端
│   └── 📄 mt_file_transfer.py # 多线程文件传输器（下载、上传、服务器端拷贝）
│
├── 📁 adv_cv/                 # 高级计算机视觉模块
│   └── 📄 basic.py           # 图像处理功能（NCC计算、CLAHE增强）
│
└── 📁 file_processing/         # 文件处理模块
    ├── 📄 basic.py           # 文件操作工具（查找、复制、移动等）
    ├── 📄 archive.py         # 压缩解压管理（支持多种格式）
    ├── 📄 annotation_convert.py # 标注格式转换（YOLO、VOC、LabelMe）
    ├── 📄 data_preprocessing.py # 数据预处理（YOLO数据增强）
    ├── 📄 image_crop.py      # 图像裁剪处理（滑动窗口、批量处理）
    └── 📄 annotation_processor.py   # 标注文件处理器
```
:::

## 📊 版本信息

:::{dropdown} {octicon}`info;1em`&nbsp; 版本详情
:animate: fade-in-slide-down
:open:

<div class="info-section">
  <div class="info-item">
    <span class="info-label">📦 当前版本</span>
    <span class="info-value">0.5.7</span>
  </div>
  <div class="info-item">
    <span class="info-label">🐍 Python 兼容</span>
    <span class="info-value">≥ 3.8</span>
  </div>
  <div class="info-item">
    <span class="info-label">📅 更新日期</span>
    <span class="info-value">2026-04-08</span>
  </div>
  <div class="info-item">
    <span class="info-label">👤 作者</span>
    <span class="info-value">Xxin_BOE</span>
  </div>
  <div class="info-item">
    <span class="info-label">🎯 主要领域</span>
    <span class="info-value">计算机视觉、数据处理、文件传输</span>
  </div>
  <div class="info-item">
    <span class="info-label">🔧 核心模块</span>
    <span class="info-value">utils、file_processing、adv_cv</span>
  </div>
</div>
:::

## 📚 模块文档

<div class="features-grid">
  <div class="module-card">
    <a href="adv_cv/index.html" class="module-link">
      <span class="module-icon">🖼️</span>
      <h3>计算机视觉</h3>
      <p>Adv_cv Module</p>
      <p>提供高级图像处理算法，包括归一化互相关计算和对比度受限的自适应直方图均衡化（CLAHE），适用于图像增强和特征匹配等场景</p>
    </a>
  </div>

  <div class="module-card">
    <a href="file_processing/index.html" class="module-link">
      <span class="module-icon">📂</span>
      <h3>文件处理</h3>
      <p>File_processing Module</p>
      <p>提供多种文件处理功能，包括标注格式转换（YOLO、VOC、LabelMe）、文件操作、压缩文件管理、图像裁剪和数据预处理等</p>
    </a>
  </div>

  <div class="module-card">
    <a href="utils/index.html" class="module-link">
      <span class="module-icon">🛠️</span>
      <h3>基础工具</h3>
      <p>Utils Module</p>
      <p>提供多种实用工具函数和类，包括FTP/SFTP客户端、数据库客户端、多线程文件传输、边界框处理和基础工具函数等</p>
    </a>
  </div>
</div>

## 🔧 快速开始 {#quick-start}

<div class="quick-start-section">

### 安装

```bash
# 克隆仓库
git clone https://github.com/Xxin980219/coreXAlgo.git

# 进入目录
cd coreXAlgo

# 安装依赖
pip install -r requirements.txt

# 安装库
pip install -e .
```

### 基本使用示例

```python
from coreXAlgo.utils import set_all_seed, colorstr, MtFileDownloader
from coreXAlgo.file_processing import get_files, YOLOAnnotation, VOCAnnotation
from coreXAlgo.adv_cv import apply_clahe
import cv2

# 设置随机种子确保可复现
set_all_seed(42)

# 输出彩色日志
print(colorstr('green', 'bold', '✅ 核心功能初始化完成'))

# 查找文件
image_files = get_files('./images', ['.jpg', '.png'])
print(f"📸 找到 {len(image_files)} 个图片文件")

# 图像处理示例
img = cv2.imread(image_files[0])
enhanced_img = apply_clahe(img, clipLimit=2.0, tileGridSize=(8, 8))
cv2.imwrite('./enhanced_image.jpg', enhanced_img)
print("✅ 图像增强完成")

# 标注处理示例
# YOLO标注
yolo_annot = YOLOAnnotation(['person', 'car'])
yolo_annot.add_annotation(0, [0.5, 0.6, 0.1, 0.2])  # 行人
yolo_annot.save('image_001.txt')

# VOC标注
voc_annot = VOCAnnotation('image_001.jpg', (640, 480))
voc_annot.add_object('person', [100, 50, 200, 150])
voc_annot.save('image_001.xml')
print("✅ 标注文件生成完成")

# 文件传输示例（需要配置服务器信息）
"""
ftp_config = {
    "my_ftp": {
        "host": "ftp.example.com",
        "port": 21,
        "username": "username",
        "password": "password",
        "type": "ftp"
    }
}

downloader = MtFileDownloader(ftp_config, workers=4)
file_list = ["/remote/file1.txt", "/remote/file2.jpg"]
local_paths = ["./local/file1.txt", "./local/file2.jpg"]
success_count = downloader.download_files_by_pathlist(
    server_name="my_ftp",
    file_path_list=file_list,
    local_path_list=local_paths
)
print(f"✅ 成功下载 {success_count} 个文件")
"""


</div>

## 🎯 主要特性

<div class="features-grid">
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">完善的文档与详细的使用示例</span>
  </div>
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">全面的类型注解提高代码可读性</span>
  </div>
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">完善的异常处理机制</span>
  </div>
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">多线程支持批量处理性能优化</span>
  </div>
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">跨平台兼容 Windows/Linux/macOS</span>
  </div>
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">模块化设计易于扩展维护</span>
  </div>
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">生产级代码质量测试覆盖完善</span>
  </div>
  <div class="feature-item">
    <span class="feature-check">✅</span>
    <span class="feature-text">活跃的社区支持与持续更新</span>
  </div>
</div>

## 📝 版本更新日志

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.7 (2026-04-11)</div>
  <ul class="changelog-list">
    <li>重命名了 file_processing/voc_xml_deal.py 为 file_processing/annotation_processor.py</li>
    <li>添加了 YOLOTXTProcessor 类，支持处理 YOLO TXT 格式标注文件</li>
    <li>支持目标检测和分割标注的类别更新</li>
    <li>完善了文档和使用示例</li>
    <li>更新了版本号到 0.5.7</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.6 (2026-04-08)</div>
  <ul class="changelog-list">
    <li>优化了 coreXAlgo/utils/bbox_util.py 中的 DetectionVisualizer 类</li>
    <li>为矩形框和多边形框添加了左上角（top_left）和左下角（bottom_left）标签位置选项</li>
    <li>实现了智能标签位置选择：优先使用左上角，当空间不足时自动切换到左下角</li>
    <li>调整了位置优先级，将左上角设为最高优先级，左下角设为其次</li>
    <li>更新了文本锚点映射，确保标签文字正确显示</li>
    <li>保持了与原有代码的兼容性</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.5 (2026-04-02)</div>
  <ul class="changelog-list">
    <li>优化了 file_processing/annotation_processor.py</li>
    <li>完善了 VOCXMLProcessor 类的文档字符串</li>
    <li>改进了 update_categories 方法的实现</li>
    <li>添加了详细的参数说明和使用示例</li>
    <li>优化了错误处理和日志记录</li>
    <li>增强了批量处理和多线程支持</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.4 (2026-04-01)</div>
  <ul class="changelog-list">
    <li>改进了 file_processing/annotation_convert.py 中的 VOCAnnotation 类</li>
    <li>在 _init_xml_structure 方法中添加了边界框越界处理</li>
    <li>在 add_object 方法中添加了边界框越界处理</li>
    <li>使用 max(1, min(x, image_width)) 和 max(1, min(y, image_height)) 确保坐标在有效范围内</li>
    <li>检查坐标有效性，确保 xmin < xmax 且 ymin < ymax</li>
    <li>当边界框无效时，抛出明确的错误信息</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.3 (2026-03-20)</div>
  <ul class="changelog-list">
    <li>修复了 utils/ftp_client.py 中的上传和下载问题</li>
    <li>实现了临时文件（.part）上传和重命名机制，确保文件上传的可靠性</li>
    <li>修复了FTP下载时因无法获取文件大小而失败的问题</li>
    <li>改进了目录切换逻辑，确保在正确的目录中执行文件操作</li>
    <li>修复了FTP重命名操作失败的问题，使用 sendcmd 代替 voidcmd 处理 "350 Ready for RNTO" 响应</li>
    <li>移除了传统下载方法，简化代码结构</li>
    <li>优化了错误处理和日志记录</li>
    <li>增强了文件传输的可靠性，添加了文件存在性检查</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.2 (2026-03-19)</div>
  <ul class="changelog-list">
    <li>优化了 utils/ftp_client.py 和 utils/sftp_client.py，添加了多线程支持</li>
    <li>实现了线程安全的连接池管理</li>
    <li>添加了 _process_upload_batch 和 _process_single_upload 方法用于并行上传</li>
    <li>添加了 _process_download_batch 和 _process_single_download 方法用于并行下载</li>
    <li>修复了 max_workers 参数未使用的问题</li>
    <li>修复了 utils/mt_file_transfer.py 中的返回值处理问题</li>
    <li>确保 parallel_download_by_instances 正确返回成功下载数量</li>
    <li>统一了FTP和SFTP客户端的返回值处理格式</li>
    <li>增强了线程安全机制，添加了 threading.RLock() 线程安全锁</li>
    <li>优化了文件传输性能，支持批量处理文件传输</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.1 (2026-03-03)</div>
  <ul class="changelog-list">
    <li>更新了 file_processing/image_crop.py，添加了新参数：separate_images_xml 和 generate_ok_xml</li>
    <li>改进了 image_crop.py 的目录结构管理</li>
    <li>增强了 image_crop.py 的错误处理和日志记录</li>
    <li>更新了 image_crop.py 的 _process_image 方法以返回正确的错误值</li>
    <li>为 image_crop.py 添加了 tqdm 安全检查以处理 stdout None 的情况</li>
    <li>重新排列了 image_crop.py 中 __init__ 方法的参数，将 verbose 移到最后</li>
    <li>隐藏了 annotation_convert.py 中的某些异常类和类型定义，使其不在文档中显示</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.5.0 (2026-02-27)</div>
  <ul class="changelog-list">
    <li>为 file_processing/basic.py 中的函数添加了详细的文档字符串和使用示例</li>
    <li>优化了 randomly_select_files 函数的代码结构</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.4.9 (2026-02-26)</div>
  <ul class="changelog-list">
    <li>修复了 sftp_client.py 中下载成功数量统计错误的问题</li>
    <li>优化了 sftp_client.py 的异常处理逻辑</li>
    <li>为 mt_file_downloader.py 添加了缺失的 logging 模块导入</li>
    <li>改进了 sftp_client.py 的连接池管理</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.4.8 (2026-02-25)</div>
  <ul class="changelog-list">
    <li>重构了文件处理模块，提升了性能</li>
    <li>优化了工具模块，包括 bbox_util.py、ftp_client.py 和 sftp_client.py</li>
    <li>新增了 mt_file_downloader.py 模块</li>
    <li>改进了数据库客户端的查询性能和错误处理</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.4.7 (2026-02-24)</div>
  <ul class="changelog-list">
    <li>修复了 SQLAlchemy 版本兼容性问题</li>
    <li>优化了 FTP/SFTP 客户端的错误处理</li>
    <li>改进了目标检测可视化的性能</li>
  </ul>
</div>

<div class="changelog-item">
  <div class="changelog-version">📌 版本 0.4.6 (2026-02-23)</div>
  <ul class="changelog-list">
    <li>初始版本发布</li>
    <li>包含核心工具模块、高级计算机视觉模块和文件处理模块</li>
  </ul>
</div>

```{toctree}
:caption: 模块文档
:hidden:

adv_cv/index
file_processing/index
utils/index
```
