# Directions

Within this docker container there are two directories of note: `/pof-ctf` and `/satori-master`. `/pof-ctf` containes pcap files made by two machines. Your goal is to determine what OS was running on those machines.

Run `pof-ctf.py` with python: `python3 pof-ctf.py`. It will ask several questions about the pcap files and provide the flag when complete.

These are the questions asked `pof-ctf.py`:
1. (machine1.pcap) What is ONE potential operating system running on THIS machine (check the local IP)? Answer with version numbers (example: Windows XP - 0000, Linux Mint 22.x)
2. (machine2.pcap) What is your best guess of the operating system running on this machine? Answer with version numbers (example: Windows XP - 0000, Linux Mint 22.x)

Ensure answers are formatted like the examples given.

To verify you received the correct hash, run `python3 verify-flag.py <flag>`, where `<flag>` is replaced by the CTF flag, without the `<>`.

It should be noted that the operating systems that recorded these .pcap files are not necessarily the OS and version the .pcap files suggest! Passive OS fingerprinting is not as accurate as other fingerprinting methods, and in some cases, what satori guesses the OS is is wildly off.

**HINTS**
- Check analysis on TCP and DNS packets
- You may need to check a fingerprint database by hand... try looking at the satori databases [here](https://github.com/xnih/satori).
