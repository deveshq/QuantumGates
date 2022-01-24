#!/usr/bin/env python
# coding: utf-8

# # Implementation of the CNOT-Gate
# Their are various possible techniques to convert Rydberg blockade operation into full C-NOT gate. We are going to discuss two different standard methods _H-CZ CNOT_ and _AS CNOT_ to implement the C-NOT quantum gate.
# 
# ## H-CZ CNOT-Gate
# This technique make use of the fact that the C-NOT gate can be obtain from CZ-gate, by applying Hadamard gate before and after it. It can be easily shown using little linear algebra, which is given into Appendix-A. So before the implementation of the C-NOT gate, let's have a look how CZ-gate can be implement.
# 
# ### CZ-Gate Implementation
# Implementation of CZ involves standard three pulse sequence, shown in the figure below.
# 
# ![3pulse](images/3pulse.png)
# 
# As shown in figure, the pulse 1 & 3 are $\pi$ pulses and the pulse 2 is a $2\pi$ pulse. A $2\pi$ rotation corresponds to excitation and de-excitation of the target atom of an effective spin $1/2$. This rotation therefore imparts a $\pi$ phase shift to the wave function of the target atom.
# 
# Gate operation begins with the application of pulse 1 on control atom, which is tuned to $|1\rangle \to |r\rangle$ transition. When the control atom is initially in state $|0\rangle$, pulses 1 \& 3 are detuned and have no effect. The pulse 2 applies a $\pi$ phase shift on the target atom. When the control atom is initially in state $|1\rangle$, from pulse 1, it get excited to Rydberg level. As a result, the $|r\rangle$ level of nearby target atom shifts due to Rydberg blockade. This shifting of the $|r\rangle$ level detunes the $2\pi$ pulse and blocks the target excitation. Then the rotation does not occur and there is no phase shift of the target atom wave function. This results in a CZ controlled phase operation.
# 
# ### CNOT-Gate Implementation
# As discussed earlier, CNOT-gate can be construct using CZ gate by applying H-gate ($\pi/2$ pulse) before and after the CZ sequence. The standard five pulse sequence for the implementation of the H-CZ CNOT sequence is given below.
# 
# ![5pulse](images/5pulse.png)
# 
# The $\pi/2$ pulse shown in figure (pulse 1), puts the atom into superposition of $|0\rangle$ \& $|1\rangle$ i.e. $\frac{|0\rangle + |1\rangle}{\sqrt{2}}$. Pulses 2, 3 and 4 performs a conditional phase gate on it, as in previous section. Depending upon state of control atom, if the phase of this state shift by $\pi$, it becomes $\frac{|0\rangle - |1\rangle}{\sqrt{2}}$. Then $\pi/2$ pulse (pulse 5) transforms it to state $|1\rangle$, collectively  applying an effective C-NOT on the target atom. 
# 
# 
# ## AS C-NOT Gate
# An alternative approach to implement C-NOT gate, is to perform a controlled amplitude swap (AS-CNOT) on the target atom. Pulses 2-6 applied on target atom, swap the amplitudes of $|0\rangle$ and $|1\rangle$ state.
# 
# ![7pulse](images/5pulse.png)
# 
# As shown in figure above, when the control atom is initially in the state $|1\rangle$, pulses 1 \& 7 are detuned and doesn't effect the atom. Meanwhile, pulses 2$-$ applies a not gate on the target atom. When the control atom is initially in state $|0\rangle$, pulse 1 excites it to the Rydberg level $|r\rangle$. Then the Rydberg blockade prevents pulses 2, 4 \& 6 on the target atom from having any effect. The final pulse 7 returns the control atom to the ground state. This corresponds to a standard C-NOT operation, with some additional single qubit phase that can be corrected.
# 
# In this chapter with discussed about two pulse sequences for implementing the CNOT quantum gate. In the chapter, we'll see how to simulate them and their simulation result.
