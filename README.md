# JSON Vizard

Brief description of your project.

Tests and code style checks: [![Unit Tests and Code Style](https://github.com/frehburg/JSON-Vizard/actions/workflows/python-app.yaml/badge.svg)](https://github.com/frehburg/JSON-Vizard/actions/workflows/python-app.yaml)

## Table of Contents

- [Project Description](#project-description)
- [Planned Features](#planned-features)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Description

This is a simple GUI to inspect, edit and create JSON files.

The following versions are planned:
- `v0.1`: Implement JSON file reading and modification
- `v1.1`: Add a tree view to the GUI
- `v1.2`: Add a JSON editor and creator to the GUI
- `v2.0`: Add MongoDB support

## Planned Features

### Version 0: Backend and CLI
#### Version 0.1: JSON File Reading and Modification
The initial version of the project is a simple suit of methods to read and modify JSON files. This is not representable
of the final product, but a first step towards it. 

The following features are planned:
- Read JSON files
  - To a dictionary
  - To String
  - From BSON (Binary JSON)
- Write JSON files
  - From a dictionary
  - From String
  - To BSON (Binary JSON)
- Remove arguments from JSON files
- Add arguments to JSON files
  - Simple types (Strings, Numbers, Booleans)
  - Lists
  - Dictionaries (Sublevels)
- Modify simple types in JSON files
- Implement search in JSON
- Add simple CLI

### Version 1: GUI
#### Version 1.1: Tree View
- Curly braces around each level, one indentation per level, different colors for different types and levels of indentation
- Expandable and collapsible nodes with little triangles
  - ▷ Expand
  - ▽ Collapse
- Add a search bar
- Add settings
  - Show/hide types
  - Font size
  - Dark mode (background and text color)
  - Show/hide line numbers
  - Custom colors schemes for different types and indentation levels

#### Version 1.2: Visual JSON Editor and Creator
- Add a button to add new nodes at each level +
  - Simple types (Strings, Numbers, Booleans)
  - Lists
  - Dictionaries (Sublevels)
- Add a button to remove nodes ✖
- Add a button to modify simple types ✎

### Version 2.0: MongoDB Support
- More to come...

## Getting Started

Instructions on how to set up and run your project locally.

### Prerequisites

List any software, libraries, or dependencies that need to be installed before setting up the project.

### Installation

Step-by-step instructions on how to install and set up your project.

## Features

Provide examples and explanations of how your project can be used. Include code snippets or screenshots if necessary.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/frehburg/JSON-Vizard/blob/main/LICENSE.txt) file for details.

## Acknowledgements

I would like to thank me, myself and I.

---
