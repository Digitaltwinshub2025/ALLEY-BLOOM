from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, Optional

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(255), nullable=True)
    role = db.Column(db.String(50), default="user", nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "full_name": self.full_name,
            "role": self.role,
            "is_active": self.is_active,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class Scenario(db.Model):
    __tablename__ = "scenarios"

    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(255), nullable=False, default="Untitled Scenario")
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String(50), nullable=False, default="baseline")
    alley_id = db.Column(db.String(64), nullable=True)

    location = db.Column(db.JSON, nullable=True)
    dimensions = db.Column(db.JSON, nullable=True)
    phase = db.Column(db.String(100), nullable=True, default="Planning")
    layers = db.Column(db.JSON, nullable=True)
    environmental_data = db.Column(db.JSON, nullable=True)
    notes = db.Column(db.Text, nullable=True)

    version = db.Column(db.Integer, nullable=False, default=1)
    created_by = db.Column(db.Integer, nullable=True)
    is_public = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "type": self.type,
            "alley_id": self.alley_id,
            "location": self.location,
            "dimensions": self.dimensions,
            "phase": self.phase,
            "layers": self.layers or [],
            "environmental_data": self.environmental_data or {},
            "notes": self.notes,
            "version": self.version,
            "created_by": self.created_by,
            "is_public": self.is_public,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }


class ScenarioVersion(db.Model):
    __tablename__ = "scenario_versions"

    id = db.Column(db.Integer, primary_key=True)
    scenario_id = db.Column(db.String(128), nullable=False, index=True)
    version = db.Column(db.Integer, nullable=False)
    data = db.Column(db.JSON, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "scenario_id": self.scenario_id,
            "version": self.version,
            "data": self.data,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class Collaboration(db.Model):
    __tablename__ = "collaborations"

    id = db.Column(db.Integer, primary_key=True)
    scenario_id = db.Column(db.String(128), nullable=True, index=True)
    user_id = db.Column(db.Integer, nullable=True, index=True)
    role = db.Column(db.String(50), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "scenario_id": self.scenario_id,
            "user_id": self.user_id,
            "role": self.role,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }


class Export(db.Model):
    __tablename__ = "exports"

    id = db.Column(db.Integer, primary_key=True)
    scenario_id = db.Column(db.String(128), nullable=True, index=True)
    export_type = db.Column(db.String(50), nullable=True)
    file_path = db.Column(db.String(1024), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "scenario_id": self.scenario_id,
            "export_type": self.export_type,
            "file_path": self.file_path,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
