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

from typing import TypeVar, List

SelfTicket = TypeVar("SelfTicket", bound="Ticket")

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

	user = relationship("User", back_populates="tickets", lazy=True)
	ticket_history = relationship("TicketHistory", back_populates="ticket", lazy=True)

	@classmethod
	def get(cls: SelfTicket, ticket_id: int) -> SelfTicket:
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
	def get_by_tn(cls: SelfTicket, tn: str) -> SelfTicket:
		"""Obtener un ticket por su tn.
		
		Parameters
		----------
		tn: str
			Número del ticket
		
		Returns
		-------
		Ticket
			Un objeto del tipo ticket
		"""
		return db.session.query(cls).filter_by(tn=tn).first()

	@classmethod
	def tickets_by_marca_in_title(cls: SelfTicket, marca=str) -> SelfTicket:
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
		return db.session.query(cls).filter(cls.title.ilike(f"%{marca}%")).all()

	@classmethod
	def tickets_by_queue_marca_date(cls: SelfTicket, queue_id: int, marca: str, start_date: str, end_date: str=None) -> List[SelfTicket]:
		"""Obtener los ticket de una cola en determinada fecha.
		
		Parameters
		----------
		queue_id: int
			ID de la cola.
		marca: str
			Frase referencial que este en el titulo.
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
				cls.title.ilike(f"%{marca}%"),
                cls.create_time>=f"{start_date} 00:00:00",
                cls.create_time<f"{end_date} 23:00:00").all()
	
	@classmethod
	def tickets_by_queue_date(cls: SelfTicket, queue_id: int, start_date: str, end_date: str=None) -> List[SelfTicket]:
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
		
	@classmethod
	def tickets_by_queue_user_date(cls: SelfTicket, queue_id: int, user_id: int, start_date: str, end_date: str=None) -> List[SelfTicket]:
		"""Obtener los ticket de una cola en determinada fecha.
		
		Parameters
		----------
		user_id: int
			ID del usuario.
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
				cls.user_id == user_id,
				cls.queue_id == queue_id,
                cls.create_time>=f"{start_date} 00:00:00",
                cls.create_time<f"{end_date} 23:00:00").all()
		
	@classmethod
	def tickets_by_user_date(cls: SelfTicket, user_id: int, start_date: str, end_date: str=None) -> List[SelfTicket]:
		"""Obtener los ticket de un usuario en determinada fecha.
		
		Parameters
		----------
		user_id: int
			ID del usuario.
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
				cls.user_id == user_id,
                cls.create_time>=f"{start_date} 00:00:00",
                cls.create_time<f"{end_date} 23:00:00").all()
		
	@classmethod
	def tickets_by_date(cls: SelfTicket, start_date: str, end_date: str=None) -> List[SelfTicket]:
		"""Obtener los ticket de una cola en determinada fecha.
		
		Parameters
		----------
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


SelfUser = TypeVar("SelfUser", bound="User")
class User(db.Base):
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
	def get(cls: SelfUser, user_id: int) -> SelfUser:
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
	def all(cls: SelfUser) -> List[SelfUser]:
		"""Obtener todos los usuarios
	
		Returns
		-------
		List[User]
			Una lista de objetos User
		"""
		return db.session.query(cls).all()

	@property
	def full_name(self):
		return f"{self.first_name} {self.last_name}"


SelfTicketHistory = TypeVar("SelfTicketHistory", bound="TicketHistory")
class TicketHistory(db.Base):
	__tablename__ = 'ticket_history'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	history_type_id = Column(Integer, ForeignKey("ticket_history_type.id"), nullable=False)
	ticket_id = Column(Integer, ForeignKey("ticket.id"), nullable=False)
	article_id = Column(Integer, nullable=True)
	type_id = Column(Integer, ForeignKey("ticket_type.id"), nullable=False)
	queue_id = Column(Integer, nullable=False)
	owner_id = Column(Integer, nullable=False)
	priority_id = Column(Integer, ForeignKey("ticket_priority.id"), nullable=False)
	state_id = Column(Integer, ForeignKey("ticket_state.id"), nullable=False)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	ticket = relationship("Ticket", back_populates="ticket_history", lazy=True)
	priority = relationship("TicketPriority", lazy=True)
	ticket_state = relationship("TicketState", lazy=True)
	ticket_type = relationship("TicketType", lazy=True)
	ticket_history_type = relationship("TicketHistoryType", lazy=True)


	@classmethod
	def get(cls: SelfTicketHistory, ticket_id: int) -> List[SelfTicketHistory]:
		"""Obtener el historial de un ticket por su ID
		
		Parameters
		----------
		ticket_id: int
			ID del ticket
		
		Returns
		-------
		List[TicketHistory]
			Un lista con objetos del tipo TicketHistory
		"""
		return db.session.query(cls).filter(cls.ticket_id == ticket_id).all()


