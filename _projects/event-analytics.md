---
layout: page
title: Data-Intensive Event Analytics & ML Data Platforms
description: "Software Architect, Hands-on Technical Lead, 2017-2021. Distributed analytics platforms for fintech and gaming built on Kafka, ClickHouse, Cassandra and Greenplum."
importance: 2
featured: true
card_title: Data-Intensive Event Analytics & ML Data Platforms
card_role: "Software Architect / Technical Lead · 2017-2021"
card_paragraphs:
  - "Designed and built distributed analytics platforms for fintech and gaming on Kafka, ClickHouse, Cassandra, and Greenplum."
  - "Focused on reliable event delivery, deduplication, data consistency, and fast analytical queries, combining hands-on development with architecture ownership and technical leadership."
card_highlights:
  - label: "Key results"
    text: "Cut recurring report time from tens of minutes to seconds · Sustained 1,000s of events/sec (peaks of 10,000s) on tens of TB of hot data"
card_focus: "Distributed Systems · Data Engineering · System Architecture"
---

**2017-2021 | Software Architect, Hands-on Technical Lead**

*Distributed Systems · Data Engineering · Event Streaming · OLAP · Backend Architecture*

## Overview

Between 2017 and 2021, I designed and developed two large-scale analytics platforms for fintech and gaming businesses.

Both systems focused on collecting and analyzing user activity events, including installations, application launches, onboarding flows, sessions, payments, and other interactions.

The goal was to turn large volumes of behavioral data into insights about user engagement, application performance, conversion, and product improvement opportunities.

The platforms operated at substantial scale:

- **Thousands of events per second**, with peaks reaching tens of thousands.
- **Tens of terabytes of hot data** and hundreds of terabytes of historical data.
- Distributed, multi-server infrastructure designed for horizontal scaling.

Both platforms have continued operating and evolving beyond my original development work.

## Architecture & Data Processing

One of the platforms used a distributed event-processing architecture built around Apache Kafka.

The processing pipeline consisted of several layers:

1. **Event ingestion.** Multiple ingestion services received events from client applications, performed initial filtering, and forwarded data into Kafka as the central event transport layer.
2. **Parallel event processing.** Independent processing services consumed and enriched incoming events, performing operations such as geographic segmentation and associating device fingerprints with user identities.
3. **Specialized storage.** Different storage engines were selected according to their workload characteristics:

   - **ClickHouse:** fast analytical queries and operational reporting.
   - **Cassandra:** event storage for workloads requiring strong durability and delivery-reliability mechanisms.
   - **Greenplum:** large-scale historical data storage, complex analytical queries, and multidimensional aggregations.

The architecture also included ETL, consistency-verification, and security layers.

## Engineering Challenge 1: Data Reliability and Deduplication

Preventing undetected data loss and controlling duplicate processing were among the most important system requirements, so we built reliability mechanisms into every layer:

- **Client applications:** unique event identifiers and sequence counters, with local buffering for temporary connectivity problems. Gaps in the sequences revealed missing events.
- **Internal event producers:** log sequence numbers (LSNs) and record hashing to track data consistency.
- **Backend processing:** redundant distributed storage and Kafka's at-least-once delivery, with deduplication at the database layer. Early versions used a custom Greenplum UPSERT, built before equivalent functionality became officially available.
- **Consistency verification:** background processes that used checksums and LSN-based markers to find discrepancies between data sources.

The system relied on explicit failure detection, durable processing, and reconciliation rather than assuming that individual infrastructure components could guarantee end-to-end exactly-once processing.

## Engineering Challenge 2: Flexible Analytics at Scale

The platforms had to support both exploratory analytics and fast recurring reports. Greenplum handled complex workloads over large raw-data tables, joins, and multidimensional analysis, but queries over raw historical data could take tens of minutes. Once recurring analytical patterns were identified, we optimized for them:

- **Pre-aggregation:** intermediate pre-aggregations, OLAP-style data structures, and workload-specific data organization.
- **Table design:** partitioning strategies and distribution keys chosen for parallel query execution.
- **Query tuning:** execution plan analysis and bottleneck identification.
- **Operational reporting:** ClickHouse served fast reports for selected event types.

Frequently used reports ran in seconds instead of repeatedly scanning and joining large raw datasets.

## Engineering Challenge 3: Horizontal Scalability

The platforms had to absorb growth in both event traffic and historical data, so the architecture scaled along two largely independent dimensions:

- **Processing throughput:** adding processing instances as event traffic grew.
- **Storage capacity:** expanding distributed storage as data volumes increased.

## My Role & Technical Ownership

I was responsible for system architecture and technical development leadership while remaining directly involved in implementation.

My work spanned distributed data-processing and storage architecture, backend services, database and event-streaming infrastructure, reliability and consistency mechanisms, query optimization, and managing the development team.

## Engineering Takeaways

**Reliability must be designed end-to-end.** Message delivery guarantees alone are insufficient without event identity, failure detection, deduplication, and consistency verification.

**Storage architecture should reflect workload requirements.** Different analytical and operational workloads benefit from different storage models rather than a single universal database.

**Scalability and query performance require different strategies.** Scaling event ingestion, expanding storage capacity, and optimizing analytical queries are related but distinct engineering challenges.

I continue to apply this experience in distributed systems, data-intensive applications, performance optimization, and production software architecture to AI/ML engineering.
