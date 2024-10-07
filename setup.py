from setuptools import setup, find_packages

setup(
    name="bluetooth_rssi",
    version="0.0.1",
    description="Detects if a Bluetooth device is near by querying its RSSI value",
    url="https://github.com/null-none/bluetooth-rssi",
    packages=find_packages(),
    zip_safe=False,
)
