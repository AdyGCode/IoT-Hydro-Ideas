# IoT Hydo Ideas

TODO: Describe what this project is for

## Contributors


## ...


## Setting Up


### update pip
python.exe -m pip install --upgrade pip

### Install Node Packages
npm install

### Install Python Packages

pip install -r requirements.txt

### Run tailwind/preline watcher

set PATH=%PATH%;c:\laragon\bin\nodejs\node-v18

npx tailwindcss -i ./src/main.css -o ./static/css/public.css --watch  


### Run Flask App



## Standards

### Message Structure

Messages will be in JSON format with a defined structure. Structure will be influenced by the type of command.

Message structure will be:

```json
{
  "command": "<COMMAND>",
  "timestamp": "<DATE_TIME>",
  "data": {
    
  }
}
```

#### Commands:

| Command       | Purpose                                             |
|---------------|-----------------------------------------------------|
| **reading**   | Readings from a sensor node                         |
| **action**    | Command for an actuator node                        |
| **health**    | Health commands ands requests data for a node       |
| **heartbeat** | Heartbeat to notify controller of the system status | 
| **error**     | Warning or similar to go to all nodes               |

#### Data packet

The data packet will contain different information depending on the command.

##### Reading

```json
{
  "command": "reading",
  "timestamp": "<STRING_DATE_TIME>",
  "data": {
    "name": "<STRING_SENSOR_NAME>",
    "reading": "<DECIMAL|STRING_VALUE>",
    "scale": "<STRING|NULL_MEASUREMENT_SCALE>"
  }
}
```

Example:

```json
{
  "command": "reading",
  "timestamp": "2023-05-22T23:21:19Z",
  "data": {
    "name": "temperature-01",
    "reading": 22.5,
    "scale":  "C"
  }
}
```

##### Action

```json
{
  "command": "action",
  "timestamp": "<STRING_ISO_DATE_TIME>",
  "data": {
    "name": "<STRING_ACTUATOR_NAME>",
    "action": "<STRING_COMMAND_TO_PERFORM>",
    "max-time": "<INTEGER_SECONDS>"
  }
}
```
Example could be:

```json
{
  "command": "action",
  "timestamp": "2023-05-22T23:21:19Z",
  "data": {
    "name": "extraction-fan-01",
    "action": "on-50",
    "max-time":  900
  }
}
```

This will turn extraction fan 01 on at 50% of max speed for 900 
seconds (15 minutes).



##### Health & Heartbeat

Two parts to status of the device:
- Health
- Heartbeat

###### Health

Health informs the nominated node of how often it must call back to 
"home" and let the controller know it is online. This is the "set" 
action part of the health command.

There is also a "get" command that has the node respond as soon as 
possible that the controller it is online. The node will use the 
"heartbeat" command to respond in this situation and also for regular 
heartbeat updates.


Set

```json
{
  "command": "health",
  "timestamp": "<STRING_ISO_DATE_TIME>",
  "data": {
    "action": "set",
    "name": "<STRING_ACTUATOR_NAME>",
    "period": "<INTEGER_HEARTBEAT_SECONDS>"
  }
}
```
Example could be:

```json
{
  "command": "health",
  "timestamp": "2023-05-22T23:21:19Z",
  "data": {
    "action": "set",
    "name": "extraction-fan-01",
    "period": 600
  }
}
```

Get

```json
{
  "command": "health",
  "timestamp": "<STRING_ISO_DATE_TIME>",
  "data": {
    "action": "get",
    "name": "<STRING_ACTUATOR_NAME>",
  }
}
```
Example could be:

```json
{
  "command": "health",
  "timestamp": "2023-05-22T23:21:19Z",
  "data": {
    "action": "get",
    "name": "extraction-fan-01",
  }
}
```




###### Heartbeat

The heartbeat is a regular call from the device to the central controller to let the controller know it is online and active.

The period between heartbeats may be altered by the HEALTH command, with a default of once every 10 minutes used
until altered.

Heartbeat will also respond when the central controller requests health. 

```json
{
  "command": "health",
  "timestamp": "<STRING_ISO_DATE_TIME>",
  "data": {
    "name": "<STRING_ACTUATOR_NAME>",
    "status": "ok"
  }
}
```
Example could be:

```json
{
  "command": "health",
  "timestamp": "2023-05-22T23:21:19Z",
  "data": {
    "name": "extraction-fan-01",
    "status": "ok"
  }
}
```




