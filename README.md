# leather
ive tried replacing the snap7.dll file and the snap7.lib file from a 32bit to a 64 bit.Using the edit system variables tool ive managed to edit the file location of the snap7.dll file and the snap7.lib file in python but despite all these solutions that i have found online i still end up with either a syntax error or this error code:
C:\Users\asus\PycharmProjects\untitled2\venv\Scripts\python.exe C:/Users/asus/PycharmProjects/untitled2/hello.py
b'CPU : Item not available'
Traceback (most recent call last):
File "C:/Users/asus/PycharmProjects/untitled2/hello.py", line 12, in
plc_info = plc.get_cpu_info()
File "C:\Users\asus\PycharmProjects\untitled2\venv\lib\site-packages\snap7\client.py", line 105, in get_cpu_info
check_error(result, context="client")
File "C:\Users\asus\PycharmProjects\untitled2\venv\lib\site-packages\snap7\common.py", line 66, in check_error
raise Snap7Exception(error)
snap7.exceptions.Snap7Exception: b'CPU : Item not available'
