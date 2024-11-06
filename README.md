# Automated Oversharing

**Automated Oversharing** is a Python-based project that integrates Flask with Tines to streamline blog post sharing on LinkedIn and X (formerly Twitter). Developed as companion content for the article *Using Tines to Broadcast Your Half-Baked Blog*, this repo provides a self-contained Flask example and a complete Tines story to automate the summarization and social sharing of blog content.

## Overview

This repository includes:

- **Flask**: Acts as a webhook provider to notify Tines when a new blog post is published.
- **Blog Manager**: Complete, ready-to-import Tines story. Uses OpenAI for automatic post summarization and API integrations to share to social media platforms.

## How It Works

1. **Trigger**: Flask sends post details (title, content, tags) to Tines via a webhook whenever a new blog post is published.
2. **Summarization**: Tines uses OpenAI to generate a concise summary of the post.
3. **Social Media Sharing**: Tines posts the summary and a link to LinkedIn and X.

## Getting Started

### Prerequisites

- **Python 3.8+** with Flask installed
- Tines account
- LinkedIn and X Developer accounts to generate API credentials

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/tyler-tee/Automated-Oversharing.git
   cd Automated-Oversharing
   ```

2. Run the Flask app:

   ```bash
   python app.py
   ```

3. Import the provided Tines story to set up automation workflows.

## Repository Structure

- **Flask/**: Contains the Flask app for triggering webhooks.
- **Tines/**: Includes a ready-to-import JSON story for Tines automation.

## License

This project is licensed under the MIT License.