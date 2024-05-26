from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Sector(db.Model):
    __tablename__ = "sectors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class Users(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    sector_id = db.Column(db.Integer, db.ForeignKey("sectors.id"), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    sector = db.relationship("Sector", backref=db.backref("users", lazy="dynamic"))


class Machine(db.Model):
    __tablename__ = "machine"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sector_id = db.Column(db.Integer, db.ForeignKey("sectors.id"), nullable=False)


class Operation(db.Model):
    __tablename__ = "operations"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sector_id = db.Column(db.Integer, db.ForeignKey("sectors.id"), nullable=False)


class TimeOfProduction(db.Model):
    __tablename__ = "time_of_production"
    id = db.Column(db.Integer, primary_key=True)
    machine_id = db.Column(db.Integer, db.ForeignKey("machine.id"), nullable=False)
    operation_id = db.Column(db.Integer, db.ForeignKey("operations.id"), nullable=False)
    time = db.Column(db.String, nullable=False)
    item = db.Column(db.Integer, nullable=False)


class EntriesAndExits(db.Model):
    __tablename__ = "entries_and_exits"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    entry_type = db.Column(db.String, nullable=False)
    sector_id = db.Column(db.Integer, db.ForeignKey("sectors.id"), nullable=False)
    machine_id = db.Column(db.Integer, db.ForeignKey("machine.id"), nullable=False)
    entry_at = db.Column(db.String, nullable=False)
    exit_at = db.Column(db.String, nullable=False)
    item = db.Column(db.Integer, nullable=False)
    time_of_production_id = db.Column(
        db.Integer, db.ForeignKey("time_of_production.id"), nullable=False
    )
    production_order = db.Column(db.Integer, nullable=False)
    operation_id = db.Column(db.Integer, db.ForeignKey("operations.id"), nullable=False)
    amount_produced = db.Column(db.Integer, nullable=False)
    reason_for_stopping_id = db.Column(
        db.Integer, db.ForeignKey("reason_for_stopping.id"), nullable=False
    )


class ReasonForStopping(db.Model):
    __tablename__ = "reason_for_stopping"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class ReasonForDiscard(db.Model):
    __tablename__ = "reason_for_discard"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class Unconformities(db.Model):
    __tablename__ = "unconformities"
    id = db.Column(db.Integer, primary_key=True)
    reason_for_discard_id = db.Column(
        db.Integer, db.ForeignKey("reason_for_discard.id"), nullable=False
    )
    amount = db.Column(db.Integer, nullable=False)
