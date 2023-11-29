

# MongoDB and RabbitMQ Integration for Data Management

## Overview
This project is divided into two main parts: the first part involves creating a MongoDB database with collections for authors and quotes, and a script for querying this data. The second part uses RabbitMQ for simulating email notifications to contacts stored in the MongoDB database, demonstrating producer and consumer patterns.

## Part 1: MongoDB Database and Query Script

### Features
- **MongoDB Collections**:
  - `authors`: Contains author details.
  - `quotes`: Contains quotes with author references.
- **Data Querying**:
  - Script to search quotes by tag, author name, or a set of tags.
  - Support for abbreviated search queries.
- **Redis Caching**:
  - Caching query results for faster retrieval.

### MongoDB Setup
1. Set up an Atlas MongoDB cloud database.
2. Create `authors` and `quotes` collections.
3. Use Mongoengine ODM for modeling and data operations.

### Usage
- Run the script and input commands in the format: `command:value`.
- Supported commands: `name:<author>`, `tag:<tag>`, `tags:<tag1>,<tag2>`, `exit`.
- Use Redis for caching query results.

## Part 2: RabbitMQ for Email Simulation

### Features
- **MongoDB Contact Model**:
  - Model for storing contact details with fields for name, email, and a boolean flag indicating if an email has been sent.
- **Producer Script (`producer.py`)**:
  - Generates fake contacts using Faker and stores them in MongoDB.
  - Sends messages to RabbitMQ queue with the ObjectID of each contact.
- **Consumer Script (`consumer.py`)**:
  - Receives messages from RabbitMQ queue.
  - Simulates email sending and updates the contact's sent flag in MongoDB.

### RabbitMQ Setup
1. Use RabbitMQ for message queuing.
2. Set up queues for managing contact notifications.

### Usage
- Run `producer.py` to generate contacts and queue messages.
- Run `consumer.py` to process messages and simulate email sending.

## Installation and Dependencies
- Clone the repository.
- Requires Python with dependencies: Mongoengine, Faker, Redis, RabbitMQ client.
- Docker for running MongoDB and RabbitMQ containers.

## Development and Testing
- Tested MongoDB models and query functionalities for accuracy.
- Validated the integration and message handling with RabbitMQ.
- Ensured Redis caching improves query response times.
