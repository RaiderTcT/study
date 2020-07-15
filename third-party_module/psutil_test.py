import psutil
# process and system utilities
# 监控系统运行状态
# cpu 逻辑核心
print('-----------cpu逻辑核心数-----------')
print(psutil.cpu_count())
# cpu 物理核心
print('-----------cpu物理核心数-----------')
print(psutil.cpu_count(logical=False))
# cpu 频率
print('-----------cpu的频率-----------')
print(psutil.cpu_freq())
# cpu 利用率
print('-----------cpu利用率-----------')
print(psutil.cpu_percent())
# 统计CPU的用户／系统／空闲时间
print(psutil.cpu_times())
for i in range(3):
    print(psutil.cpu_percent(interval=1, percpu=True))
# 物理内存 RAM 字节为单位
print('-----------物理内存-----------')
print(psutil.virtual_memory())
# 交换内存 Unix/Linux系统前台与后台之间数据交换的场所
# linux会在物理内存不足时，使用交换分区的虚拟内存
# 内核会将暂时不用的内存块信息写到交换空间，
# 这样一来，物理内存得到了释放，这块内存就可以用于其它目的，
# 当需要用到原始的内容时，这些信息会被重新从交换空间读入物理内存
print('-----------交换内存-----------')
print(psutil.swap_memory())
# 获取磁盘信息
print('-----------磁盘分区-----------')
print(psutil.disk_partitions())
# 获取磁盘使用率
print('-----------磁盘使用率-----------')
# print(psutil.disk_usage('c:'))
# 当前磁盘总容量
print(psutil.disk_usage('/'))
# 获取磁盘IO信息
print('-----------磁盘IO-----------')
print(psutil.disk_io_counters())
# 获取网络接口和网络连接信息
print('-----------网络接口-----------')
print(psutil.net_io_counters())
print('-----------网络连接-----------')
print(psutil.net_connections())

# 获取进程信息
print('-----------进程-----------')
print(psutil.pids())
p = psutil.Process(19508)
print('-----------进程名-----------')
print(p.name())
print('-----------进程路径-----------')
print(p.exe())
print('-----------进程工作目录-----------')
print(p.cwd())
print('-----------进程启动的命令行-----------')
print(p.cmdline())
print('-----------父进程id-----------')
print(p.ppid())
print('-----------父进程-----------')
print(p.parent())
print('-----------子进程-----------')
print(p.children())
print('-----------进程用户名-----------')
print(p.username())
print('-----------进程创建时间-----------')
print(p.create_time())
print('-----------进程终端-----------')
# linux or unix
# print(p.terminal())
print('-----------进程使用cpu的时间-----------')
print(p.cpu_times())
print('-----------进程使用的内存-----------')
print(p.memory_info())
print('-----------进程打开的文件-----------')
print(p.open_files())
print('-----------进程相关网络连接-----------')
print(p.connections())
print('-----------进程下的线程-----------')
print(p.threads())
print('-----------进程环境变量-----------')
print(p.environ())
print('-----------进程结束-----------')
# print(p.terminate())
print('------------模拟任务管理器-----------')
print(psutil.test())
