# ![Py The Way](./logo.png?raw=true)

[![Build Status](https://travis-ci.org/py-the-way/py-the-way.svg?branch=master)](https://travis-ci.org/py-the-way/py-the-way) 
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/7902dc936fb442a3a34222566d16ebb1)](https://www.codacy.com/app/TooFiveFive/py-the-way?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=py-the-way/py-the-way&amp;utm_campaign=Badge_Grade) 
[![License](https://img.shields.io/github/license/py-the-way/py-the-way.svg)](https://github.com/py-the-way/py-the-way/blob/master/LICENSE)

A recommendation system for suggesting where a user should live within the USA based on input data and datasets

## About this project

This project is a recommendation system that recommends where a user should live in the US using **big data**, **python** and **pandas**.

It was originally made for a hackathon where it came first place.

## Requirements
- Docker
- Docker Compose
- Python3
- Pip3
- Node.js
- Npm

## Installation

### Production
1. In the `web` directory, first change `api` in `App.js` to your backend endpoint.
2. Run `npm i` and `npm run build` in that directory.
3. In the base dir, create file called `.env`.
4. Fill that file out as such:
	```
	FRONTEND_PORT=YOUR_PORT
	BACKEND_PORT=YOUR_PORT
	HOST=YOUR_DOMAIN/HOST
	```
5. Run `docker-compose up -d` in the base dir to start the service
	
	*Run `docker-compose down`* to stop the service


	
### Development
#### Frontend
- `cd web`
- (First Time) `npm i`
- `npm start`
#### Backend
- `cd src`
- (First Time) `pip install -r requirements.txt`
- `python3 main.py`
