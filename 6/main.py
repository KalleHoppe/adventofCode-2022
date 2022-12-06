

def Part1(signal, markLength):
   pos = 0
   packet = []
   while pos < len(signal):
      packet.append(signal[pos])
      if len(set(packet)) == markLength:
         print(f"The first packet is {packet}")
         print(f"Chars processed first marker {pos+1}")
         break
      if len(packet) == markLength:
         packet.pop(0)
      pos +=1

if __name__ == "__main__":
   f = open('/workspaces/adventofCode-2022/6/input.txt')
   signal = f.read()
   Part1(signal, 4)
   Part1(signal, 14)