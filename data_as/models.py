# -*- coding: utf-8 -*-

import db
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import desc
from sqlalchemy.orm import relationship


class Ticket(db.Base):
	__tablename__ = 'ticket'
	id = Column(Integer, primary_key=True)
	tn = Column(String, nullable=False)
	title = Column(String, nullable=True)
	queue_id = Column(Integer, nullable=False)
	ticket_lock_id = Column(Integer, nullable=False)
	type_id = Column(Integer, nullable=True)
	service_id = Column(Integer, nullable=True)
	sla_id = Column(Integer, nullable=True)
	user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
	responsible_user_id = Column(Integer, nullable=False)
	ticket_priority_id = Column(Integer, nullable=False)
	ticket_state_id = Column(Integer, nullable=False)
	customer_id = Column(String, nullable=True)
	customer_user_id = Column(String, nullable=True)
	timeout = Column(Integer, nullable=False)
	until_time = Column(Integer, nullable=False)
	escalation_time = Column(Integer, nullable=False)
	escalation_update_time = Column(Integer, nullable=False)
	escalation_response_time = Column(Integer, nullable=False)
	escalation_solution_time = Column(Integer, nullable=False)
	archive_flag = Column(Integer, default=0)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	user = relationship("Users", back_populates="tickets", lazy=True)
	ticket_history = relationship("TicketHistory", back_populates="ticket", lazy=True)

	@classmethod
	def get(cls, ticket_id: int):
		"""Obtener un ticket por su ID
		
		Parameters
		----------
		ticket_id: int
			ID del ticket
		
		Returns
		-------
		Ticket
			Un objeto del tipo Ticket
		"""
		return db.session.query(cls).get(ticket_id)
	
	@classmethod
	def get_by_tn(cls, tn: str):
		"""Obtener un ticket por su tn.
		
		Parameters
		----------
		tn: str
			Número del ticket
		
		Returns
		-------
		Ticket
			Un objeto de la del tipo ticket
		"""
		return db.session.query(cls).filter_by(tn=tn).first()

	@classmethod
	def tickets_by_offense(cls, offense_id=str):
		"""Obtener los tickets asociados al id de una ofensa de QRadar
		
		Parameters
		---------
		offense_id: str
			ID de la ofensa en QRadar
			
		Returns
		-------
		list[Ticket]
			Una lista de objetos tipo ticket
		"""
		return db.session.query(cls).filter(cls.title.like(f"%{offense_id}%")).all()

	@classmethod
	def tickets_by_date(cls, queue_id: int, start_date: str, end_date: str=None):
		"""Obtener los ticket de una cola en determinada fecha.
		
		Parameters
		----------
		queue_id: int
			ID de la cola.
		start_date: str
			Fecha de inicio en formato Y-M-D
		end_date: str
			Fecha de fin en formato Y-M-D
		
		Returns
		-------
		list[Ticket]
			Una lista de objetos Ticket
		"""
		if not end_date:
			end_date = datetime.today().strftime("%Y-%m-%d")

		return db.session.query(cls).filter(
				cls.queue_id == queue_id,
                cls.create_time>=f"{start_date} 00:00:00",
                cls.create_time<f"{end_date} 23:00:00").all()
	
	@property
	def last_history(self):
		""""Obtener el último registro del historial de un ticket
		
		Returns
		-------
		TicketHistory
			Un objeto del tipo TicketHistory
		"""
		return db.session.query(TicketHistory).join(Ticket).filter(
			TicketHistory.ticket_id == self.id
		).order_by(desc(TicketHistory.change_time)).first()

class Users(db.Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	login = Column(String, nullable=False)
	pw = Column(String, nullable=False)
	title = Column(String, nullable=True)
	first_name = Column(String, nullable=False)
	last_name = Column(String, nullable=False)
	valid_id = Column(Integer, nullable=False)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	tickets = relationship("Ticket", back_populates="user", lazy=True)

	@classmethod
	def get(cls, user_id: int):
		"""Obtener un usuario por su ID
		
		Parameters
		----------
		user_id: int
			ID del usuario
		
		Returns
		-------
		User
			Un objeto del tipo User
		"""
		return db.session.query(cls).get(user_id)
	
	@classmethod
	def all(cls):
		return db.session.query(cls).all()

	@property
	def full_name(self):
		return f"{self.first_name} {self.last_name}"

class TicketHistory(db.Base):
	__tablename__ = 'ticket_history'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	history_type_id = Column(Integer, nullable=False)
	ticket_id = Column(Integer, ForeignKey("ticket.id"), nullable=False)
	article_id = Column(Integer, nullable=True)
	type_id = Column(Integer, nullable=False)
	queue_id = Column(Integer, nullable=False)
	owner_id = Column(Integer, nullable=False)
	priority_id = Column(Integer, nullable=False)
	state_id = Column(Integer, nullable=False)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	ticket = relationship("Ticket", back_populates="ticket_history", lazy=True)

	