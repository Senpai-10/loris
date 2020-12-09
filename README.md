<p align="center"> loris </p>

<br>

<p align="center">
```
 __         ______     ______     __     ______   
/\ \       /\  __ \   /\  == \   /\ \   /\  ___\  
\ \ \____  \ \ \/\ \  \ \  __<   \ \ \  \ \___  \ 
 \ \_____\  \ \_____\  \ \_\ \_\  \ \_\  \/\_____\ 
  \/_____/   \/_____/   \/_/ /_/   \/_/   \/_____/
```
</p>

<br>

**Slowloris** works by opening multiple connections to the targeted web server and keeping them open as long as possible. It does this by continuously sending partial HTTP requests, none of which are ever completed. 
The attacked servers open more and connections open, waiting for each of the attack requests to be completed.

## Disclaimer
**This project was created purely for learning purposes**

## installation

```pip install loris ```
