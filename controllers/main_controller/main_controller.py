from controller import Robot
import threading

class MotorController:
    def __init__(self, angle_instructions, velocity_instructions):
        self.robot = Robot()
        self.angle_instructions = angle_instructions
        self.velocity_instructions = velocity_instructions
        self.motor_names = ['Joint-11', 'Joint-12', 'Joint-13', 'Joint-14']
        self.motors = [self.robot.getDevice(name) for name in self.motor_names]
    
    @staticmethod
    def angle_conversion(angle):
        return angle / 180 * 3.14
    
    def target_execution(self, motor, pos, vel):
        motor.setPosition(pos)
        motor.setVelocity(vel)

    def run(self):
        threads = []
        for i, motor in enumerate(self.motors):
            angle_rad = self.angle_conversion(self.angle_instructions[i])
            vel = velocity_instructions[i]
            thread = threading.Thread(target=self.target_execution, args=(motor, angle_rad, vel), name='Thread_' + str(i))
            threads.append(thread)
            thread.start()
        
        for thread in threads:
            thread.join()
if __name__ == "__main__":
    angle_instructions = [90, 30, 90, 0]
    velocity_instructions = [0.5, 0, 0, 0]
    motor_controller = MotorController(angle_instructions, velocity_instructions)
    motor_controller.run()
# from controller import Robot
# import threading

# robot = Robot()
# angle_instruction = 45

# class MotorController:

# class MotorController:
#     def __init__(self, angle_instruction):
#         self.robot = Robot()
#         self.angle_instruction = angle_instruction
#         self.motor_name = [ 'Joint-11', 'Joint-12', 'Joint-13', 'Joint-14']
#         self.motors = [self.robot.getDevice(name) for name in self.motor_name]
#         self.i = 0
#         self.robot.run()
    
#     def angle_conversion(angle):
#         return angle/180*3.14
    
#     def target_execution(motor, pos, vel):
#         motor.setPosition(pos)
#         motor.setVelocity(vel)

#     def run(self):
#         for motor in self.motors:
#             threading.Thread(target= self.target_execution(motor, self.angle_conversion(self.angle_instruction[self.i]), 0.2), name = 'Thread_'+str(self.i))
#             self.i = self.i+1
            
# MotorController([180,0,0,0])
#     def __init__(self, angle_instruction):
#         self.target_position = angle_instruction / 180 * 3.14
#         self.motor_names = ["Joint-11", "Joint-31"]
#                             # "Joint-21", "Joint-22", "Joint-23", "Joint-24",
#                             # "Joint-31", "Joint-32", "Joint-33", "Joint-34",
#                             # "Joint-41", "Joint-42", "Joint-43", "Joint-44"]

#         self.motors = [robot.getDevice(name) for name in self.motor_names]
#         for motor in self.motors:
#             position_sensor = motor.getPositionSensor()
#             position_sensor.enable(64)
#             motor.setPosition(float('inf'))

#     @staticmethod
#     def angle_conversion(angle):
#         return angle / 180 * 3.14

#     @staticmethod
#     def target(motor, target_position, error):
#         motor.setVelocity(target_position)
#         motor.setVelocity(error * 0.2)

#     def run(self):
#         for motor in self.motors:
#             position_sensor = motor.getPositionSensor()
#             current_position = position_sensor.getValue()
#             error = self.target_position - current_position

#             if abs(error) < 0.01:
#                 motor.setVelocity(0)
#             else:
#                 thread = threading.Thread(target=self.target, args=(motor, self.target_position, error))
#                 thread.start()


# motor_controller = MotorController(angle_instruction)

# while robot.step(64) != -1:
#     motor_controller.run()
#     angle_instruction = -45
#     motor_controller.run()

# from controller import Robot
# import time
# import threading

# # 創建機器人實
# robot = Robot()

# # 獲取馬達
# motor = robot.getMotor("Joint-11")  # 請將 "motor_name" 替換為您的馬達的名稱

# # 設置目標角度
# target_angle = -3.14  # 例如，將目標角度設置為1.57弧度（約90度）
# target_velocity = 0.1
# # 將馬達移動到目標角度
# motor.setPosition(target_angle)
# motor.setVelocity(target_velocity)
# time.sleep(1)
# motor.setPosition(3.14)
# motor.setVelocity(0.5)

# # 開始運行
# robot.run()

