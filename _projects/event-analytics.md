---
layout: page
title: High-Throughput Event Processing & Real-Time Analytics Platforms
description: "Software Architect, Hands-on Technical Lead, 2017-2021. Distributed analytics platforms for fintech and gaming built on Kafka, ClickHouse, Cassandra and Greenplum."
importance: 2
featured: true
card_title: High-Throughput Event Processing & Analytics Platforms
card_role: "Software Architect / Technical Lead · 2017-2021"
card_paragraphs:
  - "Designed and implemented distributed analytics platforms for fintech and gaming applications, processing thousands of events per second with peaks in the tens of thousands."
  - "Built scalable data pipelines using Kafka, ClickHouse, Cassandra, and Greenplum, with a focus on reliable event delivery, deduplication, data consistency, and high-performance analytical queries."
  - "Combined hands-on development with architecture ownership and technical leadership."
card_highlights:
  - label: "Scale"
    text: "Tens of TB of hot data · Hundreds of TB of historical data · Distributed processing infrastructure"
card_focus: "Distributed Systems · Data Engineering · System Architecture"
---

**2017-2021 | Software Architect, Hands-on Technical Lead**

*Distributed Systems · Data Engineering · Event Streaming · OLAP · Backend Architecture*

## Overview

Between 2017 and 2021, I designed and developed two large-scale analytics platforms for fintech and gaming businesses.

Both systems focused on collecting and analyzing user activity events, including installations, application launches, onboarding flows, sessions, payments, and other interactions.

The goal was to transform large volumes of behavioral data into actionable insights about user engagement, application performance, conversion, and product improvement opportunities.

The platforms operated at substantial scale:

- **Thousands of events per second**, with peaks reaching tens of thousands.
- **Tens of terabytes of hot data** and hundreds of terabytes of historical data.
- Distributed, multi-server infrastructure designed for horizontal scaling.

My responsibilities combined system architecture, hands-on backend development, infrastructure engineering, and technical leadership.

## Architecture & Data Processing

One of the platforms used a distributed event-processing architecture built around Apache Kafka.

The processing pipeline consisted of several layers:

**1. Event Ingestion**

Multiple ingestion services received events from client applications, performed initial filtering, and forwarded data into Kafka as the central event transport layer.

**2. Parallel Event Processing**

Independent processing services consumed and enriched incoming events, performing operations such as geographic segmentation and associating device fingerprints with user identities.

**3. Specialized Storage**

Different storage engines were selected according to their workload characteristics:

- **ClickHouse:** fast analytical queries and operational reporting.
- **Cassandra:** event storage for workloads requiring strong durability and delivery-reliability mechanisms.
- **Greenplum:** large-scale historical data storage, complex analytical queries, and multidimensional aggregations.

Additional ETL, consistency verification, and security layers supported the overall architecture.

## Engineering Challenge 1: Data Reliability and Deduplication

Preventing undetected data loss and controlling duplicate processing were among the most important system requirements.

We implemented reliability mechanisms across multiple layers.

**Client-side reliability**

Client applications assigned unique event identifiers and sequence counters. Local buffering helped handle temporary connectivity problems, while gaps in event sequences provided a mechanism for detecting missing events.

**Internal event producers**

For events originating from internal services, we used mechanisms based on log sequence numbers (LSNs) and record hashing to track data consistency.

**Backend processing**

The backend used redundant distributed storage and Kafka's at-least-once delivery semantics, combined with deduplication at the database layer.

In early versions, we implemented a custom UPSERT mechanism for Greenplum before equivalent functionality became officially available.

**Consistency verification**

Dedicated background processes used checksums and LSN-based markers to identify discrepancies between data sources.

The system was designed around explicit failure detection, durable processing, and reconciliation rather than assuming that individual infrastructure components could guarantee end-to-end exactly-once processing.

## Engineering Challenge 2: Flexible Analytics at Scale

A major requirement was supporting both exploratory analytics and fast recurring reports over large datasets.

Greenplum was used for complex analytical workloads involving large raw-data tables, joins, and multidimensional analysis.

Exploratory ad hoc queries could take tens of minutes when operating directly on large volumes of historical data.

Once recurring analytical patterns were identified, we introduced intermediate pre-aggregations and OLAP-style data structures.

This allowed frequently used analytical reports to execute in seconds rather than repeatedly scanning and joining large raw datasets.

Key optimization techniques included:

- Carefully designed table partitioning strategies.
- Distribution key selection for parallel query execution.
- Query execution plan analysis and bottleneck identification.
- Pre-aggregation and workload-specific data organization.

ClickHouse complemented this approach by supporting fast operational reporting for selected event types.

## Engineering Challenge 3: Horizontal Scalability

The platforms needed to accommodate growth in both incoming event traffic and accumulated historical data.

We designed the architecture to scale along two largely independent dimensions:

- **Processing throughput:** adding processing instances to handle increased event traffic.
- **Storage capacity:** expanding distributed storage infrastructure as data volumes increased.

This separation helped the systems evolve alongside growing business and analytical requirements.

Both platforms have continued operating and evolving beyond my original development work.

## My Role & Technical Ownership

I was responsible for system architecture and technical development leadership while remaining directly involved in implementation.

My contributions included:

- Designing distributed data-processing and storage architectures.
- Implementing backend services and selected data-processing components.
- Configuring and integrating databases and event-streaming infrastructure.
- Designing reliability, deduplication, and consistency verification mechanisms.
- Analyzing and optimizing analytical queries.
- Coordinating engineering work and managing developers involved in the projects.

## Engineering Takeaways

These projects reinforced several principles that continue to shape my engineering approach:

**Reliability must be designed end-to-end.** Message delivery guarantees alone are insufficient without event identity, failure detection, deduplication, and consistency verification.

**Storage architecture should reflect workload requirements.** Different analytical and operational workloads benefit from different storage models rather than a single universal database.

**Scalability and query performance require different strategies.** Scaling event ingestion, expanding storage capacity, and optimizing analytical queries are related but distinct engineering challenges.

This experience established a strong foundation in distributed systems, data-intensive applications, performance optimization, and production software architecture, skills I continue to apply in AI/ML engineering.
