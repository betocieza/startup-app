class Prediction():

    def __init__(self, prediction_id, location, age_startup, size_startup,
                 count_profile_skill, company_total_revenue, export_cti_products,
                 main_innovation_activities, investment_rd,domestic_economic_enviroment,
                availability_skill_employees, access_finance, cost_rd,
                availability_infraestructure,innovative_enviroment,
                goverment_regulation, access_target_market,
                global_economic_enviroment,exchange_rates,
                competitive_enviroment, access_export_market,
                prediction_result, created_at, startup_id   ) -> None:
        
        self.prediction_id =prediction_id       
        self.location = location
        self.age_startup = age_startup
        self.size_startup = size_startup
        self.count_profile_skill =count_profile_skill
        self.company_total_revenue =company_total_revenue
        self.export_cti_products =export_cti_products
        self.main_innovation_activities =main_innovation_activities
        self.investment_rd = investment_rd
        self.domestic_economic_enviroment = domestic_economic_enviroment
        self.availability_skill_employees = availability_skill_employees
        self.access_finance = access_finance
        self.cost_rd = cost_rd
        self.availability_infraestructure= availability_infraestructure
        self.innovative_enviroment=innovative_enviroment
        self.goverment_regulation=goverment_regulation
        self.access_target_market=access_target_market
        self.global_economic_enviroment=global_economic_enviroment
        self.exchange_rates=exchange_rates
        self.competitive_enviroment= competitive_enviroment
        self.access_export_market=access_export_market

        self.prediction_result=prediction_result
        self.created_at=created_at
        self.startup_id=startup_id

    def to_json(self):
        return {        
            'prediction_id': self.prediction_id,           
            'location':  self.location,
            'age_startup':  self.age_startup,
            'size_startup':  self.size_startup,
            'count_profile_skill':  self.count_profile_skill,
            'company_total_revenue':  self.company_total_revenue,
            'export_cti_products':  self.export_cti_products,
            'main_innovation_activities': self.main_innovation_activities,
            'investment_rd': self.investment_rd,
            'domestic_economic_enviroment': self.domestic_economic_enviroment,
            'availability_skill_employees': self.availability_skill_employees,
            'access_finance' : self.access_finance,
            'cost_rd' : self.cost_rd,
            'availability_infraestructure': self.availability_infraestructure,
            'innovative_enviroment':self.innovative_enviroment,
            'goverment_regulation':self.goverment_regulation,
            'access_target_market':self.access_target_market,
            'global_economic_enviroment':self.global_economic_enviroment,
            'exchange_rates':self.exchange_rates,
            'competitive_enviroment': self.competitive_enviroment,
            'access_export_market':self.access_export_market,
            
            'prediction_result':self.prediction_result,
            'created_at':self.created_at,
            'startup_id':self.startup_id
        }

class PredictionResult():
    def __init__(self, prediction_id, prediction_result, created_at, startup_id,name  ) -> None:
        
        self.prediction_id =prediction_id       
        self.prediction_result=prediction_result
        self.created_at=created_at
        self.startup_id=startup_id
        self.name=name


    def to_json(self):            
        return {        
            'prediction_id': self.prediction_id,   
            'prediction_result':self.prediction_result,
            'created_at':self.created_at,
            'startup_id':self.startup_id,
            'name':self.name
            
        }
    
