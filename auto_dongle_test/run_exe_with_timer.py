import subprocess
import threading
import time

def run_exe_with_timeout(exe_path, timeout):
    # 启动exe程序
    process = subprocess.Popen(exe_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    # 定义一个线程来监视程序的执行时间
    def monitor():
        nonlocal process
        time.sleep(timeout)
        if process.poll() is None:  # 如果程序还在运行
            print("Timed out, terminating the process...")
            process.terminate()  # 强制退出程序
            try:
                # 等待程序终止，获取输出信息
                # output = process.communicate()[0]
                # print("Output from the process:")
                # print(output)
                # with open("exe_path_print_out.txt",'w') as f:
                    # f.write(output)
                pass
            except Exception as e:
                print(f"An error occurred: {e}")

    # 创建并启动监视线程
    monitor_thread = threading.Thread(target=monitor)
    monitor_thread.start()

    # 等待程序执行完成或被强制退出
    process.wait()
    monitor_thread.join()

    output = process.communicate()[0]
    with open("exe_path_print_out.txt",'w') as f:
        f.write(output)

# 调用函数，设置exe路径和超时时间
exe_path = 'D:/LandApp_make_installation_package/LandSAR_v1.3.3_beta/InSAR_Console.exe config_loooooop.txt'  # 替换为你的exe文件路径
timeout = 2  # 设置超时时间为10秒

run_exe_with_timeout(exe_path, timeout)