"""
Module: 'socket' on FiPy v1.11
"""
# MCU: (sysname='FiPy', nodename='FiPy', release='1.20.2.r6', version='v1.11-c5a0a97 on 2021-10-28', machine='FiPy with ESP32', lorawan='1.0.2', sigfox='1.0.1', pybytes='1.7.1')
# Stubber: 1.3.2

from typing import IO, Any, Optional, Tuple

AF_INET = 2
AF_LORA = 160
AF_SIGFOX = 161
IPPROTO_ICMP = 1
IPPROTO_IP = 0
IPPROTO_IPV6 = 41
IPPROTO_RAW = 255
IPPROTO_TCP = 6
IPPROTO_UDP = 17
IP_ADD_MEMBERSHIP = 3
SOCK_DGRAM = 2
SOCK_RAW = 3
SOCK_STREAM = 1
SOL_LORA = 1048325
SOL_SIGFOX = 1048326
SOL_SOCKET = 4095
SO_BIT = 983047
SO_CONFIRMED = 983042
SO_DR = 983043
SO_OOB = 983046
SO_REUSEADDR = 4
SO_RX = 983044
SO_TX_REPEAT = 983045


def dnsserver(dnsIndex=None, ip_addr=None) -> Tuple[str, str]:
  '''
  When no arguments are passed this function returns the configured DNS servers Primary (Index=0) and backup (Index = 1)
  to set primary and Backup DNS servers specify the Index and Ip Address.

  Example:

  ```python
  >>> socket.dnsserver()
  ('10.0.0.1', '8.8.8.8')
  ```
  Setting DNS servers:

  ```python
  >>> socket.dnsserver(1, '0.0.0.0')
  >>> socket.dnsserver()
  ('10.0.0.1', '0.0.0.0')
  ```
  '''
  ...


class error:
  ''


def getaddrinfo(host, port, af=0, type=0, proto=0, flags=0) -> Any:
  """
  Translate the host/port argument into a sequence of 5-tuples that contain all the
  necessary arguments for creating a socket connected to that service. Arguments
  *af*, *type*, and *proto* (which have the same meaning as for the `socket()` function)
  can be used to filter which kind of addresses are returned. If a parameter is not
  specified or zero, all combinations of addresses can be returned (requiring
  filtering on the user side).

  The resulting list of 5-tuples has the following structure::

     (family, type, proto, canonname, sockaddr)

  The following example shows how to connect to a given url::

     s = socket.socket()
     # This assumes that if "type" is not specified, an address for
     # SOCK_STREAM will be returned, which may be not true
     s.connect(socket.getaddrinfo('www.micropython.org', 80)[0][-1])

  Recommended use of filtering params::

     s = socket.socket()
     # Guaranteed to return an address which can be connect'ed to for
     # stream operation.
     s.connect(socket.getaddrinfo('www.micropython.org', 80, 0, SOCK_STREAM)[0][-1])
  """
  ...


