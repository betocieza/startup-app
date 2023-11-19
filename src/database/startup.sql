
use startup;
CREATE TABLE factors
(
	factor_id            INTEGER PRIMARY KEY AUTO_INCREMENT,
	name                 VARCHAR(255) NULL,
	description          VARCHAR(255) NULL
);


CREATE TABLE models
(
	model_id             INTEGER PRIMARY KEY AUTO_INCREMENT,
	name                 VARCHAR(255) NULL,
	url                  VARCHAR(255) NULL	
);



CREATE TABLE predictions
(
	prediction_id        INTEGER PRIMARY KEY AUTO_INCREMENT,
	location             FLOAT NULL,
	age_startup          FLOAT NULL,
	size_startup         FLOAT NULL,
	count_profile_skill  FLOAT NULL,
	company_total_revenue FLOAT NULL,
	export_cti_products  FLOAT NULL,
	main_innovation_activities FLOAT NULL,
	investment_rd        FLOAT NULL,
	domestic_economic_enviroment FLOAT NULL,
	availability_skill_employees FLOAT NULL,
	access_finance       FLOAT NULL,
	cost_rd              FLOAT NULL,
	availability_infraestructure FLOAT NULL,
	innovative_enviroment FLOAT NULL,
	goverment_regulation FLOAT NULL,
	access_target_market FLOAT NULL,
	global_economic_enviroment FLOAT NULL,
	exchange_rates       FLOAT NULL,
	competitive_enviroment FLOAT NULL,
	access_export_market FLOAT NULL,
	prediction_result    INTEGER NULL,
	create_at            DATETIME NULL,
	startup_id           INTEGER NOT NULL
);



CREATE TABLE predictions_models
(
	prediction_id        INTEGER NOT NULL,
	model_id             INTEGER NOT NULL
);



ALTER TABLE predictions_models
ADD PRIMARY KEY (prediction_id);



CREATE TABLE startups
(
	startup_id           INTEGER PRIMARY KEY AUTO_INCREMENT,
	name                 VARCHAR(255) NULL,
	location             VARCHAR(255) NULL,
	age                  INTEGER NULL,
	industry             VARCHAR(255) NULL,
	founder_first_name   VARCHAR(255) NULL,
	founder_last_name    VARCHAR(255) NULL,
	gender               VARCHAR(30) NULL,
	formation            VARCHAR(100) NULL,
	user_id              INTEGER NOT NULL
 
);




CREATE TABLE users
(
	user_id              INTEGER PRIMARY KEY AUTO_INCREMENT,
	first_name           VARCHAR(255) NULL,
	last_name            VARCHAR(255) NULL,
	email                VARCHAR(255) NULL,
	username             VARCHAR(100) NULL,
	password             VARCHAR(255) NULL
 
);




ALTER TABLE predictions
ADD FOREIGN KEY R_2 (startup_id) REFERENCES startup (startup_id);



ALTER TABLE predictions_models
ADD FOREIGN KEY R_1 (prediction_id) REFERENCES predictions (prediction_id);



ALTER TABLE predictions_models
ADD FOREIGN KEY R_4 (model_id) REFERENCES models (model_id);



ALTER TABLE startup
ADD FOREIGN KEY R_5 (user_id) REFERENCES users (user_id);


select * from users;
select P.prediction_id, P.prediction_result, P.created_at, E.name as 'startups' from predictions P join startups E on P.startup_id = E.startup_id