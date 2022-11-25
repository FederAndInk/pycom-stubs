"""
Module: 'network' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from collections.abc import Callable
from typing import Any, NamedTuple, TypeVar, overload, Literal
from typing_extensions import Self, Unpack, TypedDict, NotRequired

_T = TypeVar("_T")

class char_callback_data(NamedTuple):
    event: int
    value: bytes

class GATTCCharacteristic:
    '''
    The smallest concept in GATT is the Characteristic, which encapsulates a single data point (though it may contain an array of related data, such as X/Y/Z values from a 3-axis accelerometer, longitude and latitude from a GPS, etc.).

    The following class allows you to manage characteristics from a Client.
    '''
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

    @overload
    def callback(self, trigger, handler: Callable[[Self, char_callback_data], None]):
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

    @overload
    def callback(self, trigger, handler: Callable[[_T, char_callback_data], None], arg: _T):
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
    '''
    Services are used to categorise data up into specific chunks of data known as characteristics. A service may have multiple characteristics, and each service has a unique numeric ID called a UUID.

    The following class allows control over Client services.
    '''
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
    '''
    The GATT Client is the device that requests data from the server, otherwise known as the master device (commonly this might be a phone/tablet/PC). All transactions are initiated by the master, which receives a response from the slave.
    '''
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
    '''
    The smallest concept in GATT is the Characteristic, which encapsulates a single data point (though it may contain an array of related data, such as X/Y/Z values from a 3-axis accelerometer, longitude and latitude from a GPS, etc.).

    The following class allows you to manage Server characteristics.
    '''
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

    @overload
    def callback(self, trigger, handler: Callable[[Self, char_callback_data], None]):
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

    @overload
    def callback(self, trigger, handler: Callable[[_T, char_callback_data], None], arg: _T):
        ...


class BluetoothServerService:
    '''
    The GATT Server allows the device to act as a peripheral and hold its own ATT lookup data, server & characteristic definitions. In this mode, the device acts as a slave and a master must initiate a request.

    Services are used to categorise data up into specific chunks of data known as characteristics. A service may have multiple characteristics, and each service has a unique numeric ID called a UUID.

    The following class allows control over Server services.
    '''
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
    '''
    This class provides a driver for the Bluetooth radio in the module. Currently, only basic BLE functionality is available.
    Quick Usage Example

    ```python
    from network import Bluetooth
    import time
    bt = Bluetooth()
    bt.start_scan(-1)

    while True:
        adv = bt.get_adv()
        if adv and bt.resolve_adv_data(adv.data, Bluetooth.ADV_NAME_CMPL) == 'Heart Rate':
            try:
                conn = bt.connect(adv.mac)
                services = conn.services()
                for service in services:
                    time.sleep(0.050)
                    if type(service.uuid()) == bytes:
                        print('Reading chars from service = {}'.format(service.uuid()))
                    else:
                        print('Reading chars from service = %x' % service.uuid())
                    chars = service.characteristics()
                    for char in chars:
                        if (char.properties() & Bluetooth.PROP_READ):
                            print('char {} value = {}'.format(char.uuid(), char.read()))
                conn.disconnect()
                break
            except:
                print("Error while connecting or reading from the BLE device")
                break
        else:
            time.sleep(0.050)
    ```

    Bluetooth Low Energy (BLE)

    Bluetooth low energy (BLE) is a subset of classic Bluetooth, designed for easy connecting and communicating between devices (in particular mobile platforms). BLE uses a methodology known as Generic Access Profile (GAP) to control connections and advertising.

    GAP allows for devices to take various roles but generic flow works with devices that are either a Server (low power, resource constrained, sending small payloads of data) or a Client device (commonly a mobile device, PC or Pycom Device with large resources and processing power). Pycom devices can act as both a Client and a Server.
    '''
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

    @overload
    def callback(self, trigger, handler: Callable[[Self], None]):
        '''
        Creates a callback that will be executed when any of the triggers occurs. The arguments are:

        - `trigger` can be either `Bluetooth.NEW_ADV_EVENT `, `Bluetooth.CLIENT_CONNECTED `, or `Bluetooth.CLIENT_DISCONNECTED `
        - `handler` is the function that will be executed when the callback is triggered.
        - `arg `is the argument that gets passed to the callback. If nothing is given the bluetooth object itself is used.

        An example of how this may be used can be seen in the `bluetooth.events() `method.
        '''
        ...

    @overload
    def callback(self, trigger, handler: Callable[[_T], None], arg: _T):
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


class LoRa_stats(NamedTuple):
    rx_timestamp: int
    rssi: int
    snr: float
    sftx: int
    sfrx: int
    tx_trials: int
    tx_power: int
    tx_time_on_air: int
    tx_counter: int
    tx_frequency: int
    '''
    Where:

    - `rx_timestamp` is an internal timestamp of the last received packet with microseconds precision.
    - `rssi` holds the received signal strength in dBm.
    - `snr` contains the signal to noise ratio id dB (as a single precision float).
    - `sfrx` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet received.
    - `sftx` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet transmitted.
    - `tx_trials` is the number of tx attempts of the last transmitted packet (only relevant for LORAWAN confirmed packets).
    - `tx_power` is the power of the last transmission (in dBm).
    - `tx_time_on_air` is the time on air of the last transmitted packet (in ms).
    - `tx_counter` is the number of packets transmitted.
    - `tx_frequency` is the frequency used for the last transmission.
    '''

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

    def airtime(self):
        ...

    def compliance_test(self):
        ...

    def join_multicast_group(self):
        ...

    def leave_multicast_group(self):
        ...

    def reset(self):
        ...

    timeout = None

    @overload
    def tx_power(self, power: int):
        """
        transmit power in dBm.
        """
        ...


    @overload
    def tx_power(self) -> int:
        """
        transmit power in dBm.
        """
        ...

    def __init__(self, mode, region=LoRa.EU868, frequency: float = None, tx_power: float = None, bandwidth=LoRa.BW_125KHZ, sf=7, preamble=8, coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON, tx_iq=False, rx_iq=False, adr=False, public=True, tx_retries=2, device_class=LoRa.CLASS_A):
        '''
        Create and configure a LoRa object. See init for params of configuration.

        ```python
        lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
        ```
        '''
        ...

    def init(self, mode, region=LoRa.EU868, frequency: float =None, tx_power: float = None, bandwidth=LoRa.BW_125KHZ, sf=7, preamble=8, coding_rate=LoRa.CODING_4_5, power_mode=LoRa.ALWAYS_ON, tx_iq=False, rx_iq=False, adr=False, public=True, tx_retries=2, device_class=LoRa.CLASS_A):
        '''
        This method is used to set the LoRa subsystem configuration and to specific raw LoRa or LoRaWAN.


        The arguments are:

        - `mode` can be either
            - `LoRa.LORA` : For LoRa MAC / RAW
            - `LoRa.LORAWAN` : For use in the LoRa Wide Area Network and services like TTN and Chirpstack
        - `region` can take the following values:
            - `LoRa.AS923`
            - `LoRa.AU915`
            - `LoRa.EU868`
            - `LoRa.US915`
            - `LoRa.CN470`
            - `LoRa.IN865`


        --------
        If no region is provided, it will default to the setting provided in the CONFIG partition, set by the Firmware Updater tool.

        - `frequency` accepts values within the selected Region frequency bands.
        - `tx_power` is the transmit power in dBm.
        - `bandwidth` is the channel bandwidth in KHz.
            - `LoRa.BW_125KHZ`
            - `LoRa.BW_250KHZ`
            - `LoRa.BW_500KHZ`
        - `sf` sets the desired spreading factor. Accepts values between 7 and 12.
        - `preamble` configures the number of pre-amble symbols. The default value is 8.
        - `coding_rate` can take the following values:
            - `LoRa.CODING_4_5`
            - `LoRa.CODING_4_6`
            - `LoRa.CODING_4_7`
            - `LoRa.CODING_4_8`
        - `power_mode` can be either
            - `LoRa.ALWAYS_ON` : the radio is always listening for incoming - packets whenever a transmission is not taking place
            - `LoRa.TX_ONLY` : he radio goes to sleep as soon as the transmission completes
            - `LoRa.SLEEP` : the radio is sent to sleep permanently and won’t accept any commands until the power mode is changed.
        - `tx_iq` enables TX IQ inversion.
        - `rx_iq` enables RX IQ inversion.
        - `adr` enables Adaptive Data Rate.
        - `public` selects between the public and private sync word.
        - `tx_retries` sets the number of TX retries in `LoRa.LORAWAN` mode.
        - `device_class` sets the LoRaWAN device class. Visit the TTN Website to learn more about the LoRa device classes. Can be either:
            - `LoRa.CLASS_A`
            - `LoRa.CLASS_C`

        --------
        In `LoRa.LORAWAN` mode, only `adr` , `public` , `tx_retries` and `device_class` are used. All the other params will be ignored as they are handled by the LoRaWAN stack directly. On the other hand, in `LoRa.LORA` mode from those 4 arguments, only the public one is important in order to program the sync word. In `LoRa.LORA` mode `adr` , `tx_retries` and `device_class` are ignored since they are only relevant to the LoRaWAN stack.


        '''
        ...

    def join(self, activation, auth, timeout=None, dr=None):
        '''
        Join a LoRaWAN network. Internally the stack will automatically retry every 15 seconds until a Join Accept message is received. The parameters are:



        - `activation` : can be either:
            - `LoRa.OTAA` : Over the Air Activation
            - `LoRa.ABP` : Activation By Personalisation
        - `auth` : is a tuple with the authentication data.
        - In the case of `LoRa.OTAA` the authentication tuple is: `(dev_eui, app_eui, app_key)` where `dev_eui` is optional. If it is not provided the LoRa MAC will be used.
        - In the case of `LoRa.ABP` the authentication tuple is: `(dev_addr, nwk_swkey, app_swkey)` .
        - `timeout` : is the maximum time in milliseconds to wait for the Join Accept message to be received. If no timeout (or zero) is given, the call returns immediately and the status of the join request can be checked with `lora.has_joined()` .
        - `dr` : is an optional value to specify the initial data rate for the Join Request. values are region specific.
        '''
        ...

    @overload
    def frequency(self, frequency):
        '''
        Get or set the frequency in raw LoRa mode ( `LoRa.LORA` ). The allowed range is region-specific.

        '''
        ...

    @overload
    def frequency(self) -> float:
        '''
        Get or set the frequency in raw LoRa mode ( `LoRa.LORA` ). The allowed range is region-specific.

        '''
        ...
    @overload
    def bandwidth(self, bandwidth):
        '''
        Get or set the bandwidth in raw LoRa mode ( `LoRa.LORA` ). Bandwidth can be either: (depending on the region setting)

        - `LoRa.BW_125KHZ`
        - `LoRa.BW_250KHZ`
        - `LoRa.BW_500KHZ`
        '''
        ...
    @overload
    def bandwidth(self) -> int:
        '''
        Get or set the bandwidth in raw LoRa mode ( `LoRa.LORA` ). Bandwidth can be either: (depending on the region setting)

        - `LoRa.BW_125KHZ`
        - `LoRa.BW_250KHZ`
        - `LoRa.BW_500KHZ`
        '''
        ...

    @overload
    def coding_rate(self) -> int:
        '''
        Get or set the coding rate in raw LoRa mode ( `LoRa.LORA` ). The allowed values are: (depending on the region setting)

        - `LoRa.CODING_4_5`
        - `LoRa.CODING_4_6`
        - `LoRa.CODING_4_7`
        - `LoRa.CODING_4_8`
        '''
        ...

    @overload
    def coding_rate(self, coding_rate):
        '''
        Get or set the coding rate in raw LoRa mode ( `LoRa.LORA` ). The allowed values are: (depending on the region setting)

        - `LoRa.CODING_4_5`
        - `LoRa.CODING_4_6`
        - `LoRa.CODING_4_7`
        - `LoRa.CODING_4_8`
        '''
        ...

    @overload
    def preamble(self):
        '''
        Get or set the number of preamble symbols in raw LoRa mode ( `LoRa.LORA` ).
        '''
        ...

    @overload
    def preamble(self, preamble):
        '''
        Get or set the number of preamble symbols in raw LoRa mode ( `LoRa.LORA` ).
        '''
        ...

    @overload
    def sf(self):
        '''
        Get or set the spreading factor value in raw LoRa mode ( `LoRa.LORA` ). The minimum value is 7 and the maximum is 12:
        '''
        ...

    @overload
    def sf(self, sf):
        '''
        Get or set the spreading factor value in raw LoRa mode ( `LoRa.LORA` ). The minimum value is 7 and the maximum is 12:
        '''
        ...

    @overload
    def power_mode(self):
        '''
        Get or set the power mode in raw LoRa mode ( `LoRa.LORA` ). The accepted values are:

        - `LoRa.ALWAYS_ON`
        - `LoRa.TX_ONLY`
        - `LoRa.SLEEP`
        '''
        ...

    @overload
    def power_mode(self, power_mode):
        '''
        Get or set the power mode in raw LoRa mode ( `LoRa.LORA` ). The accepted values are:

        - `LoRa.ALWAYS_ON`
        - `LoRa.TX_ONLY`
        - `LoRa.SLEEP`
        '''
        ...

    def stats(self) -> LoRa_stats:
        '''
        Return a named tuple with useful information from the last received LoRa or LoRaWAN packet. The named tuple has the following form:

        `(rx_timestamp, rssi, snr, sftx, sfrx, tx_trials, tx_power, tx_time_on_air, tx_counter, tx_frequency)`


        Where:

        - `rx_timestamp` is an internal timestamp of the last received packet with microseconds precision.
        - `rssi` holds the received signal strength in dBm.
        - `snr` contains the signal to noise ratio id dB (as a single precision float).
        - `sfrx` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet received.
        - `sftx` tells the data rate (in the case of LORAWAN mode) or the spreading factor (in the case of LORA mode) of the last packet transmitted.
        - `tx_trials` is the number of tx attempts of the last transmitted packet (only relevant for LORAWAN confirmed packets).
        - `tx_power` is the power of the last transmission (in dBm).
        - `tx_time_on_air` is the time on air of the last transmitted packet (in ms).
        - `tx_counter` is the number of packets transmitted.
        - `tx_frequency` is the frequency used for the last transmission.

        --------
        Note that the tuple will only contain the respective information after receiving and/or sending LoRa packets.
        '''
        ...

    def has_joined(self) -> bool:
        '''
        Returns `True` if a LoRaWAN network has been joined. `False` otherwise.
        '''
        ...

    def add_channel(self, index, frequency, dr_min, dr_max):
        '''
        Add a LoRaWAN channel on the specified `index` . If there’s already a channel with that index it will be replaced with the new one. By default, the regulated LoRaWAN channels are assigned according to the region settings.


        The arguments are:

        - `index` : Index of the channel to add. Accepts values between 0 and 15 for EU and between 0 and 71 for US.
        - `frequency` : Centre frequency in Hz of the channel.
        - `dr_min` : Minimum data rate of the channel (0-7).
        - `dr_max` : Maximum data rate of the channel (0-7).

        Example:

        ```python
        lora.add_channel(index=0, frequency=868000000, dr_min=5, dr_max=6)
        ```
        '''
        ...

    def remove_channel(self, index):
        '''
        Removes the channel from the specified `index` . On EU868, the channels 0 to 2 cannot be removed, they can only be replaced by other channels using the `lora.add_channel` method. A way to remove all channels except for one is to add the same channel, 3 times on indexes 0, 1 and 2.
        '''
        ...

    def mac(self) -> bytes:
        '''
        Returns a byte object with the 8-Byte MAC address of the LoRa radio.
        '''
        ...

    @overload
    def callback(self, trigger, handler: Callable[[Self], None]):
        '''
        Specify a callback handler for the LoRa radio. The `trigger` types are

        - `LoRa.RX_PACKET_EVENT` is raised for every received packet
        - `LoRa.TX_PACKET_EVENT` is raised as soon as the packet transmission cycle ends, which includes the end of the receive windows. In the case of non-confirmed transmissions, this will occur at the end of the receive windows, but, in the case of confirmed transmissions, this event will only be raised if the `ack` is received.
        - `LoRa.TX_FAILED_EVENT` will be raised after the number of `tx_retries` configured have been performed and no `ack` is received.

        An example of how this callback functions can be seen the in method `lora.events()` .
        '''
        ...

    @overload
    def callback(self, trigger, handler: Callable[[_T], None], arg: _T):
        ...

    def ischannel_free(self, rssi_threshold) -> bool:
        '''
        This method is used to check for radio activity on the current LoRa channel, and if the `rssi` of the measured activity is lower than the `rssi_threshold` given, the return value will be `True` , otherwise `False` . Example:

        ```python
        lora.ischannel_free(-100)
        ```
        '''
        ...

    def set_battery_level(self, level):
        '''
        Set the battery level value that will be sent when the LoRaWAN MAC command that retrieves the battery level is received. This command is sent by the network and handled automatically by the LoRaWAN stack. The values should be according to the LoRaWAN specification:

        - `0` means that the end-device is connected to an external power source.
        - `1..254` specifies the battery level, 1 being at minimum and 254 being at maximum.
        - `255` means that the end-device was not able to measure the battery level.

        ```python
        lora.set_battery_level(127) # 50% battery
        ```
        '''
        ...

    def events(self) -> int:
        '''
        This method returns a value with bits sets (if any) indicating the events that have triggered the callback. Please note that by calling this function the internal events registry is cleared automatically, therefore calling it immediately for a second time will most likely return a value of 0.

        Example:

        ```python
        def lora_cb(lora):
            events = lora.events()
            if events & LoRa.RX_PACKET_EVENT:
                print('Lora packet received')
            if events & LoRa.TX_PACKET_EVENT:
                print('Lora packet sent')

        lora.callback(trigger=(LoRa.RX_PACKET_EVENT | LoRa.TX_PACKET_EVENT), handler=lora_cb)
        ```
        '''
        ...

    def nvram_save(self):
        '''
        Save the LoRaWAN state (joined status, network keys, packet counters, etc) in non-volatile memory in order to be able to restore the state when coming out of deepsleep or a power cycle.

        '''
        ...

    def nvram_restore(self):
        '''
        Restore the LoRaWAN state (joined status, network keys, packet counters, etc) from non-volatile memory. State must have been previously stored with a call to `nvram_save` before entering deepsleep. This is useful to be able to send a LoRaWAN message immediately after coming out of deepsleep without having to join the network again. This can only be used if the current region matches the one saved. Note that the nvram will be cleared after using this method.

        '''
        ...

    def nvram_erase(self):
        '''
        Remove the LoRaWAN state (joined status, network keys, packet counters, etc) from non-volatile memory.


        See the tutorials for an example on how to use nvram

        '''
        ...

    def mesh(self):
        '''
        Enable the Mesh network. Only after Mesh enabling the `lora.cli()` and `socket` can be used.

        '''
        ...

    def cli(self, ip: str):
        '''
        Send OpenThread CLI commands, the list is [here](https://github.com/openthread/openthread/tree/main/src/cli). The output is multiline string, having as line-endings the `\\r\\n` .

        ```bash
        >>> print(lora.cli("ipaddr"))
        fdde:ad00:beef:0:0:ff:fe00:fc00
        fdde:ad00:beef:0:0:ff:fe00:e800
        fdde:ad00:beef:0:e1f0:783c:1e8f:c763
        fe80:0:0:0:2c97:cb65:3219:c86
        ```
        '''
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
    '''
    This class provides a driver for the WiFi network processor in the module. Example usage:

    ```python
    import network
    import time
    # setup as a station
    wlan = network.WLAN(mode=network.WLAN.STA)
    wlan.connect('your-ssid', auth=(network.WLAN.WPA2, 'your-key'))
    while not wlan.isconnected():
        time.sleep_ms(50)
    print(wlan.ifconfig())

    # now use socket as usual
    ```

    Quick Usage Example

    ```python
    import machine
    from network import WLAN

    # configure the WLAN subsystem in station mode (the default is AP)
    wlan = WLAN(mode=WLAN.STA)
    # go for fixed IP settings (IP, Subnet, Gateway, DNS)
    wlan.ifconfig(config=('192.168.0.107', '255.255.255.0', '192.168.0.1', '192.168.0.1'))
    wlan.scan()     # scan for available networks
    wlan.connect(ssid='mynetwork', auth=(WLAN.WPA2, 'my_network_key'))
    while not wlan.isconnected():
        pass
    print(wlan.ifconfig())
    ```
    '''
    COUNTRY_POL_AUTO = 0
    COUNTRY_POL_MAN = 1

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
    AP = 2
    STA_AP = 3

    WEP = 1
    WPA = 2
    WPA2 = 3
    WPA2_ENT = 5

    def __init__(self, id=0, *, mode: int = STA, ssid: str = "", auth: tuple[Literal[1, 2, 3], str] | tuple[Literal[5], str] | None = None, channel=1, antenna=MAN_ANT, power_save=False, hidden=False, bandwidth=HT40, max_tx_pwr=78, country='CN', protocol: tuple[bool, bool, bool] = (True, True, True)):
        '''
        Create a WLAN object, and optionally configure it. See init for params of configuration.

        --------
        The WLAN constructor is special in the sense that if no arguments are given, it will return the already existing WLAN instance without re-configuring it. This is because WLAN is a system feature of the WiPy. If the already existing instance is not initialised it will do the same as the other constructors and will initialise it with default values.
        '''
        ...

    def init(self, *, mode: int = STA, ssid: str = "", auth: tuple[Literal[1, 2, 3], str] | tuple[Literal[5], str] | None = None, channel=1, antenna=MAN_ANT, power_save=False, hidden=False, bandwidth=HT40, max_tx_pwr=78, country='CN', protocol: tuple[bool, bool, bool] = (True, True, True)):
        '''
        Set or get the WiFi network processor configuration.

        Arguments are:

        - `mode` : can be either:
            - `WLAN.STA` : Station mode, connect to a WiFinetwork
            - `WLAN.AP` : Access Point mode, create a WiFi network. You must specify the `ssid`
            - `WLAN.STA_AP` : Both Station and Access Point mode are active.
        - `ssid` : a string with the SSID name.
        - `auth` : a tuple with `(sec, key)` . Security can be one of the following. The key is a string with the network password.
            - `None` :
            - `WLAN.WEP` : Using this in `WLAN.AP` , the key must be a string of hexadecimal values.
            - `WLAN.WPA`
            - `WLAN.WPA2`
            - `WLAN.WPA2_ENT` : this will use the following format: `(sec, username, password)`
        - `channel` : a number in the range 1-11. Only needed when mode is `WLAN.AP` .
        - `antenna` : select between the internal and the external antenna. With our development boards it defaults to using the on-board antenna. Value can be either:
            - `WLAN.INT_ANT` : The on-board antenna
            - `WLAN.EXT_ANT` : The U.FL connector (external antenna)
            - `WLAN.MAN_ANT` : Manually select the state of the antenna switch on `P12` . By default, this will select the on-board antenna
        - `power_save` enables or disables power save functions in `WLAN.STA` mode.
        - `hidden` : create a hidden SSID when set to `True` . only valid in `WLAN.AP` mode.
        - `bandwidth` is the Bandwidth to use, either:
            - `WLAN.HT20` : 20MHz
            - `WLAN.HT40` : 40MHz
        - `max_tx_pwr` is the maximum WiFi TX power allowed. see `WLAN.max_tx_power()` for more details
        - `country` tuple representing the country configuration parameters. see `WLAN.country()` for more details
        - `protocol` tuple representing the protocol. see `WLAN.wifi_protocol()` for more details
        '''
        ...

    def deinit(self):
        '''
        Disables the WiFi radio.
        '''
        ...

    def connect(self, ssid, *, auth: tuple[Literal[1, 2, 3], str] | tuple[Literal[5], str] | None = None, bssid: bytes | None = None, timeout: int | None = None, ca_certs: str | None = None, keyfile=None, certfile=None, identity=None, hostname=None):
        r'''
        Connect to a WiFi Access Point using the given SSID, and other parameters

        - :param ssid: a string with the SSID name.
        - :param auth: a tuple with `(sec, key)` . Security can be one of the following. The key is a string with the network password.
            - `None` :
            - `WLAN.WEP` : Using this in `WLAN.AP` , the key must be a string of hexadecimal values.
            - `WLAN.WPA`
            - `WLAN.WPA2`
            - `WLAN.WPA2_ENT` : this will use the following format: `(sec, username, password)`
        - :param bssid: is the MAC address of the AP to connect to. This is useful when there are several APs with the same SSID. The bssid is given as 6 Hexadecimal bytes literals (i.e `b'\xff\xff\xff\xff\xff\xff'` )
        - :param timeout: is the maximum time in milliseconds to wait for the connection to succeed.
        - :param ca_certs: is the path to the CA certificate. This argument is not mandatory.
        - :param keyfile: is the path to the client key. Only used if `username` and `password` are not part of the `auth` tuple.
        - :param certfile: is the path to the client certificate. Only used if `username` and `password` are not part of the `auth` tuple.
        - :param identity: is only used in case of `WLAN.WPA2_ENT` security. Needed by the server.
        - :param hostname: is the name of the host connecting to the AP. Max length of name string is 32 Bytes

        --------
        The ESP32 only handles certificates with `pkcs8` format (but not the “Traditional SSLeay RSAPrivateKey” format). The private key should be RSA coded with 2048 bits at maximum.
        '''
        ...

    class _Scan_result(NamedTuple):
        ssid: str
        bssid: bytes
        sec: int
        channel: int
        rssi: int

    def scan(self, *, ssid: str | None = None, bssid: bytes | None = None, channel=0, show_hidden=False, type=SCAN_ACTIVE, scantime: tuple[int, int] = (120, 120)) -> list[_Scan_result]:
        r'''
        Performs a network scan and returns a list of named tuples with (ssid, bssid, sec, channel, rssi). When no config args passed scan will be performed with default configurations.

        Note: For Fast scan mode ssid/bssid and channel should be

        - `ssid` : Scan only for the given ssid
        - `bssid` : Scan only for the given bssid. The bssid is given as 6 Hexadecimal bytes literals (i.e `b'\xff\xff\xff\xff\xff\xff'` )
        - `channel` : If set to 0, there will be an all-channel scan; otherwise, there will be a specific-channel scan.
        - `show_hidden` : Scan for hidden ssid’s as well.
        - `type` : The type of scan performed. Values can be
            - `WLAN.SCAN_ACTIVE` : the scan is will be performed by sending a probe request.
            - `WLAN.SCAN_PASSIVE` : switches to a specifi channel and waits for beacon
        - `scantime` : This field is used to control how long the scan dwells on each channel. For active scans, dwell times for each channel are listed below. For passive scans, this designates the dwell time for each channel. scantime is given as a tuple for min and max times `(min,max)`
            - min=0, max=0: scan dwells on each channel for 120 ms.
            - min>0, max=0: scan dwells on each channel for 120 ms.
            - min=0, max>0: scan dwells on each channel for max ms.
            - min>0, max>0: The minimum time the scan dwells on each channel is min ms. If no AP is found during this time frame, the scan switches to the next channel. Otherwise, the scan dwells on the channel for max ms.If you want to improve the performance of the the scan, you can try to modify these two parameters.
        '''
        ...

    def disconnect(self):
        '''
        Disconnect from the WiFi access point.
        '''
        ...

    def isconnected(self) -> bool:
        '''
        - In case of STA mode, returns `True` if connected to a WiFi access point and has a valid IP address.
        - In AP mode returns `True` when a station is connected, `False` otherwise.
        '''
        ...

    @overload
    def ifconfig(self, id: Literal[0, 1] = 0) -> tuple[str, str, str, str]:
        '''
        - When `id` is 0, the configuration will be get/set on the Station interface.
        - When `id` is 1 the configuration will be done for the AP interface.

        Get the interface configuration: (ip, netmask, gateway, dns)
        '''
        ...

    @overload
    def ifconfig(self, id: Literal[0, 1] = 0, config: Literal['dhcp'] | tuple[str, str, str, str] | None = None):
        '''
        - When `id` is 0, the configuration will be get/set on the Station interface.
        - When `id` is 1 the configuration will be done for the AP interface.

        Set the interface configuration.

        Optionally specify the configuration parameter:
        - `config='dhcp'` : If 'dhcp' is passed as a parameter, then the DHCP client is enabled and the IP parameters are negotiated with the DHCP server.
        - `config=(ip, netmask, gateway, dns)` : If the 4-tuple config is given then a static IP is configured.

        For example: `eth.ifconfig(config=('192.168.0.4', '255.255.255.0', '192.168.0.1', '8.8.8.8'))` .
        '''
        ...

    def ifconfig(self, id: Literal[0, 1] = 0, config: Literal['dhcp'] | tuple[str, str, str, str] | None = None) -> tuple[str, str, str, str] | None:
        ...

    @overload
    def mode(self) -> int:
        '''
        Get or set the WLAN mode.
        '''
        ...

    @overload
    def mode(self, mode: int):
        '''
        Get or set the WLAN mode.
        '''
        ...

    def mode(self, mode: int | None = None) -> int | None:
        ...

    @overload
    def ssid(self) -> str:
        '''
        Get the SSID.

        In case if mode = `WLAN.STA` this method can get the ssid of AP the board is connected to.
        In case of mode = `WLAN.AP` this method can get the ssid of the board’s own AP.
        In case of mode = `WLAN.STA_AP` this method can get the ssid of board’s own AP plus the AP the STA is connected to in form of a tuple:
        '''
        ...

    @overload
    def ssid(self, ssid: str):
        '''
        Set the SSID (Set SSID of AP).

        In case if mode = `WLAN.STA` this method can get the ssid of AP the board is connected to.
        In case of mode = `WLAN.AP` this method can get the ssid of the board’s own AP.
        In case of mode = `WLAN.STA_AP` this method can get the ssid of board’s own AP plus the AP the STA is connected to in form of a tuple:
        '''
        ...

    def ssid(self, ssid: str | None = None) -> str | None:
        ...

    def bssid(self) -> bytes:
        ...

    @overload
    def auth(self) -> tuple[Literal[1, 2, 3], str] | tuple[Literal[5], str] | None:
        '''
        Get the authentication type.
        '''
        ...

    @overload
    def auth(self, auth: tuple[Literal[1, 2, 3], str] | tuple[Literal[5], str] | None):
        '''
        Set the authentication type when in AP mode.
        '''
        ...

    def auth(self, auth: tuple[Literal[1, 2, 3], str] | tuple[Literal[5], str] | None = None) -> tuple[Literal[1, 2, 3], str] | tuple[Literal[5], str] | None:
        ...

    @overload
    def channel(self) -> int:
        '''
        - In AP mode, this will get or set the WiFi channel.
        - In STA mode, this will get the channel.
        '''
        ...

    @overload
    def channel(self, channel: int, secondary_channel=SECONDARY_CHN_NONE):
        '''
        - In AP mode, this will get or set the WiFi channel. The secondary channel has no effect.
        - In STA mode, this will get the channel. Setting the channel is only allowed in Promiscuous mode. A secondary channel can be given as well if the bandwidth is set to `WLAN.HT40`, choosing from the following:
            - `WLAN.SECONDARY_CHN_ABOVE`: Choose a secondary channel above the currently selected channel
            - `WLAN.SECONDARY_CHN_BELOW`: Choose a secondary channel below the currently selected channel
            - `WLAN.SECONDARY_CHN_NONE`: Possible channels are in the range of 1-14, depending on your country settings.
        '''
        ...

    def channel(self, channel: int | None = None, secondary_channel=SECONDARY_CHN_NONE) -> int | None:
        '''
        - In AP mode, this will get or set the WiFi channel. The secondary channel has no effect.
        - In STA mode, this will get the channel. Setting the channel is only allowed in Promiscuous mode. A secondary channel can be given as well if the bandwidth is set to `WLAN.HT40`, choosing from the following:
            - `WLAN.SECONDARY_CHN_ABOVE`: Choose a secondary channel above the currently selected channel
            - `WLAN.SECONDARY_CHN_BELOW`: Choose a secondary channel below the currently selected channel
            - `WLAN.SECONDARY_CHN_NONE`: Possible channels are in the range of 1-14, depending on your country settings.
        '''
        ...

    @overload
    def antenna(self) -> int:
        '''
        Get the antenna type (external or internal). Value can be:

        - `WLAN.INT_ANT` : The on-board antenna
        - `WLAN.EXT_ANT` : The U.FL connector (external antenna)
        - `WLAN.MAN_ANT` : Manually select the state of the antenna switch on `P12` . By default, this will select the on-board antenna

        With our development boards it defaults to using the internal antenna, but in the case of an OEM module, the antenna pin ( `P12` ) is not used, so it’s free to be used for other things.
        '''
        ...

    @overload
    def antenna(self, antenna: int) -> None:
        '''
        Set the antenna type (external or internal). Value can be:

        - `WLAN.INT_ANT` : The on-board antenna
        - `WLAN.EXT_ANT` : The U.FL connector (external antenna)
        - `WLAN.MAN_ANT` : Manually select the state of the antenna switch on `P12` . By default, this will select the on-board antenna

        With our development boards it defaults to using the internal antenna, but in the case of an OEM module, the antenna pin ( `P12` ) is not used, so it’s free to be used for other things.
        '''
        ...

    def antenna(self, antenna: int | None = None) -> int | None:
        ...

    class _Mac_addresses(NamedTuple):
        sta_mac: bytes
        ap_mac: bytes

    @overload
    def mac(self) -> _Mac_addresses:
        '''
        when no arguments are passed a 6-byte long `bytes` tuple object with the WiFI MAC address of both Wifi Station mode and Acces Point mode

        Note: STA and AP cannot have the Same Mac Address
        '''
        ...

    @overload
    def mac(self, mac: bytearray, mode: int):
        '''
        `mac` : a 6 bytes bytearray mac address
        `mode` : The Interface to set the given MAC address to `WLAN.STA` or `WLAN.AP`

        Ex: To set the mac address of Wifi Station mode:

        ```python
        wlan.mac(bytearray([0xAE, 0x77, 0x88, 0x99, 0x22, 0x44]), WLAN.STA)
        ```

        Note: STA and AP cannot have the Same Mac Address
        '''
        ...

    def mac(self, mac: bytearray | None = None, mode: int | None = None) -> _Mac_addresses | None:
        ...

    @overload
    def bandwidth(self) -> int:
        '''
        Get the bandwidth of the wifi, either 20 MHz or 40 MHz can be configured, use the following:

        - `WLAN.HT20` : 20MHz
        - `WLAN.HT40` : 40MHz
        '''
        ...

    @overload
    def bandwidth(self, bw: int) -> bool:
        '''
        Set the bandwidth of the wifi, either 20 MHz or 40 MHz can be configured, use the following:

        - `WLAN.HT20` : 20MHz
        - `WLAN.HT40` : 40MHz
        '''
        ...

    def bandwidth(self, bw: int | None = None) -> int | bool:
        ...

    @overload
    def hostname(self) -> str:
        '''
        Set the Host name of the device connecting to the AP in case of Wifi `mode=WLAN.STA` , in case of `mode=WLAN.AP` this is the name of the host hosting the AP. Max length of name string is 32 Bytes
        '''
        ...

    @overload
    def hostname(self, name: str) -> bool:
        '''
        Set the Host name of the device connecting to the AP in case of Wifi `mode=WLAN.STA` , in case of `mode=WLAN.AP` this is the name of the host hosting the AP. Max length of name string is 32 Bytes
        '''
        ...

    def hostname(self, name: str | None = None) -> str | bool:
        ...

    class _Ap_sta_info(NamedTuple):
        mac: bytes
        rssi: int
        wlan_protocol: int

    def ap_sta_list(self) -> list[_Ap_sta_info]:
        '''
        Gets an info list of all stations connected to the board’s AP.

        Info returned is a list of tuples containning ([mac address of connected STA], [average rssi value], [Wlan protocol enabled by STA]).

        Protocol types are either : `WLAN.PHY_11_B` , `WLAN.PHY_11_G` , `WLAN.PHY_11_N` or `WLAN.PHY_LOW_RATE`
        '''
        ...

    class _Ap_tcpip_sta_info(NamedTuple):
        mac: bytes
        IP: str

    def ap_tcpip_sta_list(self) -> list[_Ap_tcpip_sta_info]:
        '''
        This API returns with a list of the devices connected to the Pycom board when it is in AP mode.
        Each element of the returned list is a tuple, containing the MAC address and IP address of the device.
        '''
        ...

    @overload
    def max_tx_power(self) -> int:
        '''
        Gets the maximum allowable transmission power for wifi. This is also related to the country setting.

        Packets of different rates are transmitted in different powers according to the configuration in phy init data. This API only sets maximum WiFi transmiting power. If this API is called, the transmiting power of every packet will be less than or equal to the value set by this API.

        Possible values are between 8 and 78, where 8 corresponds to 2dBm and 78 to 20dBm. All values in between increase the maximum output power in 0.25dBm increments.
        '''
        ...

    @overload
    def max_tx_power(self, power: int) -> None:
        '''
        Sets the maximum allowable transmission power for wifi. This is also related to the country setting.

        Packets of different rates are transmitted in different powers according to the configuration in phy init data. This API only sets maximum WiFi transmiting power. If this API is called, the transmiting power of every packet will be less than or equal to the value set by this API.

        Values passed in the `power` argument are mapped to transmit power level in dBm. Possible values are between 8 and 78, where 8 corresponds to 2dBm and 78 to 20dBm. All values in between increase the maximum output power in 0.25dBm increments.
        '''
        ...

    def max_tx_power(self, power: int | None = None) -> int | None:
        ...

    class _Country(NamedTuple):
        country: str
        schan: int
        nchan: int
        max_tx_pwr: int
        policy: int

    @overload
    def country(self) -> _Country:
        '''
        Gets Country configuration parameters for wifi.

        - `country` That is the country name code , it is max 2 characters string representing the country eg: “CN” for china nad “NL” for Netherlands
        - `scahn` is the start channel number, in scan process scanning will be performed starting from this channels till the total number of channels. it should be less than or equal 14.
        - `nchan` is the total number of channels in the specified country. maximum is 14
        - `max_tx_pwr` Maximum transmission power allowed. see `WLAN.max_tx_power()` for more details.
        - `policy` Is the method when setting country configuration. Possible options are
            - `WLAN.COUNTRY_POL_AUTO` in STA mode the wifi will aquire the same country config of the connected AP
            - `WLAN.COUNTRY_POL_MAN` the configured country parameters will take effect regardless of connected AP.
        '''
        ...

    @overload
    def country(self, *, country: str, schan: int, nchan: int, max_tx_pwr: int = 0, policy: int = COUNTRY_POL_AUTO) -> None:
        '''
        Sets Country configuration parameters for wifi.

        - `country` That is the country name code , it is max 2 characters string representing the country eg: “CN” for china nad “NL” for Netherlands
        - `scahn` is the start channel number, in scan process scanning will be performed starting from this channels till the total number of channels. it should be less than or equal 14.
        - `nchan` is the total number of channels in the specified country. maximum is 14
        - `max_tx_pwr` Maximum transmission power allowed. see `WLAN.max_tx_power()` for more details.
        - `policy` Is the method when setting country configuration. Possible options are
            - `WLAN.COUNTRY_POL_AUTO` in STA mode the wifi will aquire the same country config of the connected AP
            - `WLAN.COUNTRY_POL_MAN` the configured country parameters will take effect regardless of connected AP.
        '''
        ...

    def country(self, *, country: str | None = None, schan: int | None = None, nchan: int | None = None, max_tx_pwr: int | None = None, policy: int | None = None) -> _Country | None:
        ...

    class _Joinded_ap_info(NamedTuple):
        bssid: bytes
        ssid: str
        primary_chn: int
        rssi: int
        auth: int
        standard: int

    def joined_ap_info(self) -> _Joinded_ap_info:
        '''
        Returns a tuple with `(bssid, ssid, primary channel, rssi, Authorization method, wifi standard used)` of the connected AP in case of STA mode.
        '''
        ...

    class _Wifi_protocols(NamedTuple):
        protocol_11B: bool
        protocol_11G: bool
        protocol_11N: bool

    @overload
    def wifi_protocol(self) -> _Wifi_protocols:
        '''
        Sets or gets Wifi Protocol supported in ( `PHY_11_B` , `PHY_11_G` , `PHY_11_N` ) format. Currently 802.11b or 802.11bg or 802.11bgn mode is available.
        '''
        ...

    @overload
    def wifi_protocol(self, _protocols: tuple[bool, bool, bool]):
        '''
        Sets or gets Wifi Protocol supported in ( `PHY_11_B` , `PHY_11_G` , `PHY_11_N` ) format. Currently 802.11b or 802.11bg or 802.11bgn mode is available.
        '''
        ...

    def wifi_protocol(self, _protocols: tuple[bool, bool, bool] | None = None) -> _Wifi_protocols | None:
        ...

    def send_raw(self, Buffer: bytes, interface=STA, use_sys_seq=True):
        '''
        Send raw data through the Wifi Interface.

        `Buffer` : Buffer of bytes object Containning Data to be transmitted. Data should not be greater than 1500 nor smaller than 24.
        `interface` : The Interface to use for transmitting Data AP or STA in case the mode used is APSTA. otherwise the interface currently active will be used.
        `use_sys_seq` : `True` to use the systems next sequance number for sending the data, `False` for keeping the sequance number in the given raw data buffer unchanged.
        '''
        ...

    @overload
    def callback(self, trigger: int, handler: Callable[[Self], None]):
        '''
        Register a user callback function `handler` to be called once any of the `trigger` events occures optionally with a passed `arg` . by default the wlan obj is passed as arg to the handler. To unregister the callback you can call the `wlan.callback` function with empty `handler` and `arg` parameters. Possible triggers:

        - `WLAN.EVENT_PKT_MGMT` : Managment packet recieved in promiscuous mode.
        - `WLAN.EVENT_PKT_CTRL` : Control Packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_DATA` : Data packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_DATA_MPDU` : MPDU data packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_DATA_AMPDU` : AMPDU data packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_MISC` : misc paket recieved in promiscuous mode.
        - `WLAN.EVENT_PKT_ANY` : Any packet recieved in promiscuous mode.
        - `WLAN.SMART_CONF_DONE` : Smart Config of wifi ssid/pwd Finished
        - `WLAN.SMART_CONF_TIEMOUT` : Smart Config of wifi ssid/pwd timed-out
        '''
        ...

    @overload
    def callback(self, trigger: int, handler: Callable[[_T], None], arg: _T):
        '''
        Register a user callback function `handler` to be called once any of the `trigger` events occures optionally with a passed `arg` . by default the wlan obj is passed as arg to the handler. To unregister the callback you can call the `wlan.callback` function with empty `handler` and `arg` parameters. Possible triggers:

        - `WLAN.EVENT_PKT_MGMT` : Managment packet recieved in promiscuous mode.
        - `WLAN.EVENT_PKT_CTRL` : Control Packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_DATA` : Data packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_DATA_MPDU` : MPDU data packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_DATA_AMPDU` : AMPDU data packet recieved in promiscuous mode
        - `WLAN.EVENT_PKT_MISC` : misc paket recieved in promiscuous mode.
        - `WLAN.EVENT_PKT_ANY` : Any packet recieved in promiscuous mode.
        - `WLAN.SMART_CONF_DONE` : Smart Config of wifi ssid/pwd Finished
        - `WLAN.SMART_CONF_TIEMOUT` : Smart Config of wifi ssid/pwd timed-out
        '''
        ...

    @overload
    def callback(self, trigger: int):
        '''
        Unregister the callback
        '''
        ...

    def callback(self, trigger: int, handler=None, arg=None):
        ...

    @overload
    def promiscuous(self) -> bool:
        '''
        Gets the WiFi Promiscuous mode.
        '''
        ...

    @overload
    def promiscuous(self, enable: bool):
        '''
        Gets or sets WiFi Promiscuous mode.

        Note:
        - Promiscuous mode should be enabled for Wifi packets types Events to be triggered
        - for changing wifi channel via `wlan.channel()` promiscuous mode should be enabled.

        Example using promoscious mode:

        ```python
        from network import WLAN
        import ubinascii

        def pack_cb(pack):
            mac = bytearray(6)
            pk = wlan.wifi_packet()
            control = pk.data[0]
            subtype = (0xF0 & control) >> 4
            type = 0x0C & control
            #print("Control:{}, subtype:{}, type:{}".format(control, subtype, type))
            if subtype == 4:
                for i in range (0,6):
                    mac[i] = pk.data[10 + i]
                print ("Wifi Node with MAC: {}".format(ubinascii.hexlify(mac)))

        wlan = WLAN(mode=WLAN.STA, antenna=WLAN.EXT_ANT)
        wlan.callback(trigger=WLAN.EVENT_PKT_MGMT, handler=pack_cb)
        wlan.promiscuous(True)
        w.promiscuous(False)
        ```
        '''
        ...

    def promiscuous(self, enable: bool | None = None) -> bool | None:
        ...

    def events(self) -> int:
        '''
        This function will return an integer object as mask for triggered events.
        '''
        ...

    class _Wifi_packet(NamedTuple):
        rssi: int
        rate: int
        sig_mode: int
        mcs: int
        cwb: int
        aggregation: int
        stbc: int
        fec_coding: int
        sgi: int
        noise_floor: int
        ampdu_cnt: int
        channel: int
        sec_channel: int
        time_stamp: int
        ant: int
        sig_len: int
        rx_state: int
        data: bytes

    def wifi_packet(self) -> _Wifi_packet:
        '''
        This function will return a tuple with Wifi packet info captured in promiscuous mode.
        '''
        ...

    @overload
    def ctrl_pkt_filter(self) -> int:
        '''
        Get the filter mask for Wifi control packets in promiscuous mode. Possible filters:

        - `WLAN.FILTER_CTRL_PKT_ALL` : Filter all Control packets
        - `WLAN.FILTER_CTRL_PKT_WRAPPER` : Filter control wrapper packets
        - `WLAN.FILTER_CTRL_PKT_BAR` : Filter Control BAR packets
        - `WLAN.FILTER_CTRL_PKT_BA` : Filter Control BA packets
        - `WLAN.FILTER_CTRL_PKT_PSPOLL` : Filter Control PSPOLL Packets
        - `WLAN.FILTER_CTRL_PKT_CTS` : Filter Control CTS packets
        - `WLAN.FILTER_CTRL_PKT_ACK` : Filter Control ACK packets
        - `WLAN.FILTER_CTRL_PKT_CFEND` : Filter Control CFEND Packets
        - `WLAN.FILTER_CTRL_PKT_CFENDACK` : Filter Control CFENDACK Packets
        '''
        ...

    @overload
    def ctrl_pkt_filter(self, filter: int) -> None:
        '''
        Set the filter mask for Wifi control packets in promiscuous mode. Possible filters:

        - `WLAN.FILTER_CTRL_PKT_ALL` : Filter all Control packets
        - `WLAN.FILTER_CTRL_PKT_WRAPPER` : Filter control wrapper packets
        - `WLAN.FILTER_CTRL_PKT_BAR` : Filter Control BAR packets
        - `WLAN.FILTER_CTRL_PKT_BA` : Filter Control BA packets
        - `WLAN.FILTER_CTRL_PKT_PSPOLL` : Filter Control PSPOLL Packets
        - `WLAN.FILTER_CTRL_PKT_CTS` : Filter Control CTS packets
        - `WLAN.FILTER_CTRL_PKT_ACK` : Filter Control ACK packets
        - `WLAN.FILTER_CTRL_PKT_CFEND` : Filter Control CFEND Packets
        - `WLAN.FILTER_CTRL_PKT_CFENDACK` : Filter Control CFENDACK Packets
        '''
        ...

    def ctrl_pkt_filter(self, filter: int | None = None) -> int | None:
        ...

    def smartConfig(self):
        '''
        Start SmartConfig operation, the smartConfig is a provisioning technique that enables setting Wifi credentials for station mode wirelessly via mobile app.

        Steps:
        - call `wlan.smartConfig()` (if smartConfig is not enabled on boot or you want to restart smartConfig)
        - Use mobile App (ESP touch or Pycom App) to set ssid and password for the AP
        - You can register a callback to be triggered when smart Config is Finished successfuly or times out.
        '''
        ...

    def Connected_ap_pwd(self) -> str:
        '''
        Get the password of AP the Device is connected to.
        '''
        ...

