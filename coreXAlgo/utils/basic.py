import json
import os
import pickle

import yaml
from tqdm import tqdm


def colorstr(*input):
    """
    输出带颜色和样式的字符串（ANSI转义码）

    Args:
        *input: 可变参数，最后一个参数为要格式化的字符串，前面的参数为颜色和样式
                    如果只提供一个参数，则默认使用蓝色粗体

    Returns:
            str: 带有ANSI转义码的格式化字符串

    Example:
        >>> # 基本用法
        >>> print(colorstr('red', 'bold', 'Error Message'))
        >>> print(colorstr('green', 'Success!'))
        >>> print(colorstr('hello world'))  # 默认蓝色粗体
        >>>
        >>> # 组合使用
        >>> warning_msg = colorstr('yellow', 'underline', 'Warning:')
        >>> print(f"{warning_msg} This is a warning message")
        >>>
        >>> # 在日志中使用
        >>> logger.info(colorstr('bright_red', 'CRITICAL:') + " System error occurred")
    """
    # Colors a string https://en.wikipedia.org/wiki/ANSI_escape_code, i.e.  colorstr('blue','bold', 'hello world')
    *args, string = input if len(input) > 1 else ('blue', 'bold', input[0])  # color arguments, string
    COLORS = {
        # basic colors
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        # bright colors
        'bright_black': '\033[90m',
        'bright_red': '\033[91m',
        'bright_green': '\033[92m',
        'bright_yellow': '\033[93m',
        'bright_blue': '\033[94m',
        'bright_magenta': '\033[95m',
        'bright_cyan': '\033[96m',
        'bright_white': '\033[97m',
        # misc
        'end': '\033[0m',
        'bold': '\033[1m',
        'underline': '\033[4m'}

    # 验证颜色参数
    for arg in args:
        if arg not in COLORS:
            raise ValueError(f"Invalid color/style argument: '{arg}'. "
                             f"Available options: {list(COLORS.keys())}")

    # 构建颜色字符串
    color_codes = ''.join(COLORS[arg] for arg in args)
    return f"{color_codes}{string}{COLORS['end']}"


def obj_to_json(obj, json_path, ensure_ascii=True):
    """
    将Python对象保存为JSON文件

    Args:
        obj: 要保存的Python对象
        json_path (str): JSON文件路径
        ensure_ascii (bool): 是否确保ASCII编码

    Example:
        >>> # 保存配置字典
        >>> config = {'lr': 0.01, 'batch_size': 32}
        >>> obj_to_json(config, 'config.json')
        >>>
        >>> # 保存训练结果
        >>> results = {'accuracy': 0.95, 'loss': 0.1}
        >>> obj_to_json(results, 'results/training_results.json')
    """
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'wt', encoding='utf-8') as fp:
        json.dump(obj, fp, indent=2, ensure_ascii=ensure_ascii)


def obj_from_json(json_path):
    """
     从JSON文件加载Python对象

     Args:
         json_path (str): JSON文件路径

     Returns:
         object: 从JSON文件加载的Python对象

     Example:
         >>> # 加载配置文件
         >>> config = obj_from_json('config.json')
         >>>
         >>> # 加载训练结果
         >>> results = obj_from_json('results/training_results.json')
     """
    with open(json_path, 'rt', encoding='utf-8') as fp:
        return json.load(fp)


def obj_to_yaml(obj, yaml_path):
    """
    将Python对象保存为YAML文件

    Args:
        obj: 要保存的Python对象
        yaml_path (str): YAML文件路径

    Example:
        >>> # 保存YAML配置
        >>> config = {'model': 'resnet', 'params': {'depth': 50}}
        >>> obj_to_yaml(config, 'config.yaml')
    """
    os.makedirs(os.path.dirname(yaml_path), exist_ok=True)
    with open(yaml_path, 'wt', encoding='utf-8') as fp:
        yaml.dump(obj, fp)


