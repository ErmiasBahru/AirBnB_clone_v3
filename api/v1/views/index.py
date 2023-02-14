#!/usr/bin/python3
"""Index view"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


stats = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}


@app_views.route('/status', strict_slashes=False)
def status_route():
    """Status of the web server"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', strict_slashes=False)
def stats_route():
    """Stats"""
    return_dict = {key: storage.count(value) for key, value in stats.items()}
    return jsonify(return_dict)

