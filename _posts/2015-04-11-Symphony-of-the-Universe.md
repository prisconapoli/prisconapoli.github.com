---
layout: post
category : Physics
tags: [quantum physics, computational Universe, Uncertainty principle, atom]
image : post_quantum_part/sym.jpg
tagline: We have to remember that what we observe is not nature herself, but nature exposed to our method of questioning - Werner Heisenberg
---
{% include JB/setup %}

**Quantum computing is like a symphony, where multiple tones overlap each other.**

<!--more-->
In the previous post [Entropy]({% post_url 2015-04-08-Entropy %}), we saw that without observing it, a particle can pass through both slits on the wall at the same time. If we make a measurement (another name for observation), the particle will pass through one slit or the other one, but not both. In other words, the measurement disturbs the particle; when asked where the particle is located, it is forced to confess his position.

In a system, no matter how small it is, having information on the position of the particle destroys the interference pattern. It is sufficient that the particle hits an electron or even a molecule of the air, and its position is irretrievably revealed.
The process by which the environment destroys the wave nature of objects through obtaining information (e.g. position) is called de-coherence.

##Quantum Bit
A good example of quantum bit is the nuclear spin; spin up is associated with *0* and spin down to *1*. The wave that corresponds to 0 is represented by the symbol **|0〉**, while the other with **|1〉**; the bracket symbol **|>** has a mathematics meaning, and serves to indicate that everything that lies inside this symbol is a quantum object (e.g. a wave). Waves can be combined: the combination is called superposition.

<div style="text-align:center" markdown="1">
![]({{ site.url }}/assets/images/post_quantum_part/qubit.jpg "Qubits")
</div>

######Qubits(Credit: AWS Official Blog, https://aws.amazon.com/blogs/aws/)