class socket:
  """
    This module provides access to the BSD socket interface.

    See corresponding CPython module for comparison.
    Socket Address Format(s)

    Functions below which expect a network address, accept it in the format of `(ipv4_address, port)`, where `ipv4_address` is a string with dot-notation numeric IPv4 address, e.g. `8.8.8.8`, and port is integer port number in the range 1-65535. Note the domain names are not accepted as `ipv4_address`, they should be resolved first using `socket.getaddrinfo()`.

    Create a new socket using the given address family, socket type and
    protocol number. Note that specifying *proto* in most cases is not
    required (and not recommended, as some MicroPython ports may omit
    ``IPPROTO_*`` constants). Instead, *type* argument will select needed
    protocol automatically::

         # Create STREAM TCP socket
         socket(AF_INET, SOCK_STREAM)
         # Create DGRAM UDP socket
         socket(AF_INET, SOCK_DGRAM)
    """

  def close(self):
    '''
    Mark the socket closed. Once that happens, all future operations on the socket object will fail. The remote end will receive no more data (after queued data is flushed).


    Sockets are automatically closed when they are garbage-collected, but it is recommended to `close()` them explicitly, or to use a with statement around them.

    '''
    ...

  def bind(self, address: Tuple[str, int] | int):
    '''
    Bind the `socket` to `address` . The socket must not already be bound. The `address` parameter must be a tuple containing the IP address and the port.

    --------
    In the case of LoRa sockets, the address parameter is simply an integer with the port number, for instance: `s.bind(1)`
    '''
    ...

  def listen(self, backlog=None):
    '''
    Enable a server to accept connections. If backlog is specified, it must be at least 0 (if it’s lower, it will be set to 0); and specifies the number of unaccepted connections that the system will allow before refusing new connections. If not specified, a default reasonable value is chosen.
    '''
    ...

  def accept(self) -> Tuple['socket', str | int]:
    '''
    Accept a connection. The socket must be bound to an address and listening for connections. The return value is a pair `(conn, address)` where `conn` is a new socket object usable to send and receive data on the connection, and `address` is the address bound to the socket on the other end of the connection.
    '''
    ...

  def connect(self, address):
    '''
    Connect to a remote socket at `address` .
    '''
    ...

  def send(self, bytes) -> int:
    '''
    Send data to the socket. The socket must be connected to a remote socket.
    '''
    ...

  def sendall(self, bytes) -> int:
    '''
    Alias of `s.send(bytes)` .

    -------
    Micropython doc:

    Send all data to the socket. The socket must be connected to a remote socket.
    Unlike `send()`, this method will try to send all of data, by sending data
    chunk by chunk consecutively.

    The behaviour of this method on non-blocking sockets is undefined. Due to this,
    on MicroPython, it's recommended to use `write()` method instead, which
    has the same "no short writes" policy for blocking sockets, and will return
    number of bytes sent on non-blocking sockets.
    '''
    ...

  def recv(self, bufsize: int) -> bytes:
    '''
    Receive data from the socket. The return value is a bytes object representing the data received. The maximum amount of data to be received at once is specified by `bufsize` .
    '''
    ...

  def sendto(self, bytes, address):
    '''
    Send data to the socket. The socket should not be connected to a remote socket, since the destination socket is specified by address.

    '''
    ...

  def recvfrom(self, bufsize: int) -> Tuple[bytes, str | int]:
    '''
    Receive data from the socket. The return value is a pair `(bytes, address)` where `bytes` is a bytes object representing the data received and `address` is the address of the socket sending the data.
    '''
    ...

  def settimeout(self, value):
    '''
    Set a timeout on blocking socket operations. The value argument can be a nonnegative floating point number expressing seconds, or `None` . If a non-zero value is given, subsequent socket operations will raise a timeout exception if the timeout period value has elapsed before the operation has completed. If zero is given, the socket is put in non-blocking mode. If None is given, the socket is put in blocking mode.
    '''
    ...

  def setblocking(self, flag: bool):
    '''
    Set blocking or non-blocking mode of the socket: if flag is false, the socket is set to non-blocking, else to blocking mode. This will override the timeout setting

    This method is a shorthand for certain `settimeout()` calls:

    ```python
    s.setblocking(True) # is equivalent to s.settimeout(None)
    s.setblocking(False) #is equivalent to s.settimeout(0.0)
    ```
    '''
    ...

  def makefile(self, mode='rb') -> IO:
    '''
    Return a file object associated with the socket. The exact returned type depends on the arguments given to makefile(). The support is limited to binary modes only ( `rb` and `wb` ). CPython’s arguments: `encoding` , `errors` , and `newline` are not supported.

    The socket must be in blocking mode; it can have a timeout, but the file object’s internal buffer may end up in a inconsistent state if a timeout occurs.

    --------
    Difference to CPython
    Closing the file object returned by `makefile()` WILL close the original socket as well.
    '''
    ...

  def read(self, size=None) -> bytes:
    '''
    Read up to size bytes from the socket. Return a bytes object. If `size` is not given, it behaves just like `socket.readall()` , see below.
    '''
    ...

  def readall(self) -> bytes:
    '''
    Read all data available from the socket until EOF. This function will not return until the socket is closed.
    '''
    ...

  def readinto(self, buf, nbytes=None) -> int:
    '''
    Read bytes into the `buf` . If `nbytes` is specified then read at most that many bytes. Otherwise, read at most `len(buf)` bytes.

    Return value: number of bytes read and stored into `buf` .
    '''
    ...

  def readline(self) -> str:
    '''
    Read a line, ending in a newline character.


    Return value: the line read.

    '''
    ...

  def write(self, buf) -> int:
    '''
    Write the buffer of bytes to the socket.


    Return value: number of bytes written.

    '''
    ...

  def do_handshake(self):
    '''
    Perform the SSL handshake on the previously “wrapped” socket with ssl.wrap_socket().
    could be used when the socket is non-blocking and the SSL handshake is not performed during connect().


    Example:

    ```python
    from network import WLAN
    import time
    import socket
    import ssl
    import uselect as select

    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid='<AP_SSID>', auth=(WLAN.WPA2, '<PASS>'))
    while not wlan.isconnected():
      time.sleep(1)
      print("Wifi .. Connecting")

    print ("Wifi Connected")

    a = socket.getaddrinfo('www.postman-echo.com', 443)[0][-1]
    s = socket.socket()
    s.setblocking(False)
    s = ssl.wrap_socket(s)
    try:
      s.connect(a)
    except OSError as e:
      if str(e) == '119': # For non-Blocking sockets 119 is EINPROGRESS
          print("In Progress")
      else:
          raise e
    poller = select.poll()
    poller.register(s, select.POLLOUT | select.POLLIN)
    while True:
      res = poller.poll(1000)
      if res:
          if res[0][1] & select.POLLOUT:
              print("Doing Handshake")
              s.do_handshake()
              print("Handshake Done")
              s.send(b"GET / HTTP/1.0\r\n\r\n")
              poller.modify(s,select.POLLIN)
              continue
          if res[0][1] & select.POLLIN:
              print(s.recv(4092))
              break
      break
    ```
    '''
    ...

  def setsockopt(self, level, optname, value) -> None:
    '''
    Set the value of the given socket option. The needed symbolic constants are defined in the socket module ( `SO_*` etc.). The value can be an integer or a bytes-like object representing a buffer. This function takes the following arguments:

    `level` : The socket type, can take the following values. Select the socket option layer for the socket you’re using:
    - `socket.SOL_SOCKET`
    - `socket.SOL_LORA`
    - `socket.SOL_SIGFOX`

    `optname` : The option name, can take the following values, depending on the chosen socket level.
    - IP socket options:
      - `socket.SO_REUSEADDR` : Enable address reusing (Enabled by default)
    - LoRa socket options:
      - `socket.SO_CONFIRMED` : Request a LoRa packet to be acknowledged by the network.
      - `socket.SO_DR` : Set the datarate, see the LoRa Socket API for more information.
    - Sigfox socket options:
      - `socket.SO_RX` : Wait for a downlink after sending the uplink packet
      - `socket.SO_TX_REPEAT` : Repeat the transmitted packet
      - `socket.SO_OOB` : Use the socket to send a Sigfox Out Of Band (OOB) message
      - `socket.SO_BIT` : Select the bit value when sending bit-only packets
    '''
    ...

  def __init__(self, af=AF_INET, type=SOCK_STREAM,
               proto=IPPROTO_TCP):
    '''
    Create a new socket using the given address family, socket type and protocol number. The initialiser takes the following arguments:
    Family type:

    - `socket.AF_INET` : For use with Internet protocols (WiFi, LTE, Ethernet)
    - `socket.AF_LORA` : For use with LoRa RAW or LoRaWAN.
    - `socket.AF_SIGFOX` : For use with Sigfox.

    Socket type:
    - `socket.SOCK_STREAM` : Creates a stream socket (INET socket only, UDP protocol only).
    - `socket.SOCK_DGRAM` : Creates a datagram socket (INET socket only, TCP protocol only).
    - `socket.SOCK_RAW` : A raw socket receives or sends the raw datagram not including link level headers (INET, LoRa and Sigfox)

    Socket protocol options:
    - `socket.IPPROTO_IP`
    - `socket.IPPROTO_ICMP`
    - `socket.IPPROTO_UDP`
    - `socket.IPPROTO_TCP`
    - `socket.IPPROTO_IPV6`
    - `socket.IP_ADD_MEMBERSHIP`
    - `socket.IPPROTO_RAW` : Only option for LoRa and Sigfox.

    By default, sockets are set to be blocking.
    '''
    ...


timeout = TimeoutError
