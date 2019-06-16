[![Build 
Status](https://travis-ci.org/anadolski/armmwave.svg?branch=master)](https://travis-ci.org/anadolski/armmwave)
[![codecov](https://codecov.io/gh/anadolski/armmwave/branch/master/graph/badge.svg)](https://codecov.io/gh/anadolski/armmwave)
![PyPI](https://img.shields.io/pypi/v/armmwave.svg)
![PyPI - License](https://img.shields.io/pypi/l/armmwave.svg)
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
dielectric media. To do this, create one or more `Layer`'s (with associated 
refractive index and thickness---and an optional loss term), create a `Source` 
layer and `Terminator` layer (which are required for bookkeeping), and a 
`Model`. By default, reflectance and transmittance is calculated between 500 MHz 
and 500 GHz, but you can change this if you want. Here's an example model of a 
sheet of ceramic material (in this case aluminum oxide) in a vacuum:

```python
import armmwave.layer as awl
import armmwave.model as awm

# First create a list of layers (dielectrics) in the order
# they should be evaluated
layers = [awl.Source(),
          awl.Layer(rind=3.1, thick=2e-3), # thickness in meters
          awl.Terminator()]
# Now create the model framework, feed it the layers, and run!
model = awm.Model()
model.set_up(layers)
results = model.run()
```

`model.run()` returns a dictionary with three keys: `frequency`, 
`transmittance`, and `reflectance`.

# Contribution guidelines
This code is under active development. If you have an idea for a feature or use 
case, please open an issue ticket. Let's talk! If you have an idea and you've 
already written the code---that's great! Create a pull request and we can go 
from there.

## Bugs
Let's face it: there are probably bugs. If you find one, please open an issue 
ticket. Include a description of the issue and, if possible, a minimal working 
example. I appreciate your patience (and your help).

# TODO
 * Figure out how to make TravisCI make wheels for me
 * Better docs
 * Examples
