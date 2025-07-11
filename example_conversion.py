#!/usr/bin/env python3
"""
Zapier-n8n Workflow Converter - Example Conversion Scripts
=========================================================

This module provides comprehensive examples of converting workflows between
Zapier and n8n platforms using AI-powered intelligent mapping.

Author: AI Workflow Converter
License: MIT
"""

import json
import logging
from typing import Dict, List, Any
from workflow_converter_app import WorkflowConverter

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def example_zapier_to_n8n_conversion():
    """
    Example: Convert a Zapier workflow to n8n format
    Demonstrates Gmail trigger -> Slack notification workflow
    """
    
