# General OS Fingerprint

## How to run this CTF

Download the `pof-gof-ctf.tar` file. Ensure that Docker is running.

Import the image by running:
```bash
docker load < pof-gof-ctf.tar
```

This will load the docker image.

Run the image with:
```bash
docker run -it --name pof-gof-ctf 266pof/pof-gof-ctf
```

This will create a docker container named `pof-gof-ctf` and open it as an interactive terminal.

To exit the terminal type exit. This will also stop the docker container.

To start the container (AFTER you have created it with `docker run`) in an interactive terminal, run `docker container start -i pof-gof-ctf`. If you ever accidently run or start the container without `-it` (for `docker run`) or `-i` (for `docker container`), the container will start without the terminal. Simply stop it with `docker container stop pof-gof-ctf`, and then start it with the `docker container start` command above.

The following directions are within the docker image at the `/pof-ctf` directory:

## Directions

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

## How was this Docker Container Made?

Fun little FYI for anyone interested:

The `Dockerfile` contains directions for creating a docker image. It creates a base `Ubuntu 24.04` image, imports a bunch of packages, and then copies over directories from this repository. The image can be built with `docker build -t 266pof/pof-gof-ctf .`, which builds the image and tags it "`266pof/pof-gof-ctf`".

The Dockerfile can then be exported using `docker save 266pof/pof-gof-ctf:latest > pof-gof-ctf.tar`, which creates the tar file that can be used to import the image, as used above.

## Sources/Resources:
- https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/
- https://stackoverflow.com/questions/22907231/how-can-i-copy-files-from-a-host-to-a-docker-container
- https://www.howtogeek.com/devops/how-to-share-docker-images-with-others/
- https://docs.docker.com/reference/dockerfile#run
- https://docs.docker.com/get-started/docker-concepts/building-images/build-tag-and-publish-an-image/
- https://docs.docker.com/build/building/base-images/
- https://dev.to/chaymaekhl/create-a-container-using-the-ubuntu-image-in-docker-1aa
- https://docs.docker.com/reference/cli/docker/container/start/

The source code for [satori](https://github.com/xnih/satori) is included within the repository and the docker image; it is built within the docker container for the CTF. I do not claim any ownership for satori and include it here according to the GNU GPL 2 License, which satori is under. The license is included in the satori source code under the `satori` directory. The source code is verbatim as downloaded and extracted from the [satori repository](https://github.com/xnih/satori) on 2026-04-10.