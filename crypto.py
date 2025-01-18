import base64
import json

def hex_to_unknown(hex_string):


    hex_bytes = bytes.fromhex(hex_string)


    unknown_string = base64.b64encode(hex_bytes).decode('utf-8')

    return unknown_string

def unknown_to_hex(unknown_string):


    hex_bytes = base64.b64decode(unknown_string)


    hex_string = hex_bytes.hex()

    return hex_string


def hex_to_ascii(hex_string):


    hex_bytes = bytes.fromhex(hex_string)


    ascii_string = hex_bytes.decode('utf-8', errors='replace')

    return ascii_string



def ascii_to_hex(ascii_string):


    ascii_bytes = ascii_string.encode('utf-8')


    hex_string = ascii_bytes.hex()

    return hex_string



hex_string = "d8ab19d5c7a0f27c10fa57540506ac688a1ab567203b3b18c418776ea447ddc8f05caf755deeae280e7de639df70c2b12c1197be47f516e8d52b3d012b80a4ecdc732bd524a6ae6b082d5dfd4c05b0d2efad862ab3e60a17fcf6c1ab1dd0e4533240e8e2a189bad65679b57dfdc007fea8667ca8deab450bf58473c53dec02ebb06adaf7bc4ab050d5300af19d78187debec52822fed00fcd6369e60d8fce594d3d7b2f19010dbfed68b52eccef8ea1eed89b34a2496e107b71432b5d63e83a98f625ed2bdbfbe116e340dd0c9e2939134b29856721046d95cd99906c7e3255cca3810924bad3394c4afa314656f4e41d2deeb69845765db2bb269b0fd10774931eba5067bc997d973898200a86fb7e7ad3df561f022a7f4cfdafcb231bd860bf00256f573a6d89f7738a0e4f2baf86ceea93dbba35d541998e630bfcfc48619919acdf2aad85c92d0864b867816d93ea052af02b612fab3cee14f4545763a47cb35a58fed417dd4f13c3a18c26c7460"

unknown_string = hex_to_unknown(hex_string)
print("Unknown string:", unknown_string)

reconstructed_hex_string = unknown_to_hex(unknown_string)
print("Reconstructed hex string:", reconstructed_hex_string)

ascii_string = hex_to_ascii(hex_string)
print("ASCII string:", ascii_string)

reconstructed_ascii_string = ascii_to_hex(ascii_string)
print("Reconstructed ASCII string:", reconstructed_ascii_string)