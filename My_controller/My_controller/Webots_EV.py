import subprocess
import time

def start_webots():
    # 指定Webots的安裝路徑
    webots_path = '/path/to/webots'

    # 啟動Webots進程
    subprocess.Popen([webots_path])

def load_world(world_file):
    # 等待Webots啟動
    time.sleep(5)  # 根據實際情況調整等待時間

    # 載入世界文件
    subprocess.run(['webots', '--batch', world_file])

def reload_world():
    # 等待一段時間確保Webots已經載入世界文件
    time.sleep(5)  # 根據實際情況調整等待時間

    # 重新加載世界文件
    subprocess.run(['webots', '--batch', '--world', '--mode=fast', '--run-service', 'simulation reset'])

def set_robot_position(robot_name, x, y, z):
    # 等待一段時間確保Webots已經載入世界文件
    time.sleep(5)  # 根據實際情況調整等待時間

    # 設置機器人的位置
    subprocess.run(['webots', '--batch', '--world', '--mode=fast', '--run-service', f'{robot_name}.set_translation {x} {y} {z}'])

if __name__ == "__main__":
    # 啟動Webots
    start_webots()

    # 載入環境和機器人
    load_world('/path/to/your/world_file.wbt')

    # 設置機器人的位置
    set_robot_position('robot_name', x=1.0, y=0.0, z=0.5)  # 替換'robot_name'為你的機器人名稱，並設置所需的位置坐標
    # 重新加載環境
    reload_world()