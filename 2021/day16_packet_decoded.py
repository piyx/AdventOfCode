from dataclasses import dataclass, field
from collections import deque
import operator
import math


@dataclass
class Packet:
    version: int = None
    typeid: int = None
    value: int = 0
    subpackets: list = field(default_factory=list)

    def versions(self):
        yield self.version
        for subpacket in self.subpackets:
            yield from subpacket.versions()
    
    def values(self):
        return (subpacket.evaluate() for subpacket in self.subpackets)

    def evaluate(self):
        match self.typeid:
            case 0: return sum(self.values())
            case 1: return math.prod(self.values())
            case 2: return min(self.values())
            case 3: return max(self.values())
            case 4: return self.value
            case 5: return operator.gt(*self.values())
            case 6: return operator.lt(*self.values())
            case 7: return operator.eq(*self.values())


@dataclass
class Reader:
    bits: deque
    position: int = 0
    
    def read_int(self, num_bits):
        binary = ''.join(self.bits.popleft() for _ in range(num_bits))
        self.position += num_bits
        return int(binary, 2)


def decode():
    packet = Packet()
    packet.version = reader.read_int(3)
    packet.typeid = reader.read_int(3)

    if packet.typeid == 4:
        msb = 1
        while msb:
            msb = reader.read_int(1)
            packet.value = packet.value << 4 | reader.read_int(4)
        return packet
    
    if reader.read_int(1) == 0:
        length = reader.read_int(15)
        position = reader.position
        while reader.position != position+length:
            packet.subpackets.append(decode())
        return packet

    packet.subpackets = [decode() for _ in range(reader.read_int(11))]    
    return packet


with open("inputs/day16.txt") as f:
    hex_sequence = f.read().strip()
    bin_sequence = ''.join(f'{int(hex, 16):04b}' for hex in hex_sequence)
    reader = Reader(deque(bin_sequence))


decoded_packet = decode()
print(sum(decoded_packet.versions()))
print(decoded_packet.evaluate())