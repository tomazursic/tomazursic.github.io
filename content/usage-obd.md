title: Exploring OBDII
date: Mon Mar 4 11:09:02 CEST 2019
author: Tomaz
category: blog
tags: python, raspberry-pi, obd


To satisfy the curiosity for reading car on-board diagnostics using Raspberry PI with build in Bluetooth
and ODBII Bluetooth adapter.

Turn on the car engine after attaching the adapter.

## Setup:

Example target device MAC address

```text
00:19:5D:FE:9A:8F OBDII
```

### Terminal 1:

Turn on the bluetoot and scan for adapter address

```sh
$ sudo bluetoothctl
    power on
    agent on
    default-agent
    scan on
    pair 00:19:5D:FE:9A:8F
    trust 00:19:5D:FE:9A:8F
```

### Terminal 2

rfcomm associates the paired device ID with a serial device name

```sh
sudo rfcomm bind rfcomm0 00:19:5D:FE:9A:8F
```

### Read output with pyobd

http://brendan-w.com/python-obd

```python
    import obd
    connection = obd.OBD('/dev/rfcomm0')
    cmd = obd.commands.RPM
    c = connection.query(cmd).value
    print(c)
```

Example output:

![OBDII Output]({static}/images/obdII_output.jpg)

## Unpairing a Bluetooth device

Start the Bluetooth utility.

```
    bluetoothctl
```

Unpair the Bluetooth device if required.

```
    remove <dev>
```

Make sure the agent is stopped for the Bluetooth device.

```
    agent off
```

Make sure the Bluetooth device is powered down.

```
    power off

```
Exit the Bluetooth utility.

```
    quit
```

## Release serail

To remove the serial device do the following if required.

```
    rfcomm release 00:19:5D:FE:9A:8F
```

Shouldn't need this command, force rfdevices to stop.

```
    rfkill list
```

