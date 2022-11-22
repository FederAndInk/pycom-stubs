"""
Module: 'network' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from collections.abc import Callable
from typing import Any, NamedTuple, overload

class GATTCCharacteristic:
    def uuid(self) -> int | bytes:
        '''
        Returns the UUID of the service. In the case of 16-bit or 32-bit long UUIDs, the value returned is an integer, but for 128-bit long UUIDs the value returned is a bytes object.
        
        '''
        ...


    def instance(self) -> int:
        '''
        Returns the instance ID of the service.
        
        '''
        ...


    def properties(self) -> int:
        '''
        Returns an integer indicating the properties of the characteristic. Properties are represented by bit values that can be OR-ed together. See the constants section for more details.
        
        '''
        ...


    def read(self) -> bytes:
        '''
        Read the value of the characteristic, sending a request to the GATT server. Returns a bytes object representing the characteristic value.
        
        '''
        ...


    def value(self) -> bytes:
        '''
        Returns the locally stored value of the characteristic without sending a read request to the GATT server. If the characteristic value hasn’t been read from the GATT server yet, the value returned will be 0.
        
        '''
        ...


    def write(self, value: bytes):
        '''
        Writes the given value on the characteristic. For now it only accepts bytes object representing the value to be written.
        
        ```python
        
        characteristic.write(b'x0f')
        ```
        '''
        ...

    def callback(self, trigger=None, handler: Callable[[Any], None] =None, arg=None):
        '''
        Creates a callback that will be executed when any of the triggers occur. The arguments are:
        
        
        
        - `trigger` can be `Bluetooth.CHAR_NOTIFY_EVENT`.
        
        - `handler` is the function that will be executed when the callback is triggered.
        
        - `arg` is the argument that gets passed to the callback. If nothing is given, the characteristic object that owns the callback will be used.
        
        
        
        Beyond the `arg` a tuple (called `data` ) is also passed to `handler` . The tuple consists of (event, value), where `event` is the triggering event and `value` is the value strictly belonging to the `event` .
        
        
        We recommend getting both the `event` and new `value` of the characteristic via this tuple, and not via `characteristic.event()` and `characteristic.value()` calls in the context of the `handler` to make sure no event and value is lost.
        The reason behind this is that `characteristic.event()` and `characteristic.value()` return with the very last event received and with the current value of the characteristic, while the input parameters are always linked to the specific event triggering the `handler` . If the device is busy executing other operations,  the `handler` of an incoming event may not be called before the next event occurs and is processed.
        
        
        Usage example can be found under GATTSCharacteristic page.
        
        '''
        ...


    def read_descriptor(self, uuid) -> None | bytes:
        '''
        Returns the value of the descriptor specified by the `uuid` parameter. If no descriptor found for the characteristic returns None.
        
        ```python
        descriptor = char.read_descriptor(0x2900)
        if(descriptor != None):
        print("Characteristic Extended Properties: " + str(binascii.hexlify((descriptor))))
        
        descriptor = char.read_descriptor(0x2901)
        if(descriptor != None):
        print("Characteristic User Description: " + str(binascii.hexlify((descriptor))))
        
        descriptor = char.read_descriptor(0x2902)
        if(descriptor != None):
        print("Client Characteristic Configuration: " + str(binascii.hexlify((descriptor))))
        
        descriptor = char.read_descriptor(0x2904)
        if(descriptor != None):
        print("Characteristic Presentation Format: " + str(binascii.hexlify((descriptor))))
        ```
        '''
        ...

class GATTCService:
    def isprimary(self) -> bool:
        '''
        Returns `True` if the service is a primary one. `False` otherwise.
        
        '''
        ...


    def uuid(self) -> int | bytes:
        '''
        Returns the UUID of the service. In the case of 16-bit or 32-bit long UUIDs, the value returned is an integer, but for 128-bit long UUIDs the value returned is a bytes object.
        
        '''
        ...


    def instance(self) -> int:
        '''
        Returns the instance ID of the service.
        
        '''
        ...

    def characteristics(self) -> list[GATTCCharacteristic]:
        '''
        Performs a get characteristics request on the connected BLE peripheral a returns a list containing objects of the class GATTCCharacteristic if the request succeeds.
        
        '''
        ...


class GATTCConnection:
    def disconnect() -> None:
        '''
        Closes the BLE connection. Returns `None `.
        
        '''
        ...


    def isconnected() -> bool:
        '''
        Returns `True `if the connection is still open. `False `otherwise.
        
        
        Example:
        
        ```python
        
        from network import Bluetooth
        import ubinascii
        bluetooth = Bluetooth()
        
        # scan until we can connect to any BLE device around
        bluetooth.start_scan(-1)
        adv = None
        while True:
        adv = bluetooth.get_adv()
        if adv:
            try:
                bluetooth.connect(adv.mac)
            except:
                # start scanning again
                bluetooth.start_scan(-1)
                continue
            break
        print("Connected to device with addr = {}".format(ubinascii.hexlify(adv.mac)))
        ```
        '''
        ...

    def services() -> list[GATTCService]:
        '''
        Performs a service search on the connected BLE peripheral (server) a returns a list containing objects of the class `GATTCService` if the search succeeds.
        
        
        Example:
        
        ```python
        
        # assuming that a BLE connection is already open
        services = connection.services()
        print(services)
        for service in services:
        print(service.uuid())
        ```
        '''
        ...

class GATTSCharacteristic:
    @overload
    def value(self) -> int | str | bytes:
        '''
        Get the value of the characteristic. Can return an integer, a string or a bytes object.

        ```python

        # set characteristic value to an integer with the value 123
        characteristic.value(123)
        characteristic.value() # get characteristic value
        ```
        '''
        ...


    @overload
    def value(self, value: int | str | bytes) -> None:
        '''
        Sets the value of the characteristic. Can take an integer, a string or a bytes object.
        
        ```python
        
        characteristic.value(123) # set characteristic value to an integer with the value 123
        characteristic.value() # get characteristic value
        ```
        '''
        ...


    def events(self) -> int:
        '''
        Returns a value with bit flags, identifying the events that have occurred since the last call. Calling this function clears the events.
        
        '''
        ...

    def callback(self, trigger=None, handler: Callable[[Any], None] = None, arg=None):
        '''
        Creates a callback that will be executed when any of the triggers occur. The arguments are:
        
        
        
        - `trigger` can be either `Bluetooth.CHAR_READ_EVENT` or `Bluetooth.CHAR_WRITE_EVENT` . 
        
        - `handler` is the function that will be executed when the callback is triggered. 
        
        - `arg` is the argument that gets passed to the callback. If nothing is given, the characteristic object that owns the callback will be used. 
        
        
        
        Beyond the `arg` a tuple (called `data` ) is also passed to `handler` . The tuple consists of (event, value), where `event` is the triggering event and `value` is the value strictly belonging to the `event` in case of a WRITE event. If the `event` is not a WRITE event, the `value` has no meaning.
        
        
        We recommend getting both the `event` and new `value` of the characteristic via this tuple, and not via `characteristic.event()` and `characteristic.value()` calls in the context of the `handler` to make sure no event and value is lost.
        The reason behind this is that `characteristic.event()` and `characteristic.value()` return with the very last event received and with the current value of the characteristic, while the input parameters are always linked to the specific event triggering the `handler` . If the device is busy executing other operations,  the `handler` of an incoming event may not be called before the next event occurs and is processed.
        
        
        An example of how this can be implemented is shown below, via an example of advertising and creating services on the device:
        
        ```python
        
        from network import Bluetooth
        
        def conn_cb (bt_o):
            events = bt_o.events()
            if  events & Bluetooth.CLIENT_CONNECTED:
                print("Client connected")
            elif events & Bluetooth.CLIENT_DISCONNECTED:
                print("Client disconnected")
        
        def char1_cb_handler(chr, data):
            # The data is a tuple containing the triggering event and the value if the event is a WRITE event.
            # We recommend fetching the event and value from the input parameter, and not via characteristic.event() and characteristic.value()
            events, value = data
            if  events & Bluetooth.CHAR_WRITE_EVENT:
                print("Write request with value = {}".format(value))
            else:
                print('Read request on char 1')
        
        def char2_cb_handler(chr, data):
            # The value is not used in this callback as the WRITE events are not processed.
            events, value = data
            if  events & Bluetooth.CHAR_READ_EVENT:
                print('Read request on char 2')
        
        bluetooth = Bluetooth()
        bluetooth.set_advertisement(name='LoPy', service_uuid=b'1234567890123456')
        bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
        bluetooth.advertise(True)
        
        srv1 = bluetooth.service(uuid=b'1234567890123456', isprimary=True)
        chr1 = srv1.characteristic(uuid=b'ab34567890123456', value=5)
        char1_cb = chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT | Bluetooth.CHAR_READ_EVENT, handler=char1_cb_handler)
        
        srv2 = bluetooth.service(uuid=1234, isprimary=True)
        chr2 = srv2.characteristic(uuid=4567, value=0x1234)
        char2_cb = chr2.callback(trigger=Bluetooth.CHAR_READ_EVENT, handler=char2_cb_handler)
        ```
        '''
        ...


class BluetoothServerService:
    def start(self):
        '''
        Starts the service if not already started.
        
        '''
        ...


    def stop(self):
        '''
        Stops the service if previously started.
        
        '''
        ...

    def characteristic(self, uuid, *, permissions: int = None, properties: int = None, value: int | str | bytes = None) -> GATTSCharacteristic:
        '''
        Creates a new characteristic on the service. Returns an object of the class `GATTSCharacteristic` . The arguments are:
        
        
        
        - `uuid` is the UUID of the service. Can take an integer or a 16 byte long string or bytes object. 
        
        - `permissions` configures the permissions of the characteristic. Takes an integer with a combination of the flags. When bluetooth object is initialized with PIN, read and write permissions are set to encrypted. Setting PIN later with set_pin() call does not affect the permissions of the already existing characteristics, thus they will remain not secured. 
        
        - `properties` sets the properties. Takes an integer with an OR-ed combination of the flags. 
        
        - `value` sets the initial value. Can take an integer, a string or a bytes object. 
        
        
        ```python
        
        service.characteristic('temp', value=25)
        ```
        '''
        ...

class ble_adv_data(NamedTuple):
    mac: bytes
    addr_type: int
    adv_type: int
    rssi: int
    data: bytes

class Bluetooth:
    ''
    ADV_128SERVICE_DATA = 33
    ADV_128SRV_CMPL = 7
    ADV_128SRV_PART = 6
    ADV_16SRV_PART = 2
    ADV_32SERVICE_DATA = 32
    ADV_32SRV_CMPL = 5
    ADV_32SRV_PART = 4
    ADV_ADV_INT = 26
    ADV_APPEARANCE = 25
    ADV_BLE_ADDR_TYPE_PUBLIC = 0
    ADV_BLE_ADDR_TYPE_RANDOM = 1
    ADV_BLE_ADDR_TYPE_RPA_PUBLIC = 2
    ADV_BLE_ADDR_TYPE_RPA_RANDOM = 3
    ADV_CHNL_37 = 1
    ADV_CHNL_38 = 2
    ADV_CHNL_39 = 4
    ADV_CHNL_ALL = 7
    ADV_DEV_CLASS = 13
    ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY = 0
    ADV_FILTER_ALLOW_SCAN_ANY_CON_WLST = 2
    ADV_FILTER_ALLOW_SCAN_WLST_CON_ANY = 1
    ADV_FILTER_ALLOW_SCAN_WLST_CON_WLST = 3
    ADV_FLAG = 1
    ADV_MANUFACTURER_DATA = 255
    ADV_NAME_CMPL = 9
    ADV_NAME_SHORT = 8
    ADV_SERVICE_DATA = 22
    ADV_T16SRV_CMPL = 3
    ADV_TX_PWR = 10
    ADV_TYPE_DIRECT_IND_HIGH = 1
    ADV_TYPE_DIRECT_IND_LOW = 4
    ADV_TYPE_IND = 0
    ADV_TYPE_NONCONN_IND = 3
    ADV_TYPE_SCAN_IND = 2
    CHAR_CONFIG_INDICATE = 2
    CHAR_CONFIG_NOTIFY = 1
    CHAR_NOTIFY_EVENT = 32
    CHAR_READ_EVENT = 8
    CHAR_SUBSCRIBE_EVENT = 128
    CHAR_WRITE_EVENT = 16
    CLIENT_CONNECTED = 2
    CLIENT_DISCONNECTED = 4
    CONN_ADV = 0
    CONN_DIR_ADV = 1
    DISC_ADV = 2
    EXT_ANT = 1
    INT_ANT = 0
    MAN_ANT = 2
    NEW_ADV_EVENT = 1
    NON_CONN_ADV = 3
    PERM_READ = 1
    PERM_READ_ENCRYPTED = 2
    PERM_READ_ENC_MITM = 4
    PERM_WRITE = 16
    PERM_WRITE_ENCRYPTED = 32
    PERM_WRITE_ENC_MITM = 64
    PERM_WRITE_SIGNED = 128
    PERM_WRITE_SIGNED_MITM = 256
    PROP_AUTH = 64
    PROP_BROADCAST = 1
    PROP_EXT_PROP = 128
    PROP_INDICATE = 32
    PROP_NOTIFY = 16
    PROP_READ = 2
    PROP_WRITE = 8
    PROP_WRITE_NR = 4
    PUBLIC_ADDR = 0
    PUBLIC_RPA_ADDR = 2
    RANDOM_ADDR = 1
    RANDOM_RPA_ADDR = 3
    SCAN_RSP = 4
    TX_PWR_0 = 4
    TX_PWR_ADV = 9
    TX_PWR_CONN = 0
    TX_PWR_DEFAULT = 11
    TX_PWR_N12 = 0
    TX_PWR_N3 = 3
    TX_PWR_N6 = 2
    TX_PWR_N9 = 1
    TX_PWR_P3 = 5
    TX_PWR_P6 = 6
    TX_PWR_P9 = 7
    TX_PWR_SCAN = 10


    def gatts_mtu(self):
        ...

    def modem_sleep(self):
        ...

    def nvram_erase(self):
        ...

    def set_advertisement_raw(self):
        ...

    timeout = None

    def __init__(self, id=0, argv = ...):
        '''
        Create a Bluetooth object, and optionally configure it. See init for params of configuration.
        
        
        Example:
        
        ```python
        from network import Bluetooth
        bluetooth = Bluetooth()
        ```
        '''
        ...


    def init(self, id=0, antenna=Bluetooth.INT_ANT, modem_sleep=True, pin=None, privacy=True, secure_connections=True, mtu=200):
        '''
        
        
        - `id `Only one Bluetooth peripheral available so must always be 0 
        
        - `mode `currently the only supported mode is `Bluetooth.BLE `
        
        - `modem_sleep `Enables or Disables BLE modem sleep, Disable modem sleep as a workaround when having Crashes due to flash cache being disabled, as this prevents BLE task saving data in external RAM while accesing external flash for R/W 
        
        - `antenna `selects between the internal and the external antenna. Can be either:
        
        
        - `bluetooth.INT_ANT `: The on-board antenna 
        
        - `bluetooth.EXT_ANT `: The U.FL connector (external antenna) 
        
        - `bluetooth.MAN_ANT `: Manually select the state of the antenna switch on `P12 `. By default, this will select the on-board antenna 
        
        
        
        - `secure `enables or disables the GATT Server security feature 
        
        - `pin `a six digit number to connect to the GATT Sever     Setting any valid pin, GATT Server security features are activated. 
        
        - `privacy `Enables or Disables local privacy settings so address will be random or public. 
        
        - `secure_connections `Enables or Disables Secure Connections and MITM Protection. 
        
        - `mtu `Maximum Transmission Unit (MTU) is the maximum length of an ATT packet. Value must be between `23 `and `200 `. 
        
        
        
        With our development boards it defaults to using the internal antenna, but in the case of an OEM module, the antenna pin ( `P12 `) is not used, so it’s free to be used for other things.
        Initialises and enables the Bluetooth radio in BLE mode.
        
        '''
        ...


    def deinit(self):
        '''
        Disables the Bluetooth radio.
        
        '''
        ...


    def start_scan(self, timeout: float):
        '''
        Starts performing a scan listening for BLE devices sending advertisements. This function always returns immediately, the scanning will be performed on the background. The return value is `None `. After starting the scan the function `get_adv() `can be used to retrieve the advertisements messages from the FIFO. The internal FIFO has space to cache 16 advertisements.
        
        
        The arguments are:
        
        
        
        - `timeout `specifies the amount of time in seconds to scan for advertisements, cannot be zero. If timeout is > 0, then the BLE radio will listen for advertisements until the specified value in seconds elapses. If timeout < 0, then there’s no timeout at all, and stop_scan() needs to be called to cancel the scanning process. 
        
        
        
        Examples:
        
        ```python
        bluetooth.start_scan(10)        # starts scanning and stop after 10 seconds
        bluetooth.start_scan(-1)        # starts scanning indefinitely until bluetooth.stop_scan() is called
        ```
        '''
        ...


    def stop_scan(self):
        '''
        Stops an ongoing scanning process. Returns `None `.
        
        '''
        ...


    def isscanning(self) -> bool:
        '''
        Returns `True `if a Bluetooth scan is in progress. `False `otherwise.
        
        '''
        ...

    def get_adv(self) -> ble_adv_data:
        '''
        Gets an named tuple with the advertisement data received during the scanning. The tuple has the following structure: `(mac, addr_type, adv_type, rssi, data) `
        
        
        
        - `mac `is the 6-byte ling mac address of the device that sent the advertisement. 
        
        - `addr_type `is the address type. See the constants section below for more details. 
        
        - `adv_type `is the advertisement type received. See the constants section below fro more details. 
        
        - `rssi `is signed integer with the signal strength of the advertisement. 
        
        - `data `contains the complete 31 bytes of the advertisement message. In order to parse the data and get the specific types, the method `resolve_adv_data() `can be used. 
        
        
        
        Example for getting `mac `address of an advertiser:
        
        ```python
        import ubinascii
        
        bluetooth = Bluetooth()
        bluetooth.start_scan(20) # scan for 20 seconds
        
        adv = bluetooth.get_adv() #
        ubinascii.hexlify(adv.mac) # convert hexadecimal to ascii
        ```
        '''
        ...


    def get_advertisements(self) -> list[ble_adv_data]:
        '''
        Same as the `get_adv() `method, but this one returns a list with all the advertisements received.
        
        '''
        ...


    def resolve_adv_data(self, data, data_type) -> str | None:
        '''
        Parses the advertisement data and returns the requested `data_type `if present. If the data type is not present, the function returns `None `.
        
        
        Arguments:
        
        
        
        - `data `is the bytes object with the complete advertisement data. 
        
        - `data_type `is the data type to resolve from from the advertisement data. See constants section below for details. 
        
        
        
        Example:
        
        ```python
        import ubinascii
        from network import Bluetooth
        bluetooth = Bluetooth()
        
        bluetooth.start_scan(20)
        while bluetooth.isscanning():
        adv = bluetooth.get_adv()
        if adv:
            # try to get the complete name
            print(bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL))
        
            mfg_data = bluetooth.resolve_adv_data(adv.data, Bluetooth.ADV_MANUFACTURER_DATA)
        
            if mfg_data:
                # try to get the manufacturer data (Apple's iBeacon data is sent here)
                print(ubinascii.hexlify(mfg_data))
        ```
        '''
        ...


    def set_pin(self, pin: int):
        '''
        Configures a new PIN to be used by the device. The PIN is a 1-6 digit length decimal number, if less than 6 digits are given the missing leading digits are considered as 0. E.g. 1234 becomes 001234. When a new PIN is configured, the information of all previously bonded device is removed and the current connection is terminated. To restart advertisement the advertise() must be called after PIN is changed.
        
        '''
        ...

    def connect(self, mac_addr, timeout=None) -> GATTCConnection:
        '''
        
        
        - `mac_addr `is the address of the remote device to connect 
        
        - `timeout `specifies the amount of time in milliseconds to wait for the connection process to finish. If not given then no timeout is applied The function blocks until the connection succeeds or fails (raises OSError) or the given `timeout `expires (raises `Bluetooth.timeout TimeoutError `). If the connections succeeds it returns a object of type `GATTCConnection `. 
        
        
        ```python
        bluetooth.connect('112233eeddff') # mac address is accepted as a string
        ```
        '''
        ...


    def callback(self, trigger=None, handler: Callable[[Any], None] =None, arg=None):
        '''
        Creates a callback that will be executed when any of the triggers occurs. The arguments are:
        
        
        
        - `trigger` can be either `Bluetooth.NEW_ADV_EVENT `, `Bluetooth.CLIENT_CONNECTED `, or `Bluetooth.CLIENT_DISCONNECTED `
        
        - `handler` is the function that will be executed when the callback is triggered. 
        
        - `arg `is the argument that gets passed to the callback. If nothing is given the bluetooth object itself is used. 
        
        
        
        An example of how this may be used can be seen in the `bluetooth.events() `method.
        
        '''
        ...


    def events(self) -> int:
        '''
        Returns a value with bit flags identifying the events that have occurred since the last call. Calling this function clears the events.
        
        
        Example of usage:
        
        ```python
        from network import Bluetooth
        
        bluetooth = Bluetooth()
        bluetooth.set_advertisement(name='LoPy', service_uuid=b'1234567890123456')
        
        def conn_cb (bt_o):
            events = bt_o.events()   # this method returns the flags and clears the internal registry
            if events & Bluetooth.CLIENT_CONNECTED:
                print("Client connected")
            elif events & Bluetooth.CLIENT_DISCONNECTED:
                print("Client disconnected")
        
        bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)
        
        bluetooth.advertise(True)
        ```
        '''
        ...


    def set_advertisement(self, name : str=None, manufacturer_data : str=None, service_data =None, service_uuid=None):
        '''
        Configure the data to be sent while advertising. If left with the default of `None `the data won’t be part of the advertisement message.
        
        
        The arguments are:
        
        
        
        - `name `is the string name to be shown on advertisements. 
        
        - `manufacturer_data `manufacturer data to be advertised (hint: use it for iBeacons). 
        
        - `service_data `service data to be advertised. 
        
        - `service_uuid `uuid of the service to be advertised. 
        
        
        
        Example:
        
        ```python
        bluetooth.set_advertisement(name="advert", manufacturer_data="lopy_v1")
        ```
        '''
        ...


    def set_advertisement_params(self, adv_int_min=0x20, adv_int_max=0x40, adv_type=Bluetooth.ADV_TYPE_IND, own_addr_type=Bluetooth.BLE_ADDR_TYPE_PUBLIC, channel_map=Bluetooth.ADV_CHNL_ALL, adv_filter_policy=Bluetooth.ADV_FILTER_ALLOW_SCAN_ANY_CON_ANY):
        '''
        Configure the parameters used when advertising.
        
        
        The arguments are:
        
        
        
        - `adv_int_min `is the minimum advertising interval for undirected and low duty cycle directed advertising. 
        
        - `adv_int_max `is the maximum advertising interval for undirected and low duty cycle directed advertising. 
        
        - `adv_type `is the advertising type. 
        
        - `own_addr_type `is the owner bluetooth device address type. 
        
        - `channel_map `is the advertising channel map. 
        
        - `adv_filter_policy `is the advertising filter policy. 
        
        
        '''
        ...


    def advertise(self, Enable = True):
        '''
        Start or stop sending advertisements. The `set_advertisement() `method must have been called prior to this one.
        
        '''
        ...

    def service(self, uuid, isprimary=True, nbr_chars=1, start=True) -> BluetoothServerService:
        '''
        Create a new service on the internal GATT server. Returns a object of type `BluetoothServerService `.
        
        
        The arguments are:
        
        
        
        - `uuid `is the UUID of the service. Can take an integer or a 16 byte long string or bytes object. 
        
        - `isprimary `selects if the service is a primary one. Takes a `bool `value. 
        
        - `nbr_chars `specifies the number of characteristics that the service will contain. 
        
        - `start `if `True `the service is started immediately. 
        
        
        ```python
        bluetooth.service('abc123')
        ```
        '''
        ...


    def disconnect_client(self):
        '''
        Closes the BLE connection with the client.
        
        '''
        ...


    def tx_power(self, type, level):
        '''
        Gets or sets the TX Power level.
        If called with only `type `parameter it returns with the current value belonging to the given type.
        If both `type `and `level `parameters are given, it sets the TX Power.
        
        
        Valid values for `type`:
            - `Bluetooth.TX_PWR_CONN` -> for handling connection
            - `Bluetooth.TX_PWR_ADV` -> for advertising
            - `Bluetooth.TX_PWR_SCAN` -> for scan
            - `Bluetooth.TX_PWR_DEFAULT` -> default if others not set

        Valid values for `level`:
            - Bluetooth.TX_PWR_N12` -> -12dbm
            - `Bluetooth.TX_PWR_N9` -> -9dbm
            - `Bluetooth.TX_PWR_N6` -> -6dbm
            - `Bluetooth.TX_PWR_N3` -> -3dbm
            - `Bluetooth.TX_PWR_0` -> 0dbm
            - `Bluetooth.TX_PWR_P3` -> 3dbm
            - `Bluetooth.TX_PWR_P6` -> 6dbm
            - `Bluetooth.TX_PWR_P9` -> 9dbm
        '''
        ...

Coap = None

class LTE:
    ''
    EVENT_BREAK = 2
    EVENT_COVERAGE_LOSS = 1
    IP = 'IP'
    IPV4V6 = 'IPV4V6'
    PSM_ACTIVE_1M = 1
    PSM_ACTIVE_2S = 0
    PSM_ACTIVE_6M = 2
    PSM_ACTIVE_DISABLED = 7
    PSM_PERIOD_10H = 2
    PSM_PERIOD_10M = 0
    PSM_PERIOD_1H = 1
    PSM_PERIOD_1M = 5
    PSM_PERIOD_2S = 3
    PSM_PERIOD_30S = 4
    PSM_PERIOD_320H = 6
    PSM_PERIOD_DISABLED = 7
    def attach():
        ...

    def connect():
        ...

    def deinit():
        ...

    def detach():
        ...

    def dettach():
        ...

    def disconnect():
        ...

    def events():
        ...

    def factory_reset():
        ...

    def iccid():
        ...

    def imei():
        ...

    def init():
        ...

    def isattached():
        ...

    def isconnected():
        ...

    def lte_callback():
        ...

    def modem_upgrade_mode():
        ...

    def pppresume():
        ...

    def pppsuspend():
        ...

    def psm():
        ...

    def reconnect_uart():
        ...

    def reset():
        ...

    def send_at_cmd():
        ...

    def time():
        ...

    def ue_coverage():
        ...


class LoRa:
    ''
    ABP = 1
    ALWAYS_ON = 0
    AS923 = 0
    AU915 = 1
    BW_125KHZ = 0
    BW_250KHZ = 1
    BW_500KHZ = 2
    CLASS_A = 0
    CLASS_C = 2
    CN470 = 2
    CODING_4_5 = 1
    CODING_4_6 = 2
    CODING_4_7 = 3
    CODING_4_8 = 4
    EU433 = 4
    EU868 = 5
    IN865 = 7
    LORA = 0
    LORAWAN = 1
    OTAA = 0
    RX_PACKET_EVENT = 1
    SLEEP = 2
    TX_FAILED_EVENT = 4
    TX_ONLY = 1
    TX_PACKET_EVENT = 2
    US915 = 8
    def add_channel():
        ...

    def airtime():
        ...

    def bandwidth():
        ...

    def callback():
        ...

    def coding_rate():
        ...

    def compliance_test():
        ...

    def events():
        ...

    def frequency():
        ...

    def has_joined():
        ...

    def init():
        ...

    def ischannel_free():
        ...

    def join():
        ...

    def join_multicast_group():
        ...

    def leave_multicast_group():
        ...

    def mac():
        ...

    def nvram_erase():
        ...

    def nvram_restore():
        ...

    def nvram_save():
        ...

    def power_mode():
        ...

    def preamble():
        ...

    def remove_channel():
        ...

    def reset():
        ...

    def set_battery_level():
        ...

    def sf():
        ...

    def stats():
        ...

    timeout = None
    def tx_power():
        ...

MDNS = None

class Server:
    ''
    def deinit():
        ...

    def init():
        ...

    def isrunning():
        ...

    def timeout():
        ...


class Sigfox:
    ''
    RCZ1 = 0
    RCZ2 = 1
    RCZ3 = 2
    RCZ4 = 3
    SIGFOX = 0
    def config():
        ...

    def cw():
        ...

    def freq_offset():
        ...

    def frequencies():
        ...

    def id():
        ...

    def info():
        ...

    def init():
        ...

    def mac():
        ...

    def pac():
        ...

    def public_key():
        ...

    def reset():
        ...

    def rssi():
        ...

    def rssi_offset():
        ...

    def test_mode():
        ...

    def version():
        ...


class WLAN:
    ''
    AP = 2
    COUNTRY_POL_AUTO = 0
    COUNTRY_POL_MAN = 1
    def Connected_ap_pwd():
        ...

    EVENT_PKT_ANY = 63
    EVENT_PKT_CTRL = 2
    EVENT_PKT_DATA = 4
    EVENT_PKT_DATA_AMPDU = 32
    EVENT_PKT_DATA_MPDU = 16
    EVENT_PKT_MGMT = 1
    EVENT_PKT_MISC = 8
    EXT_ANT = 1
    FILTER_CTRL_PKT_ACK = 536870912
    FILTER_CTRL_PKT_ALL = -8388608
    FILTER_CTRL_PKT_BA = 33554432
    FILTER_CTRL_PKT_BAR = 16777216
    FILTER_CTRL_PKT_CFEND = -1073741824
    FILTER_CTRL_PKT_CFENDACK = 0
    FILTER_CTRL_PKT_CTS = 268435456
    FILTER_CTRL_PKT_PSPOLL = 67108864
    FILTER_CTRL_PKT_WRAPPER = 8388608
    HT20 = 1
    HT40 = 2
    INT_ANT = 0
    MAN_ANT = 2
    PHY_11_B = 1
    PHY_11_G = 2
    PHY_11_N = 3
    PHY_LOW_RATE = 4
    SCAN_ACTIVE = 0
    SCAN_PASSIVE = 1
    SECONDARY_CHN_ABOVE = 1
    SECONDARY_CHN_BELOW = 2
    SECONDARY_CHN_NONE = 0
    SMART_CONF_DONE = 64
    SMART_CONF_TIMEOUT = 128
    STA = 1
    STA_AP = 3
    WEP = 1
    WPA = 2
    WPA2 = 3
    WPA2_ENT = 5
    def antenna():
        ...

    def ap_sta_list():
        ...

    def ap_tcpip_sta_list():
        ...

    def auth():
        ...

    def bandwidth():
        ...

    def bssid():
        ...

    def callback():
        ...

    def channel():
        ...

    def connect():
        ...

    def country():
        ...

    def ctrl_pkt_filter():
        ...

    def deinit():
        ...

    def disconnect():
        ...

    def events():
        ...

    def hostname():
        ...

    def ifconfig():
        ...

    def init():
        ...

    def isconnected():
        ...

    def joined_ap_info():
        ...

    def mac():
        ...

    def max_tx_power():
        ...

    def mode():
        ...

    def promiscuous():
        ...

    def scan():
        ...

    def send_raw():
        ...

    def smartConfig():
        ...

    def ssid():
        ...

    def wifi_packet():
        ...

    def wifi_protocol():
        ...

