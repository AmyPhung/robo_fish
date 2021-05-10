---
title: "Conclusion & Future Work"
permalink: /conclusion/
layout: posts
sidebar:
  nav: "docs"
---

Overall, it was pretty cool to see the soft robotic tail actuate in a controlled manner by the Arduino, even if that version of the fish wasn't able to swim forwards. Originally, we chose to go with a smaller sized fish since we thought that would make the project cheaper and easier to do. In hindsight, while aiming for a smaller robot size definitely helped to keep material costs and manufacturing time down, it was significantly more difficult to get to work - making a robot fish would have made it easier to fit our electronics inside, and it also would've allowed us to use bigger pumps and valves which are necessary to fix some of the primary issues our design faced.

There's two primary improvements to this project that we would make given more time. We would: 1) Improve the soft robotic tail's deflation rate, and 2) Create a fully self-contained system with onboard power and computation. In order to improve the tail's deflation rate, we would need to use valves, additional pumps, or a modified pump design such that the inflation and deflation rates were approximately equal. This would allow us safely to increase the frequency of tail oscillations without concern for the chambers over-inflating and bursting, which is something we ran into with the existing design.   fully self-contained version of the hard-tail design.

From working on this project, we've come to realize the extent to which a tether affects water-based robots - since robots in the water have much less "surface friction" than most robots on land do, the tether ends up acting like a giant spring and makes it difficult to test. If we were to do this project over again, we would make a bigger robot that could fit all of the power and computing hardware onboard so that we don't need to work around the dynamics that the tether creates.

Project organization-wise, an additional challenge to working on this project was the fact that all three of us were located across the US (one of us was in California, one was in Texas, and one was in Massachusetts). There was a fair bit of time spent on fabrication that we normally wouldn't have needed to spend since we each needed to re-create hardware systems individually. Despite being far from each other, we were able to collaborate by sharing 3D printable designs and code which ultimately worked out pretty well.
