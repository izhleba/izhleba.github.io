---
layout: about
title: about
permalink: /
subtitle: Head of AI Research at <a href="https://www.panopto.com/" target="_blank">Panopto</a>. Applied AI leader, ex-co-founder &amp; CRDO at <a href="https://elai.io/" target="_blank">Elai.io</a>.

profile:
  align: right
  image: prof_pic.jpg
  image_circular: true # crops the image to make it circular
  more_info: >
    <p>Barcelona, Spain</p>
    <p>Open to: Head of AI / Applied AI Lead / Staff Research Engineer</p>

selected_papers: false # includes a list of papers marked as "selected={true}"
social: true # includes social icons at the bottom of the page

announcements:
  enabled: false

latest_posts:
  enabled: false
---

Hi! I'm Aleksei, an applied AI leader with 15+ years in software, data and machine learning. I currently lead AI research at [Panopto](https://www.panopto.com/), where I turn research ideas into product features used by learning and enterprise video customers.

Before that, I co-founded [Elai.io](https://elai.io/) and served as its Chief R&D Officer. There I led the research and engineering of AI video avatar technology: a text-to-video platform that makes creating e-learning content fast and accessible. Earlier, I co-founded DataSpike (NLP for AML/KYC in financial institutions), led an analytics platform for mobile games, and built real-time data and machine learning infrastructure in Scala and Python.

I enjoy the full path from research to production: choosing the right problems, building and mentoring research and engineering teams, and shipping AI that creates measurable business value. My interests include generative AI for video and avatars, NLP, and data-driven product development.

I'm currently open to **Head of AI / Applied AI Lead / Staff Research Engineer** roles and R&D leadership positions. Please feel free to get in touch!

{% assign featured = site.projects | where: "featured", true | first %}
{% if featured %}
<h2 class="mt-4">Featured project</h2>
<div class="card hoverable mb-4" style="position: relative; display: flex; flex-direction: row; flex-wrap: wrap; overflow: hidden;">
  {% if featured.youtube_id %}
  <div style="flex: 1 1 280px; min-height: 180px;">
    <img src="https://img.youtube.com/vi/{{ featured.youtube_id }}/hqdefault.jpg" alt="Video preview: {{ featured.title }}" style="width: 100%; height: 100%; object-fit: cover; display: block;">
  </div>
  {% endif %}
  <div class="card-body" style="flex: 2 1 340px;">
    <h3 class="card-title"><a href="{{ featured.url | relative_url }}" style="position: static;">{{ featured.title }}</a></h3>
    <p class="card-text"><strong>Elai</strong> &middot; Co-Founder / Principal Engineer / R&amp;D Lead</p>
    <p class="card-text">Led hands-on R&amp;D of neural systems for speech-driven facial animation and realistic talking-head video generation.</p>
    <p class="card-text">Tackled expressive motion modeling, lip-sync evaluation and real-time neural rendering. Built production ML systems and led a small engineering team, combining model research with architecture and performance optimization.</p>
    <p class="card-text"><strong>Key results:</strong> 300K+ avatar videos generated on the platform (2024-2026), production deployment of the developed models, and a real-time avatar MVP achieving 25+ FPS.</p>
    <p class="card-text"><small>Focus: Generative AI &middot; Neural Rendering &middot; Research Engineering &middot; ML Systems</small></p>
    <p class="card-text"><a href="{{ featured.url | relative_url }}">Read the full case study &rarr;</a></p>
  </div>
</div>
{% endif %}
