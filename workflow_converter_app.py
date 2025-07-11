#!/usr/bin/env python3
"""
Zapier to n8n Workflow Converter
AI-powered workflow converter for seamlessly migrating automation workflows 
between Zapier and n8n platforms with intelligent mapping and optimization.
"""

import os
import json
import logging
import requests
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path

# Flask web framework
from flask import Flask, render_template, request, jsonify, send_file, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

# AI and ML libraries
import openai
