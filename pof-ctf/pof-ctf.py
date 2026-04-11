#!/usr/bin/env python3
import hashlib

# Keeps track of which answer is correct.
q1_correct = False
q2_correct = False

print("Welcome to the General OS Fingerprinting CTF, part of the Cyber-266 Vulnerability Walkthrough Wiki.")
print("Respond to the following questions. If both are answered correctly, the flag will be given. You will be told which is incorrect.")
print()

# Question 1. Loop until they get it right.
print("---- Analyze machine1.pcap ----")
print("What is one potential operating system running on THIS machine (check the local IP)? Answer with version numbers (example: Windows XP - 0000, Linux Mint 22.x)")
q1_answer = input()        # get user input.

# hash the answer and compare with hashes of correct answers.
m = hashlib.sha256()
m.update(q1_answer.encode('utf-8')) # encode into byte string.
if(m.hexdigest() == "e23a908b084629a23959b424511f1bc14634158d55eae27a1b9f5545f2fef3b0" or
    m.hexdigest() == "c401f91a2bb5e697182894e5a61fd3b08d4804d3e974de84e6033f263a76abcc" or
    m.hexdigest() == "5bda25fa657accc0daeba9feb86bbd477d8fd16291195e0ae2961aebd9250279" or
    m.hexdigest() == "56b74ace4b4701f19ea4a778c2062065835d9c1b6f33dba980550e7e5ea79d10"
    ):
    q1_correct = True
else:
    print("Incorrect.")
    
print()

# Question 2.
print("---- Analyze machine2.pcap ----")
print("What is your best guess of the operating system running on this machine? Answer with version numbers (example: Windows XP - 0000, Linux Mint 22.x)")

q2_answer = input()        # get user input.

# hash the answer and compare with hashes of correct answers.
d = hashlib.sha384()
d.update(q2_answer.encode('utf-8')) # encode into byte string.
if(d.hexdigest() == "ef3a312cfef03908fc63b1ab55f3b7750f74ec06eaf8ab36167c91a69209ca197af47984741a10bd8b3dacaa828c90e4" or
    d.hexdigest() == "816e4d0834b276873de4185ac1902b930eea4b7c1d1c6c93284c51c08525a9448074fa3a35959d843e8171d33b04d547"
    ):
    q2_correct = True
else:
    print("Incorrect.")

print()
if(q1_correct and q2_correct):
    print("266_ctf{os_fingerprint_007990cc124a}")
else:
    print("Try again!")

# resources:
# https://www.w3schools.com/python/python_user_input.asp
# https://www.w3schools.com/python/python_variables.asp
# https://emn178.github.io/online-tools/sha256.html
# https://docs.python.org/3/library/hashlib.html
# https://www.geeksforgeeks.org/python/what-is-the-common-header-format-of-python-files/
# https://www.geeksforgeeks.org/python/python-convert-string-to-bytes/