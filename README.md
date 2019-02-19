example usage:

```
ansible -u giddy -i "$(python main.py)" all -m shell -a "uptime" -vv
META: ran handlers
10.10.10.14 | SUCCESS | rc=0 >>
 17:31:14 up  2:07,  1 user,  load average: 0.22, 0.19, 0.21

10.10.10.248 | SUCCESS | rc=0 >>
 17:31:14 up  1:40,  1 user,  load average: 0.37, 0.21, 0.19

10.10.10.80 | SUCCESS | rc=0 >>
 17:31:14 up  2:07,  1 user,  load average: 0.57, 0.30, 0.20

10.10.10.78 | SUCCESS | rc=0 >>
 17:31:14 up  1:38,  1 user,  load average: 0.99, 0.42, 0.23

10.10.10.51 | SUCCESS | rc=0 >>
 17:31:16 up  3:27,  1 user,  load average: 0.51, 0.51, 0.55

10.10.10.50 | SUCCESS | rc=0 >>
 17:31:36 up 407 days,  1:58,  2 users,  load average: 22.18, 22.95, 22.84
```
