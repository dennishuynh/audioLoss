import sys
import random
import struct

#open input file
input = open(sys.argv[1], 'rb')
#open output file
output = open(sys.argv[2], 'wb')
#the percentage chance of failure
chance = 10
#type of loss policy, 0 = replace with 0, anything else = replace with last
policy = 1
#packet size in bytes
size = 1
#zero byte
zero = b'0'
#previous packet
previous = zero
#read and write header without modification
byte_input = input.read(24)
output.write(byte_input)
while True:
      #read in packet from input
      byte_input = input.read(size)
      #get length of packet
      leng = len(byte_input)
      #break if EOF
      if not byte_input:
         break
      #generate random number used simulate loss
      possibility = random.randrange(0,100)
      #chance of failing
      if possibility > 99-chance:
         #if zero policy
         if policy == 0:
                #loop and write 0's for size of packet
                for ii in range(leng):
                        output.write(zero)
         #if last packet policy
         else:
                #if first packet is lost, write 0's
                if previous == zero:
                        for ii in range(leng):
                                output.write(zero)
                #writes last packet
                else:
                        output.write(previous[:leng+1])
      #if no lost packet, write normally
      else:
           output.write(byte_input)
      #save packet in case of last packet policy
      previous = byte_input
#close input and output
input.close()
output.close()