###Uncertainty principle
The *inherently unpredictable nature* of quantum mechanics has been immortalized by the [Uncertainty principle](http://en.wikipedia.org/wiki/Uncertainty_principle), also known as [Heisenberg](http://en.wikipedia.org/wiki/Werner_Heisenberg)'s uncertainty principle. This principle states that if a value of a certain physical quantity is known, then the value of a complementary quantity is uncertain. For example position **x** and momentum **p** of a particle are complementary variables.
Therefore, any measurement process that makes a certain physical quantity precise, inherently makes the value of the other complementary amount less precise. Once again, the confirmation that the measurements tend to disturb the measured system.
This principle is incredibly important, because it assert a fundamental limit to the precision with which certain pairs of physical properties of a particle known as complementary variables, can be known simultaneously.

Applying a magnetic fields is possible rotate the spin and have different overlaps. The rotation of the spin preserves the information. AND, OR, NOT and COPY constitute a universal set of classical logic operations. Any physical transformation can be constructed from these basic elements.

The state **\|0〉+\|1〉** is equivalent to the quantic state of the particles in the double-slit experiment. Historically, the process of measuring in a quantum experiment is considered irreversible.

The [Copenhagen interpretation](http://en.wikipedia.org/wiki/Copenhagen_interpretation) assumes that once a macroscopic apparatus has become correlated with a microscopic system such as a particle, **the correlation is irreversible**. In these irreversibility of the measurement, the reader may review an echo of the second law of thermodynamics.

Quantum mechanics, unlike classical mechanics, *can create information from nothing*. In an entangled state, we can know the overall state of a quantum system as a whole, but we are not able to give information about its individual components. Entanglement is responsible for what Einstein called a *spooky action at a distance*.

Consider **\|01〉-\|10〉**, in which the qubits have opposite value. Measure the first spin has an impact on the second spin. The first particle may be far away from the second and be affected from the first one.

###Atoms at work
Einstein was confused about quantum mechanics. As is well known in history, he never completely believed the theory, arguing its probabilistic nature. In fact, quantum mechanics went against his intuition, and he, like all of us, had the right to not trust. Einstein's insight led him astray, because quantum mechanics is inherently probabilistic.

An atom consists of a nucleus (protons + neutrons) around which electrons orbit. When an atom is in its normal state, called **ground state**, the electrons are accumulated around the nucleus as much as possible. The core itself is kept together by the **strong nuclear force**. Quantum mechanics explains atom's stability. Indeed, the classical physics, incorrectly predicted the collapse of electrons on the nucleus and the annihilation of the atom in an emission of light.

<div style="text-align:center" markdown="1">
![]({{ site.url }}/assets/images/post_quantum_part/atom.jpg "Atom")
</div>

######Atomic Structure (Credit: http://www.sophia.org)

**How quantum mechanics explain atom stability?** Recall that every electron has a wave associated with his position and velocity. Where the wave has a peak, there is more likely to find the electron. The smaller the wavelength, the faster the electron moves. The rate at which it moves up and down is proportional to its entropy.

The easiest way to imagine a wave function around a nucleus, is to think of a sphere, called ground state. Then a second sphere with a peak, then a third sphere with two peaks etc. etc. More energy has the electron, farther from the nucleus it rotates (as a stone tied to a rubber band that rotates around your head).
The wave-particle duality dictates that the electrons of an atom consist in a set of discrete waves, so there is are a limited number of orbits that can be covered. They never fall into a nucleus, and we can count the possible options (one peak, two peaks, etc. etc.).

When an electron moves from a high energy orbit to a low energy orbit, it emits a photon whose energy is equal to the energy difference of the two orbits.
The so-called *spectrum* of the atom is nothing but the frequencies of light photons emitted by the atom.
That atoms emit light with a characteristic frequency, or spectrum, was discovered in the first half of the nineteenth century. But no one could explain why. But atoms can also absorb photons, as they pass from an orbit at low energy (ground state) to an orbit at high energy (excited state). Atoms can only absorb energy in a given quantity (how many). In particular, it is possible to subject the atoms to a pulse of laser light, and cause them to pass from the base state **\|0〉** at the excited state **\|1〉**.

Fluorescence is a phenomenon in which an atom emits photons spontanemanete. This is useful to see if the atom is in the ground state or not. When an atom goes from ground state to exited state, is located in a superposition of states.

As you can talk to an atom? Simply by hitting it with a laser, to make sure that they change their status. The talk with the light (laser) and you respond with light (photons). And activating cyclic transaction, and can make the atom constantly communicates its status.

How to build a quantum computer?
Hitting an atom with a pulse of light, and can take from state **\|0〉** to state **\|1〉** and vice versa. We are changing the status of bit, e.g. a NOT operation. But with the right laser pulses, you can have AND, OR and COPY operations. But atoms recording more than one bit; they register qubit. And unlike the classical mechanics, the qubit can be in a quantum superposition **\|0〉** and **\|1〉**; which means, in few terms, that are capable of recording 0 and 1 at the same time.

Does exist a way so that the state **superposition can be used to perform a computation that a conventional computer is not able to do**? The answer is **yes**.

To understand, we must think of a traditional bit. It can be an instruction (or command) or a data in memory. But a qubit can record 0 and 1 at the same time. It follows that when a quantum computer interprets a qubit as a command, it must be in superposition of states (0 and 1, do *this* and *that*). In practice, it does two computations **simultaneously**.

This is called [quantum parallelism](http://physics.about.com/od/physicsqtot/g/quantumparallel.htm), and is quite different from the classic parallelism. In a quantum computer, which has **embedded** quantum parallelism, several tasks are performed at one time.

A classical computation is like as a single voice, a line of pure tones that follow one after the other; quantum computing is like a symphony, where multiple tones overlap each other. The quantum parallelism allows you to have a relatively low number of quantum computers, which contain only few hundred qubits, and **explore a vastness of possibilities simultaneously**.

In a quantum computation, if you want to see fully the benefits and effects of computation, we must not look to computation while it is happening.
To exploit the quantum parallelism, it is necessary to wait until all the waves go in superposition. Observe the system makes it behave classically and quantum.

###Factorization
A quantum computer can explore **all possible solutions to a difficult problem at the same time**. For example, using a traditional computer is not thinkable to address the problem of [factorization](http://en.wikipedia.org/wiki/Factorization). The apparent difficulty of factoring large numbers is the basis of a powerful method to protect information, the [Public-key cryptography](http://en.wikipedia.org/wiki/Public-key_cryptography).

<div style="text-align:center" markdown="1">
![]({{ site.url }}/assets/images/post_quantum_part/math.gif "Factorization")
</div>

######Prime Factorization (Credit: http://www.coolmath.com)

A quantum computer would be able to factorize large integers in polynomial time, thus making obsolete the traditional cryptographic techniques. To get the full benefit of quantum computing, we must not disturb your computer while you are working, it is necessary to leave the waves interfere. In order to exploit the natural symphony of quantum parallelism, you must allow that the different parts of the system can interfere in a quantum.

###Further Information

[Programming the Universe](http://www.amazon.com/Programming-Universe-Quantum-Computer-Scientist/dp/1400033861), by Seth Lloyd

[Ultimate physical limits to computation](http://www.nature.com/nature/journal/v406/n6799/full/4061047a0.html), by Seth Lloyd

[The Universe as Quantum Computer](http://arxiv.org/abs/1312.4455), by Seth Lloyd

[Quantum Computing](http://en.wikipedia.org/wiki/Quantum_computing), Wikipedia.org

[The Road to Reality: A Complete Guide to the Laws of the Universe](http://books.google.ie/books/about/The_Road_to_Reality.html?id=jjG_ngEACAAJ&redir_esc=y), by Roger Penrose

[Dance of the Photons: From Einstein to Quantum Teleportation](http://books.google.ie/books/about/Dance_of_the_Photons.html?id=HhGfPAAACAAJ&redir_esc=y)

[Quantum Parallelism](http://physics.about.com/od/physicsqtot/g/quantumparallel.htm)



