"""
Module: 'pycom' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2
from typing import overload
import machine

FACTORY = 0
FAT = 0
LittleFS = 1
OTA_0 = 1

def create_128bit_le_uuid_from_string():
    pass

def pybytes_device_token():
    pass

def pybytes_extra_preferences():
    pass

def pybytes_force_update():
    pass

def pybytes_lte_config():
    pass

def pybytes_mqttServiceAddress():
    pass

def pybytes_network_preferences():
    pass

def pybytes_userId():
    pass


@overload
def heartbeat() -> bool:
    '''
    Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and returns boolean values.
    
    '''
    ...

@overload
def heartbeat(boolean: bool):
    '''
    Get or set the state (enabled or disabled) of the heartbeat LED. Accepts and returns boolean values.
    
    '''
    ...


@overload
def rgbled() -> int:
    '''
    Get or set the colour of the RGB LED. The colour is specified as 24 bit value representing red, green and blue, in the following order `0xRRGGBB` . For instance, passing the value `0x00FF00` will light up the LED in a very bright green. If no color is provided, this will return the current color of the LED.
    
    '''
    ...

@overload
def rgbled(color: int):
    '''
    Get or set the colour of the RGB LED. The colour is specified as 24 bit value representing red, green and blue, in the following order `0xRRGGBB` . For instance, passing the value `0x00FF00` will light up the LED in a very bright green. If no color is provided, this will return the current color of the LED.
    
    '''
    ...


def nvs_set(key, value: int):
    '''
    Set the value of the specified key in the NVRAM memory area of the external flash. Data stored here is preserved across resets and power cycles. Value can only take 32-bit integers at the moment. Example:
    
    '''
    ...


def nvs_get(key) -> None | int:
    '''
    Get the value the specified key from the NVRAM memory area of the external flash. Example:
    
    
    If a non-existing key is given the returned value will be `None` .
    
    '''
    ...


def nvs_erase(key):
    '''
    Erase the given key from the NVRAM memory area.
    
    '''
    ...


def nvs_erase_all():
    '''
    Erase the entire NVRAM memory area.
    
    '''
    ...


def pulses_get(pin: machine.Pin, timeout: int) -> list[tuple]:
    '''
    Return a list of pulses at `pin` . The methods scans for transitions at `pin` and returns a list of tuples, each telling the pin value and the duration in microseconds of that value. `pin` is a pin object, which must have set to `IN` or `OPEN_DRAIN` mode. The scan stops if no transitions occur within `timeout` milliseconds.
    
    Example:
    
    ```python
    # get the raw data from a DHT11/DHT22/AM2302 sensor
    from machine import Pin
    from pycom import pulses_get
    from time import sleep_ms
    
    pin = Pin("G7", mode=Pin.OPEN_DRAIN)
    pin(0)
    sleep_ms(20)
    pin(1)
    data = pulses_get(pin, 100)
    ```
    '''
    ...


def get_free_heap() -> int:
    '''
    Returns the free heap bytes in the memory allocation
    '''
    ...


@overload
def sigfox_info() -> bool:
    '''
    With no arguments, this function will return if the SigFox settings on the device are valid.
    
    With arguments, the specified keys will be set.
    '''
    ...

@overload
def sigfox_info(id, pac, publickey, privatekey):
    '''
    With no arguments, this function will return if the SigFox settings on the device are valid.
    
    With arguments, the specified keys will be set.
    '''
    ...


@overload
def pybytes_on_boot(boolean: bool):
    '''
    Get or set the activation of pybytes on boot.
    
    '''
    ...


@overload
def heartbeat_on_boot(boolean: bool):
    '''
    Allows you permanently disable or enable the heartbeat LED. Once this setting is set, it will persist between reboots. Note, this only comes into effect on the next boot, it does not stop the already running heartbeat.
    
    '''
    ...


@overload
def lte_modem_en_on_boot(boolean: bool):
    '''
    Get or set the LTE modem on boot flag. When this flag is set to `True` , the LTE modem will be enabled.
    
    '''
    ...


@overload
def wifi_on_boot(boolean: bool):
    '''
    Get or set the WiFi on boot flag. When this flag is set to `True` , The WiFi will be enabled according to the other WiFi settings. when `False` the WiFi module will be disabled until enabled directly via WLAN class. This setting is stored in the non-volatile memory which preserves it across resets and power cycles. See FTP & Telnet for more information on possible usage.
    
    '''
    ...


@overload
def wifi_mode_on_boot(mode: int):
    '''
    Set or get the Wifi Mode at startup, valid options are:
    - `WLAN.STA` 
    - `WLAN.AP` 
    - `WLAN.APSTA` 
    This setting is stored in non-volatile memory which preserves it across resets and power cycles 
    '''
    ...


@overload
def wifi_ssid_sta(ssid: str):
    '''
    Get or set the ssid of the Access Point the device should connect to on startup.
    This setting is stored in non-volatile memory which preserves it across resets and power cycles
    '''
    ...


@overload
def wifi_ssid_ap(ssid: str):
    '''
    Get or set the ssid of the Access point that should be started by the device at startup, if not set and startup Wifi mode is AP the default AP name ( `xxpy-wlan-####` ) will be used. This setting is stored in non-volatile memory which preserves it across resets and power cycles.
    
    '''
    ...


@overload
def wifi_pwd_sta(key: str):
    '''
    Get or set the Password of the Access point the device should connect to on startup, leave the password unset if the AP is open.This setting is stored in non-volatile memory which preserves it across resets and power cycles
    
    '''
    ...


@overload
def wifi_pwd_ap(key: str):
    '''
    Get or set the Password of the Access point that should be started by the device at startup, leave unset if the AP should be open.This setting is stored in non-volatile memory which preserves it across resets and power cycles
    
    '''
    ...


@overload
def pybytes_on_boot() -> bool:
    '''
    Get or set the activation of pybytes on boot.
    
    '''
    ...


@overload
def heartbeat_on_boot() -> bool:
    '''
    Allows you permanently disable or enable the heartbeat LED. Once this setting is set, it will persist between reboots. Note, this only comes into effect on the next boot, it does not stop the already running heartbeat.
    
    '''
    ...


@overload
def lte_modem_en_on_boot() -> bool:
    '''
    Get or set the LTE modem on boot flag. When this flag is set to `True` , the LTE modem will be enabled.
    
    '''
    ...


@overload
def wifi_on_boot() -> bool:
    '''
    Get or set the WiFi on boot flag. When this flag is set to `True` , The WiFi will be enabled according to the other WiFi settings. when `False` the WiFi module will be disabled until enabled directly via WLAN class. This setting is stored in the non-volatile memory which preserves it across resets and power cycles. See FTP & Telnet for more information on possible usage.
    
    '''
    ...


@overload
def wifi_mode_on_boot() -> int:
    '''
    Set or get the Wifi Mode at startup, valid options are:
    - `WLAN.STA` 
    - `WLAN.AP` 
    - `WLAN.APSTA` 
    This setting is stored in non-volatile memory which preserves it across resets and power cycles 
    '''
    ...


@overload
def wifi_ssid_sta() -> str:
    '''
    Get or set the ssid of the Access Point the device should connect to on startup.
    This setting is stored in non-volatile memory which preserves it across resets and power cycles
    '''
    ...


@overload
def wifi_ssid_ap() -> str:
    '''
    Get or set the ssid of the Access point that should be started by the device at startup, if not set and startup Wifi mode is AP the default AP name ( `xxpy-wlan-####` ) will be used. This setting is stored in non-volatile memory which preserves it across resets and power cycles.
    
    '''
    ...


@overload
def wifi_pwd_sta() -> str:
    '''
    Get or set the Password of the Access point the device should connect to on startup, leave the password unset if the AP is open.This setting is stored in non-volatile memory which preserves it across resets and power cycles
    
    '''
    ...


@overload
def wifi_pwd_ap() -> str:
    '''
    Get or set the Password of the Access point that should be started by the device at startup, leave unset if the AP should be open.This setting is stored in non-volatile memory which preserves it across resets and power cycles
    
    '''
    ...


@overload
def smart_config_on_boot() -> bool:
    '''
    Read or (Enable/Disable) SmartConfig functionality on startup, this flag will be reset after successful completion of the smartConfig process after startup.This setting is stored in non-volatile memory which preserves it across resets and power cycles
    
    '''
    ...

@overload
def smart_config_on_boot(boolean: bool):
    '''
    Read or (Enable/Disable) SmartConfig functionality on startup, this flag will be reset after successful completion of the smartConfig process after startup.This setting is stored in non-volatile memory which preserves it across resets and power cycles
    
    '''
    ...

@overload
def wdt_on_boot_timeout() -> int:
    '''
    Sets or gets the WDT on boot timeout in milliseconds. The minimum value is 5000 ms.
    '''
    ...

@overload
def wdt_on_boot_timeout(timeout: int):
    '''
    Sets or gets the WDT on boot timeout in milliseconds. The minimum value is 5000 ms.
    '''
    ...


def wdt_on_boot(enable: bool):
    '''
    Enables the WDT at boot time with the timeout in ms set by the function `wdt_on_boot_timeout` . If this flag is set, the application needs to reconfigure the WDT with a new timeout and feed it regularly to avoid a reset
    '''
    ...


def bootmgr(boot_partition=FACTORY, fs_type=FAT, safeboot=False, reset=False):
    '''
    - `boot_partition` This is to set the partition to boot from , this could be set to either:
      - `pycom.FACTORY` : The factory boot partition. 
      - `pycom.OTA_0` : The OTA boot partition 
    - `fs_type` This is to set the filesystem to use for the flash memory ( `/flash` ). This could be set to
      - `pycom.FAT` for the FatFS (FAT16) filesystem. 
      - `pycom.LittleFS` for LittleFS filesystem. 
    
    --------
    Note: When the firmware is built with option `FS_USE_LITTLEFS` the file system for `/flash` is forced to be LittleFS.
    
    - `safeboot` Enable or Disable safemoot mode. 
    - `reset` Set `True` to reset target after updating the `bootmgr` options, `False` for not resetting. 
    '''
    ...


def ota_start():
    '''
     
    '''
    ...


def ota_write(buffer):
    '''
     
    '''
    ...


def ota_finish():
    '''
     
    '''
    ...


def ota_slot():
    '''
     
    '''
    ...


def ota_verify():
    '''
    Perform a firmware update. These methods are internally used by a firmware update through FTP. The update starts with a call to `ota_start()` , followed by a series of calls to `ota_write(buffer)` , and is terminated with `ota_finish()` . After reset, the new image gets active. `buffer` shall hold the image data to be written, in arbitrary sizes. A block size of 4096 is recommended.
    
    
    Example:
    
    ```python
    # Firmware update by reading the image from the SD card
    #
    from pycom import ota_start, ota_write, ota_finish
    from os import mount
    from machine import SD
    
    BLOCKSIZE = const(4096)
    APPIMG = "/sd/appimg.bin"
    
    sd = SD()
    mount(sd, '/sd')
    
    with open(APPIMG, "rb") as f:
       buffer = bytearray(BLOCKSIZE)
       mv = memoryview(buffer)
       size=0
       ota_start()
       while True:
           chunk = f.readinto(buffer)
           if chunk > 0:
               ota_write(mv[:chunk])
               size += chunk
               print("\r%7d " % size, end="")
           else:
               break
       ota_finish()
    ```
    Instead of reading the data to be written from a file, it can obviously also be received from a server using any suitable protocol, without the need to store it in the devices file system.
    
    
    --------
    For more information about the OTA process, go here
    
    
    '''
    ...


def diff_update_enabled() -> bool:
    '''
    Provides the status of the differential update feature. Returns `True` if differential update is enabled and `False` otherwise. `DIFF_UPDATE_ENABLED` build flag can be used to enable the differential update feature.
    
    
    --------
    Note: This function is only available in the firmware versions which support differential update feature. If you get an exception while calling this function, your firmware version does not support this feature.
    '''
    ...
