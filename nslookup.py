import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)




 #输出结果
"""

非权威应答:
名称:    dualstack.python.map.fastly.net
Addresses:  2a04:4e42:36::223
          151.101.108.223
Aliases:  www.python.org

Exit code: 0

"""