---
layout: post
category : Physics
tags: [quantum physics, computational universe, thermodynamics, entropy, information]
image : post_quantum_part/qm.jpg
tagline: Quantum computation is... a distinctively new way of harnessing nature. - David Deutsch
---
{% include JB/setup %}

**Is it an ultimate limitation for our knowledge or more a powerful resource?**
<!--more-->

In these series of articles [Bits inside an apple]({% post_url 2015-04-05-Bits-inside-an-apple %}), [Entropy]({% post_url 2015-04-08-Entropy %}), [Symphony of the universe]({% post_url 2015-04-11-Symphony-of-the-Universe %}), [Simulation and reality]({% post_url 2015-04-12-Simulation-and-reality %}) and [Towards Complexity]({% post_url 2015-04-15-Towards-complexity %}), I posed lots of questions of whether the universe is in fact a giant computer, and if yes, what kind of computer it is.
We have seen that the universe can be seen as a giant quantum computer. Furthermore, it was found that this quantum computational model of universe explains quite well a series of physical phenomena that are not fully explained by classical laws of physics.

With this article, in particular, I want to tell you about the relationship between energy, entropy and computation, and the impact of quantum mechanics in computing. Furthermore, I will show how it is possible to calculate in few steps the physical limit for the construction of a computer.

##Do you really think that your computer is fast?
Laws of physics says that to perform a logic operation in a Δt time, is necessary an average amount of energy ![]({{ site.url }}/assets/images/post_quantum_part/f1.png), where *h* is the Planck's constant, a very little value **6.62606957×10<sup>−34</sup> Js**.
As a result, a system with an average energy **E** can make at most of ![]({{ site.url }}/assets/images/post_quantum_part/f2.png) operations per second. It follows that the rate at which it can operate is limited by its energy.

Now, let's consider a computer of 1Kg, more or less the weight of a macbook air. 1kg of matter has **E=mc<sup>2</sup>**, it follows that the last computer may perform ~5.42558x10<sup>50</sup> operations per second (recall speed of the ligth *c* is ~**299792458 m/s**).
If you consider that a moder computer equipped with a 3Ghz processor can performs 3x10<sup>9</sup> ops per sec, you can figure out how fast the ultimate computer will be.



<div style="text-align:center" markdown="1">
![DWave Chip]({{ site.url }}/assets/images/post_quantum_part/DWave_chip.jpg "DWave Chip")
</div>

######DWave Chip(Credit: D-Wave Systems, Inc, www.dwavesys.com)


The first interesting consideration that comes out from this formula, is that this physical limit is totally independent from the computer architecture.

To deeply understand the meaning of the maximum speed for logic operation, we must recall the uncertainty principle.

The correct interpretation of Heisenberg Uncertainty Principle for the time and energy, is that a system to switch from one state to another state orthogonal and distinguishable, whose energy difference is ΔE, requires at least a time ![]({{ site.url }}/assets/images/post_quantum_part/f3.png)
. 
Quantum mechanics, therefore, provides a simple answer to the question of how fast the information can be processed using a given amount of energy.
Thermodynamics and Statistical mechanics, in fact, provide a fundamental limit on how many bits of information can be processed using a given quantity of energy confined in a finite volume. The energy available necessarily limits the rate at which a computer can process information. Similarly, the maximum entropy of a physical system determines the amount of information that can be processed. The energy limits the speed. Entropy limits memory.


The amount of information that a physical system can save and process is related to the number of its distinct physical states that are also accessible.

A collection of m bi-state elements has m<sup>2</sup> accessible states and can record m bits of information. 
It is known for over a century that the number of accessible states of a physical system, W, is related to the entropy by the formula **S=kTln(W)**, where kT is the Boltzmann constant ~1.3806488×10<sup>-23</sup> J/K.

It follows that the information that can be stored by a physical system is **I=S(E)/kTln2**, where **S(E)** is the entropy of the system with an expected value of energy **E**.

