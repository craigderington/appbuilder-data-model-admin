from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction
from markupsafe import Markup, escape
from werkzeug.security import generate_password_hash
from app import appbuilder, db
from .models import CampaignType, Campaign, Store, Visitor, AppendedVisitor, \
    Lead, PixelTracker, DealerUser


class CampaignModelView(ModelView):
    datamodel = SQLAInterface(Campaign)
    list_columns = ['store', 'name', 'created_date', 'job_number', 'description', 'campaign_type', 'pixeltracker']
    base_order = ('created_date', 'desc')
    show_fieldsets = [
        ('Campaign Details',
            {'fields': ['store', 'campaign_type', 'name', 'start_date', 'end_date', 'client_id',
                        'created_date', 'job_number', 'description', 'pixeltracker',
                        'rvm_campaign_id', 'rvm_send_count', 'rvm_limit'], 'expanded': True}),
    ]

    add_fieldsets = [
        ('Campaign Details',
            {'fields': ['store', 'campaign_type', 'name', 'start_date', 'end_date', 'client_id',
                        'created_date', 'job_number', 'description', 'radius', 'pixeltracker',
                        'rvm_campaign_id', 'rvm_send_count', 'rvm_limit'], 'expanded': True}),
    ]

    edit_fieldsets = [
        ('Campaign Details',
            {'fields': ['store', 'campaign_type', 'name', 'start_date', 'end_date', 'client_id',
                        'created_date', 'job_number', 'description', 'pixeltracker',
                        'rvm_campaign_id', 'rvm_send_count', 'rvm_limit'], 'expanded': True}),
    ]


class CampaignTypeModelView(ModelView):
    datamodel = SQLAInterface(CampaignType)
    list_columns = ['name']
    base_order = ('name', 'asc')
    show_fieldsets = [
        ('Campaign Type Details',
         {'fields': ['name'], 'expanded': True}),
    ]
    add_fieldsets = [
        ('Campaign Type Details',
         {'fields': ['name'], 'expanded': True}),
    ]
    edit_fieldsets = [
        ('Campaign Type Details',
         {'fields': ['name'], 'expanded': True}),
    ]


class StoreModelView(ModelView):
    datamodel = SQLAInterface(Store)
    list_columns = ['client_id', 'name', 'address1', 'address2', 'city', 'state', 'zip_code', 'zip_4',
                    'status', 'phone_number']
    base_order = ('name', 'asc')
    show_fieldsets = [
        ('Store Information',
         {'fields': ['name', 'address1', 'address2', 'city', 'state', 'zip_code', 'zip_4', 'status',
                     'phone_number', 'reporting_email', 'notification_email', 'adf_email', ],
          'expanded': True}),
        ('SimpliFi Details',
         {'fields': ['simplifi_company_id', 'simplifi_client_id', 'simplifi_name'],
          'expanded': True}),
    ]
    add_fieldsets = [
        ('Store Information',
         {'fields': ['client_id', 'name', 'address1', 'address2', 'city', 'state', 'zip_code',
                     'zip_4', 'status', 'phone_number', 'reporting_email', 'notification_email', 'adf_email', ],
          'expanded': True}),
        ('SimpliFi Details',
         {'fields': ['simplifi_company_id', 'simplifi_client_id', 'simplifi_name'],
          'expanded': False}),
    ]
    edit_fieldsets = [
        ('Store Information',
         {'fields': ['client_id', 'name', 'address1', 'address2', 'city', 'state', 'zip_code',
                     'zip_4', 'status', 'phone_number', 'reporting_email', 'notification_email', 'adf_email', ],
          'expanded': True}),
        ('SimpliFi Details',
         {'fields': ['simplifi_company_id', 'simplifi_client_id', 'simplifi_name'],
          'expanded': False}),
    ]


class VisitorModelView(ModelView):
    datamodel = SQLAInterface(Visitor)
    list_columns = ['processed', 'store', 'campaign', 'job_number', 'client_id', 'created_date',
                    'ip', 'appended', 'num_visits', ]
    base_order = ('created_date', 'desc')
    show_fieldsets = [
        ('Visitor Info',
         {'fields': ['job_number', 'created_date', 'ip', 'appended', 'client_id', 'num_visits',
                     'processed', 'store', 'campaign'], 'expanded': True}),
        ('Visitor Details',
         {'fields': ['send_hash', 'open_hash', 'campaign_hash', 'raw_data', 'user_agent'],
          'expanded': False}),
        ('GeoIP',
         {'fields': ['country_code', 'city', 'region', 'postal_code', 'country_code', 'time_zone',
                     'area_code', 'dma_code', 'traffic_type', 'latitude', 'longitude'], 'expanded': False}),
    ]
    add_fieldsets = [
        ('Visitor Info',
         {'fields': ['store', 'campaign', 'job_number', 'created_date', 'ip', 'appended', 'client_id', 'num_visits',
                     'processed'], 'expanded': True}),
        ('Visitor Details',
         {'fields': ['user_agent', 'send_hash', 'open_hash', 'campaign_hash', 'raw_data', 'appended', 'user_agent'],
          'expanded': False}),
    ]
    edit_fieldsets = [
        ('Visitor Info',
         {'fields': ['store', 'campaign', 'job_number', 'created_date', 'ip', 'appended', 'client_id', 'num_visits',
                     'processed'], 'expanded': True}),
        ('Visitor Details',
         {'fields': ['user_agent', 'send_hash', 'open_hash', 'campaign_hash', 'raw_data', 'appended'],
          'expanded': False}),
    ]


