import yaml

with open("config.yml", 'r') as ymlfile:
	cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

telegram_token = cfg['telegram_token']