SelfTicketPriority = TypeVar("SelfTicketPriority", bound="TicketPriority")
class TicketPriority(db.Base):
	__tablename__ = 'ticket_priority'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	valid_id = Column(Integer, nullable=False)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	@classmethod
	def get(cls: SelfTicketPriority, ticket_priority_id: int) -> SelfTicketPriority:
		"""Obtener la prioridad del ticket por su ID
		
		Parameters
		----------
		ticket_priority_id: int
			ID del ticket_priority
		
		Returns
		-------
		TicketPriority
			Un objeto del tipo TicketPriority
		"""
		return db.session.query(cls).get(ticket_priority_id)
	
	@classmethod
	def all(cls: SelfTicketPriority) -> List[SelfTicketPriority]:
		"""Obtener todos las prioridades del ticket
	
		Returns
		-------
		List[SelfTicketPriority]
			Una lista de objetos TicketPriority
		"""
		return db.session.query(cls).all()


SelfTicketStateType = TypeVar("SelfTicketStateType", bound="TicketStateType")
class TicketStateType(db.Base):
	__tablename__ = 'ticket_state_type'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	comments = Column(String, nullable=True)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	@classmethod
	def get(cls: SelfTicketStateType, ticket_state_type_id: int) -> SelfTicketStateType:
		"""Obtener el tipo del estado del ticket por su ID
		
		Parameters
		----------
		ticket_state_type_id: int
			ID del ticket_state_type_id
		
		Returns
		-------
		TicketStateType
			Un objeto del tipo TicketStateType
		"""
		return db.session.query(cls).get(ticket_state_type_id)
	
	@classmethod
	def all(cls: SelfTicketStateType) -> List[SelfTicketStateType]:
		"""Obtener todos los tipos de los estados del ticket
	
		Returns
		-------
		List[SelfTicketStateType]
			Una lista de objetos SelfTicketStateType
		"""
		return db.session.query(cls).all()


SelfTicketState = TypeVar("SelfTicketState", bound="TicketState")
class TicketState(db.Base):
	__tablename__ = 'ticket_state'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	comments = Column(String, nullable=True)
	type_id = Column(Integer, ForeignKey("ticket_state_type.id"), nullable=False)
	valid_id = Column(Integer, nullable=False)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	type_state = relationship("TicketStateType", lazy=True)

	@classmethod
	def get(cls: SelfTicketState, ticket_state_id: int) -> SelfTicketState:
		"""Obtener el estado del ticket por su ID
		
		Parameters
		----------
		ticket_priority_id: int
			ID del ticket_state_id
		
		Returns
		-------
		TicketState
			Un objeto del tipo TicketState
		"""
		return db.session.query(cls).get(ticket_state_id)
	
	@classmethod
	def all(cls: SelfTicketState) -> List[SelfTicketState]:
		"""Obtener todos los estados del ticket
	
		Returns
		-------
		List[SelfTicketState]
			Una lista de objetos SelfTicketState
		"""
		return db.session.query(cls).all()


SelfTicketType = TypeVar("SelfTicketType", bound="TicketType")
class TicketType(db.Base):
	__tablename__ = 'ticket_type'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	valid_id = Column(Integer, nullable=False)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	@classmethod
	def get(cls: SelfTicketType, ticket_type_id: int) -> SelfTicketType:
		"""Obtener el tipo del estado del ticket por su ID
		
		Parameters
		----------
		ticket_type_id: int
			ID del ticket_type_id
		
		Returns
		-------
		TicketType
			Un objeto del tipo TicketType
		"""
		return db.session.query(cls).get(ticket_type_id)
	
	@classmethod
	def all(cls: SelfTicketType) -> List[SelfTicketType]:
		"""Obtener todos los typos de los estados del ticket
	
		Returns
		-------
		List[SelfTicketType]
			Una lista de objetos SelfTicketType
		"""
		return db.session.query(cls).all()


SelfTicketHistoryType = TypeVar("SelfTicketHistoryType", bound="TicketHistoryType")
class TicketHistoryType(db.Base):
	__tablename__ = 'ticket_history_type'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable=False)
	comments = Column(String, nullable=True)
	valid_id = Column(Integer, nullable=False)
	create_time = Column(DateTime, nullable=False)
	create_by = Column(Integer, nullable=False)
	change_time = Column(DateTime, nullable=False)
	change_by = Column(Integer, nullable=False)

	@classmethod
	def get(cls: SelfTicketHistoryType, ticket_history_type_id: int) -> SelfTicketHistoryType:
		"""Obtener la historia del tipo del estado del ticket por su ID
		
		Parameters
		----------
		ticket_type_id: int
			ID del ticket_type_id
		
		Returns
		-------
		TicketHistoryType
			Un objeto del tipo TicketHistoryType
		"""
		return db.session.query(cls).get(ticket_history_type_id)
	
	@classmethod
	def all(cls: SelfTicketHistoryType) -> List[SelfTicketHistoryType]:
		"""Obtener todas las historias de los tipos de los estados del ticket
	
		Returns
		-------
		List[TicketHistoryType]
			Una lista de objetos TicketHistoryType
		"""
		return db.session.query(cls).all()
