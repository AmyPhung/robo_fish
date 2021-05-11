---
title: "Robotics System Design"
permalink: /sys-design/
layout: posts
sidebar:
  nav: "docs"
---
As mentioned in the abstract of this project this project seeks to build a robotic fish with a range of capabilities. It was important to us that the fish lended itself to future applications in swarms and self contained/autonomous operation.

As noted earlier this fish is closely based off of MIT’s Sofi [[1]](/references#1). We have designed our fish such that it is a ½ scale version of Sofi. The choice to do this is based on Sofi’s success and our hope to make use of existing work to streamline our design.

## Distinctions
Seeing as we are operating with fewer resources than the Sofi researchers we have made several design changes. These key differences are captured here:
- Single centrifugal pump/rotating valve as opposed to a gear pump
- No fins/depth control (fixed depth surface fish)
- No acoustic underwater control
- Tethered Power instead of batteries
- ½ scale

## Our System and Subsystems
<center>
  <img src="/robo_fish/img/sys_diagram.jpg" width="100%">
  <br/>
  <div class="caption">
    System diagram showing subsytems
  </div>
</center>
The fish is split into three subsystems as such: [Soft Tail subsystem](/subsys-tail), [Actuation/Pump subsystem](/subsys-actuate), [Software/Electronics subsystem](/subsys-software) 

## Fish CAD
<center>
  <img src="/robo_fish/img/sys_cad.jpg" width="100%">
  <br/>
  <div class="caption">
    Full Cad of original fish with subsytems labeled
  </div>
</center>



"...the **go to** statement should be abolished..." [[1]](/references#1).
