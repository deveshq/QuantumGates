# Introduction

The field of *Quantum Information & Quantum Computing* attracting great interest nowadays, because of its promising applications and rapid practical development. Physical realization of Quantum Computing is feasible in various systems like trapped-ion, superconducting circuits, photonic qubits, etc. In which trapped ion systems are one of the most promising one. They exhibit all properties necessary for building such a system and have only a few fundamental limitations to the achievable gate fidelity.

Neutral atom qubits represent another promising approach. They share many features in common with trapped ion systems, including long-lived encoding of quantum information in atomic hyperfine states and the possibility of manipulating and measuring the qubit state using resonant laser pulses. The provision of a strong long-range interaction that can be coherently turned on and off is an enabling resource for a wide range of quantum information tasks, which takes it far beyond the original gate proposal. The availability of precise control over strong long-range interaction, makes neutral atom a promising system for multi qubit controlled gates. This project involves simulation of various pulse sequences for neutral atom C-NOT quantum gate and use them to prepare entangled pair of two qubits using Pulser, an open-source Python software package. We analyse different pulse sequences for C-NOT quantum gate, find out their fidelity and compare them. We use these pulse sequences to produce entanglement, to verify that the C-NOT gates are working properly. We further extend it to simulate 'Superdense coding algorithm' on neutral atoms, using pulse sequence we had for C-NOT gate.

In chapter 2, we discuss about single qubit quantum gates. We also briefly discuss about some multi qubit gates like controlled-Z gate and controlled-NOT gate. In next chapter, we talk about two level quantum system and discuss how to extract gates from them. In chapter 4, we introduce two different pulse sequence for implementing C-NOT gate, discuss their simulation using Pulser, present the results and compare them. In next chapter, we discuss how to produce entanglement using C-NOT gate, prepared entangled using both the C-NOT sequences, present the simulation result and compare them. In chapter 6, we introduce Superdense Coding Algorithm, as an application of entanglement. Discuss about it's simulation and present the result. In the final section, we conclude our results with some ideas for future.