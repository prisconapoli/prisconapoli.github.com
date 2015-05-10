---
layout: post
category : Security
tags: [mac spoofing, yosemite]
image : macspoof/logo.png
tagline: Who in the world am I? Ah, that's the great puzzle. ― Lewis Carroll, Alice in Wonderland
---
{% include JB/setup %}

###Learn how change your identity

<!--more-->

I love spending part of my free time writing for my blog and reading a book. During the weekend, I like do this in a quite place, drinking my favourite coffee and tasting tarts or cakes.

Few weeks ago I was studying in a coffee shop and everything seemed fine. The place was pretty nice and quite, the coffee amazing. Except one thing: the use of wifi connectivity was time limited. Every 25 minutes wifi connection dropped down: to continue to surf the web there were two options: compile a registration form providing all your personal details, or spoof the airport MAC address.

Spoof a MAC address is really easy in Mac OSX and in all Unix/Linux based systems. However, running the same commands several times per day can get everyone bored in short time. So I decided to write a little script for spoofing the wifi interface in OSX Yosemite and make all the process automatic and invisible to the user. The script is very easy and it is fundamentally based on the ifconfig command. 

MAC spoofing entails changing a computer's identity. Technically speaking, it is a technique for masking the MAC address of the network interface. Indeed, each network interface is uniquely identified by a factory-assigned hard-coded address called Media Access Control (MAC). This address cannot be changed. However, there are several tools for Windows or Unix based systems, which can make the operating system believe that the NIC has the MAC address of a user's choosing.


Every spoofing software use a foundamental command: **ifconfig**.
Looking in the **man** page, providing the *ether* option (an alias for lladdr), is possible to change the MAC address.


{% highlight bash %}
2L:~ prisconapoli man ifconfig
IFCONFIG(8)               BSD System Manager's Manual              IFCONFIG(8)

NAME
     ifconfig -- configure network interface parameters

[...]

     ether   Another name for the lladdr parameter.

     lladdr addr
             Set the link-level address on an interface.  This can be used to e.g. set a new
             MAC address on an ethernet interface, though the mechanism used is not ethernet-
             specific.  The address addr is specified as a series of colon-separated hex dig-
             its.  If the interface is already up when this option is used, it will be brief-
             ly brought down and then brought back up again in order to ensure that the recei-
             ve filter in the underlying ethernet hardware is properly reprogrammed.


{% endhighlight %}


It is worth to note that in OSX there are some limitations to overcome in order to make the script well working:

1. not all the combination to build a mac addresses can be used. Indeed there are some digits reserved that can have a limited range of values (e.g the first or the last bytes related, depending by the card manufacturer). The script should generate a new MAC address until it can be used.

2. every *virtual* hardware change need be detected and the wifi interface should automatically reconnect to the wifi network

3. I want the script is executed automatically at login time

4. I want the possibility to set a special MAC address to use

5. I want disable the automatic execution, if necessary


##MAC spoofing on OSX Yosemite: yospoof.sh
Below you can see the bash script I wrote to spoof the wifi network card on my Macbook Pro 
([download]({{ site.url }}/assets/images/macspoof/yospoof.sh)).

It is very easy to understand. As first thing it parses the options provided through the command line. Indeed is possible to use a custom MAC address using -m as option. In case no address is provided, the script will generate a new MAC randomly and it will try to spoof the mac. The process is repeated again up to 5 times in case the MAC address generated is not valid.

In order to perform the spoof operation correctly, is necessary previously to disconnect the interface from any network and then, after the spoof, detect hardware changes.
As last thing, the script disables and re-enables the airport interface in order to reconnect automatically to the network.

{% highlight bash %}
#!/bin/bash

#title                    :yospoof.sh
#description     :Spoof airport MAC address in Yosemite.
#author               :Prisco Napoli
#contact             :prisco.napoli@gmail.com
#date                   :20 April 2015
#version             :0.2

usage() {
cat << EOF
Usage:\n$0 [-i <wifi-interface>] [-m <mac-address>]

This script must be run with super-user privileges.

OPTIONS:
   -h      Show this message
   -i      Wifi interface name (default is en0)
   -m      MAC Address. If empty, a random address is used
   -v      Verbose
EOF
} 


