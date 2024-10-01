# CPU 性能测试器 / CPU Performance Tester

## 简介 / Introduction

该项目是一个基于 Python 编写的 **CPU 性能测试器**，可以执行多种 CPU 和系统性能测试，包括单核与多核计算、CPU 使用率、浮点运算、磁盘 I/O 性能、线程切换性能等。用户可以通过简单的图形界面（GUI）选择需要的测试项，程序会自动进行测试并给出每个测试的耗时与性能评分。测试结果将以文本形式呈现，并且可以保存或导出。

This project is a **CPU Performance Tester** written in Python, capable of executing various CPU and system performance tests, including single-core and multi-core calculations, CPU usage, floating point operations, disk I/O performance, thread switching performance, etc. Users can select the tests through a simple Graphical User Interface (GUI), and the program will automatically perform the tests and display the results with execution time and performance scores. The test results are presented as text and can be saved or exported.

## 功能 / Features

- 单核和多核计算测试
- CPU 使用率监测
- 浮点运算测试
- 磁盘 I/O 读写性能测试
- 线程切换性能测试
- 随机数生成测试
- 矩阵运算性能测试（基于 Numpy）
- 数据压缩和解压性能测试（基于 zlib）
- 哈希计算性能测试（基于 SHA256）
- 文件读写性能测试

- Single-core and multi-core calculation tests
- CPU usage monitoring
- Floating point operations test
- Disk I/O read/write performance test
- Thread switching performance test
- Random number generation test
- Matrix operations performance test (based on Numpy)
- Data compression and decompression test (based on zlib)
- Hashing performance test (based on SHA256)
- File read/write performance test

## 安装 / Installation

### 依赖库 / Dependencies

在运行该程序之前，请确保已经安装以下依赖库：

Before running the program, please ensure the following dependencies are installed:

```bash
pip install psutil numpy matplotlib zlib tkinter
```

### 运行 / Run

要运行该项目，请在终端中执行以下命令：

To run the project, execute the following command in the terminal:

```bash
python main.py
```

## 使用说明 / Usage Instructions

1. 打开程序后，用户可以选择需要的性能测试项。
2. 点击 "开始测试" 按钮，程序将依次执行选择的测试项目，并在右侧显示每个项目的耗时和性能评分。
3. 测试过程中，会显示一个动态进度条，指示测试进度。
4. 测试完成后，结果将会保存到内存中，可以进一步导出或查看。

1. After opening the program, users can select the performance tests they wish to run.
2. Click the "Start Test" button, and the program will execute the selected tests in sequence, displaying the time taken and performance scores for each test in the right panel.
3. A dynamic progress bar will show the testing progress.
4. After the tests are completed, the results will be stored in memory and can be further exported or reviewed.


## 测试项目 / Test Items

- 单核计算测试（Timeit）/ Single-core Calculation (Timeit)
- 多核计算测试（多进程）/ Multi-core Calculation (Multiprocessing)
- CPU 使用率测试 / CPU Usage (%)
- 浮点运算性能（矩阵）/ Floating Point Operations (Matrix)
- 内存读取性能 / Memory Read Performance
- 线程切换性能 / Thread Switching Performance
- 磁盘 I/O 写入速度 / Disk I/O (Write Speed)
- 随机数生成性能 / Random Number Generation
- 延迟测试 / Latency Test
- 矩阵运算性能（Numpy）/ Matrix Operations (Numpy)
- 素数生成测试 / Prime Number Generation
- 排序算法性能 / Sorting Algorithm Performance
- 数据压缩性能（zlib）/ Compression Test (zlib)
- 数据解压性能（zlib）/ Decompression Test (zlib)
- SHA256 哈希性能测试 / SHA256 Hashing Performance
- 文件读取性能 / File Read Performance
- 文件写入性能 / File Write Performance
- 内存分配速度 / Memory Allocation Speed
- 上下文切换性能 / Context Switching
- CPU 任务切换延迟 / CPU Task Switching Latency

## 贡献 / Contributing

如果你有任何改进建议或发现了问题，欢迎提交 issue 或 pull request。

If you have any suggestions for improvements or encounter any issues, feel free to submit an issue or a pull request.


This project is licensed under the MIT License.

---

通过该 `README.md` 文件，用户可以了解项目的功能、安装步骤、使用说明和测试项的详细信息。
