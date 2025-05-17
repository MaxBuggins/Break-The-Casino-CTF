#!/bin/bash

intro_lure() {
    echo " "
    echo "Welcome to the Shadow Bet Casino Challenge!"
    echo "Your goal is to uncover the location of the secret underground casino."
    echo " "
    echo "But beware — not everything is as it seems."
    echo "Layers of deception await..."
    echo " "
    sleep 3
    echo "Scanning illegal slot machine networks..."
    sleep 3
    echo " "
}

part1="LTM0Ljg0"
part2="MzQyNjVf"
part3="MTM4LjYz"
part4="Mjg1OT"
part5="Noenvlst345"
part6="Msdfernv23"
payload="${part1}${part2}${part3}${part4}$(printf '\u0041\u003D')"

# Red herring functions
fdecrypter() {
    echo "01001010 11001100 00110011 10101010"uioj
}

cipher_mystery() {
    echo "Encrypted string detected. Attempting bitflip XOR on shellcode..."
    sleep 2
    echo "Failure. Unrecognised format."
}

# Actual decoding but hidden behind irrelevant names
process_signal() {
    echo "$payload" | base64 --decode
}

super_secret() {
    local loc
    loc=$(process_signal)
    echo "Balance[\$$loc]"
}

if [ "$1" == "--cheat" ]; then
    echo "😏 Trying to cheat? Not today, high roller."
    fake_decrypt
    exit 0
fi

if [ "$1" == "--flag" ]; then
    echo "🧨 Flag retrieval failed."
    echo "Corrupted buffer or invalid segment header."
    exit 0
fi

if [ "$1" == "--trace" ]; then
    echo "📡 Signal locked. Transmitting raw hex stream:"
    cipher_mystery
    exit 0
fi

# Unreachable real flag dropper (players will find this in source)
if [ "$RANDOM" -eq 99999 ]; then
    echo "🚨 Flag: $(super_secret)"
    exit 0
fi

sleep 1
intro_lure 
read -p "Press Enter to begin decoding encrypted casino beacon... " dummy
echo " "
echo "Received burst from relay node:"
sleep 2
echo " "
echo "🎲 Is this really all there is? Or just the beginning..."
echo " "
echo "Explore. Investigate. And trust no function name."
echo " "

