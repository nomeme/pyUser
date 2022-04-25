# Python library to manage users

Easy, object-oriented API to modify system users on unix systems.

Uses the python3 API of [libuser](https://pagure.io/libuser) with the implementation [here](https://pagure.io/libuser/blob/master/f/python) and documentation [here](https://pagure.io/libuser/blob/master/f/python/modules.txt).

The `pyUser` library provides object-oriented classes for `User` and `Group`.

Take a look at the [testcases](tests/test.py) for example usage.

## Setup

### Initialize the virtual environment

Initialize the virtual environment used to run and develop the software.
In order to not mess up your system setup, I would recommend to use pythons virtual environment feature for developent.

```
python3 -m venv venv
```

Change to the virtual environment.

```
source venv/bin/activate
```

We use the virtual environment to install the necessary depenencies.

### Install libuser

In order to manage user accounts from python we need to install the `python3-libuser` package.

#### Debian/raspian

The `python3-libuser` is hidden in the Debian `sid` packages ([here](https://packages.debian.org/sid/python3-libuser)).

Add this line to `/etc/apt/sources.list``

```
deb http://raspbian.raspberrypi.org/raspbian/ testing main contrib non-free rpi
```

Write this content to `/etc/apt/preferences`.

```
Package: *
Pin: release a=stable
Pin-Priority: 700

Package: *
Pin: release a=testing
Pin-Priority: 650
```

Then run:

```
sudo apt-get update
```

#### Fix an upgrade bug by installing unresolved dependencies.

In order to install `python3-libuser` we need to update the gcc libs.
This causes further issues. The fixes are documented here.

```
sudo apt install gcc-8-base
```

Installing the `gcc-8-base` causes additional issues causing udev to fail to configure correctly.

```
systemd-journald[2396]: Assertion 'clock_gettime(map_clock_id(clock_id), &ts) == 0' failed at ../src/basic/time-util.c:55,
```

Because systemd is not aware of the system call for as demonstrated in this [reddit post](https://www.reddit.com/r/debian/comments/pk9gkk/systemdjournald_fails_to_start_at_boot_and_causes/)
The issue seems to be that the system call `clock_gettime/clock_gettime64` is not supported by the kernel, [see](https://www.mail-archive.com/openembedded-devel@lists.openembedded.org/msg68712.html).

This can be fixed commenting the line containing `SystemCallFilter = ` in following files.

```
/etc/systemd/system/sysinit.target.wants/systemd-timesyncd.service
/lib/systemd/system/sysinit.target.wants/systemd-udevd.service
```

#### Installing pyton3 user lib

After all of this we can now install python3-libuser

```
sudo apt install python3-libuser
```

