---
layout: post
category : Development
tags: [defensive programmig, c, c++]
image : defensive_programming/cover.png
tagline: Design and write software easy to understand and use. A misuse should be always hard and not the obvious way.
---
{% include JB/setup %}

**Design and develop software components with security in mind**

<!--more-->

Today security is a major issues for Banks, Financial Institutions and Governments. 
Financial transactions and money transfers are made trough Internet. There is real money on the line and there are many peolpe trying to get their hands on it. 
In addition, crack the Government machines is a one of new form of attacks made by terrorist and criminals organizations.
<!--summary-->

An enormous quantity of software and operating systems are based on C/C++ languages and Unix API.
The main focus of the C/C++ and Unix APIs was efficiency in performance and memory-usage. As a consequence, today development require some more effort to write code which can be securely deploy. 

This post covers several aspects of the C/C++ languages and Unix APIs that need attention and provide and overview of the good practices that should to be handled to ensure security.


#Safe programming
The main problem in C programming language is the memory handling. Indeed, in the language itself there is no support for memory allocation and, as a consequence, allocation is always a weak point and very frequently the start point for malicious exploits.

The C Standard Library contains the malloc() family of functions for allocating mamory;  however, there are many possibilities for incorrect use that require good programming skills.

With C++ language, these issues are less frequent thanks to the new operator and the standardization of higher-level data structure which helps to reduce the direct use of the malloc() functions.

###Memory Handling


####Be careful about memory bounds
Every time that is required write in a memory block, the program must be aware of the block size and check whether boundaries are violated or not. 
The same considerations can be made in case of a function that receive a reference to an array of objects. The size of the array should always be passed to the function togheter with a reference to the array. 

{% highlight cpp %}
char* gets(char* s);
char* getwd(char* buf);
{% endhighlight %}

As example, consider these two functions:
The **gets()** function reads input from standard input and stores it into the buffer pointed to by s.
However, it's easy to see that the input can in theory be arbitrarily long and could lead to a buffer overflow.

**getwd()** function has a similar problem. It copies the absolute pathname of the current working directory into the memory referenced by buf and returns a pointer to buf. However is not rarely that the maximum path name length is not known and it can overflow the buffer.

Both these functions cannot prevent a buffer overflow, and their use should be always discouraged. Instead of these two functions programmers should always use **fgets()** and **getcwd()**. Both have almost the same interface but the length of the buffer is passed to the function as well.


{% highlight cpp %}
char * fgets(char *restrict s, int n, FILE *restrict stream);
char * getcwd(char *buf, size_t size);
{% endhighlight %}


####Allows implicit memory allocation
In order to avoid buffer overflow, one possibility is design functions so that necessary buffers are allocated in the interfaces themselves. As examples we can look at **printf()** functions family:

{% highlight cpp %}
int asprintf(char **ret, const char *format, ...);

int fprintf(FILE *restrict stream, const char *restrict format, ...);

int printf(const char *restrict format, ...);

int snprintf(char *restrict s, size_t n, const char *restrict format, ...);

int sprintf(char *restrict s, const char *restrict format, ...);
{% endhighlight %}

**printf() and sprintf()** do not prevent buffer overflow.
**snprintf()** takes as parameter the size of the buffer, so it solve the overflow issues. However, the output is truncated in case of the string is greater than the buffer.
In order to overcome these issue **asprintf()** has been introduced. These interfaces work just like the rest of the **sprintf()** functions but the buffer is allocated by the function and therefore is never too small. The caller has the responsibility to free the buffer after it is not needed anymore. Even though the memory allocation has to be performed at each call, the use of **asprintf()** interface might in fact be faster since it is not necessary to perform computations to determine the buffer size in advance.

###Filesystem


####Never trust file names
A golden rule to follow in the development of a robust program, is try to identify files before they are used. Identification is, for instance, possible by comparing file ownership, creation time, or even location of the data on the storage media.

This information is available through the stat() system calls.

{% highlight cpp %}
stat(filename, &st);
if (S_ISREG(st.st_mode)
  && st.st_ino == ino
  && st.st_dev == dev) {
    fd = open(filename, O_RDWR);
    // Use the file
    ...
    close(fd);
}
{% endhighlight %}

