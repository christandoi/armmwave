[![Build 
Status](https://travis-ci.org/anadolski/armmwave.svg?branch=master)](https://travis-ci.org/anadolski/armmwave)
[![codecov](https://codecov.io/gh/anadolski/armmwave/branch/master/graph/badge.svg)](https://codecov.io/gh/anadolski/armmwave)
# armmwave
Code that calculates transmittace and reflectance of materials at millimeter 
wavelengths.

This software was developed to aid in development of anti-reflection coatings 
for millimeter-wave optics---specifically, for optics used in Cosmic Microwave 
Background (CMB) experiments. CMB experiments have begun to adopt 
high-refractive index materials for their lenses. While there are many perks to 
this optical design, there are also a few drawbacks. One of these is reflection.  
High-refractive index materials---such as aluminum oxide and silicon, both of 
which are used in CMB experiments---reflect a significant fraction of the light 
that fall on them. To reduce that fraction we create anti-reflection coatings to 
cover the lenses.

One way to make a coating that operates over a wide range of frequencies 
(wavelengths) is to stack layers of different dielectric materials. Working out 
the transmittance and reflectance of a multilayer dielectric structure is a 
problem that can be handled using the characteristic matrix method. Enter 
`armmwave`.

Please note: This code is under active development. While it has been verified 
against experimental spectroscopic data (~25 to 500 GHz; examples will be 
uploaded soon), make sure you understand the intricacies of your specific data 
or model.

# Examples
`armmwave` provides a means to set up and evaluate models of multilayer 
dielectric media.


# Contribution guidelines
This code is under active development. If you have an idea for a feature or use 
case, please open an issue ticket. Let's talk! If you have an idea and you've 
already written the code---that's great! Create a pull request and we can go 
from there.

## Bugs
Let's face it: there are probably bugs. If you find one, please open an issue 
ticket. Include a description of the issue and, if possible, a minimal working 
example. I appreciate your patience (and your help).

