# Bluetooth Proximity Detection

Python code for getting the RSSI value of a Bluetooth device by address. Based on the value returned, can determine the proximity of the device.


## Requirements

This code requires the `bluetooth` and `python-bluez` modules to be installed. On Ubuntu/Debian systems, this can usually be done with the following commands:

```
sudo apt-get install bluetooth
sudo apt-get install python-bluez
```

## Example

```python
from bluetooth_rssi import BluetoothRSSI

BT_ADDR = "C4:36:8D:29:34:CE"  # You can put your Bluetooth address here

def main():
    bt_rssi = BluetoothRSSI(addr=BT_ADDR)
    print(bt_rssi.get_rssi())

if __name__ == "__main__":
    main()

```
