from github import github import yaml

# credentials.yml contains username/repo and Personal Access Token
# load this data into a yaml object
privData = yaml.safe_load(open('lake0065_credentials.yml'))

# extract the user and token from the object
user = privData['creds']['pat1']['username']
token = privData['creds']['pat1']['token']

# using the access token
g = Github(token)
repo = g.get_repo(user)
