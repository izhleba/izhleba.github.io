---
layout: page
title: Memory-Efficient Planning for Autonomous Game Agents
description: "Backend & AI Engineer, 2010-2014. Server-side autonomous agents for a multiplayer tactical strategy game, with compact precomputed simulation data."
importance: 3
featured: true
card_title: Memory-Efficient Planning for Game AI
card_role: "Backend & AI Engineer · 2010-2014"
card_paragraphs:
  - "Developed server-side autonomous agents for a multiplayer tactical strategy game."
  - "Designed a memory-efficient planning approach combining simulation precomputation, compact data representations, and pattern clustering to reduce runtime computational costs."
card_highlights:
  - label: "Key results"
    text: "Reduced precomputed data requirements from an estimated tens of gigabytes to approximately <strong>100 MB per map</strong>, enabling around <strong>1,000 AI agents across hundreds of concurrent sessions</strong> on a single game server."
card_focus: "Classical AI · Search Algorithms · Simulation · Memory Optimization"
---

**2010-2014 | Backend & AI Engineer**

*Classical AI · Search Algorithms · Simulation · Data Compression · Performance Engineering*

## Overview

I developed server-side AI for autonomous agents in a multiplayer tactical strategy game inspired by classic turn-based tactical games such as UFO and Jagged Alliance.

The game combined a persistent strategic world with online tactical combat sessions.

The main engineering challenge was enabling agents to plan by simulating the consequences of their actions while supporting hundreds of concurrent game sessions on a single server.

## Technical Challenge

The game server maintained the complete world state in memory, together with simulation functions describing how the environment changed in response to player actions.

AI agents had full access to the world state and could evaluate possible actions by simulating their consequences.

However, exhaustive multi-step planning was computationally impractical because the number of possible action sequences grew exponentially with planning depth.

Precomputing and reusing simulation results offered a way to reduce runtime computation, but storing the resulting data in a straightforward representation would have required tens of gigabytes of RAM per game map.

This created a tradeoff between planning capabilities, computational cost, memory consumption, and the accuracy of precomputed information.

## Engineering Approach

I developed a memory-efficient way to represent and reuse precomputed simulation data, combining four techniques:

- **Compact data representation:** Selecting efficient byte-level representations according to the characteristics and ranges of individual data types.
- **Pattern clustering:** Identifying similar patterns in precomputed data and reducing redundancy.
- **Iterative optimization:** Repeatedly refining the representation to balance memory usage against the accuracy of precomputed results.
- **Offline precomputation:** Moving expensive calculations out of the runtime decision-making process.

Precomputation could take several hours, but the resulting data occupied approximately **100 MB per map**, making it practical to keep the necessary information in server memory.

## Results

The approach made it possible to run approximately **1,000 autonomous agents across hundreds of concurrent game sessions on a single game server**.

## My Contribution

I worked as a hands-on backend and AI engineer, developing the autonomous agent system and contributing to:

- Server-side gameplay logic.
- World-state simulation.
- AI algorithms and performance optimization.
- Network protocols and backend components.

## Engineering Takeaways

**Rethink the representation before adding hardware.** This project was an early example of a recurring theme in my engineering work: solving difficult performance problems by reconsidering how computations and data are represented, rather than relying solely on additional hardware.
