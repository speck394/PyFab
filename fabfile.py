from fabric.api import run, env, roles, task, hide, open_shell, runs_once, execute
from fabric.colors import red, cyan, yellow
from fabric.contrib.console import confirm
from getpass import getpass



#env.hosts = ['muc-a-lan-rt-02', 'muc-a-lan-rt-01']

env.roledefs['c4500x'] = ['muc-a-lan-rt-02', 'muc-a-lan-rt-01']
env.roledefs['c4500'] = ['muc-a-lan-sw-02', 'muc-a-lan-sw-03']
env.roledefs['c3000'] = ['muc-a-lab-sw-01', 'muc-a-lan-sw-01', 'muc-a-lan-sw-04']

@roles('c4500x')
def sho_power45ex():
    with hide('status', 'running', 'stdout'):
	    env = run("show power",shell=False)
    list = env.split()
    #print list
    print list[16:21]
    print list[23:28]

@roles('c4500')
def sho_power45():
    with hide('status', 'running', 'stdout'):
	    env = run("show power",shell=False)
    list = env.split()
    #print list
    print list[16:21]
    print list[29:34]    

@roles('c3000')
def sho_power3k():
    with hide('status', 'running', 'stdout'):
	    env = run("sho env power",shell=False)
    list = env.split()
    #print list
    print list[16:21]
    print list[23:28]    

#@roles('awsdns')
def get_named():
    """
        Get the named.conf file information for an AWS server
                                           """    
    with hide('status', 'running', 'stdout'):                                      
        env.output_prefix = False                               
        env.user = 'ec2-user'
        env.key_filename = '/Users/shafiek/Dropbox/Qualcomm/My Projects/AWS/New folder/pem/ITNET-key.pem' 
        result = run("sudo cat /etc/named.conf | grep 'options\|forwarders\|zone\ '")
        print "\n"
        print result
        #run("sudo cat /etc/named.conf | grep zone") 