Despite the firs implementation looks correct, it hides a trap. Indeed, it could be happen that the filename changes between the calls to **open()** and **stats()**. To avoid this, is possible to use the extended version **fstats()**, which takes as input a file descriptor:

{% highlight cpp %}
fd = open(filename, O_RDWR);
if (fd != -1 && fstat (fd, &st) != -1
	&& st.st_ino == ino
	&& st.st_dev == dev) {
	// Use the file
	...
	close(fd);
}
{% endhighlight %}

####Checksum binary
In a robust system, everytime that is necessary execute a binary, the system should checks the bynary's **MD5 checksum** and,  if it right (e.g. matches with an entry in a Checksum DB), runs the binary.  However, if the checksumming and the execution are performed independently, there would be no guarantee that the checksummed binary is the same as the binary which gets executed. **fexecve()** helps us to avoid to expose the system to an attack. **fexecve()** performs the same task as **execve()**, with the difference that the file to be executed is specified via a file descriptor, fd, rather than via a pathname. So the code which performs the checksumming opens a file descriptor for the binary, then gets the binary content to compute the checksum. If the checksum matches, the file descriptor is not closed. Instead it is used in the **fexecve()** call to start the execution.


###Good practices in software development and compilation

####Code Documentation, Pre and Post Conditions

As software engineers or software developers, we are responsible for ensuring that the software we design and write is easy to understand and use. A misuse should be always hard and not the obvious way.

Personally I always try to do my best for writing code which is efficient and elegant in the same time. It's my opinion that the best code is auto-explicative and easy to read.

Often is necessary document methods, classes or particular sets of instructions that perform sophisticated mathematical operations.

Personally I avoid to overload my code with too much documentation, but I concentrate myself to document only the parts that could lead to a misuse. I also prefer a simple graph to explains design choice instead of heavy document that could bring yourself so far from the core design. Moreover, I really encourage the use of agile methodologies, code review and pair programming. 
Is my conviction that everything that lead to sharing knowledge should be alway encouraged in each IT company.

The first advice is always use **code conventions** during the development of a piece of code. For instance, there are a lot of information in Internet about C++, Java  or Python's code style. Follow code conventions is the first way to communicate what code is intend to do. 

But all this is not enough. As example, **in Object Oriented Software Development**, an essential part of design by contract are represented by **preconditions, postcondition and class invariant**.

Is very common to see a function's documentation which explains in details what these stuff are.
 
In a general way, we can define a **precondition** as *a constraint which is necessary for a successful execution of generic piece of code*.
From the program developer's viewpoint, in the most cases this constitutes the caller's portion of a function. The caller then is obligated to ensure that the precondition holds prior to calling the function. The reward for the caller's effort is expressed in the called routines **postcondition*, a constraint which is true just after the execution of the function. An **invariant** is a  special condition that is always satisfied *before, during and after the execution of the code*.

####Compilation
Compilers can really help you to detect code defects and make your life easy. The GNU C compiler has a lot of capabilities such as static code analysis, function annotations, and an innumerable quantity of warnings that help you to write high quality code.

The most important advice for using the compiler is to enable all generally accepted warnings and eliminate them. Moreover, compilation would be always interrupted when a warning is printed.
Is sufficient to add the following line in gcc to obtain this:

{% highlight cpp %}
-Wall -Wextra -Werror
{% endhighlight %}

You can also add annotations to functions in order to print warning in gcc when they are used; for instance, in case you would advice the user that a function is now deprecated or that the  return value is unused.

{% highlight cpp %}
extern int funcA(int)
	__attribute((__deprecated__));

extern int funcB(int)
	__attribute((__warn_unused_result__));
{% endhighlight %}


##Further Information

[C++11](http://en.wikipedia.org/wiki/C%2B%2B11)

[Defensive Programming for Red Hat Enterprise Linux](http://www.akkadia.org/drepper/defprogramming.pdf), by Ulrich Drepper. Red Hat, Inc.

[Defensive Programming Done Right](https://www.youtube.com/watch?v=1QhtXRMp3Hg) by  John Lakos, CppCon 2014


