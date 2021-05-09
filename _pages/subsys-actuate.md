---
title: "Actuation"
permalink: /subsys-actuate/
layout: posts
sidebar:
  nav: "docs"
---

In order to make our fish move, we need to find a way to physically actuate it and have it controllable by some sort of "brain." This page documents the various methods we tested to actuate our fish, and documents the results from creating each of these systems.

# Switching Pump - Iteration 1
SoFi, the robotic fish we are basing our project off, got good results from using a custom gear pump. However, they note that this method of actuation requires a lot of power to operate and is rather energy inefficient since it requires regularly switching the motor direction back and forth. [NEED CITATION] Since we only had access to consumer-grade 3D printers, we weren't confident in our print tolerances being sufficient to create a gear pump like in their design. In another one of their papers on SoFi, they discuss the potential for creating a pump design that could quickly switch the inlet and outlet flows by only using continuously rotating parts.[NEED CITATION]

The first thing we attempted to do was to re-create this setup, but customize the parts to fit the geometry of our half-scale fish body. We ultimately purchased this submersible 12V pump, since its flow rate and pressure (estimated from its rated max lift) seemed sufficient for our needs. ([Amazon link](https://www.amazon.com/gp/product/B07HQLVCRX/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1))
<center>
  <img src="/img/pump.png" width="40%" height="40%">
  <br/>
  <div class="caption">
    12V, 7W pump we purchased for actuation testing
  </div>
</center>

We then created a valve based on the design for a two-way valve attachment to a centrifugal pump as proposed in [NEED CITATION]. For this initial test, the valve was designed to be manually driven by a screwdriver or something similar, so we left a square hole where it would normally mount to a servo.

<center>
  <img src="/img/pumpv1-valve-front.png" width="30%">
  <img src="/img/pumpv1-valve-back.png" width="30%">
  <br/>
  <div class="caption">
    Front (left) and back (right) of the switching valve
  </div>
</center>

To route water from the pump through the valve, we created a housing for the assembly.

<center>
  <img src="/img/pumpv1.png" width="40%">
  <img src="/img/pumpv1-front.png" width="30%">
  <br/>
  <div class="caption">
    Side (left) and front (right) view of iteration 1 on the two-way centrifugal pump assembly
  </div>
</center>

<center>
  <img src="/img/pumpv1-cover_off.png" width="40%">
  <br/>
  <div class="caption">
    Iteration 1 of the two-way centrifugal pump assembly with the front cover removed
  </div>
</center>

### Testing & Results

We 3D printed these parts and tested the assembly in a large bucket of water. It's a bit difficult to tell in the video feed, but if you look closely at the bumps created by the water flow to the left and right of the screwdriver, you can see that the water flow does indeed switch.

<center>
  <img src="/img/valve-v1-switch.gif" width="40%">
  <br/>
  <div class="caption">
    Testing assembly in a bucket of water - the flow switches
  </div>
</center>

It's worth noting that the valve took quite some force to turn, and I don't think most servos would be able to use this assembly as-is. This assembly was also too wide to properly fit into the fish body, so that also needed to be improved.

# Switching Pump - Iteration 2
To improve upon the first iteration of the switching pump design, the geometry of the parts in this iteration were optimized to fit into the space we had allotted to it onboard the fish. We also made the tolerances more generous in this design to ensure that the switching valve could be rotated with a small 9g servo.

<center>
  <img src="/img/pumpv2.png" width="40%">
  <img src="/img/pumpv2-cover_off.png" width="40%">
  <br/>
  <div class="caption">
    View of the full assembly for iteration 2 (left) and the assembly with the front cover off (right)
  </div>
</center>

<center>
  <img src="/img/pumpv2-in_assem.png" width="90%">
  <br/>
  <div class="caption">
    View of the assembly in context of the fish design
  </div>
</center>

Since we now needed to drive a servo, we needed to add a bit more complexity to our circuit (in our first iteration, the pump was simply plugged into a 12V power supply).
<center>
  <img src="/img/Robosys - Pump Testing Rig.jpg" width="100%">
  <br/>
  <div class="caption">
    Wiring diagram for pump testing rig
  </div>
</center>

### Testing & Results
Once again, we 3D printed these parts and tested the assembly in a large bucket of water. Since

<center>
  <img src="/img/pumpv2-assembly.jpg" width="70%">
  <br/>
  <div class="caption">
    Finished assembly of our 2nd iteration pump design
  </div>
</center>


We decided to first test to see if we could rec

For more information on how we waterproofed our servos, visit the page here [TODO]

reached out and decided we couldn't do it

# Soft Tail Actuation with 2 Pumps


# Hard Tail Actuation
submarine mode

[[1]](/references#1).

 design
Switching pump design & results, analysis
Soft tail actuation & results, analysis
Hard tail actuation & results, analysis
