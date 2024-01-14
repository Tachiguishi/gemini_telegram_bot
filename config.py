import yaml

with open("config.yml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

telegram_token = cfg['telegram_token']
gemini_api_key = cfg['gemini_api_key']