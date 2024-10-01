import timeit
import time
import psutil
import numpy as np
import os
import random
import json
from datetime import datetime
import threading
import matplotlib.pyplot as plt
from tkinter import Tk, Text, Label, Button, StringVar, ttk, filedialog, messagebox, Checkbutton, IntVar
from concurrent.futures import ThreadPoolExecutor

# 定义一个CPU密集型任务函数
def cpu_intensive_task(index):
    total = 0
    for i in range(1000000):
        total += i ** 2
    return total

# 后台测试线程类
class CpuTestWorker(threading.Thread):
    def __init__(self, update_progress, update_results, on_done, record_results, selected_tests):
        super().__init__()
        self.update_progress = update_progress
        self.update_results = update_results
        self.on_done = on_done
        self.record_results = record_results
        self.selected_tests = selected_tests
        self._is_running = True
        self.executor = ThreadPoolExecutor(max_workers=psutil.cpu_count(logical=True))

    def run(self):
        tests = {
            "Single-core calculation (Timeit)": self.single_core_test,
            "Multi-core calculation (Multiprocessing)": self.multi_core_test,
            "CPU Usage (%)": self.cpu_usage_test,
            "Floating Point Operations (Matrix)": self.float_operations_test,
            "Memory Read Performance": self.memory_test,
            "Thread Switching Performance": self.thread_switching_test,
            "Disk I/O (Write Speed)": self.disk_io_test,
            "Random Number Generation": self.random_number_test,
            "Latency Test": self.latency_test,
            "Matrix Operations (Numpy)": self.matrix_operations_test,
            "Prime Number Generation": self.prime_generation_test,
            "Sorting Algorithm Performance": self.sorting_test,
            "Compression Test (zlib)": self.compression_test,
            "Decompression Test (zlib)": self.decompression_test,
            "SHA256 Hashing Performance": self.hashing_test,
            "File Read Performance": self.file_read_test,
            "File Write Performance": self.file_write_test,
            "Memory Allocation Speed": self.memory_allocation_test,
            "Context Switching": self.context_switch_test,
            "CPU Task Switching Latency": self.cpu_task_switching_test
        }

        selected_tests = [test for i, test in enumerate(tests) if self.selected_tests[i].get() == 1]
        total_tests = len(selected_tests)
        results = []

        for i, test_name in enumerate(selected_tests):
            if not self._is_running:
                break

            start_time = time.time()
            duration = tests[test_name]()
            end_time = time.time()
            score = self.calculate_score(duration)

            self.update_progress(int((i + 1) / total_tests * 100))
            result_text = f"{test_name}: {duration:.4f} seconds"
            self.update_results(result_text, score)
            results.append({
                "test_name": test_name,
                "duration": duration,
                "score": score,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            time.sleep(0.5)  # 模拟稍微等待

        self.record_results(results)
        self.on_done()

    def stop(self):
        self._is_running = False
        self.executor.shutdown(wait=True)

    def calculate_score(self, duration):
        base_time = 1
        score = max(0, 1000 * (base_time / (duration + 0.0001)))
        return round(score, 2)

    # 测试项定义
    def single_core_test(self):
        return timeit.timeit("sum(range(1000000))", number=50)

    def multi_core_test(self):
        start_time = time.time()
        futures = [self.executor.submit(cpu_intensive_task, i) for i in range(psutil.cpu_count(logical=True))]
        for future in futures:
            future.result()
        end_time = time.time()
        return end_time - start_time

    def cpu_usage_test(self):
        return psutil.cpu_percent(interval=1)

    def float_operations_test(self):
        matrix_size = 500
        A = np.random.rand(matrix_size, matrix_size)
        B = np.random.rand(matrix_size, matrix_size)
        start = time.time()
        np.dot(A, B)
        end = time.time()
        return end - start

    def memory_test(self):
        memory_size = 100000
        data = list(range(memory_size))
        start = time.time()
        sum(data)
        end = time.time()
        return end - start

    def thread_switching_test(self):
        start = time.time()
        for _ in range(10000):
            pass
        end = time.time()
        return end - start

    def disk_io_test(self):
        start = time.time()
        with open("test_file", "wb") as f:
            f.write(os.urandom(1024 * 1024 * 5))  # 写入 5MB 随机数据
        end = time.time()
        os.remove("test_file")
        return end - start

    def random_number_test(self):
        start = time.time()
        [random.random() for _ in range(1000000)]
        end = time.time()
        return end - start

    def latency_test(self):
        start = time.time()
        time.sleep(1)
        end = time.time()
        return end - start

    def matrix_operations_test(self):
        matrix_size = 2000
        A = np.random.rand(matrix_size, matrix_size)
        start = time.time()
        np.linalg.inv(A)
        end = time.time()
        return end - start

    def prime_generation_test(self):
        start = time.time()
        primes = []
        for possiblePrime in range(2, 50000):
            isPrime = True
            for num in range(2, int(possiblePrime ** 0.5) + 1):
                if possiblePrime % num == 0:
                    isPrime = False
                    break
            if isPrime:
                primes.append(possiblePrime)
        end = time.time()
        return end - start

    def sorting_test(self):
        start = time.time()
        data = [random.randint(0, 100000) for _ in range(10000)]
        sorted(data)
        end = time.time()
        return end - start

    def compression_test(self):
        import zlib
        data = os.urandom(1024 * 1024 * 5)  # 5MB 随机数据
        start = time.time()
        zlib.compress(data)
        end = time.time()
        return end - start

    def decompression_test(self):
        import zlib
        data = os.urandom(1024 * 1024 * 5)
        compressed = zlib.compress(data)
        start = time.time()
        zlib.decompress(compressed)
        end = time.time()
        return end - start

    def hashing_test(self):
        import hashlib
        data = os.urandom(1024 * 1024 * 5)
        start = time.time()
        hashlib.sha256(data).hexdigest()
        end = time.time()
        return end - start

    def file_read_test(self):
        with open("test_file_read", "wb") as f:
            f.write(os.urandom(1024 * 1024 * 5))  # 写入 5MB 随机数据
        start = time.time()
        with open("test_file_read", "rb") as f:
            f.read()
        end = time.time()
        os.remove("test_file_read")
        return end - start

    def file_write_test(self):
        start = time.time()
        with open("test_file_write", "wb") as f:
            f.write(os.urandom(1024 * 1024 * 5))  # 写入 5MB 随机数据
        end = time.time()
        os.remove("test_file_write")
        return end - start

    def memory_allocation_test(self):
        start = time.time()
        data = [None] * 1000000
        end = time.time()
        return end - start

    def context_switch_test(self):
        start = time.time()
        for _ in range(10000):
            pass
        end = time.time()
        return end - start

    def cpu_task_switching_test(self):
        start = time.time()
        for _ in range(10000):
            pass
        end = time.time()
        return end - start


# 界面创建和优化部分
class PerformanceTesterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("性能测试器")
        self.root.geometry("600x600")  # 修改窗口尺寸

        self.selected_tests = [IntVar(value=1) for _ in range(20)]  # 20个测试选项

        self.create_widgets()
        self.progress_value = 0
        self.history_data = []

    def create_widgets(self):
        self.label = Label(self.root, text="性能测试器", font=("Arial", 18, "bold"), fg="blue")
        self.label.pack(pady=10)

        test_names = [
            "Single-core calculation (Timeit)", "Multi-core calculation (Multiprocessing)",
            "CPU Usage (%)", "Floating Point Operations (Matrix)", "Memory Read Performance",
            "Thread Switching Performance", "Disk I/O (Write Speed)", "Random Number Generation",
            "Latency Test", "Matrix Operations (Numpy)", "Prime Number Generation",
            "Sorting Algorithm Performance", "Compression Test (zlib)", "Decompression Test (zlib)",
            "SHA256 Hashing Performance", "File Read Performance", "File Write Performance",
            "Memory Allocation Speed", "Context Switching", "CPU Task Switching Latency"
        ]

        # 使用表格布局，让界面更加整齐
        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        for i, test_name in enumerate(test_names):
            Checkbutton(frame, text=test_name, variable=self.selected_tests[i]).grid(row=i // 2, column=i % 2, sticky="w")

        self.progress_var = StringVar()
        self.progress_label = Label(self.root, textvariable=self.progress_var, font=("Arial", 12))
        self.progress_label.pack(pady=10)

        # 添加进度条
        self.progress_bar = ttk.Progressbar(self.root, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=10)

        self.run_button = Button(self.root, text="开始测试", command=self.start_test, bg="green", fg="white", font=("Arial", 12, "bold"))
        self.run_button.pack(pady=10)

        self.results_text = Text(self.root, height=10, width=80, wrap="word")
        self.results_text.pack(pady=10)

    def start_test(self):
        self.results_text.delete(1.0, "end")
        self.progress_var.set("测试进行中...")
        self.progress_bar["value"] = 0
        self.run_button.config(state="disabled")
        self.worker = CpuTestWorker(self.update_progress, self.update_results, self.on_done, self.record_results, self.selected_tests)
        self.worker.start()

    def update_progress(self, value):
        self.progress_var.set(f"测试进度: {value}%")
        self.progress_bar["value"] = value

    def update_results(self, result_text, score):
        self.results_text.insert("end", f"{result_text}, Score: {score}\n")

    def on_done(self):
        self.progress_var.set("测试完成！")
        self.run_button.config(state="normal")

    def record_results(self, results):
        self.history_data.extend(results)


if __name__ == "__main__":
    root = Tk()
    app = PerformanceTesterApp(root)
    root.mainloop()
