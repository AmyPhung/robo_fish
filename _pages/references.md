---
title: "References"
permalink: /references/
layout: posts
sidebar:
  nav: "docs"
---

<a id="1">[1]</a>
R. K. Katzschmann, J. DelPreto, R. MacCurdy and D. Rus, "Exploration of Underwater Life with an Acoustically Controlled Soft Robotic Fish," Science Robotics, 2018, Vol. 3, Issue 16, doi: 10.1126/scirobotics.aar3449. <http://robert.katzschmann.eu/wp-content/uploads/2018/04/katzschmann2018exploration.pdf>
- This paper documents the creation of SoFi, a robotic fish with a soft tail that formed the primary inspiration for our project
- Provides a high-level overview of their soft robotic system which we based ours off of
- Companion video: <https://www.youtube.com/watch?v=Dy5ZETdaC9k&ab_channel=MITCSAIL>

<a id="2">[2]</a>
R. K. Katzschmann, A. d. Maille, D. L. Dorhout and D. Rus, "Cyclic hydraulic actuation for soft robotic devices," 2016 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), 2016, pp. 3048-3055, doi: 10.1109/IROS.2016.7759472. <http://robert.katzschmann.eu/wp-content/uploads/2017/08/katzschmann2016cyclic.pdf>
- Explores 6 different pump designs for SoFi
- Original gear pump design isn’t great because it requires changing direction of a motor frequently
- We created a pump based on their design using a centrifugal pump with a custom rotating valve to make it bidirectional

<a id="3">[3]</a>
Rus, Daniela & Tolley, Michael. (2015). Design, fabrication and control of soft robots. Nature. 521. 467-75. 10.1038/nature14543.  https://www.researchgate.net/publication/277410991_Design_fabrication_and_control_of_soft_robots
- Lit review for soft robots, from the lab that created SoFi

<a id="4">[4]</a>
Chen, Z., Hou, P., and Ye, Z. (March 25, 2019). "Robotic Fish Propelled by a Servo Motor and Ionic Polymer-Metal Composite Hybrid Tail." ASME. J. Dyn. Sys., Meas., Control. July 2019; 141(7): 071001. doi:10.1115/1.4043101 <https://asmedigitalcollection.asme.org/dynamicsystems/article/141/7/071001/726553/Robotic-Fish-Propelled-by-a-Servo-Motor-and-Ionic>
- A hybrid fish tail design that uses both servos and soft actuators
- Notes that servos are generally more capable of high-frequency movement than soft actuators are, which is important for good fish motion
- Uses the strengths of servos and soft actuators to make a good fish tail

<a id="5">[5]</a>
F. Berlinger, J. Dusek, M. Gauci, and R. Nagpal, "Robust Maneuverability of a Miniature, Low-Cost Underwater Robot Using Multiple Fin Actuation," in IEEE Robotics and Automation Letters, vol. 3, no. 1, pp. 140-147, Jan. 2018, doi: 10.1109/LRA.2017.2734969. <https://www.florianberlinger.ch/publications/pdf/ral2017-berlinger.pdf>
- This paper documents Blueswarm, another robotic fish platform that’s smaller than SoFi and uses a simpler actuation method
- Design uses lots of small fins for control
- Low-cost, high maneuverability platform
- Good example of a self-contained robotic system

<a id="6">[6]</a>
F. Berlinger, M. Gauci, and R.Nagpal, "Implicit coordination for 3D underwater collective behaviors in a fish-inspired robot swarm," in Science Robotics, vol. 6, no. 50, 2021, doi: 10.1126/scirobotics.abd8668. <https://robotics.sciencemag.org/content/6/50/eabd8668>
- Blueswarm platform has been used to demonstrate swarm behavior

<a id="7">[7]</a>
F Berlinger, M Saadat, H Haj-Hariri, G V Lauder, and R Nagpal. "Fish-like three-dimensional swimming with an autonomous, multi-fin, and biomimetic robot".Bioinspiration & Biomimetics 16, no.2 (2021): 026018. <https://www.florianberlinger.ch/publications/pdf/berlinger2020fish.pdf>
- Documents Blueswarm fish tail dimensions & design
- We’re using a different fish tail design, but this analysis on the importance of the relative size and shape of the fish body/tail is useful

<a id="8">[8]</a>
K. Soltan, J. O'Brien, J. Dusek, F. Berlinger and R. Nagpal, "Biomimetic actuation method for a miniature, low-cost multi-jointed robotic fish," OCEANS 2018 MTS/IEEE Charleston, 2018, pp. 1-9, doi: 10.1109/OCEANS.2018.8604763. <https://ieeexplore.ieee.org/document/8604763>
- Different form of fish locomotion using the same actuator as Blueswarm

<a id="9">[9]</a>
Lloret, Jaime et al. “Underwater wireless sensor communications in the 2.4 GHz ISM frequency band.” Sensors (Basel, Switzerland) vol. 12,4 (2012): 4237-64. doi:10.3390/s120404237 <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3355409/>
- Evaluates WiFi range underwater
- At 15cm distance there’s 0% packet loss, at 18cm it’s 100% - in theory, if we don’t dive below 15cm, we could use WiFi to communicate with the robot. Also opens the door for “returning to surface” as a failsafe behavior

<a id="10">[10]</a>
G. Schirripa Spagnolo, L. Cozzella, and F. Leccese, “Underwater Optical Wireless Communications: Overview,” Sensors, vol. 20, no. 8, p. 2261, Apr. 2020. <https://www.mdpi.com/1424-8220/20/8/2261/htm>
- Light absorption by water based on wavelength
- Documents high attenuation rates for non-visible wavelengths - motivates use of cameras in our design

<a id="11">[11]</a>
Y. Zhong, Z. Li and R. Du, "A Novel Robot Fish With Wire-Driven Active Body and Compliant Tail," in IEEE/ASME Transactions on Mechatronics, vol. 22, no. 4, pp. 1633-1643, Aug. 2017, doi: 10.1109/TMECH.2017.2712820. <https://ieeexplore.ieee.org/document/7942132>
- Cable driven fish tail design
- We’re not using this design, but it’s another helpful reference as a full self-contained robotic system

<a id="12">[12]</a>
A. K. Saha et al., "A low cost remote controlled underwater rover using raspberry Pi," 2018 IEEE 8th Annual Computing and Communication Workshop and Conference (CCWC), 2018, pp. 769-772, doi: 10.1109/CCWC.2018.8301657. <https://ieeexplore-ieee-org.olin.idm.oclc.org/document/8301657?arnumber=8301657>
- Similar scope to our project, tethered video feed and power
- Integrates several other sensors
- Measuring depth/pressure underwater ttps://github.com/AmyPhung/robo_fishwould require waterproofed pressure sensors

<a id="13">[13]</a>
“Pneumatic Networks for Soft Robotics That Actuate Rapidly.” Soft Robotics Toolkit. <https://softroboticstoolkit.com/publications/pneumatic-networks-soft-robotics-actuate-rapidly>
- Design documented here helped improve the actuation rate of our soft tail design

<a id="14">[14]</a>
“Towards a Soft Pneumatic Glove for Hand Rehabilitation.” Soft Robotics Toolkit. <https://softroboticstoolkit.com/publications/towards-soft-pneumatic-glove-hand-rehabilitation>
- Design documented here helped improve the degree of actuation of our soft tail design 


<a id="15">[15]</a>
“Hydraulic Autonomous Soft Robotic Fish for 3D Swimming. <http://robert.katzschmann.eu/wp-content/uploads/2017/08/katzschmann2014hydraulic.pdf>
- Design documented here helped us design our soft tails
