#!/usr/bin/env python
# coding: utf-8

# # Quantum gates
# 
# ## Single Qubit Gates
# To help understand the evolution of states in a two level quantum system, the concept of the _Bloch Sphere_ was introduced. The Bloch sphere places the  |0⟩  and  |1⟩  states at the south and north poles of a unit sphere. Then a vector pointing to a point on the surface can represent all possible quantum states of the system. Single qubit quantum gates then simply represents rotations around some axis of this sphere.
# 
# ![Bloch Sphere](images/bloch.png)

# ## Pauli Gates
# We are familiar with the Pauli matrices with our background in quantum mechanics. These are a set of three $2\times2$, hermitian and unitary complex matrices. We will see how these Pauli matrices can be used to represent some common single qubit quantum gates.
# 
# ### The X-Gate
# The X-Gate is a quantum analogue of classical not gate. It switches the amplitude of $|0\rangle\text{ and } |1\rangle$ state. So it is also known as bit flip gate. We can think of it as a rotation by $\pi$ radians about x-axis on the Bloch sphere. The X-gate is represented by the Pauli-X matrix:
# 
# $$
# X = 
# \begin{bmatrix}
#     0 & 1 \\
#     1 & 0
# \end{bmatrix}
# = |0\rangle\langle1|+|1\rangle\langle0|
# $$
# 
# The symbol of X-gate is 
# 
# ![Bloch Sphere](images/x.png)
# 
# 
# ### The Y-Gate
# We can think of the Y-gate as a rotation by $\pi$ radians about y-axis on the Bloch sphere. It flips the phase as well as amplitude of the states, so it is also known as bit & phase flip gate. The Y-gate correspond to the Pauli-Y matrix:
# 
# $$
# Y = 
# \begin{bmatrix}
#     0 & -i \\
#     i & 0
# \end{bmatrix}
# = -i|0\rangle\langle1|+i|1\rangle\langle0|
# $$
# 
# The symbol of Y-gate is
# 
# ![Bloch Sphere](images/x.png)
# 
# ### The Z-Gate
# We can think of the Z-gate as a rotation by $\pi$ radians about z-axis on the Bloch sphere. Z-gate when applied introduce a phase of $\pi$, So it is also known as phase flip gate. The Z-gate is represented by the Pauli-Z matrix:
# 
# $$
# Z = 
# \begin{bmatrix}
#     1 & 0 \\
#     0 & -1
# \end{bmatrix}
# = |0\rangle\langle0|-|1\rangle\langle1|
# $$
# 
# The symbol of Z-gate is 
# 
# ![Bloch Sphere](images/z.png)
# 
# 
# ### The Hadamard Gate
# The H-Gate is the fundamental quantum gate. It maps $|0\rangle\text{ and } |1\rangle$ states to their superposition state. It has the matrix form:
# 
# $$
# H = \frac{1}{\sqrt{2}}
# \begin{bmatrix}
#     1 & 1 \\
#     1 & -1
# \end{bmatrix}
# = |0\rangle\langle0|-|1\rangle\langle1|
# $$
# 
# We can think of it as a rotation about axis between x and z axes on the Bloch sphere or as transforming the state of the qubit between the X and Z bases.
# 
# H-gate performs the following transformations:
# 
# $$ H|0\rangle = |+\rangle$$
# 
# $$H|1\rangle = |-\rangle $$
# 
# The symbol of H-gate is 
# 
# ![Bloch Sphere](images/h.png)

# ## Multi Qubit Gates
# We have seen how single qubit gates can be used to manipiulate the state of the qubit. Multi qubit gates are required to make qubits interact with each other. An important two qubit gate is CNOT-gate.
# 
# ### Controlled-NOT Gate
# This is a 2-qubit conditional gate that performs a NOT-gate on target, when the control is in the $|1\rangle$ state. We've already know that X-Gate switch the amplitude of $|0\rangle$ and $|1\rangle$. The matrix representation of the CNOT-gate, when control is $|1\rangle$, is:
# 
# $$
# H =
# \begin{bmatrix}
#     1 & 0 & 0 & 0\\
#     0 & 1 & 0 & 0\\
#     0 & 0 & 0 & 1\\
#     0 & 0 & 1 & 0\\
# \end{bmatrix}
# $$
# 
# The symbol of CNOT-gate is
# 
# ![Bloch Sphere](images/cnot.png)
# 
# ### Controlled-Z Gate
# This is also a 2-qubit conditional gate that performs a phase gate on target, when the control is in the $|1\rangle$ state. We've already know that Z-Gate performs rotation on qubit by $\pi$, around z-axis. Controlled-Z gate flips the phase of the target when the control is in $|1\rangle$ state. The matrix representation of the CZ-gate, when control is $|1\rangle$, is:
# 
# $$H =
# \begin{bmatrix}
#     1 & 0 & 0 & 0\\
#     0 & 1 & 0 & 0\\
#     0 & 0 & 1 & 0\\
#     0 & 0 & 0 & -1\\
# \end{bmatrix}
# $$
# 
# The symbol of CZ-gate is 
# 
# ![Bloch Sphere](images/cz.png)
# 
# This ends our discussion about quantum gates. In the next chapter, we will discuss about physical realisation of these gates on neutral atoms. We will see that these gates naturally occurs in the atomic systems and learn how we can extract them.
