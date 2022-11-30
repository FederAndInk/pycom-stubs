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

from typing import overload, Callable, TypeVar, Any
from typing_extensions import Self

_T = TypeVar('_T')


PWRON_RESET = 0
HARD_RESET = 1
WDT_RESET = 2
DEEPSLEEP_RESET = 3
SOFT_RESET = 4
BROWN_OUT_RESET = 5

PWRON_WAKE = 0
PIN_WAKE = 1
RTC_WAKE = 2
ULP_WAKE = 3

WAKEUP_ALL_LOW = 0
WAKEUP_ANY_HIGH = 1

mem16 = None
mem32 = None
mem8 = None


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


class PWM:
    ''
    def channel():
        pass

    def init():
        pass


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

    def __init__(self, id: str, mode=OUT, pull: int | None = None, alt=-1):
        '''
        Create a new Pin object associated with the string `id` . If additional arguments are given, they are used to initialise the pin. See pin.init()

        ```python

        from machine import Pin
        p = Pin('P10', mode=Pin.OUT, pull=None, alt=-1)
        ```
        '''
        ...

    def init(self, mode: int, pull: int | None, *, alt: int | str):
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

    def id(self) -> str:
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

    def value(self, value: bool | int | None = None) -> bool | int | None:
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

    def __call__(self, value: bool | int | None = None) -> bool | int | None:
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

    def mode(self, mode: int | None = None) -> int | None:
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

    def pull(self, pull: int | None = None) -> int | None:
        ...

    @overload
    def hold(self) -> bool:
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

    def hold(self, hold: bool | None = None) -> bool | None:
        ...

    @overload
    def callback(self, trigger: int, handler: Callable[[_T], None], arg: _T):
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
        For more information on how Pycom’s products handle interrupts, see [here](https://docs.pycom.io/firmwareapi/notes/#interrupt-handling).
        '''
        ...

    @overload
    def callback(self, trigger: int, handler: Callable[[Self], None]):
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
        For more information on how Pycom’s products handle interrupts, see [here](https://docs.pycom.io/firmwareapi/notes/#interrupt-handling).
        '''
        ...

    @overload
    def callback(self, trigger: int):
        '''
        remove callbacks specified by `trigger`
        '''
        ...

    @overload
    def callback(self):
        '''
        remove all callbacks
        '''
        ...

    def callback(self, trigger: int | None = None, handler=None, arg=None):
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
    '''
    Measure Time and Set Alarms

    Timers can be used for a great variety of tasks, like measuring time spans or being notified that a specific interval has elapsed.

    These two concepts are grouped into two different subclasses:

    - Chrono: used to measure time spans.
    - Alarm: to get interrupted after a specific interval.

    You can create as many of these objects as needed.
    '''
    class Alarm:
        '''
        Example:

        ```python
        from machine import Timer

        class Clock:

        def __init__(self):
            self.seconds = 0
            self.__alarm = Timer.Alarm(self._seconds_handler, 1, periodic=True)

        def _seconds_handler(self, alarm):
            self.seconds += 1
            print("%02d seconds have passed" % self.seconds)
            if self.seconds == 10:
                alarm.cancel() # stop counting after 10 seconds

        clock = Clock()
        ```
        --------
        For more information on how Pycom’s products handle interrupts, see [notes](https://docs.pycom.io/firmwareapi/notes/#interrupt-handling).
        '''

        @overload
        def __init__(self, handler: Callable[[Self], None], s: float | None = None, *, ms: int | None = None, us: int | None = None, periodic=False):
            '''
            Create an Alarm object.

            - `handler` : will be called after the interval has elapsed. If set to `None` , the alarm will be disabled after creation.
            - `arg` : an optional argument can be passed to the callback handler function. If `None` is specified, the function will receive the object that triggered the alarm.
            - `s, ms, us` : the interval can be specified in seconds (float), miliseconds (integer) or microseconds (integer). Only one at a time can be specified.
            - `periodic` : an alarm can be set to trigger repeatedly by setting this parameter to `True` .
            '''
            ...

        @overload
        def __init__(self, handler: Callable[[_T], None], s: float | None = None, *, ms: int | None = None, us: int | None = None, arg: _T, periodic=False):
            '''
            Create an Alarm object.

            - `handler` : will be called after the interval has elapsed. If set to `None` , the alarm will be disabled after creation.
            - `arg` : an optional argument can be passed to the callback handler function. If `None` is specified, the function will receive the object that triggered the alarm.
            - `s, ms, us` : the interval can be specified in seconds (float), miliseconds (integer) or microseconds (integer). Only one at a time can be specified.
            - `periodic` : an alarm can be set to trigger repeatedly by setting this parameter to `True` .
            '''
            ...

        def __init__(self, handler: Callable[[Any], None], s: float | None = None, *, ms: int | None = None, us: int | None = None, arg = None, periodic=False):
            ...

        @overload
        def callback(self, handler: Callable[[Self], None] | None):
            ...
            '''
            Specify a callback handler for the alarm. If set to `None` , the alarm will be disabled.

            An optional argument `arg` can be passed to the callback handler function. If `None` is specified, the function will receive the object that triggered the alarm.
            '''

        @overload
        def callback(self, handler: Callable[[_T], None] | None, arg: _T):
            '''
            Specify a callback handler for the alarm. If set to `None` , the alarm will be disabled.

            An optional argument `arg` can be passed to the callback handler function. If `None` is specified, the function will receive the object that triggered the alarm.
            '''
            ...

        def callback(self, handler: None | Callable[[Any], None], arg=None):
            '''
            Specify a callback handler for the alarm. If set to `None` , the alarm will be disabled.

            An optional argument `arg` can be passed to the callback handler function. If `None` is specified, the function will receive the object that triggered the alarm.
            '''
            ...

        def cancel(self):
            '''
            Disables the alarm.
            '''
            ...

    class Chrono:
        '''
        Example:

        ```python
        from machine import Timer
        import time

        chrono = Timer.Chrono()

        chrono.start()
        time.sleep(1.25) # simulate the first lap took 1.25 seconds
        lap = chrono.read() # read elapsed time without stopping
        time.sleep(1.5)
        chrono.stop()
        total = chrono.read()

        print()
        print("the racer took %f seconds to finish the race" % total)
        print("  %f seconds in the first lap" % lap)
        print("  %f seconds in the last lap" % (total - lap))
        ```
        '''

        def __init__(self):
            '''
            Create a chronometer object.
            '''
            ...
        def start(self):
            '''
            Start the chronometer.
            '''
            ...

        def stop(self):
            '''
            Stop the chronometer.
            '''
            ...

        def reset(self):
            '''
            Reset the time count to 0.
            '''
            ...

        def read(self) -> float:
            '''
            Get the elapsed time in seconds.
            '''
            ...

        def read_ms(self) -> float:
            '''
            Get the elapsed time in milliseconds.

            '''
            ...

        def read_us(self) -> float:
            '''
            Get the elapsed time in microseconds.
            '''
            ...

    def sleep_us(self, us: int):
        '''
        Delay for a given number of microseconds, should be positive or 0 (for speed, the condition is not enforced). Internally it uses the same timer as the other elements of the `Timer` class. It compensates for the calling overhead, so for example, 100us should be really close to 100us. For times bigger than 10,000us it releases the GIL to let other threads run, so exactitude is not guaranteed for delays longer than that.
        '''
        ...


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


class WDT:
    ''
    def feed():
        pass

    def init():
        pass


def flash_encrypt():
    pass


def secure_boot():
    pass


def reset():
    '''
    Resets the device in a manner similar to pushing the external RESET button.
    '''
    ...


def reset_cause() -> int:
    '''
    Returns an integer. The possible values are:

    - `machine.PWRON_RESET` : Reset by power on or reset button
    - `machine.HARD_RESET` :
    - `machine.WDT_RESET` : Reset by watchdog timer
    - `machine.DEEPSLEEP_RESET` : Reset caused by deepsleep
    - `machine.SOFT_RESET` : Reset by e.g. `sys.init()`
    - `machine.BROWN_OUT_RESET` : Reset caused by low voltage
    '''
    ...


def disable_irq() -> int:
    '''
    Disable interrupt requests. Returns and integer representing the previous IRQ state. This return value can be passed to `enable_irq` to restore the IRQ to its original state.
    '''
    ...


def enable_irq(state: int | None = None):
    '''
    Enable interrupt requests. The most common use of this function is to pass the value returned by `disable_irq` to exit a critical section. Another options is to enable all interrupts which can be achieved by calling the function with no parameters.
    '''
    ...


def freq() -> int:
    '''
    Returns CPU frequency in hertz.
    '''
    ...


def idle():
    '''
    Gates the clock to the CPU, useful to reduce power consumption at any time during short or long periods. Peripherals continue working and execution resumes as soon as any interrupt is triggered (on many ports this includes system timer interrupt occurring at regular intervals on the order of millisecond).
    '''
    ...


def sleep(time_ms=None, resume_wifi_ble=False):
    '''
    Sets the device in to light sleep mode , where in this mode digital peripherals, most of the RAM, and CPUs are clock-gated, and supply voltage is reduced. Upon exit from light sleep, peripherals and CPUs resume operation, their internal state is preserved.

    - `time_ms` is the sleep time in milliseconds. If not given, it will sleep indefinitely unless power is removed, the reset button is pressed or another wakeup source is configured.
    - `resume_wifi_ble` is a boolean value that enables or disable restoring after wakeup any WiFi or BLE connection that was interrupted by light sleep.
      - `True` Restore WiFi / BLE connections
      - `False` Do not restore WiFi / BLE connections restoration (default)

    --------
    Note: in light sleep mode LoRa/LTE modems are stopped and have to be re-initialized after wakeup.
    '''
    ...


def deepsleep(time_ms=None):
    '''
    Stops the CPU and all peripherals, including the networking interfaces (except for LTE). Execution is resumed similar to pressing the reset button. The pin states are not held by default. You can choose to hold specific pins using `machine.pin.hold()`

    - `time_ms` is the sleep time in milliseconds. If not given, it will sleep indefinitely unless power is removed, the reset button is pressed or another wakeup source is configured.

    Products with LTE connectivity, such as the FiPy, GPy, G01, need to have the LTE radio disabled separately via the LTE class before entering deepsleep. This is necessary because the LTE radio is powered independently, which allows for use cases that wake the system from deepsleep by an event from the LTE network, for example receiving data or an SMS.

    --------
    Note: in deep sleep mode LoRa/LTE modems are stopped and have to be re-initialized after wakeup.
    '''
    ...


def pin_sleep_wakeup(pins: list[Pin | str] | tuple[Pin | str, ...], mode: int, enable_pull: bool):
    '''
    Configure pins to wake up from sleep mode. The pins which have this capability are: `P2, P3, P4, P6, P8 to P10 and P13 to P23` .

    The arguments are:

    - `pins` a list or tuple containing the `GPIO` to setup for sleep wakeup.
    - `mode` selects the way the configure `GPIO` s can wake up the module. The possible values are:
      - `machine.WAKEUP_ALL_LOW`
      - `machine.WAKEUP_ANY_HIGH` .
    - `enable_pull` if set to `True` keeps the pull up or pull down resistors enabled during sleep. If this variable is set to `True` , then `ULP` or capacitive touch wakeup cannot be used in combination with `GPIO` wakeup.
    '''
    ...


def wake_reason() -> tuple[int, list]:
    '''
    Get the wake reason. See constants for the possible return values. Returns a tuple of the form: `(wake_reason, gpio_list)` . When the wakeup reason is either GPIO or touch pad, then the second element of the tuple is a list with GPIOs that generated the wakeup. The possible wake reasons are:

    - `machine.PWRON_WAKE` : Wake up by power on or reset button
    - `machine.PIN_WAKE` : Wake up by interrupt on pin
    - `machine.RTC_WAKE` : Wake up because sleep time is over
    - `machine.ULP_WAKE` : Wake up by touch button
    '''
    ...


def remaining_sleep_time() -> int:
    '''
    Returns the remaining timer duration (in milliseconds) if the ESP32 is woken up from deep sleep by something other than the timer. For example, if you set the timer for 30 seconds (30000 ms) and it wakes up after 10 seconds then this function will return 20000.
    '''
    ...


def main(filename: str):
    '''
    Set the `filename` of the main script to run after `boot.py` is finished. If this function is not called then the default file `main.py` will be executed.

    It only makes sense to call this function from within `boot.py` .
    '''
    ...


def rng() -> int:
    '''
    Return a 24-bit software generated random number.
    '''
    ...


def unique_id() -> bytes:
    '''
    Returns a byte string with a unique identifier of a board/SoC. It will vary from a board/SoC instance to another, if underlying hardware allows. Length varies by hardware (so use substring of a full value if you expect a short ID). In some MicroPython ports, ID corresponds to the network MAC address.

    --------
    Use `ubinascii.hexlify()` to convert the byte string to hexadecimal form for ease of manipulation and use elsewhere.
    '''
    ...


def info():
    '''
    Prints the high water mark of the stack associated with various system tasks, in words (1 word = 4 bytes on the ESP32). If the value is zero then the task has likely overflowed its stack.
    '''
    ...


def temperature() -> int:
    '''
    Returns the temperature of the ESP32 core in degrees Farenheit. You can convert this to Celcius by `((machine.temperature() - 32) / 1.8)`
    '''
    ...

