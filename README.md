# TaskMon

Command line task manager. Keep track of important tasks and show completed historical tasks. 

# Usage
### Add a new task
```
> python3.11 TaskMon add "Learn Python" --priority high

Ex:

> python3.11 TaskMon add "Learn Python" --priority high
Added task: Learn Python (Priority: high)
```
### List pending tasks
```
> python3.11 TaskMon list

Ex:
> python3.11 TaskMon list
Showing pending tasks:
----------------------------------------
Title: Learn Python
Priority: high
Created: 2025-05-27 07:26:59
----------------------------------------
```
### Mark a task as completed
```
> python3.11 TaskMon complete "Learn Python"

Ex:
> python3.11 TaskMon complete "Learn Python"
Marked task 'Learn Python' as completed
```
### List completed tasks
```
> python3.11 TaskMon list --completed

Ex:
> python3.11 TaskMon list --completed

Showing completed tasks:
----------------------------------------
Title: Learn Python
Priority: high
Created: 2025-05-27 07:26:59
----------------------------------------
```
### Show help
```
> python3.11 TaskMon --help

Ex:
> python3.11 TaskMon --help
usage: TaskMon [-h] {add,list,complete} ...

Task Manager CLI

positional arguments:
  {add,list,complete}  Commands
    add                Add a new task
    list               List tasks
    complete           Mark task as completed

options:
  -h, --help           show this help message and exit
```