Making a comparison, we realize that modern computers operate much more slowly than the ultimate computer.
There are two reasons for this inefficiency. First, much of the energy is locked up in the mass of the particles with which the computer is constructed, leaving only an infinitesimal fraction of it to perform logical operations.
Second, our computers take several degrees of freedom, which implies billions and billions of electrons to record a single bit.
From a physical perspective, our computer operates in an incredibly redundant way. However, there are good technical reasons for this redundancy, which are reliability and maintainability. But obviously Laws of physics do not require redundancy to perform logical operations: quantum computers need only one degree of freedom and each bit work at Heisenberg limit Δt for the time required to change its state.

###Thermodynamics role in computation.

The fact that entropy and information are intimately linked is known for long time, so that Maxwell introduced his famous demon about a century ago.

Maxwell's demon is a hypothetical being who uses his skills of information processing to reduce the entropy of a gas. Indeed, the first results of physics in information processing were derived in an attempt to understand how the demon Maxwell works.

The explaination of the role of entropy in computing is due to [Landauer](http://en.wikipedia.org/wiki/Rolf_Landauer), who demonstrated that reversible operations (ie one-to-one) as NOT can be performed by principle without dissipation, while irreversible operations (ie many-to-one operations) such  AND or ERASE, require a dissipation at least of **kTln2** for each bit of information lost.

Essentially, the one-to-one dynamic of the Hamiltonian implies that when a bit is deleted, the information contained in it will end up somewhere else. If the information ends up in an observable degree of freedom, as another bit, then it is not canceled but simply moved. But if it should be in a degree of freedom which is not observable as the microscopic movement of a molecule, it follows an increase in total entropy of at least **kTln2**. This is the so called [Landauer's principle](http://en.wikipedia.org/wiki/Landauer's_principle).

In 1973, [Bennett](http://en.wikipedia.org/wiki/Charles_H._Bennett_(computer_scientist)) proved that any computation can be performed using only reversible operations. Consequently, togheter with Laundauer's principle, he established that a computation does not require necessarily a dissipation. The energy used for making a logical operation can be borrowed from a power source (ie a battery), sent to a logic gate that performs the operation, and returned back to the source after the operation has carried out, with a net profit in terms of information processed.
So, by principle, the computation requires no dissipation. But practically any computation, and therefore also our last computer, will dissipate energy.

<div style="text-align:center" markdown="1">
![Maxwell's Demon]({{ site.url }}/assets/images/post_quantum_part/maxwellsdemon-1.jpg "Maxwell's Demon")
</div>

######Illustration of Maxwell's Demon (Credit: Jason Torchinsky)

###Bonus question: are blacks holes really dark so?
In the classical vision, no information can escape from a black hole. What goes in cannot get out anymore. However, the quantum vision of a black hole is quite different: first of all, blacks holes are not completely black; they radiate at Hawking's temperature.
Recent studies in String Theory suggest that blacks holes do not destroy information, but instead they process it and can output the information processed as part of the Hawking radiation when they evaporate.
What enters is re-emitted later but in an altered form.
Does this suggest anything to you? Simply. A black hole could potentially be programmed to process information. Also, because of nothing can escape from a black hole, you can push inside it everything and everyone you don't like. Perhaps it could be definitively the computer a lots of people would like to buy.


###From energy to information

In the beginning of the twentieth century, the dominant paradigm in both science and technology was **energy**. Laws of physics developed until then, were to explain the nature of energy and how it can be transformed.

In the mid-twentieth century, however,  a revolution began. That revolution was centered around the concept of **information**, not more energy. This technology has led to new forms and applications in computing and communication.

Our current understanding of the universe is not in terms of the guiding forces of force and mass. Rather, the world we see around us comes from a dance between equal partners, information and energy, where the first takes control over the other. The bits meets the energy, and the result is the universe. The type of information of the universe is not a classical bit, but a quantum information, or qubits. Consequently, the computational model that applies to the universe in its smaller parts and fundamental level **is not a conventional digital computation but a quantum computation**.

[Alan Turing](http://en.wikipedia.org/wiki/Alan_Turing) played a key role in shifting from energy to information paradigm. Its development of a formal theory of digital computation made him one of the most influential mathematicians of the twentieth century. However, remember that **computing machines are not a modern invention**. The [abacus](http://en.wikipedia.org/wiki/Abacus) was invented in Babylon more than four thousand years ago. Other mechanisms gears based were developed in Greece and China thousands of years ago.

The first inventor of the modern digital computer was [Charles Babbage](http://en.wikipedia.org/wiki/Charles_Babbage), who had the intuition that calculations made by mathematicians could be broken down into a series of small steps, each performed by a machine. He tried too to develop a computer from a series of prototypes called [differential machines](http://en.wikipedia.org/wiki/Charles_Babbage#Difference_engine), but he failed.
Subsequently, in 1830 and 1840, [Augustus de Morgan](http://en.wikipedia.org/wiki/Augustus_De_Morgan) and the mathematician [George Boole](http://en.wikipedia.org/wiki/George_Boole) developed the bit-based logic, on which the whole classical digital computation is based.

In the late nineteenth century, the German mathematician [David Hilbert](http://en.wikipedia.org/wiki/David_Hilbert) proposed an ambitious program to axiomatize mathematics. He challenged all the mathematicians in the world with a list of [23 problems](http://en.wikipedia.org/wiki/David_Hilbert#The_23_Problems) whose solution, he thought, led to a complete theory of mathematics and a new vision of physical reality. There were several attempts, until [Kurt Gödel](http://en.wikipedia.org/wiki/Kurt_Gödel) publiced his incompleteness theorem. He demonstrated that any logical system that is powerful enough to describe the natural numbers is basically incomplete, in the sense that there will be always well formulated (ie true) propositions that cannot be proved inside the system. Basically, Gödel destroyed Hilbert's program.

The great Alan Turing's contribution to the logic, was the rejection of logic as a Platonic ideal and rethinking it as a process. He proved that the process of making Boolean logic can be implemented by an abstract machine, later called [Turing machine](http://en.wikipedia.org/wiki/Turing_machine) in his honor.

A Turing machine is nothing more than **an abstraction of a mathematician who performs calculations thinking and writing the results on a piece of paper**. Perhaps the most fascinating aspect of the formulation of a mechanistic logic Turing, was how it has treated the [self-reference](http://en.wikipedia.org/wiki/Self-reference) and incompleteness aspects raised by Godel's incompleteness theorem.

<div style="text-align:center" markdown="1">
![Turing machine]({{ site.url }}/assets/images/post_quantum_part/turingMachine.gif "Turing machine")
</div>

######Turing machine (Credit: www.felienne.com)

Godel's theorems arise from the possibilities to have a logical system with predicates (or statement) which are self-referential, nothing more that a modern formulation of the ancient paradox of the [Epimenides's Cretan liar](http://en.wikipedia.org/wiki/Epimenides_paradox), in which **a statement declare itself as false**. If it is true, then it is false; if it is false, then it is true.

As regarding the demonstration, ie prove that a statement is true or false, as a logical process, Gödel reformulated the paradox as a predicate that states "it cannot be proven as true."

There are two possibilities; if it is false, then it can be proven as true. However if a false statement can be proven as true, then the system is inconsistent (or incoerent). If it is true, then it is true that it cannot be demonstrated, and it affirms this. It follows that the system is necessarily incomplete because it is not able to demonstrate a true predicate, one of the many truth of the world.

In Turing formulation, Godel's self-referentiality predicates are translated into predicates on the behavior of the Turing machine. Turing proved that no machine is able to answer the question whether or not it will stop. This is the famous [halting problem](http://en.wikipedia.org/wiki/Halting_problem). In other words, the simplest question you can ask to a computer *Will give you to me an answer?*, cannot be calculated!


<div style="text-align:center" markdown="1">
![Ouroboros]({{ site.url }}/assets/images/post_quantum_part/ouroboros.jpg "Ouroboros")
</div>

######The Ouroboros, a dragon that continually consumes itself, is used as a symbol for self-reference (Credit: Wikipedia.org)

The so-called [Church-Turing hypothesis](http://en.wikipedia.org/wiki/Church–Turing_thesis) states that **any computable function can be computed using a universal Turing machine**. The inherently self-contradictory nature of the Turing machine and the halting problem are inherent problems of any computer. Another implications of the halting problem is that does not exist a systematic way to debug a digital computer.

Belongs to [Claude Shannon](http://en.wikipedia.org/wiki/Claude_Shannon) the result that any logic function can be realized with an electronic switching circuit (1937).

In light of all these considerations, think back our questions about the universe: **it is universe computing? and if yes, is it doing something else in addition to compute?**

Why is possible to say that our is a computing universe? Well, the answer lies in the computation definition, which Turing was the first developer. According to Turing, *a digital computer is a system that can be programmed to perform any sequence of logical operations*. We have seen in 
[Bits inside an apple]({% post_url 2015-04-05-Bits-inside-an-apple %}) that *molecules, atoms and even electrons can be programmed to perform logical operations*. But this leads to more questions:

- **The universe is able to perform a computation in the sense of Turing?** Maybe. To simulate the universe requires a Turing machine with infinite space; in cosmology, it is still an open question whether the universe is able to provide an infinite memory.

- **The universe, or a part of it, can be programmed to simulate a Turing machine Universal?**Probably not. As the necessary resources are too large to simulate a small part of space-time, we could not be able to use it efficiently.

- **A Turing machine would be able to simulate the universe?** No, because the traditional digital devices are not able to reproduce the universe cha has a quantum nature; there is a way to simulate phenomena such as superposition of states or entanglment.

The difficulty with which a classical computer can reproduce quantum effects makes it difficult to support the idea that the universe may be at the bottom of a classical computer.
However, quantum computers are known for the fact they can reproduce quantum effects. Recall that a quantum computer is a computer that uses quantum effects such as **superposition** and **entanglement of state** to perform computations in a way that *cannot be done by traditional computers*. They were proposed in 1980 by [Paul Benioff](https://www.phy.anl.gov/theory/staff/Benioff_P.html) and remained for a long time only an interesting curiosity.

**But since it seems that the universe is a huge quantum computer, what can it tell us more about the nature?**
For example, a computational universe is able to explain why it is so complex and orderly. The ordinary laws of physics do not tell much about why the universe complexity. **This complexity is quite mysterious in ordinary physics**, because of laws of physics are quite simple, ie due their shortness, they are often written on T-shirts. Furthermore, research in the field of cosmology clearly indicate that the *initial state of the universe was simple*.
The universe just after the Big Bang was simple and homogeneous. But if we look out the window, we see it is very complex now.

**A quantum computational model of the universe** not only **explains this complexity**, but also requires that it should exist. To understand why the quantum computational model necessarily lead to complexity, it is sufficient to consider the old story of the [typing monkeys](http://en.wikipedia.org/wiki/Infinite_monkey_theorem) hitting keys at random on a keyboard, but with  typewriter replaced by computers.
It can be proven mathematically that **monkeys have good chance of generating a working progam**, because of **many complex structures can be produced by small programs**.
In Nature, monkeys are replaced by energy density random fluctuations, which automatically provide the random seeds in the Universe.

###A limitation for our knowledge or a powerful resource?

What has happened to quantum mechanics in recent years is quite interesting. In the past it was seen as an absolute limit on knowledge and technology. But today quantum theory is used to expand the power of computer and knowledge of mind. The attributes of quantum mechanics such as superposition, entanglement, discretization and causality, have proven to be **not limitations, but useful resources**.

In 1965, the co-founder of Intel, [Gordon Moore](http://en.wikipedia.org/wiki/Gordon_Moore) predicted that engineers would be able to double the number of transistors on the chip about every two years. This law, known as [Moore's Law](http://en.wikipedia.org/wiki/Gordon_Moore#Moore.27s_law), gave warning signs from the beginning. If the law continues to hold, it is possible to predict when transistors will reach the size of individual atoms, **and then what?**Engineers may enter the **realm of the unknowable**.

In the traditional conception of Quantum Theory, the uncertainty principle puts a limit that no technological progress can ever overcome; more we know of some properties, such as the position of the particle, the less we know of other related properties, such as speed. And what can not be known, of course, can not be controlled.
The attempt to manipulate small objects leads to problems, ie uncertainty. The end of progress in information technology was near.

Today, however, the **physicists regularly control the quantum world**, no matter of these barriers. They can encode information in individual atoms or elementary particles, despite the uncertainty principle, creating functionality would otherwise be impossible to achieve.

*How do they do that?* At the atomic level, you can use the two states of an electron, with 0 representing the **ground state** and 1 the **excited state**. To manipulate this information, physicists send pulses of laser light to atoms.
With a pulse at the right frequency, duration and amplitude, called *π pulse*, they can bring the state from 0 to 1 and vice versa. To avoid falling into the uncertainty principle, the trick is **not to try to save information in complementary variables**. Moreover, with a **π/2v pulse**, the same frequency but half duration or amplitude, is possible to bring the bit in a quantum superposition (0 and 1).

As you can see, Quantum mechanics which has been often portrayed as the last obstacle to electronics miniaturization, is not such kind of limitation because of physicists have learned how to work with it weirdness. In fact, it **is at the quantum level that computers will reach their true potential, getting a power far greater than ordinary computers**.

Not all quantum measurements are subject to the limitation of the uncertainty principle.
In situations where the position and speed are uncertain, other properties such as energy are perfectly well defined and can be used to store a bit, ie particles orbits have defined energy.

The first practical application of a general purpose quantum computer is not the factorization of a number, but the simulation of another quantum system; a task that requires exponential time in classical computers. The quantum simulation could have a tremendous impact in fields such as drug discovery or development of new materials.
Skeptics of the practical applicability of quantum computing cite the problem of **chain together quantum logic gates**. Aside from the technical difficulties of working at the atomic scale, the main problem in this context is **avoid that environment ruins the computation**. This process, called **de-coherence**, is often presented as a fundamental limit to quantum computing. Fortunately, quantum mechanics provides the tools to correct these types of errors.


###Further Information

[Programming the Universe](http://www.amazon.com/Programming-Universe-Quantum-Computer-Scientist/dp/1400033861), by Seth Lloyd

[Ultimate physical limits to computation](http://www.nature.com/nature/journal/v406/n6799/full/4061047a0.html), by Seth Lloyd

[The Universe as Quantum Computer](http://arxiv.org/abs/1312.4455), by Seth Lloyd

[Quantum Computing](http://en.wikipedia.org/wiki/Quantum_computing), Wikipedia.org

[The Road to Reality: A Complete Guide to the Laws of the Universe](http://books.google.ie/books/about/The_Road_to_Reality.html?id=jjG_ngEACAAJ&redir_esc=y), by Roger Penrose

[Irreversibility and heat generation in the computing process](), by R. Landauer, IBM Journal of Research and Development

[Logical Reversibility of Computation](www.math.ucsd.edu/~sbuss/CourseWeb/.../Bennett_Reversibiity.pdf), by C.H. Bennet

[http://www.amazon.com/The-Fabric-Reality-Universes-Implications/dp/014027541X](http://en.wikipedia.org/wiki/The_Fabric_of_Reality), by David Deutsch