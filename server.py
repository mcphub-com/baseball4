import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/sparior/api/baseball4'

mcp = FastMCP('baseball4')

@mcp.tool()
def v1_schedule(date: Annotated[Union[str, None], Field(description='Enter a date: YYYY-MM-DD')] = None) -> dict: 
    '''Baseball (MLB) schedule'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/schedule'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'date': date,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_leagues() -> dict: 
    '''Get baseball league information.'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/leagues'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_seasons(seasonId: Annotated[Union[str, None], Field(description='Enter a season year, ex: 2010')] = None) -> dict: 
    '''Baseball (MLB) seasons'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/seasons'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'seasonId': seasonId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_venues() -> dict: 
    '''Get Baseball (MLB) venues'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/venues'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_teams(teamId: Annotated[Union[str, None], Field(description='Enter an optional teamId to get information only for that team.')] = None) -> dict: 
    '''Get all Baseball (MLB) teams in the league.'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/teams'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamId': teamId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_teams_roster(teamIds: Annotated[Union[str, None], Field(description='Enter a team ID - which can be found in the Teams endpoint')] = None) -> dict: 
    '''Query Baseball (MLB) team roster by team ID'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/teams-roster'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamIds': teamIds,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_teams_history(teamIds: Annotated[Union[str, None], Field(description='Enter a team ID - which can be found in the Team endpoint')] = None) -> dict: 
    '''Query Baseball (MLB) team history by ID'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/teams-history'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamIds': teamIds,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_teams_personnel(teamIds: Annotated[Union[str, None], Field(description='Enter a team ID - which can be found in the Teams endpoint')] = None) -> dict: 
    '''Get Baseball (MLB) team history by team ID'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/teams-personnel'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamIds': teamIds,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_teams_affiliates(teamIds: Annotated[Union[str, None], Field(description='Enter a team ID - which can be found in the Teams endpoint')] = None) -> dict: 
    '''Get Baseball (MLB) team affiliates by team ID'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/teams-affiliates'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamIds': teamIds,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_teams_coaches(teamIds: Annotated[Union[str, None], Field(description='Enter a team ID - which can be found in the Teams endpoint')] = None) -> dict: 
    '''Get Baseball (MLB) team coaches by team ID'''
    url = 'https://baseball4.p.rapidapi.com/v1/mlb/teams-coaches'
    headers = {'x-rapidapi-host': 'baseball4.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'teamIds': teamIds,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
