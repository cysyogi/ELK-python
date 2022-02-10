from datetime import datetime
from random import randrange

def gen_data(no_of_devices = 3):
    data = []
    now = datetime.now()
    # now = now.strftime("%m/%d/%Y, %H:%M:%S")
    for j in range(0, no_of_devices):
        record = {
            'deviceId' : "RaspberryPi{}".format(j),
            'dateTime' : now,
            'temperature': randrange(25,31),
            'humdity': randrange(18,21),
            'pressure': randrange(97,100),
            'moisture' : randrange(0,60),
            'VOC': randrange(1,10000),
            'C02': randrange(18,22),
            'gas': randrange(1,30),
            'radon': randrange(1,255),
        }
        data.append(record)
    return data
if __name__ == '__main__':
    print(gen_data())

