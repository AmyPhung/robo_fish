---
title: "Waterproofing"
permalink: /waterproofing/
layout: posts
sidebar:
  nav: "docs"
---
Waterproofing became a necessary part of our project when we started using servos underwater. Buying waterproof servos off-the-shelf would have been quite pricey, and since we were only creating prototypes that would be in shallow water for short durations of time that seemed like an excessive expense for our limited budget.

Our first attempt of waterproofing servos involved filling the servos to the brim with white lithium grease and hoping that the grease alone would be enough to keep water out of the servo.

<center>
  <img src="/robo_fish/img/waterproofing-v1-2.jpg" width="30%">
  <br/>
  <div class="caption">
    Tube of white lithium grease we used for our first waterproofing attempt
  </div>
</center>


<center>
  <img src="/robo_fish/img/waterproofing-v1-3.jpg" width="40%">
  <img src="/robo_fish/img/waterproofing-v1-1.jpg" width="40%">
  <br/>
  <div class="caption">
    Disassembling the servo and filling it with grease
  </div>
</center>

Unfortunately, the lithium grease was too viscous for the small 9g servo, and so after we sealed it back up the servo could no longer move.

This time, we ordered 9g servos with metal gears (MG90S servo - [Amazon link](https://www.amazon.com/gp/product/B07L6FZVT1/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)) since they had more torque for the same sized servo. We also chose to fill the servos with mineral oil instead of lithium grease since the oil is less viscous. However, since the oil is less viscous, we were concerned about potential leaks near the point of rotation, so we also purchased O-rings (7.5mm OD, 4.5mm ID, 1.5mm Width - [Amazon link](https://www.amazon.com/gp/product/B08F2G63CL/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)) that fit well onto these servos.

<center>
  <img src="/robo_fish/img/mineral-oil.png" width="32%">
  <img src="/robo_fish/img/waterproofing-v2.jpg" width="40%">
  <br/>
  <div class="caption">
    Filling the servos with mineral oil and adding O-rings
  </div>
</center>

Waterproofing this servo worked well for the first 5 minutes or so, but after a while of running underwater it began acting a bit strange - it ran as expected most of the time, but every now and then it would just stop for awhile before resuming. I'm not sure if this is caused by water getting into the servo, but for the next fish iteration, we decided to coat the servo in epoxy after filling it with oil to ensure it was properly sealed.

<center>
  <img src="/robo_fish/img/epoxy-servo.png" width="40%">
  <br/>
  <div class="caption">
    Oil-filled, epoxy-coated metal gear servo with an O-ring
  </div>
</center>

Epoxy takes a long time to cure, but it was well worth the wait considering that this servo worked without issues. The mount dimensions needed to be adjusted slightly since the epoxy added some thickness to the plastic housing, but this was straightforward to do.
