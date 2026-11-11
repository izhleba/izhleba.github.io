---
layout: page
title: Audio-Driven Facial Animation & Neural Video Generation
description: "Elai | Co-Founder, Principal Engineer & R&D Lead. Hands-on R&D of speech-driven facial animation and talking-head video generation, from research to production."
importance: 1
featured: true
card_role: "Elai · Co-Founder / Principal Engineer / R&D Lead · 2021-2026"
card_paragraphs:
  - "Led hands-on R&D of neural systems for speech-driven facial animation and realistic talking-head video generation."
  - "Tackled expressive motion modeling, lip-sync evaluation and real-time neural rendering. Built production ML systems and led a small engineering team, combining model research with architecture and performance optimization."
card_highlights:
  - label: "Key results"
    text: "300K+ avatar videos generated on the platform (2024-2026), production deployment of the developed models, and a real-time avatar MVP achieving 25+ FPS."
card_focus: "Generative AI · Neural Rendering · Research Engineering · ML Systems"
# Paste the YouTube video ID of the demo (the part after "v=" in the URL), e.g. dQw4w9WgXcQ.
# While empty, the video block and the thumbnail on the home page are hidden.
youtube_id:
---

**2021-2026 | Co-Founder, Principal Engineer & R&D Lead**

*Generative AI · Deep Learning · Neural Rendering · Real-Time ML Systems*

## Overview

At Elai, I led the development of neural technologies for generating realistic talking-head videos from speech audio, combining hands-on research engineering with technical leadership.

We developed a two-stage generation pipeline:

- **Audio-to-Animation:** predicting frame-level facial motion, including lip articulation, eye and eyebrow movements, and emotional expressions.
- **Animation-to-Video:** generating realistic avatar videos driven by the predicted facial motion.

These technologies were deployed in Elai's production platform, where users generated over 300,000 avatar videos between 2024 and 2026.

{% if page.youtube_id %}
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 1.5rem 0 0.5rem;">
  <iframe
    src="https://www.youtube-nocookie.com/embed/{{ page.youtube_id }}"
    title="Elai avatar video demonstration"
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;"
    allow="accelerometer; encrypted-media; picture-in-picture"
    allowfullscreen
    loading="lazy"></iframe>
</div>
<div class="caption">
  Elai avatar video demonstration. Earlier public demonstration of the avatar-generation technology developed at Elai.
  It does not represent the latest model generation: subsequent production models included additional quality improvements.
</div>
{% endif %}

## Research Challenge: Learning Expressive Facial Motion

One of the fundamental challenges was the ambiguous relationship between speech audio and facial animation.

The same audio can correspond to multiple plausible facial movements and emotional expressions. Straightforward supervised learning approaches tend to average over these possibilities, producing overly smooth articulation and limited expressiveness.

This manifested in several ways:

- Models reacted to speech but avoided sharp or uncommon mouth movements.
- Emotional expressions were difficult to learn because of their high variability and uneven representation in training datasets.
- Improvements in numerical objectives did not always translate into perceptually better animation.

We investigated different approaches to addressing these limitations. Our research indicated that training data design and neural architecture improvements were more effective directions than relying primarily on additional loss functions or behavior-encouraging techniques.

The resulting improvements were integrated into the production models.

## Research Challenge: Reliable Evaluation

Evaluating generated facial animation required more than optimizing a single metric.

Automated measurements were useful for rapid iteration but introduced biases and did not fully capture perceived visual quality.

I helped establish a multi-layer evaluation process combining:

- Fast automated measurements for experimental iteration.
- Structured human assessments using formalized evaluation protocols.
- Human-preference comparisons against competing solutions.
- Comprehensive internal acceptance testing to evaluate artifacts and production readiness.

Our visual quality assessment covered a broad range of potential artifacts, including issues that can also occur in real-world video due to camera, lighting, or compression effects.

Internal testing found no significant visual artifacts under the defined evaluation criteria, supporting the production release of the models.

## Engineering Challenge: Real-Time Neural Avatar Generation

We also developed an MVP for interactive, real-time AI avatars.

The system combined streaming LLM responses, text-to-speech synthesis, audio-driven animation, and neural video rendering.

**Technical results:**

- Video rendering performance exceeding 25 FPS on a basic cloud GPU configuration.
- Approximately 2-3 seconds from the first audio chunk to the first generated video frame.
- Around 4 seconds end-to-end latency in representative scenarios, depending on request and response length.
- Support for 1080p video output, without requiring neural generation of every output pixel.

The key architectural improvement was organizing the system as a streaming pipeline processing small chunks, allowing multiple stages to execute concurrently.

This made neural video rendering the primary performance bottleneck.

We improved throughput by modifying the model architecture to balance rendering quality and computational cost, followed by targeted optimizations of critical operations, including CPU-GPU data transfers.

Although we eventually discontinued the standalone real-time avatar direction for product-strategy reasons, the performance optimizations were reused in the main generation platform.

## My Role & Technical Ownership

I served as a hands-on Principal Engineer and R&D Lead, working with a small cross-functional team of typically 4-5 engineers, including myself, 2-3 ML Engineers, and a Software Engineer.

My responsibilities combined:

- Neural model development, training, implementation, and experimentation.
- Research into facial animation and generative video techniques.
- Technical architecture and performance optimization.
- Research planning, hypothesis formulation, and experimental evaluation.
- Training infrastructure, experiment tracking, and evaluation workflows.
- Technical leadership and coordination of the R&D team.

Our primary development stack included Python and PyTorch, with performance-critical components optimized using native code, CUDA, Cython, Numba, and JIT compilation where appropriate.

## Engineering Takeaways

Three principles shaped my approach throughout this work:

**Understand the learning problem before optimizing the objective.** Data ambiguity and dataset composition can limit model performance more fundamentally than the choice of loss function.

**Build evaluation systems you can trust.** Automated metrics and human assessments provide different kinds of evidence. Reliable research decisions require understanding the limitations of both.

**Optimize the whole system, not just the model.** Streaming architecture, computational tradeoffs, and targeted bottleneck optimization can be as important as model-level improvements.

This project reflects the kind of engineering I enjoy most: working on difficult ML problems, designing experiments, building production-ready systems, and taking technical ownership from research to deployment.
