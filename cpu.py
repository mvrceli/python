import time

memory = {0: "10010001", 1: "00111111", 2: "10010001", 3: "00011111", 4: "10010010", 5: "00000000", 6: "00000000", 7: "00000000", 
          8: "00000000", 9: "00000000", 10: "00000000", 11: "00000000", 12: "00000000",
          13: "00000000", 14: "00000000", 15: "00000000"}

class CPU:
    def __init__(self):
        print("\n" * 10)
        self.reset()

    def reset(self):
        self.pc = 0
        self.ir = ""
        self.acc = 0
        self.timex = 1 # CHANGE THIS TO VARY CLOCK SPEED
        self.signal = ""
        self.alu = False
        pc = self.pc
        ir = self.ir
        acc = self.acc
        print("CPU RESET")
        print("MEMORY INITIALIZED")
        return pc, ir, acc

    def fetch(self):
        # global memory
        print("START FETCH")
        self.mar = self.pc
        self.time_delay()
        print("CU copies the value in the PC to MAR and onto the Address bus")
        print("PC =", self.pc)
        self.address_bus = self.mar
        self.time_delay()
        print("CU tells memory store to look at address on Adress bus and load value onto Data bus")
        self.data_bus = (self.address_bus, memory[self.address_bus])
        self.time_delay()
        self.mdr = self.data_bus
        print("CU stores the value on Data bus into MDR")
        self.time_delay()
        self.cir = self.mdr
        print("CU copies value from MDR into CIR")
        self.time_delay()
        self.pc += 1
        print("CU increments PC\nPC after increment:",self.pc,"\nFETCH END")
        self.time_delay()

    def decode(self):
        print("START DECODE")
        self.opcode = self.cir[1][:len(self.cir[1])//2]
        self.operand = self.cir[1][len(self.cir[1])//2:]
        print("Decode unit breaks value in CIR into opcode and operand")
        print(f"OPCODE: {self.opcode}, OPERAND: {self.operand}")
        self.time_delay()

        if self.opcode and self.operand == "0000":
            #END
            print("END OF CYCLE")
            quit()

        elif self.opcode == "0011":
            #STORE
            self.cb = "store"
            print("DECODE UNIT STORE")
            self.mdr = self.acc
            self.acc = 0
            print("The opcode and CU sends value from Accumulator to MDR which gets copied onto Data bus")
            self.time_delay()
            self.data_bus = self.mdr
            print("Data bus =", self.data_bus)
            self.time_delay()
            print("The Decode unit sends the operand to the MAR which gets copied into Address bus")
            self.mar = self.operand
            self.address_bus = self.mar
            print(f"data bus: {self.data_bus}, address bus: {self.address_bus}")
            self.time_delay()
            self.mdr = bin(self.mdr)
            self.mdr = self.mdr[2:]
            while len(self.mdr) != 8:
                self.mdr = "0" + self.mdr
            self.temp = int(self.operand,2)
            self.execute()

        elif self.opcode == "1001" and self.operand == "0001":
            #INPUT
            self.cb = "input"
            print("DECODE UNIT INPUT")
            if self.pc == 3: 
                self.inp1 = 4
            elif self.pc == 1:
                self.inp1 = 5
            self.time_delay()
            self.execute()

        elif self.opcode == "1001" and self.operand == "0010":
            #OUTPUT
            self.cb = "output"
            print("DECODE UNIT OUTPUT")
            print("DECODE END")
            return self.execute()
        
        elif self.opcode == "0001":
            #ADD
            self.signal = "add"
            self.alu = True
            print("DECODE UNIT ADD")
            print("DECODE END")
            return self.execute()
            
        elif self.opcode == "0010":
            #SUBTRACT
            self.signal = "subtract"
            self.alu = True
            print("DECODE UNIT SUBTRACT")
            print("DECODE END")
            return self.execute()

        elif self.opcode == "0100":
            #MULTIPLY
            self.signal = "multiply"
            self.alu = True
            print("DECODE UNIT MULTIPLY")
            print("DECODE END")
            return self.execute()
        
        elif self.opcode == "1000":
            #DIVIDE
            self.signal = "divide"
            self.alu = True
            print("DECODE UNIT DIVIDE")
            print("DECODE END")
            return self.execute()
            
    def str_to_bin(self):
        self.inp1 = bin(int(self.inp1))
        self.inp1 = self.inp1[2:]
        self.time_delay()

    def time_delay(self):
        time.sleep(self.timex)

    def execute(self):
        def input(self):
            print("START EXECUTE")
            print("Opcode and Control bus read from input and place value into Accumulator")
            self.acc += self.inp1
            print("ACC =", self.acc)
            print("EXECUTE END")
            self.run()

        def output(self):
            print("START EXECUTE")
            print("OUTPUT")
            print(self.final)
            print("EXECUTE END")
            self.run()

        def store(self):
            print("START EXECUTE")
            self.operand_temp = "0000"+self.operand
            self.operand_temp = int(self.operand_temp,2)
            self.data_bus = bin(self.data_bus)
            self.data_bus = self.data_bus[2:]
            self.data_bus = str(self.data_bus)
            while len(self.data_bus) != 8:
                self.data_bus = "0" + self.data_bus
            memory[self.operand_temp] = self.data_bus
            print(f"CU tells memory store to store value on the Data bus {self.data_bus} into the address on Address bus {self.operand_temp}")
            print("EXECUTE END")
            self.run()

        def falu(self):
            if self.signal == "add":
                print("ALU ADD")
                add1 = self.acc
                add1 = int(add1)
                self.mdr = memory[self.temp]
                add2 = self.mdr
                add2 = int(add2, 2)
                print("ADDING", add1,"+", add2)
                self.time_delay()
                self.final = add1 + add2
                print("EXECUTE END")
                self.alu = False
                self.run()
                
            elif self.signal == "subtract":
                print("ALU SUBTRACT")
                add1 = self.acc
                add2 = memory[self.temp]
                add2 = int(add2, 2)
                print("SUBTRACTING", add1,"+", add2)
                self.time_delay()
                self.final = add1 - add2
                print("EXECUTE END")
                self.alu = False
                self.run()

            elif self.signal == "multiply":
                print("ALU MULTIPLY")
                add1 = self.acc
                add2 = memory[self.temp]
                add2 = int(add2, 2)
                print("MULTIPLYING", add1,"*", add2)
                self.time_delay()
                self.final = add1 * add2
                print("EXECUTE END")
                self.alu = False
                self.run()
            
            elif self.signal == "divide":
                print("ALU DIVIDE")
                add1 = self.acc
                add2 = memory[self.temp]
                add2 = int(add2, 2)
                print("DIVIDING", add1,"/", add2)
                self.time_delay()
                self.final = add1 / add2
                print("EXECUTE END")
                self.alu = False
                self.run()
            else:
                pass

        if self.alu == True:
            falu(self)
        elif self.cb == "input":
            input(self)
        elif self.cb == "output":
            output(self)
        elif self.cb == "store":
            store(self)
        else:
            pass

    def run(self):
        self.fetch()
        self.decode()

    def test(self):
        self.run()
        
 
c = CPU()
print(c.test())