class AppendedVisitorModelView(ModelView):
    datamodel = SQLAInterface(AppendedVisitor)
    list_columns = ['first_name', 'last_name', 'created_date', 'email', 'cell_phone', 'city', 'state', 'zip_code']
    base_order = ('last_name', 'asc')
    show_fieldsets = [
        ('Appended Visitor Info',
         {'fields': ['visitor_relation', 'first_name', 'last_name', 'created_date', 'email', 'cell_phone'],
          'expanded': True}),
        ('Appended Visitor Details',
         {'fields': ['address1', 'address2', 'city', 'state', 'zip_code', 'zip_4'],
          'expanded': True}),
        ('Vehicle Data',
         {'fields': ['credit_range', 'car_year', 'car_make', 'car_model'],
          'expanded': True}),
    ]
    add_fieldsets = [
        ('Appended Visitor Info',
         {'fields': ['visitor_relation', 'first_name', 'last_name', 'created_date', 'email', 'cell_phone'],
          'expanded': True}),
        ('Appended Visitor Details',
         {'fields': ['address1', 'address2', 'city', 'state', 'zip_code', 'zip_4'],
          'expanded': True}),
    ]
    edit_fieldsets = [
        ('Appended Visitor Info',
         {'fields': ['visitor_relation', 'first_name', 'last_name', 'created_date', 'email', 'cell_phone'],
          'expanded': True}),
        ('Appended Visitor Details',
         {'fields': ['address1', 'address2', 'city', 'state', 'zip_code', 'zip_4'],
          'expanded': True}),
        ('Vehicle Data',
         {'fields': ['credit_range', 'car_year', 'car_make', 'car_model'],
          'expanded': True}),
    ]


class LeadModelView(ModelView):

    datamodel = SQLAInterface(Lead)
    list_columns = ['appended_visitor', 'created_date', 'sent_to_dealer', 'email_verified', 'processed', 'lead_optout',
                    'followup_email']
    base_order = ('created_date', 'desc', )
    show_fieldsets = [
        ('Lead Details',
         {'fields': ['appended_visitor', 'appended_visitor_id', 'get_link', 'created_date', 'email_verified',
                     'processed', 'lead_optout'], 'expanded': True}),
        ('Lead Follow Up',
         {'fields': ['sent_to_dealer', 'sent_adf', 'followup_email', 'followup_voicemail', 'followup_print'],
          'expanded': True}),
        ('Lead Receipts',
         {'fields': ['email_receipt_id', 'email_validation_message', 'adf_email_receipt_id',
                     'adf_email_validation_message'], 'expanded': False}),
    ]


class DealerUserView(ModelView):

    def process_form(self, form, is_created):
        if form.password.data:
            form.password.data = generate_password_hash(form.password.data)

    datamodel = SQLAInterface(DealerUser)
    list_columns = ['first_name', 'last_name', 'username', 'active', 'store_name']
    search_columns = ['store_name', 'username', 'first_name', 'last_name', 'last_login']
    show_fieldsets = [
        ('Dealer User Info:',
         {'fields': ['id', 'store_name', 'first_name', 'last_name', 'username', 'email', 'last_login', 'active'],
          'expanded': True}),
    ]
    add_fieldsets = [
        ('New Dealer User:',
         {'fields': ['store_name', 'first_name', 'last_name', 'username', 'email', 'password'],
          'expanded': True}),
    ]
    edit_fieldsets = [
        ('Modify Dealer User:',
         {'fields': ['store_name', 'first_name', 'last_name', 'username', 'email', 'password', 'last_login'],
          'expanded': True}),
    ]


class PixelTrackerModelView(ModelView):
    datamodel = SQLAInterface(PixelTracker)
    list_columns = ['name', 'ip_addr', 'fqdn', 'active']
    base_order = ('name', 'asc')
    show_fieldsets = [
        ('Pixel Tracker Details',
         {'fields': ['name', 'ip_addr', 'fqdn', 'capacity', 'total_campaigns', 'active'], 'expanded': True}),
    ]
    add_fieldsets = []
    edit_fieldsets = []


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 404


@appbuilder.app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html', base_template=appbuilder.base_template, appbuilder=appbuilder), 500


db.create_all()
appbuilder.add_view(CampaignModelView, "Campaign View", icon="fa-th-list", category="Campaigns",
                    category_icon='fa-th-list')
appbuilder.add_view(CampaignTypeModelView, "Campaign Types View", icon="fa-th-large", category="Campaigns",
                    category_icon='fa-th-list')
appbuilder.add_view(StoreModelView, "Store View", icon="fa-plus-square", category="Stores",
                    category_icon='fa-plus-square')
appbuilder.add_view(DealerUserView, "Dealer Users", icon="fa-user-circle-o", category="Stores",
                    category_icon="fa-secret")
appbuilder.add_view(VisitorModelView, "Visitor View", icon="fa-user", category="Visitor Data",
                    category_icon='fa-user')
appbuilder.add_view(AppendedVisitorModelView, "Appended Visitor View", icon="fa-user-plus", category="Visitor Data",
                    category_icon='fa-user-plus')
appbuilder.add_view(LeadModelView, "Lead View", icon="fa-address-card-o", category="Visitor Data",
                    category_icon='fa-address-card-o')
appbuilder.add_view(PixelTrackerModelView, "Pixel Tracker View", icon="fa-globe", category="Campaigns",
                    category_icon='fa-globe')


