import bluetooth
import bluetooth._bluetooth as bt
import struct
import array
import fcntl


class BluetoothRSSI(object):

    def __init__(self, addr):
        self.addr = addr
        self.hci_sock = bt.hci_open_dev()
        self.hci_fd = self.hci_sock.fileno()
        self.bt_sock = bluetooth.BluetoothSocket(bluetooth.L2CAP)
        self.bt_sock.settimeout(10)
        self.connected = False
        self.cmd_pkt = None

    def prep_cmd_pkt(self):
        reqstr = struct.pack("6sB17s", bt.str2ba(self.addr), bt.ACL_LINK, b"\0" * 17)
        request = array.array("c", reqstr)
        handle = fcntl.ioctl(self.hci_fd, bt.HCIGETCONNINFO, request, 1)
        handle = struct.unpack("8xH14x", request.tostring())[0]
        self.cmd_pkt = struct.pack("H", handle)

    def connect(self):
        self.bt_sock.connect_ex((self.addr, 1))
        self.connected = True

    def get_rssi(self):
        try:
            if not self.connected:
                self.connect()
            if self.cmd_pkt is None:
                self.prep_cmd_pkt()
            rssi = bt.hci_send_req(
                self.hci_sock,
                bt.OGF_STATUS_PARAM,
                bt.OCF_READ_RSSI,
                bt.EVT_CMD_COMPLETE,
                4,
                self.cmd_pkt,
            )
            rssi = struct.unpack("b", rssi[3].to_byte(1, "big"))[0]
            return rssi
        except IOError:
            self.connected = False
            return None
