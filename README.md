# EARL-Data-Model-AppBuilder
The EARL Data Model Web Application Wrapper with Flask AppBuilder.  

Detailed instructions for installing this application can be found in this repository's Wiki at: https://github.com/DiamondMediaSolutions/EARL-Data-Model-AppBuilder/wiki


```
 class Visitor(Model):
            __tablename__ = 'visitor'
            id = Column(Integer, primary_key=True)
            campaign_id = Column(Integer, ForeignKey('campaign.id') nullable=False)
            store_id = Column(Integer, ForeignKey('store.id'), nullable=False)
            created_date = Column(DateTime, onupdate=datetime.now)
            ip = Column(String(15), index=True)
            user_agent = Column(String(255))
            job_number = Column(Integer, index=True)
            client_id = Column(String(255))
            appended = Column(Boolean, default=False)
            open_hash = Column(String(255))
            campaign_hash = Column(String(255))
            send_hash = Column(String(255))
            num_visits = Column(Integer)
            last_visit = Column(DateTime)
            raw_data = Column(Text)
            processed = Column(Boolean, default=False)
            campaign = relationship("Campaign")
            store = relationship("Store")

            def __init__(self, campaign_id, store_id, created_date, ip):
                self.campaign_id = campaign_id
                self.store_id = store_id
                self.created_date = created_date
                self.ip = ip

            def __repr__(self):
                return '{} {} {}'.format(
                    self.ip,
                    self.created_date,
                    self.campaign_id
                )


        class AppendedVisitor(Model):
            __tablename__ = 'appendedvisitor'
            id = Column(Integer, primary_key=True)
            visitor = Column(Integer, ForeignKey('visitor.id'))
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

            def __init__(self, visitor, created_date, first_name, last_name, email, cell_phone, address1, city, state, zip_code):
                self.visitor = visitor
                self.created_date = created_date
                self.first_name = first_name
                self.last_name = last_name
                self.email = email
                self.cell_phone = cell_phone
                self.address1 = address1
                self.city = city
                self.state = state
                self.zip_code = zip_code

            def __repr__(self):
                return '{} {} {}'.format(
                    self.first_name,
                    self.last_name,
                    self.created_date
                )


        class Lead(Model):
            __tablename__ = 'lead'
            id = Column(Integer, primary_key=True)
            appended_visitor_id = Column(Integer, ForeignKey('appendedvisitor.id'))
            appended_visitor = relationship("AppendedVisitor")
            created_date = Column(DateTime, onupdate=datetime.now)
            email_verified = Column(Boolean, default=False)
            lead_optout = Column(Boolean, default=False)

            def __init__(self, appended_visitor_id, created_date, email_verified, lead_output):
                self.appended_visitor_id = appended_visitor_id
                self.created_date = created_date
                self.email_verified = email_verified
                self.lead_optout = lead_optout

            def __repr__(self):
                return '{} {} {} {}'.format(
                    self.id,
                    self.appended_visitor,
                    self.email_verified,
                    self.lead_optout,
                )


        class Store(Model):
            __tablename__ = 'store'
            id = Column(Integer, primary_key=True)
            client_id = Column(String(255), unique=True)
            name = Column(String(255), unique=True)
            address1 = Column(String(255))
            address2 = Column(String(255))
            city = Column(String(255))
            state = Column(String(2))
            zip_code = Column(Integer)
            zip_4 = Column(Integer)
            status = Column(String(20), default='Active')
            adf_email = Column(String(255))
            notification_email = Column(String(255))
            reporting_email = Column(String(255))
            phone_number = Column(String(20))
            simplifi_company_id = Column(Integer)
            simplifi_client_id = Column(String(255))
            simplifi_name = Column(String(255))

            def __init__(self, client_id, name, address1, address2, city, state, zip_code, zip_4, status):
                self.client_id = client_id
                self.name = name
                self.address1 = address1
                self.address2 = address2
                self.city = city
                self.state = state
                self.zip_code = zip_code
                self.zip_4 = zip_4
                self.status = status

            def __repr__(self):
                return '{} {} {}'.format(
                    self.name,
                    self.client_id,
                    self.status
                )


        class CampaignType(Model):
            __tablename__ = 'campaigntype'
            id = Column(Integer, primary_key=True)
            name = Column(String(255))

            def __init__(self, name):
                self.name = name

            def __repr__(self):
                return '{}'.format(
                    self.name
                )


        class Campaign(Model):
            __tablename__ = 'campaign'
            id = Column(Integer, primary_key=True)
            store_id = Column(Integer, ForeignKey('store.id'))
            name = Column(String(255))
            job_number = Column(Integer, unique=True)
            created_date = Column(DateTime, onupdate=datetime.now)
            created_by = Column(Integer, ForeignKey('ab_user.id'))
            campaign_type = Column(Integer, ForeignKey('campaigntype.id'))
            options = Column(Text)
            description = Column(Text)
            funded = Column(Boolean, default=0)
            approved = Column(Boolean, default=0)
            approved_by = Column(Integer, ForeignKey('ab_user.id'))
            status = Column(String(255))
            objective = Column(Text)
            frequency = Column(String(255))
            start_date = Column(DateTime)
            end_date = Column(DateTime)
            radius = Column(Integer, default=50)
            store = relationship("Store")
            campaigntype = relationship("CampaignType")

            def __init__(self, store_id, name, job_number, created_date, created_by, campaign_type, options, description,
                         funded, approved, approved_by, status, objective, frequency, start_date, end_date, radius):
                self.store_id = store_id
                self.name = name
                self.job_number = job_number
                self.created_date = created_date
                self.created_by = created_by
                self.campaign_type = campaign_type
                self.options = options
                self.description = description
                self.funded = funded
                self.approved = approved
                self.approved_by = approved_by
                self.status = status
                self.objective = objective
                self.frequency = frequency
                self.start_date = start_date
                self.end_date = end_date
                self.radius = radius

            def __repr__(self):
                return '{} {} {}'.format(
                    self.name,
                    self.store_id,
                    self.status
                )



```
