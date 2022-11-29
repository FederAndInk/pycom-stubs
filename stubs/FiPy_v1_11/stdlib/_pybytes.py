"""
The Pybytes library is positioned in the [frozen](https://docs.pycom.io/advance/frozen/) section of the firmware.

It can be imported like regular modules:

```python
from _pybytes import Pybytes
from _pybytes_config import PybytesConfig
conf = PybytesConfig().read_config()
pybytes = Pybytes(conf)

pybytes.start()
```

Or start the connection to Pybytes on boot, this way it’s always available:

```python
import pycom
import machine
pycom.pybytes_on_boot(True)
machine.reset()
```

Debugging:

Enable debugging if you are having any issues. There are multiple debug levels, the lowest is 0 which is for warnings only and 99 is the highest used and will print more debugging messages
use:

```python
import pycom;
pycom.nvs_set('pybytes_debug', debugLevel)
```

e.g.

```python
import pycom;
pycom.nvs_set('pybytes_debug', 99)
```
"""


class Pybytes:
    def __init__(self, conf: dict) -> None:
        ...

    def activate(self, activationstring: str):
        '''
        Provision the device to Pybytes. Use the `activationstring` provided in Pybytes to activate the device.
        '''
        ...

    def read_config(self, filename='/flash/pybytes_config.json', reconnect=False):
        '''
        Load the Pybytes configuration file. By default, this is found in `/flash/pybytes_config.json` 
        '''
        ...

    def update_config(self, key, value=None, permanent=True, silent=False, reconnect=False):
        '''
        Update a `key` and `value` of the default configuration file. additional options:
        
        - `permanent` : will call `pybytes.write_config()` . If set `False` , the new value will not be stored in the configuration file and only used this session. 
        - `silent` : set `silent` to `True` to not print to REPL. 
        - `reconnect` : calls `pybytes.reconnect()`
        '''
        ...

    def set_config(self, key=None, value=None, permanent=True, silent=False, reconnect=False):
        '''
        Same as `update_config(...)` 
        '''
        ...

    def write_config(self, file='/flash/pybytes_config.json', silent=False):
        '''
        Writes the updated configuration to the default configuration file. The parameters:
        
        - `file` : The file name and location 
        - `silent` : set `silent` to `True` to not print to REPL. 
        '''
        ...

    def print_config(self):
        '''
        Print the configuration settings to the REPL.
        '''
        ...

    def connect(self):
        '''
        Connect the device to Pybytes following the loaded configuration file. You will need to load a configuration file before calling this. If you are using the WiFi or LTE connection, and it is already available, Pybytes will use the existing connection.
        '''
        ...

    def start(self, autoconnect=True):
        '''
        Same as `pybytes.connect()` , with the option to set `autoconnect` . Setting `autoconnect` to `False` will not start the connection immediately.
        '''
        ...

    def enable_lte(self, carrier=None, cid=None, band=None, apn=None, type=None, reset=None, fallback=False):
        '''
        Enable the LTE connection to pybytes. Enter the paramters you would normally enter for a LTE connection.
        '''
        ...

    def connect_lte(self):
        '''
        Connect to Pybytes using LTE and the settings from the configuration file.
        '''
        ...

    def connect_wifi(self):
        '''
        Connect to Pybytes using WiFi and the settings from the configuration file.
        '''
        ...

    def connect_sigfox(self):
        '''
        Connect to Pybytes using SigFox and the settings from the configuration file.
        '''
        ...

    def connect_lora_otaa(self, timeout=120, nanogateway=False):
        '''
        Connect to Pybytes using LoRa OTAA and the settings from the configuration file.
        '''
        ...

    def connect_lora_abp(self, timeout: int, nanogateway=False):
        '''
        Connect to Pybytes using LoRa ABP and the settings from the configuration file.
        '''
        ...

    def disconnect(self):
        '''
        Disconnect from Pybytes gracefully. Closes the MQTT connection and socket.
        '''
        ...

    def reconnect(self):
        '''
        Calls `pybytes.disconnect()` followed by `pybytes.connect()` 
        '''
        ...

    def isconnected(self):
        '''
        Returns the connection status to Pybytes, can be `True` or `False` .
        '''
        ...

    def is_connected(self):
        '''
        Same as `pybytes.isconnected()` 
        '''
        ...

    def enable_ssl(self):
        '''
        Enable SSL on the Pybytes connection
        
        --------
        Note that SSL might not be supported by your LTE connection
        '''
        ...

    def dump_ca(self, file='/flash/cert/pycom-ca.pem'):
        '''
        Write SSL certificate to file.
        '''
        ...

    def send_signal(self, signal_number: int, value):
        '''
        Send a signal to Pybytes. Arguments are:
        
        - `signal_number` : The signal number in Pybytes, can be any value between 0-254 (255 is reserved) 
        - `value` : The value you want to send, this can be any type. 
        
        --------
        This will also work in Pymesh.
        '''
        ...

    def send_ping_message(self):
        '''
        Sends a ping (is-alive) message to Pybytes.
        
        '''
        ...

    def send_info_message(self):
        '''
        Send an info message to Pybytes containing the device type and firmware version.
        '''
        ...

    def send_battery_level(self, battery_level: int):
        '''
        Sends the battery level to Pybytes. The argument `battery_level` can be any integer.
        
        You can define `battery_level` with a function depending on your shield. Check example code by visiting Reading Battery Voltage page.
        
        For example, using an Expansion Board 3.1, you can send battery level to Pybytes using the below code:
        
        ```python
        from machine import ADC
        def battery_level():
          adc = ADC()
          bat_voltage = adc.channel(attn=ADC.ATTN_11DB, pin='P16')
          vbat = bat_voltage.voltage()
          print('battery voltage:', vbat*2, 'mV')
          return vbat*2
        pybytes.send_battery_level(battery_level())
        ```
        '''
        ...

    def deepsleep(self, ms: int, pins=None, mode=None, enable_pull=None):
        '''
        See `machine.deepsleep()` for more details. Additionally, this method disconnects from Pybytes gracefully. The optional arguments operate `machine.pin_sleep_wakeup()`
        '''
        ...

    def smart_config(self):
        '''
        Allows for the usage of `smart_config()` , see `pycom.smart_config()` for more information [here](https://docs.pycom.io/firmwareapi/pycom/pycom/#pycomsmart_config_on_bootboolean)
        '''
        ...
