**Description:**
This project is an arcade-style survival game inspired from "Crossy Road," built entirely in Python. The objective is to navigate a turtle across a busy multi-lane highway where traffic density and speed increase with every successful crossing.

**Purpose of project:**
For years, Crossy Road was my go-to mobile game. I spent a lot of time playing it, and so I wanted to challenge myself to build the game that gave me so much joy. I built this project to peel back the curtain: to understand how to generate "random" traffic that still feels fair, how to handle collision detection in real-time, and how to scale difficulty mathematically. It was an exercise in taking a product I loved as a consumer and rebuilding it as an engineer.

**Tech Stack:**
Language: Python
Library: Turtle Graphics (Standard Library)
Concepts: OOP, Memory Management, Collision Detection, Event Listeners

**Difficulties:**
In early versions, the game would slow down significantly after level 5. I realized that while cars were disappearing visually off the left side of the screen, they still existed in the computer's memory. I implemented a cleanup_traffic() method that filters the list of active cars every frame, deleting objects that drift out of bounds. This taught me the importance of resource management.
Initially, cars spawned at random Y-coordinates, leading to messy overlaps and "unfair" deaths. I solved this by implementing a Lane System in the configuration file (LANES list). Cars now snap to specific grid lines, simulating organized traffic flow and making the gameplay fair.

**Changes for the future:**
I plan to build an autonomous agent that can automatically find the safest path through the traffic, effectively letting the computer play itself.
