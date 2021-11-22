import struct

class Segment:
  def __init__(self) -> None:
      self.seqnumber = 0
      self.acknumber = 0
      self.checksum = 0
      self.flag = 0b00000000
      self.data = b''
      self.bytes = b''

  def load_bytes(self, bytes):
    self.bytes = bytes

  def load_segmentation(self, bytes):
      pass

  def get_flag_type(self):
    if(self.flag == 0b00000000):
      return "NONE"
    elif(self.flag == 0b00000001):
      return "FIN"
    elif(self.flag == 0b00001000):
      return "ACK"
    elif(self.flag == 0b00000010):
      return "SYN"

  def get_data(self):
    return self.data

  def generate_checksum(self):
    # generate checksum using other bytes
    # convert to 16-bit integers
    # calculate sum
    
    pass
  
  def validate_checksum(self):
    # check using checksum
    # add checksum to final sum total
    # check if there is any 0 -> corrupt
    pass

  def get_bytes(self):
    seq_bytes = struct.pack("i", self.seqnumber)
    ack_bytes = struct.pack("i", self.acknumber)
    flag_bytes = struct.pack("b", self.flag)
    empty_bytes = struct.pack("x")
    self.checksum = self.generate_checksum()
    checksum_bytes = struct.pack("H", self.checksum)
    data_bytes = self.data

    message_bytes = seq_bytes + ack_bytes + flag_bytes + empty_bytes + checksum_bytes + data_bytes
    return message_bytes

  def load_data(self, data):
    self.data = data

  def set_flag(self, flag):
    if(flag == "SYN"):
      print("Flag set to SYN")
      self.flag = 0b00000010
    elif(flag == "ACK"):
      print("Flag set to ACK")
      self.flag = 0b00001000
    elif(flag == "FIN"):
      print("Flag set to FIN")
      self.flag = 0b00000001
    else:
      print("Invalid flag input")
      print("Flag set to NONE")
      self.flag = 0b00000000

  def set_headers(self, sequence_number, ack_number):
    self.seqnumber = sequence_number
    self.acknumber = ack_number