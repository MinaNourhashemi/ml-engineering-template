# ML Engineering Template

Production-style template for building machine learning systems with clean code, testing, and automation.

## Features

- Modular project structure (`src/`, `tests/`, `scripts/`)
- Ruff for linting and formatting
- pre-commit hooks for automated code quality checks
- pytest for unit testing
- structured logging for ML pipelines

## Project Structure

src/app → core application logic  
tests → unit tests  
scripts → runnable scripts  

## Example

Run training script:

python scripts/run_training.py

Run tests:

pytest

Run linting:

ruff check .

Format code:

ruff format .

## Goal

This repository demonstrates best practices for organizing machine learning engineering projects for research and production environments.

## ML Pipeline

Typical machine learning workflow implemented in this repository:

data → preprocessing → model → evaluation → logging