class Startup():

    def __init__(self, startup_id, name, location, age, industry,founder_first_name, founder_last_name, gender, formation, user_id) -> None:
        self.startup_id = startup_id
        self.name = name
        self.location = location
        self.age = age
        self.industry = industry
        self.founder_first_name =founder_first_name
        self.founder_last_name =founder_last_name
        self.gender =gender
        self.formation =formation
        self.user_id = user_id


    def to_json(self):
        return {        
            'startup_id': self.startup_id,
            'name': self.name,
            'location':  self.location,
            'age':  self.age,
            'industry':  self.industry,
            'founder_first_name':  self.founder_first_name,
            'founder_last_name':  self.founder_last_name,
            'gender':  self.gender,
            'formation': self.formation,
            'user_id': self.user_id
        }