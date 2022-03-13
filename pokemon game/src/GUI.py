import sys
from time import sleep

import pygame
from pygame import *
from pygame import gfxdraw
from GraphAlgo import GraphAlgo
from src import Pokemon
from serverData import serverData
import json

#get current screen size
def scale(data, minScreen, maxScreen, min_data, max_data):
    return ((data - min_data) / (max_data-min_data)) * (maxScreen - minScreen) + minScreen

def scaleX(data, minX, maxX):
    return scale(data, 50, screen.get_width() - 50, minX, maxX)

def scaleY(data, minY, maxY):
    return scale(data, 50, screen.get_height() - 50, minY, maxY)

#set deafult values
WIDTH, HEIGHT = 1080, 720


pygame.init()
screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)
#adding background music
# try:
#     pygame.mixer.init()
#     pygame.mixer.music.load("../data/patiah.mp3")
#     pygame.mixer.music.play(-1)
# except:
#     pass
#set background
bg = pygame.image.load("../data/pokemon background.jpg")
clock = pygame.time.Clock()
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 20, bold=True)
pygame.display.set_caption("POKEMON CHASE")
serverData = serverData()
graph_json = serverData.getGraph()
g = GraphAlgo()
g.load_graph_from_json(graph_json)
graph = g.get_graph()
center = g.centerPoint()
minX, maxX, minY, maxY = g.getMin()
pokemons_json = serverData.getPokemons()
g.load_pokemons_from_json(pokemons_json)
pikachu = pygame.image.load("../data/pikachu.png")
pikachu = pygame.transform.scale(pikachu, (25, 25))
bulbasaur = pygame.image.load("../data/bulbasaur.png")
bulbasaur = pygame.transform.scale(bulbasaur, (35, 35))
ash = pygame.image.load("../data/ash.png")
ash = pygame.transform.scale(ash, (30, 30))
#set all agents in there places near pokemons for the start position
for pokemon in graph.pokemons.values():
    if pokemon.type > 0:
        place: int = int(min(pokemon.edge))
    else:
        place: int = int(max(pokemon.edge))
    serverData.addAgent(place)
serverData.startGame()
#for calculate where is an agent
lastMove: float = float(serverData.getTime())
abc = 0
while serverData.isOnline() == 'true':
    #get new pokemons and agents info
    pokemons_json = serverData.getPokemons()
    g.load_pokemons_from_json(pokemons_json)
    agents_json = serverData.getAgents()
    g.load_agents_from_json(agents_json)
    #check if the game still runing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if button.collidepoint(mouse_pos):
                serverData.stopGame()
                print("Game over")
                print(gameDetails)
                sys.exit()

    bg = pygame.transform.scale(bg, (screen.get_width(), screen.get_height()))
    screen.blit(bg, (0, 0))
    stop = FONT.render('click to stop', True, Color(153, 56, 80))
    color_light = (170, 170, 170)
    button = stop.get_rect(center=(41, 61))
    #draw edges
    edges = graph.edges
    for n in edges.keys():
        src = graph.getNode(n[0])
        xSrc = scaleX(float(src[0]), minX, maxX)
        ySrc = scaleY(float(src[1]), minY, maxY)
        dest = graph.getNode(n[1])
        xDest = scaleX(float(dest[0]), minX, maxX)
        yDest = scaleY(float(dest[1]), minY, maxY)
        pygame.draw.line(screen, Color(100, 210, 255), (xSrc, ySrc + 1), (xDest, yDest + 1))
        pygame.draw.line(screen, Color(100, 210, 255), (xSrc, ySrc), (xDest, yDest))
    #draw nodes
    nodes = graph.nodes
    for n in nodes.keys():
        x = scaleX(float(nodes[n][0]), minX, maxX)
        y = scaleY(float(nodes[n][1]), minY, maxY)
        gfxdraw.aacircle(screen, int(x), int(y), 10, Color(255, 0, 0))
        FONT = pygame.font.SysFont('Arial', 15, bold=True)
        idDraw = FONT.render(str(n), True, Color(0, 255, 0))
        rect = idDraw.get_rect(center=(x, y))
        screen.blit(idDraw, rect)
    #draw pokemons
    for p in graph.pokemons:
        p.setFirst(False)
        x = scaleX(float(p.pos[0]), minX, maxX)
        y = scaleY(float(p.pos[1]), minY, maxY)
        if p.type < 0:
            screen.blit(pikachu, (x - 5, y - 10))
        else:
            screen.blit(bulbasaur, (x - 15, y - 10))
    #draw agnets
    for a in graph.agents.values():
        tup = a.pos.split(',')
        x = tup[0]
        y = tup[1]
        x = scaleX(float(x), minX, maxX)
        y = scaleY(float(y), minY, maxY)
        screen.blit(ash, (x - 15, y - 10))
    #print some game info
    info = serverData.getInfo()
    if (info == '' or info == False):
        continue
    info = json.loads(info)
    time = serverData.getTime()
    time = FONT.render(str("time left : " + time), True, Color(153, 56, 80))
    screen.blit(time, (5, 5))
    moves = str(info["GameServer"]["moves"])
    moves = FONT.render(str("moves : " + moves), True, Color(153, 56, 80))
    screen.blit(moves, (5, 20))
    score = str(info["GameServer"]["grade"])
    score = FONT.render(str("score : " + score), True, Color(153, 56, 80))
    screen.blit(score, (5, 35))
    pygame.draw.rect(screen, (100, 100, 100), button)
    screen.blit(stop, (5, 50))
    #update the frame
    display.update()
    clock.tick(60)

    #calculate which agent to allocate to which pokemon
    agentsDistance: {} = {}
    flag = 1
    pokemonCatch: Pokemon
    for agent in graph.agents.values():
        if agent.dest == -1:
            dist, path, pokemon = g.allocate_agent(agent)
            if dist == -1:
                continue
            nextEdge: str = "0"
            if float(dist) == 0.0:
                edge = pokemon.edge
                agent.pokeball = True
                if flag != 0:
                    pokemonCatch = pokemon
                    flag = 0
                if pokemon.type > 0:
                    nextEdge = str(max(edge[0], edge[1]))
                else:
                    nextEdge = str(min(edge[0], edge[1]))
            else:
                agent.pokeball = False
                nextEdge = str(path[1])
            serverData.setNextEdge(agent.id, nextEdge)
        else:
            nextEdge = agent.dest
        agentsDistance[agent.id] = g.distance_agent(agent, nextEdge)
    agentsDistance = dict(sorted(agentsDistance.items(), key=lambda item: item[1]))

    #calculate where is agent to know if it 'worth' to make a move call
    # currMove = float(client.time_to_end())
    # loopTime = (lastMove - currMove) / 100000
    # agentID = list(agentsDistance.keys())[0]
    # agentsDistance = list(agentsDistance.values())[0]
    # arrive = agentsDistance - loopTime
    # for agent in graph.agents.values():
    #     if agent.pokeball:
    #         pos = (graph.agents[agentID].pos).split(',')
    #         x = (abs(float(pos[0]) - float(pokemonCatch.pos[0]))) ** 2
    #         y = (abs(float(pos[1]) - float(pokemonCatch.pos[1]))) ** 2
    #         distance = (x + y) ** 0.5
    #         if distance < 0.01:
    #             client.move()
    # if arrive < 0.0001227448804736697:
    #     client.move()
    #     lastMove = currMove
    gameDetails = serverData.getInfo()
    serverData.move()
    # to not pass 10 call in every second
    pygame.time.delay(90)
print("Game over")
print(gameDetails)
sys.exit()






