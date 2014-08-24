---
layout: post
category : boost
tags: [boost, program_options, C++]
---
{% include JB/setup %}

**How to add options in your C++ using the boost::program_options library.**

<!--more-->

Boost is a collection of open-source and general-purpose libraries for **C++**. They solve a wide range of problems and are massively used in software development. 
Every persone that consider himself a good C++ programmer, should know and master Boost libraries.

In this post I'll show you how is easy add options to ours programs using Boost. Sometimes parse the input provided by the users can be complicated in case the input parameters do not depend on any position or can have abbreviations. Moreover, a good software should always have **- -help** that describe its correct usage and the meaning of the options.

Let's try to write an easy program that is able to calculate the **power** or the **logarithm** of a number,  depending on the type of argument provided: 

1. power if base and exponent are present,
2. logarithm if base and number are present.

The first think to do is to include the *program_options* header and make an alias for the **boost::program_options**.

{% highlight cpp %}
#include <boost/program_options.hpp>
namespace opt=boost::program_options;
{% endhighlight %}

After this, is possible use an object of type **opt::options_description** that describes a number of options and call the method **add_options**. The syntax is preatty easy:

1. name to be used in command line
2. type of the option wrapped in value<> class
3. short description 

{% highlight cpp %}
opt::options_description desc("All options");
desc.add_options()
        ("base,b", opt::value<double>(), "Base Value"),
	    ("exp,e", opt::value<double>(), "Exponent value");
{% endhighlight %}

Is also possible define default using the method *default_value()*. In our case we can image to have 10 as default base.

At this point we need two variables to parse the command line and store the command line arguments:

{% highlight cpp %}
//variable used to store the command line arguments
opt::variables_map vm;
//parse the command line and store them in a variables_map object
opt::store(opt::parse_command_line(argc, argv, desc), vm);
{% endhighlight %}


As last thing, to check if an option is present or to get its value is enough to use the methods *counts* and *as\<T\>()*:

{% highlight cpp %}
if (vm.count("exp")) {
    std::cout << "Power: " <<
    pow(vm["base"].as<double>(), vm["exp"].as<double>()) <<
    std::endl;
}
{% endhighlight %}

At this point all the necessary has been explained. You can look at the final code below:

{% highlight cpp %}
#include <boost/program_options.hpp>
#include <iostream>
#include <math.h>

namespace opt=boost::program_options;

int main(int argc, char **argv){
    opt::options_description desc("All options");
    desc.add_options()
        ("base,b", opt::value<double>()->default_value(10), "Base Value")
        ("exp,e", opt::value<double>(), "Exponent value")
        ("num,n", opt::value<double>(), "Number")
        ("help,h", "Produces help message")
    ;
    //variable used to store the command line arguments
    opt::variables_map vm;
    //parse the command line and store them in a variables_map object
    opt::store(opt::parse_command_line(argc, argv, desc), vm);
    opt::notify(vm);
    if (vm.count("help")) {
        std::cout << desc << std::endl;
        return 1;
    }
    if (vm.count("exp")) {
        std::cout <<
        "Power: " <<
        pow(vm["base"].as<double>(), vm["exp"].as<double>()) <<
        std::endl;
    }
    if (vm.count("num")) {
        std::cout <<
        "Logarithm: " <<
        (log(vm["num"].as<double>()) / log(vm["base"].as<double>())) <<
        std::endl;
    }
} 
{% endhighlight %}


As last thing, we have to link the *libboost_program_ options library*  because **boost::program_options** is not a header-only library:

**g++ -o options_example options.cpp -lboost_program_options**


Below are reported test results. How you can see, the output is different and depends by the input provided:
 
{% highlight cpp %}
bb2l@host:BoostExamples/Program-option$ ./options_example -e 5
Power: 100000
bb2l@host:BoostExamples/Program-option$ ./options_example -e 3
Power: 1000
bb2l@host:BoostExamples/Program-option$ ./options_example -n 1000
Logarithm: 3
bb2l@host:BoostExamples/Program-option$ ./options_example -b 2 -e 16
Power: 65536
bb2l@host:BoostExamples/Program-option$ ./options_example -b 2 -n 65536
Logarithm: 16
bb2l@host:BoostExamples/Program-option$ ./options_example -b 2 -e 16 -n 65536
Power: 65536
Logarithm: 16
{% endhighlight %}

##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)

[Boost Libraries](http://www.boost.org/doc/libs/1_56_0/doc/html/program_options/tutorial.html#idp344363808)

[Advantages of using the C++ Boost Libraries](http://stackoverflow.com/questions/125580/what-are-the-advantages-of-using-the-c-boost-libraries)
