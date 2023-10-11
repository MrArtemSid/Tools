from os import stat


def open_files(files):
    while True:
        try:
            res = []
            for f in files:
                res.append(open(f[0], f[1]))
            else:
                break
        except:
            input(f"{f[0]} doesn't exist. Put it and press Enter")
    return res


def get_eeprom_address():
    while True:
        try:
            eeprom_start_region = int(input("Write HEX EEPROM address(like 0x40000): "), 16)
            break
        except:
            print("Wrong input, try again")
    return eeprom_start_region


def eeprom_dumper():
    print("\nEEPROM dumper")
    dump_filename = input("Write your dump filename(like rom.bin): ")
    eeprom_filename = "eeprom_dump.bin"
    eeprom_start_region = get_eeprom_address()
    rom, res = open_files([[dump_filename, "rb"], [eeprom_filename, "wb"]])
    while True:
        try:
            eeprom_size = int(input("Write EEPROM size in KB: ")) * 1024
            break
        except:
            input("Incorrect input")
    rom.seek(eeprom_start_region)
    res.write(rom.read(eeprom_size))
    print("EEPROM has dumped successfully and saved as eeprom_dump.bin\n")
    res.close()


def eeprom_changer():
    print("\nEEPROM changer")
    dump_filename = input("Write dump filename(like rom.bin): ")
    eeprom_filename = input("Write eeprom filename(like eeprom.bin): ")
    eeprom_start_region = get_eeprom_address()
    rom, eeprom, res = open_files([[dump_filename, "rb"], [eeprom_filename, "rb"], ["res.bin", "wb"]])

    eeprom_size = stat(eeprom_filename).st_size
    rom_size = stat(dump_filename).st_size

    res.write(rom.read(eeprom_start_region))
    res.write(eeprom.read(eeprom_size))
    rom.seek(eeprom_size)
    res.write(rom.read(rom_size - eeprom_start_region - eeprom_size))
    print("EEPROM has changed successfully and new dump saved as res.bin\n")
    res.close()


def main():
    while True:
        print("EEPROM tools\nSelect Program\n1) EEPROM dumper\n2) EEPROM changer\nPress 0 to Exit\n")
        choice = input()
        match choice:
            case '0':
                return
            case '1':
                eeprom_dumper()
            case '2':
                eeprom_changer()


main()
