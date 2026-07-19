#Name: Adamtey Alan Nene Terkpeh
#EL 1A FOE.41.006.010.25
class SmartDevice:
    def __init__(self, name, device_id):
        self.name = name
        self.__device_id = device_id
        self.__power_status = False

    def get_device_id(self):
        return self.__device_id

    def set_device_id(self, device_id):
        if device_id != "":
            self.__device_id = device_id
        else:
            print("Device ID cannot be empty.")

    def get_power_status(self):
        return self.__power_status

    def set_power_status(self, status):
        self.__power_status = status

    def turn_on(self):
        self.__power_status = True
        print("The", self.name, "device is now on")

    def turn_off(self):
        self.__power_status = False
        print("The", self.name, "device is now off")

    def display_info(self):
        print("\n----- DEVICE INFORMATION -----")
        print("Device Name :", self.name)
        print("Device ID   :", self.__device_id)
        print("Power Status:", "ON" if self.__power_status else "OFF")


class TemperatureSensor(SmartDevice):
    def __init__(self, name, device_id, temperature):
        super().__init__(name, device_id)
        self.temperature = temperature

    def read_temperature(self):
        ans1 = input("Please, do you want to read the temperature?[yes/no] ")
        if ans1.lower() == "yes":
            print("The room's temperature is ", self.temperature, "°C")
        elif ans1.lower() == "no":
            print("Temperature reading aborted")

    def display_info(self):
        super().display_info()
        print("Temperature :", self.temperature, "°C")


class SecurityCamera(SmartDevice):
    def __init__(self, name, device_id, recording_status):
        super().__init__(name, device_id)
        self.recording_status = recording_status

    def start_recording(self):
        ans2 = input("Please, do you want to start recording?[yes/no] ")
        if ans2.lower() == "yes":
            self.recording_status = True
            print("Scene is being recorded")
        elif ans2.lower() == "no":
            self.recording_status = False
            print("Recording is aborted")

    def stop_recording(self):
        ans3 = input("Scene is being recorded, are you sure you want to stop recording?[yes/no] ")
        if ans3.lower() == "yes":
            self.recording_status = False
            print("Recording has stopped")
        elif ans3.lower() == "no":
            print("Recording is continuing")

    def display_info(self):
        super().display_info()
        print("Recording :", "YES" if self.recording_status else "NO")


class SmartLight(SmartDevice):
    def __init__(self, name, device_id, brightness):
        super().__init__(name, device_id)
        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            self.brightness = 50

    def increase_brightness(self):
        ans4 = input("Do you want to increase the brightness? [yes/no]: ")
        if ans4.lower() == "yes":
            level = int(input("Enter the new brightness level (0-100): "))
            if level > 100:
                print("Brightness cannot exceed 100%.")
            elif level < self.brightness:
                print("Brightness must be greater than current brightness.")
            else:
                self.brightness = level
                print(f"Brightness has been increased to {self.brightness}%.")
        else:
            print("Brightness was not changed.")

    def decrease_brightness(self):
        ans = input("Do you want to decrease the brightness? [yes/no]: ")
        if ans.lower() == "yes":
            level = int(input("Enter the new brightness level (0-100): "))
            if level < 0:
                print("Brightness cannot be less than 0%.")
            elif level > self.brightness:
                print("Brightness must be less than current brightness.")
            else:
                self.brightness = level
                print(f"Brightness has been decreased to {self.brightness}%.")
        else:
            print("Brightness was not changed.")

    def display_info(self):
        super().display_info()
        print("Brightness  :", self.brightness, "%")



light = SmartLight("Porchlight", 3423, 30)
cctv = SecurityCamera("Veranda cctv", 34583, True)
TempSensor = TemperatureSensor("HeatSensor 1", 345867657, 10)

while True:
    print("\n~~~~~~~~~~~ SMART DEVICE MANAGEMENT ~~~~~~~~~")
    print("1. Display Device Info")
    print("2. Turn ON  Device")
    print("3. Turn  OFF Device")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start/Stop Recording")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        light.display_info()
        cctv.display_info()
        TempSensor.display_info()

    elif choice == "2":
        print("\n1. Smart Light")
        print("2. Security Camera")
        print("3. Temperature Sensor")
        device = input("Choose device: ")

        if device == "1":
            light.turn_on()
        elif device == "2":
            cctv.turn_on()
        elif device == "3":
            TempSensor.turn_on()
        else:
            print("Invalid choice.")

    elif choice == "3":
        print("\n1. Smart Light")
        print("2. Security Camera")
        print("3. Temperature Sensor")
        device = input("Choose device: ")

        if device == "1":
            light.turn_off()
        elif device == "2":
            cctv.turn_off()
        elif device == "3":
            TempSensor.turn_off()
        else:
            print("Invalid choice.")

    elif choice == "4":
        TempSensor.read_temperature()

    elif choice == "5":
        print("\n1. Increase Brightness")
        print("2. Decrease Brightness")
        option = input("Choose option: ")

        if option == "1":
            light.increase_brightness()
        elif option == "2":
            light.decrease_brightness()
        else:
            print("Invalid choice.")

    elif choice == "6":
        print("\n1. Start Recording")
        print("2. Stop Recording")
        option = input("Choose option: ")

        if option == "1":
            cctv.start_recording()
        elif option == "2":
            cctv.stop_recording()
        else:
            print("Invalid choice.")

    elif choice == "7":
        print("Thank you for using Smart Device Management System.")
        break
    else:
        print("Invalid choice.")