function getmac(){
    # first byte need to be even number
    # just generate a randon number between 1 and 127 and double it
    n=$[ 1 + $[ RANDOM % 127 ]]
    result=$(($n*2))
    printf -v first_byte "%x:" "$result"
    local new_mac=$first_byte$(openssl rand -hex 5 | sed 's/\(..\)/\1:/g; s/.$//')
    echo $new_mac
}

if [ $# -gt 5 ]
then
    usage
    exit 1
fi

INTERFACE="en0"
MAC=
RNDMAC=1
VERBOSE=
CurrentMAC=
NewMAC=
DissociateFromNetwork="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -z"
DetectHW="networksetup -detectnewhardware"
readMac="ifconfig $INTERFACE | grep ether| cut -d ' ' -f 2"
ON="networksetup -setairportpower $INTERFACE on"
OFF="networksetup -setairportpower $INTERFACE off"
while getopts “hi:m:v” OPTION
do
    case $OPTION in
         h)
             usage
             exit 1
             ;;
         i)
             INTERFACE=$OPTARG
             ;;
         m)
             MAC=$OPTARG
             RNDMAC=0
             ;;
         v)
             VERBOSE=1
             ;;
         ?)
             usage
             exit
             ;;
    esac
done

# Dissociating from the newtork
if [[ "$VERBOSE" != "" ]]
then
    echo -e "Dissociating from the newtork"
fi
eval "$DissociateFromNetwork"

COUNTER=0
until [[ "$CurrentMAC" != "$NewMAC" ]]; do
    if [[ "$COUNTER" -ge 5 ]]; then
       echo "Counter: $COUNTER times reached; Exiting loop!"
       exit 1
    fi

    COUNTER=$((COUNTER+1))

    CurrentMAC=$(eval "$readMac")
    if [[ "$VERBOSE" != "" ]]
    then
        echo -e "Current MAC Address $CurrentMAC"
    fi
    if [[ "$RNDMAC" -eq 1 ]]
    then
        MAC=$(getmac)
        if [[ "$VERBOSE" != "" ]]
        then
            echo -e "MAC Address generated: $MAC"
        fi
    fi

    # Spoof MAC address
    if [[ "$VERBOSE" != "" ]]
    then
        echo -e "Spoofing MAC: ifconfig $INTERFACE ether $MAC"
    fi
    eval "ifconfig $INTERFACE ether $MAC"

    # Detect hardware changes
    eval "$DetectHW"
    NewMAC=$(eval "$readMac")
    if [[ "$VERBOSE" != "" ]]
    then
        echo -e "Detecting hardware changes... new MAC is $NewMAC"
    fi
done

if [[ "$COUNTER" -lt 5 ]]; then
    #Turn wifi off
    if [[ "$VERBOSE" != "" ]]
    then
        echo -e "Turning off wifi"
    fi
    eval "$OFF"

    #Turn wifi on
    if [[ "$VERBOSE" != "" ]]
    then
        echo -e "Turning on wifi"
    fi
    eval "$ON"    
fi  
{% endhighlight %}



Below the results after a script excecution (use **-v** for *verbose mode*):

{% highlight bash %}
2L:~ prisconapoli$ sudo ./yospoof.sh -v
Password:*
Current MAC Address b6:5f:22:8e:83:9e
MAC Address generated: 2e:3d:8c:17:08:75
Turn off interface en0: ifconfig en0 down
Turn on interface en0: ifconfig en0 up
Apply new MAC address: ifconfig en0 ether 2e:3d:8c:17:08:75
Done.
{% endhighlight %}


##Execute the script at login time: Automator
As last thing, you can make airspoof.sh automatically run on each login time.
Simply open Automator, select **Run AppleScript**, and past the code below:

{% highlight bash %}
do shell script "script_path" with administrator privileges user name "username" password "password" 
{% endhighlight %}

After the field customization (script_path, username and password), save the script as **yospoof.app** or any other name you like.

<div style="text-align:center" markdown="1">
![Login Items]({{ site.url }}/assets/images/macspoof/automator.jpg "Automator")
</div>

Then open **Control Panel** and add the app in **Login Items**:

<div style="text-align:center" markdown="1">
![Automator]({{ site.url }}/assets/images/macspoof/yospoof.jpg "Yospoof")
</div>



##Further Information
[MAC spoofing](http://en.wikipedia.org/wiki/MAC_spoofing), Wikipedia.org

[do shell script in AppleScript](https://developer.apple.com/library/mac/technotes/tn2065/_index.html), Technical Note TN2065: do shell script in AppleScript

