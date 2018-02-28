from datetime import datetime
from flask import Markup, url_for
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
from sqlalchemy.orm import relationship

# Define application models


class Visitor(Model):
    __tablename__ = 'visitors'
    id = Column(Integer, primary_key=True)
    campaign_id = Column(Integer, ForeignKey('campaigns.id'), nullable=False)
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
    created_date = Column(DateTime, default=datetime.now)
    ip = Column(String(15), nullable=False, index=True)
    user_agent = Column(String(255))
    job_number = Column(Integer, nullable=False)
    client_id = Column(String(255), nullable=False)
    appended = Column(Boolean, default=False)
    open_hash = Column(String(255))
    campaign_hash = Column(String(255))
    send_hash = Column(String(255))
    num_visits = Column(Integer)
    last_visit = Column(DateTime, default=datetime.now)
    raw_data = Column(Text)
    processed = Column(Boolean, default=False)
    campaign = relationship("Campaign")
    store = relationship("Store")
    country_name = Column(String(255))
    city = Column(String(255))
    time_zone = Column(String(50))
    longitude = Column(String(50))
    latitude = Column(String(50))
    metro_code = Column(String(10))
    country_code = Column(String(2), nullable=False, default='NOTSET')
    country_code3 = Column(String(3))
    dma_code = Column(String(3))
    area_code = Column(String(3))
    postal_code = Column(String(5))
    region = Column(String(50))
    region_name = Column(String(255))
    traffic_type = Column(String(255))
    retry_counter = Column(Integer)
    last_retry = Column(DateTime)
    status = Column(String(10))
    locked = Column(Boolean, default=0)

    def __repr__(self):
        return 'From {} on {} for {}'.format(
            self.ip,
            self.created_date,
            self.campaign
        )

    def get_geoip_data(self):
        return '{} {} {} {} {}'.format(
            self.country_code,
            self.city,
            self.region,
            self.postal_code,
            self.traffic_type
        )


class AppendedVisitor(Model):
    __tablename__ = 'appendedvisitors'
    id = Column(Integer, primary_key=True)
    visitor = Column(Integer, ForeignKey('visitors.id'))
    visitor_relation = relationship("Visitor")
    created_date = Column(DateTime, onupdate=datetime.now)
    first_name = Column(String(255))
    last_name = Column(String(255))
    email = Column(String(255))
    home_phone = Column(String(15))
    cell_phone = Column(String(15))
    address1 = Column(String(255))
    address2 = Column(String(255))
    city = Column(String(255))
    state = Column(String(2))
    zip_code = Column(String(5))
    zip_4 = Column(Integer)
    credit_range = Column(String(50))
    car_year = Column(Integer)
    car_make = Column(String(255))
    car_model = Column(String(255))
    processed = Column(Boolean, default=False)
    ppm_type = Column(String(10))
    ppm_indicator = Column(String(10))
    ppm_segment = Column(String(50))

    def __repr__(self):
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )


class Lead(Model):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True)
    appended_visitor_id = Column(Integer, ForeignKey('appendedvisitors.id'), nullable=False)
    appended_visitor = relationship("AppendedVisitor")
    created_date = Column(DateTime, onupdate=datetime.now)
    email_verified = Column(Boolean, default=False)
    lead_optout = Column(Boolean, default=False)
    processed = Column(Boolean, default=False)
    followup_email = Column(Boolean, default=False)
    followup_voicemail = Column(Boolean, default=False)
    followup_print = Column(Boolean, default=False)
    email_receipt_id = Column(String(255))
    sent_to_dealer = Column(Boolean, default=False)
    email_validation_message = Column(String(50))
    sent_adf = Column(Boolean, default=False)
    adf_email_receipt_id = Column(String(255))
    adf_email_validation_message = Column(String(50))

    def __repr__(self):
        return '{}'.format(
            self.id
        )

    def get_link(self):
        return Markup(
            '<a href="' + url_for('AppendedVisitorModelView.show',
                                  pk=self.appended_visitor_id) + '">Link to Appended Visitor</a>')


class Store(Model):
    __tablename__ = 'stores'
    id = Column(Integer, primary_key=True)
    client_id = Column(String(255), unique=True, nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    address1 = Column(String(255), nullable=False)
    address2 = Column(String(255))
    city = Column(String(255), nullable=False)
    state = Column(String(2), nullable=False)
    zip_code = Column(Integer, nullable=False)
    zip_4 = Column(Integer)
    status = Column(String(20), default='Active', nullable=False)
    adf_email = Column(String(255))
    notification_email = Column(String(255), nullable=False)
    reporting_email = Column(String(255), nullable=False)
    phone_number = Column(String(20), nullable=False)
    simplifi_company_id = Column(Integer)
    simplifi_client_id = Column(String(255))
    simplifi_name = Column(String(255))

    def __repr__(self):
        return '{}'.format(
            self.name
        )


class CampaignType(Model):
    __tablename__ = 'campaigntypes'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return '{}'.format(
            self.name
        )


class Campaign(Model):
    __tablename__ = 'campaigns'
    id = Column(Integer, primary_key=True)
    store_id = Column(Integer, ForeignKey('stores.id'), nullable=False)
    store = relationship("Store")
    name = Column(String(255), nullable=False)
    job_number = Column(Integer, unique=True, nullable=False)
    created_date = Column(DateTime, default=datetime.now)
    created_by = Column(Integer, ForeignKey('ab_user.id'))
    type = Column(Integer, ForeignKey('campaigntypes.id'), nullable=False)
    campaign_type = relationship("CampaignType")
    options = Column(Text)
    description = Column(Text, nullable=False)
    funded = Column(Boolean, default=0)
    approved = Column(Boolean, default=0)
    approved_by = Column(Integer, ForeignKey('ab_user.id'))
    status = Column(String(255), nullable=False, default='INACTIVE')
    objective = Column(Text)
    frequency = Column(String(255))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    radius = Column(Integer, default=50, nullable=False)
    pixeltrackers_id = Column(Integer, ForeignKey('pixeltrackers.id'), nullable=False)
    pixeltracker = relationship("PixelTracker")
    client_id = Column(String(20), nullable=False)
    rvm_campaign_id = Column(Integer, unique=True, nullable=True, default=0)
    rvm_send_count = Column(Integer, default=0)
    rvm_limit = Column(Integer, nullable=False, default=10000)

    def __repr__(self):
        return '{}'.format(
            self.name
        )


class PixelTracker(Model):
    __tablename__ = 'pixeltrackers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    ip_addr = Column(String(15), unique=True, nullable=False)
    fqdn = Column(String(255), unique=True, nullable=False)
    capacity = Column(Integer, default=200, nullable=False)
    total_campaigns = Column(Integer)
    active = Column(Boolean, default=1)

    def __repr__(self):
        return '{}'.format(
            self.name
        )
