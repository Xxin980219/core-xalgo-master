import re

from setuptools import setup, find_packages
import os


# 自动读取版本号
def get_version():
    # 尝试从 version.py 读取版本号
    version_path = os.path.join("coreXAlgo", "version.py")
    with open(version_path, "r", encoding="utf-8") as f:
        version_match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", f.read(), re.M)
        if version_match:
            return version_match.group(1)

    # 如果找不到，使用默认版本
    return "0.1.0"

get_version()

def read_requirements():
    """读取requirements.txt"""
    with open('requirements.txt') as f:
        return [line.strip() for line in f if line.strip()]


# 核心依赖包
core_dependencies = [
    'numpy>=1.20.0',
    'opencv-python>=4.5.0',
    'lxml>=4.6.0',
    'tqdm>=4.53.0',
    'PyYAML>=6.0',
    'paramiko>=3.0.0',
    'pandas>=1.3.0',
    'sqlalchemy>=1.3.0',
    'matplotlib>=3.3.0',
    'torch>=1.8.0'
]

# 合并所有依赖
# all_dependencies = core_dependencies + read_requirements()
all_dependencies = core_dependencies

setup(
    name="coreXAlgo",
    version=get_version(),
    packages=find_packages(),  # 自动发现所有包
    include_package_data=True,  # 包含非代码文件

    # 重要：包含模型权重和其他资源文件
    package_data={},

    # 依赖项
    install_requires=all_dependencies,

    # 元数据
    author="Xiong Xin",
    author_email="",
    description="coreXAlgo - CoreX Algorithm Library for computer vision and data processing.",
    long_description="A comprehensive algorithm library for computer vision and data processing, providing tools for file processing, annotation conversion, image cropping, and more.",
    license="AGPL-3.0",
    python_requires=">=3.7",  # Python版本要求
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Computer Vision",
        "Topic :: Utilities"
    ]
)