def obj_from_yaml(yaml_path):
    """
    从YAML文件加载Python对象

    Args:
        yaml_path (str): YAML文件路径

    Returns:
        object: 从YAML文件加载的Python对象

    Example:
        >>> # 加载YAML配置
        >>> config = obj_from_yaml('config.yaml')
    """
    with open(yaml_path, 'rt', encoding='utf-8') as fp:
        return yaml.load(fp, Loader=yaml.FullLoader)


def obj_to_pkl(obj, pkl_path):
    """
    将Python对象保存为pickle文件

    Args:
        obj: 要保存的Python对象
        pkl_path (str): pickle文件路径

    Example:
        >>> # 保存模型权重
        >>> obj_to_pkl(model.state_dict(), 'model_weights.pkl')
        >>>
        >>> # 保存复杂数据结构
        >>> data = {'images': images, 'labels': labels}
        >>> obj_to_pkl(data, 'dataset.pkl')
    """
    os.makedirs(os.path.dirname(pkl_path), exist_ok=True)
    with open(pkl_path, 'wb') as fp:
        pickle.dump(obj, fp)


def obj_from_pkl(pkl_path):
    """
    从pickle文件加载Python对象

    Args:
        pkl_path (str): pickle文件路径

    Returns:
        object: 从pickle文件加载的Python对象

    Example:
        >>> # 加载模型权重
        >>> weights = obj_from_pkl('model_weights.pkl')
        >>> model.load_state_dict(weights)
        >>>
        >>> # 加载数据集
        >>> dataset = obj_from_pkl('dataset.pkl')
    """
    with open(pkl_path, 'rb') as fp:
        return pickle.load(fp)


def _worker_func(func, items, idxs, progress_bar, failed_idxs):
    """
    线程工作函数（内部使用）
    """
    for i in idxs:
        try:
            item = items[i]  # Assuming items supports indexing
            if func:
                func(item)
            progress_bar.update()
        except Exception as e:
            failed_idxs.append(i)
            progress_bar.write(f"Failed at index {i}: {str(e)}")


def thread_pool(func, items, workers):
    """
    使用线程池并行处理数据项,使用多线程并行处理可迭代对象中的每个元素，支持进度显示和错误处理。

    Args:
        func: 处理每个元素的函数，可使用functools.partial固定参数
        items: 可迭代对象（列表、生成器等）
        workers: 工作线程数量

    Returns:
        List[int]: 处理失败的索引列表（空列表表示全部成功）

    Example:
        >>> # 并行处理图像文件
        >>> def process_image(image_path):
        >>>     img = Image.open(image_path)
        >>>     img = img.resize((256, 256))
        >>>     img.save(image_path)
        >>>
        >>> image_files = glob.glob('images/*.jpg')
        >>> failed = thread_pool(process_image, image_files, workers=4)
        >>>
        >>> # 使用partial固定参数
        >>> from functools import partial
        >>> def process_with_params(image_path, size):
        >>>     img = Image.open(image_path)
        >>>     img = img.resize(size)
        >>>     img.save(image_path)
        >>>
        >>> process_func = partial(process_with_params, size=(128, 128))
        >>> failed = thread_pool(process_func, image_files, workers=4)
        >>>
        >>> # 处理失败项
        >>> for idx in failed:
        >>>     print(f"Failed to process: {image_files[idx]}")
    """
    import concurrent.futures

    if not hasattr(items, "__getitem__"):
        items = list(items)

    failed_idxs = []
    total = len(items)

    with tqdm(total=total) as pbar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            # Divide work evenly among workers
            futures = []
            for i in range(workers):
                idxs = list(range(i, total, workers))
                if not idxs:
                    continue
                futures.append(
                    executor.submit(_worker_func, func, items, idxs, pbar, failed_idxs)
                )

            # Wait for all tasks to complete
            concurrent.futures.wait(futures)

    return failed_idxs
