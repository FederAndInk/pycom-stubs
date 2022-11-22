"""
Module: 'machine' on FiPy v1.11

The machine module contains specific functions related to the board.
Quick Usage Example

```python
import machine

help(machine) # display all members from the machine module
machine.freq() # get the CPU frequency
machine.unique_id() # return the 6-byte unique id of the board (the LoPy's WiFi MAC address)
```
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from typing import overload

class ADC:
    ''
    ATTN_0DB = 0
    ATTN_11DB = 3
    ATTN_2_5DB = 1
    ATTN_6DB = 2
    def channel():
        pass

    def deinit():
        pass

    def init():
        pass

    def vref():
        pass

    def vref_to_pin():
        pass

BROWN_OUT_RESET = 5

class CAN:
    ''
    FILTER_LIST = 0
    FILTER_MASK = 2
    FILTER_RANGE = 1
    FORMAT_BOTH = 3
    FORMAT_EXT = 2
    FORMAT_STD = 1
    NORMAL = 0
    RX_FIFO_NOT_EMPTY = 2
    RX_FIFO_OVERRUN = 4
    RX_FRAME = 1
    SILENT = 1
    def callback():
        pass

    def deinit():
        pass

    def events():
        pass

    def init():
        pass

    def recv():
        pass

    def send():
        pass

    def soft_filter():
        pass


class DAC:
    ''
    def deinit():
        pass

    def init():
        pass

    def tone():
        """
        test

        ```python
        def t():
            pass
        ```
        """
        pass

    def write():
        pass

DEEPSLEEP_RESET = 3
HARD_RESET = 1

class I2C:
    ''
    MASTER = 0
    def deinit():
        pass

    def init():
        pass

    def readfrom():
        pass

    def readfrom_into():
        pass

    def readfrom_mem():
        pass

    def readfrom_mem_into():
        pass

    def scan():
        pass

    def writeto():
        pass

    def writeto_mem():
        pass

PIN_WAKE = 1

class PWM:
    ''
    def channel():
        pass

    def init():
        pass

PWRON_RESET = 0
PWRON_WAKE = 0

class board:
    G0: 'Pin'
    G1: 'Pin'
    G2: 'Pin'
    G3: 'Pin'
    G4: 'Pin'
    G5: 'Pin'
    G6: 'Pin'
    G7: 'Pin'
    G8: 'Pin'
    G9: 'Pin'
    G10: 'Pin'
    G11: 'Pin'
    G12: 'Pin'
    G13: 'Pin'
    G14: 'Pin'
    G15: 'Pin'
    G16: 'Pin'
    G17: 'Pin'
    G22: 'Pin'
    G23: 'Pin'
    G24: 'Pin'
    G28: 'Pin'
    G30: 'Pin'
    G31: 'Pin'

class cpu:
    P0: 'Pin'
    P1: 'Pin'
    P2: 'Pin'
    P3: 'Pin'
    P4: 'Pin'
    P5: 'Pin'
    P6: 'Pin'
    P7: 'Pin'
    P8: 'Pin'
    P9: 'Pin'
    P10: 'Pin'
    P11: 'Pin'
    P12: 'Pin'
    P13: 'Pin'
    P14: 'Pin'
    P15: 'Pin'
    P16: 'Pin'
    P17: 'Pin'
    P18: 'Pin'
    P19: 'Pin'
    P20: 'Pin'
    P21: 'Pin'
    P22: 'Pin'
    P23: 'Pin'

class Pin:
    '''
    A pin is the basic object to control I/O pins (also known as GPIO - general-purpose input/output). It has methods to set the mode of the pin (input, output, etc) and methods to get and set the digital logic level. For analog control of a pin, see the ADC class.
    Quick Usage Example

    ```python
    from machine import Pin

    # initialize `P9` in gpio mode and make it an output
    p_out = Pin('P9', mode=Pin.OUT)
    p_out.value(1)
    p_out.value(0)
    p_out.toggle()
    p_out(True)

    # make `P10` an input with the pull-up enabled
    p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
    p_in() # get value, 0 or 1
    ```
    '''
    IN = 1
    IRQ_FALLING = 2
    IRQ_HIGH_LEVEL = 5
    IRQ_LOW_LEVEL = 4
    IRQ_RISING = 1
    OPEN_DRAIN = 7
    OUT = 2
    PULL_DOWN = 2
    PULL_UP = 1

    exp_board: board
    module: cpu

    def __init__(self, id: str, mode=Pin.OUT, pull=None, alt=-1):
        '''
        Create a new Pin object associated with the string `id` . If additional arguments are given, they are used to initialise the pin. See pin.init()
        
        ```python
        
        from machine import Pin
        p = Pin('P10', mode=Pin.OUT, pull=None, alt=-1)
        ```
        '''
        ...

    def init(self, mode, pull, *, alt):
        '''
        Initialise the pin:
        
        - `mode` can be one of:
            - `Pin.IN` - input pin.
            - `Pin.OUT` - output pin in push-pull mode.
            - `Pin.OPEN_DRAIN` - input or output pin in open-drain mode.
        
        - `pull` can be one of:
            - `None` - no pull up or down resistor.
            - `Pin.PULL_UP` - pull up resistor enabled.
            - `Pin.PULL_DOWN` - pull down resistor enabled.
        
        - `*`
            - Pin value: `0` or `1`
        
        - `alt` is the id of the alternate function.
        Returns: `None` .
        '''
        ...

    def id(self):
        '''
        Get the pin id.
        
        '''
        ...

    @overload
    def value(self) -> bool | int:
        '''
        Get or set the digital logic level of the pin. This only works in `Pin.OUT` mode. Values can be:
        
        - `True` or 1: High 
        - `False` or 0: Low 
        '''
        ...

    @overload
    def value(self, value: bool | int):
        '''
        Get or set the digital logic level of the pin. This only works in `Pin.OUT` mode. Values can be:
        
        - `True` or 1: High 
        - `False` or 0: Low 
        '''
        ...

    @overload
    def __call__(self) -> bool | int:
        '''
        Pin objects are callable. The call method provides a (fast) shortcut to set and get the value of the pin.
        
        
        Example:
        
        ```python
        
        from machine import Pin
        pin = Pin('P12', mode=Pin.IN, pull=Pin.PULL_UP)
        pin()   # fast method to get the value
        ```
        See `pin.value()` for more details.
        
        '''
        ...

    @overload
    def __call__(self, value: bool | int):
        '''
        Pin objects are callable. The call method provides a (fast) shortcut to set and get the value of the pin.
        
        
        Example:
        
        ```python
        
        from machine import Pin
        pin = Pin('P12', mode=Pin.IN, pull=Pin.PULL_UP)
        pin()   # fast method to get the value
        ```
        See `pin.value()` for more details.
        
        '''
        ...

    def toggle(self):
        '''
        Toggle the value of the pin.
        
        '''
        ...

    @overload
    def mode(self) -> int:
        '''
        Get or set the pin mode. Modes can be:
        
        - `Pin.IN` 
        - `Pin.OUT` 
        - `Pin.OPEN_DRAIN` 
        '''
        ...

    @overload
    def mode(self, mode: int):
        '''
        Get or set the pin mode. Modes can be:
        
        - `Pin.IN` 
        - `Pin.OUT` 
        - `Pin.OPEN_DRAIN` 
        '''
        ...

    @overload
    def pull(self) -> int:
        '''
        Get or set the pin pull. Pull can be:
        
        - `Pin.PULL_UP` 
        - `Pin.PULL_DOWN` 
        - `None` 
        '''
        ...

    @overload
    def pull(self, pull: int):
        '''
        Get or set the pin pull. Pull can be:
        
        - `Pin.PULL_UP` 
        - `Pin.PULL_DOWN` 
        - `None` 
        '''
        ...

    @overload
    def hold(self, hold) -> bool:
        '''
        Get or set the pin hold. This functionality can be used to hold a pin’s state after deepsleep, `machine.reset()` or a watchdog timer reset. Passing `True` will hold the current value of the pin, `False` will release the hold state. When a pin is in hold state, its value cannot be changed by using `Pin.value()` or `Pin.toggle()` , until the hold is released. Only pins in the RTC power domain can retain their value through deep sleep or reset. These are: `P2, P3, P4, P6, P8, P9, P10, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23` 
        
        
        You can use the following example:
        
        ```python
        from machine import Pin
        import machine
        p3 = Pin('P3', mode=Pin.OUT)
        p3.value(1) #can also be p3.value(0)
        p3.hold(True) #hold the pin high
        machine.reset()
        # instead, you can use:
        # machine.deepsleep(10000)
        
        # P3 will still be high here
        ```
        A few things to keep in mind when using the pin hold functionality:
        
        
        
        - This feature only preserves the pin value:
            - During a (deep)sleep 
            - After waking up from deepsleep 
            - After `machine.reset()` 
            - After a WDT reset 
        
        - The hold state itself is not preserved in Micropython after the above mentioned resets. This means that `pin.hold()` will return `False` after such reset, even though the pin is actually still held in hardware . 
        - `pin.hold()` does not return the pin’s value. You can hold a pin high or low. 
        - Applying a hard-reset, by for example pressing the reset button, will reset the pin value and release the hold. 
        '''
        ...

    @overload
    def hold(self, hold: bool):
        '''
        Get or set the pin hold. This functionality can be used to hold a pin’s state after deepsleep, `machine.reset()` or a watchdog timer reset. Passing `True` will hold the current value of the pin, `False` will release the hold state. When a pin is in hold state, its value cannot be changed by using `Pin.value()` or `Pin.toggle()` , until the hold is released. Only pins in the RTC power domain can retain their value through deep sleep or reset. These are: `P2, P3, P4, P6, P8, P9, P10, P13, P14, P15, P16, P17, P18, P19, P20, P21, P22, P23` 
        
        
        You can use the following example:
        
        ```python
        from machine import Pin
        import machine
        p3 = Pin('P3', mode=Pin.OUT)
        p3.value(1) #can also be p3.value(0)
        p3.hold(True) #hold the pin high
        machine.reset()
        # instead, you can use:
        # machine.deepsleep(10000)
        
        # P3 will still be high here
        ```
        A few things to keep in mind when using the pin hold functionality:
        
        
        
        - This feature only preserves the pin value:
            - During a (deep)sleep 
            - After waking up from deepsleep 
            - After `machine.reset()` 
            - After a WDT reset 
        
        - The hold state itself is not preserved in Micropython after the above mentioned resets. This means that `pin.hold()` will return `False` after such reset, even though the pin is actually still held in hardware . 
        - `pin.hold()` does not return the pin’s value. You can hold a pin high or low. 
        - Applying a hard-reset, by for example pressing the reset button, will reset the pin value and release the hold. 
        '''
        ...

    def callback(self, trigger,handler=None,arg=None):
        '''
        Set a callback to be triggered when the input level at the pin changes.
        
        
        
        - `trigger` is the type of event that triggers the callback. Possible values are:
            - `Pin.IRQ_FALLING` interrupt on falling edge. 
            - `Pin.IRQ_RISING` interrupt on rising edge. 
            - `Pin.IRQ_LOW_LEVEL` interrupt on low level. 
            - `Pin.IRQ_HIGH_LEVEL` interrupt on high level. 
        
        The values can be OR-ed together, for instance `trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING` 
        
        - `handler` is the function to be called when the event happens. This function will receive one argument. Set `handler` to `None` to disable it. 
        - `arg` is an optional argument to pass to the callback. If left empty or set to `None` , the function will receive the Pin object that triggered it. 
        
        Example:
        
        ```python
        
        from machine import Pin
        
        def pin_handler(arg):
            print("got an interrupt in pin %s" % (arg.id()))
        
        p_in = Pin('P10', mode=Pin.IN, pull=Pin.PULL_UP)
        p_in.callback(Pin.IRQ_FALLING | Pin.IRQ_RISING, pin_handler)
        ```
        --------
        For more information on how Pycom’s products handle interrupts, see here.
        '''
        ...

class RMT:
    ''
    HIGH = 1
    LOW = 0
    def deinit():
        pass

    def init():
        pass

    def pulses_get():
        pass

    def pulses_send():
        pass


class RTC:
    ''
    INTERNAL_RC = 0
    XTAL_32KHZ = 1
    def init():
        pass

    def memory():
        pass

    def now():
        pass

    def ntp_sync():
        pass

    def synced():
        pass

RTC_WAKE = 2

class SD:
    ''
    def deinit():
        pass

    def init():
        pass

    def ioctl():
        pass

    def readblocks():
        pass

    def writeblocks():
        pass

SOFT_RESET = 4

class SPI:
    ''
    LSB = 1
    MASTER = 0
    MSB = 0
    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def write():
        pass

    def write_readinto():
        pass


class Timer:
    ''
    Alarm = None
    Chrono = None
    def sleep_us():
        pass


class Touch:
    ''
    def config():
        pass

    def init_value():
        pass

    def read():
        pass


class UART:
    ''
    EVEN = 2
    ODD = 3
    def any():
        pass

    def deinit():
        pass

    def init():
        pass

    def read():
        pass

    def readinto():
        pass

    def readline():
        pass

    def sendbreak():
        pass

    def wait_tx_done():
        pass

    def write():
        pass

ULP_WAKE = 3
WAKEUP_ALL_LOW = 0
WAKEUP_ANY_HIGH = 1

class WDT:
    ''
    def feed():
        pass

    def init():
        pass

WDT_RESET = 2
def deepsleep():
    pass

def disable_irq():
    pass

def enable_irq():
    pass

def flash_encrypt():
    pass

def freq():
    pass

def idle():
    pass

def info():
    pass

def main():
    pass

mem16 = None
mem32 = None
mem8 = None
def pin_sleep_wakeup():
    pass

def remaining_sleep_time():
    pass

def reset():
    pass

def reset_cause():
    pass

def rng() -> int:
    '''
    Return a 24-bit software generated random number.
    '''
    ...

def secure_boot():
    pass

def sleep():
    pass

def temperature():
    pass

def unique_id():
    pass

def wake_reason():
    pass

