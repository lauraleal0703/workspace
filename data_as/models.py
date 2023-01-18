# -*- coding: utf-8 -*-

import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
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
	user_id = Column(Integer, nullable=False)
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