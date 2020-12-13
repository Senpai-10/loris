<h1 align="center"> loris </h1>

<br>

**Slowloris** works by opening multiple connections to the targeted web server and keeping them open as long as possible. It does this by continuously sending partial HTTP requests, none of which are ever completed. 
The attacked servers open more and connections open, waiting for each of the attack requests to be completed.

<br>

## Disclaimer
**This project was created purely for learning purposes**

## installation

1. clone            ```$ git clone  ```
2. change directory ```$ cd loris ```
3. install          ```$ python setup.py install ``` or ```$ python3 setup.py install ```

## Usage

```$ loris <IP> ```
