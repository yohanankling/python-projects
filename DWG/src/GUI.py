import pygame
from src import DiGraph
from pygame import Color, display, gfxdraw

WIDTH, HEIGHT = 800, 600
class GUI:
    def __init__(self, graph: DiGraph):
        self.graph = graph
        pygame.init()
        screen = display.set_mode((WIDTH, HEIGHT))
        while (True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            screen.fill(Color(15, 100, 100))
            self.drawNodes(screen)
            self.drawEdges(screen)


    def drawNodes(self, screen):
        minX, maxX, minY, maxY = self.findMin()
        nodes = self.graph.get_all_v()
        for n in nodes.keys():
            x = self.scaleX(float(nodes[n][0]), minX, maxX)
            y = self.scaleY(float(nodes[n][1]), minY, maxY)
            gfxdraw.aacircle(screen, int(x), int(y), 10, Color(255, 255, 5))
            FONT = pygame.font.SysFont('Arial', 15, bold=True)
            idDraw = FONT.render(str(n), True, Color(255, 255, 255))
            rect = idDraw.get_rect(center=(x, y))
            screen.blit(idDraw, rect)

    def drawEdges(self, screen):
        minX, maxX, minY, maxY = self.findMin()
        edges = self.graph.edges
        for n in edges.keys():
            src = self.graph.getNode(n[0])
            xSrc = self.scaleX(float(src[0]), minX, maxX)
            ySrc = self.scaleY(float(src[1]), minY, maxY)
            dest = self.graph.getNode(n[1])
            xDest = self.scaleX(float(dest[0]), minX, maxX)
            yDest = self.scaleY(float(dest[1]), minY, maxY)
            pygame.draw.line(screen, Color(255, 0, 0), (xSrc, ySrc), (xDest, yDest))

        display.update()

    def findMin(self):
        dict = self.graph.get_all_v()
        maxX = float('-inf')
        maxY = float('-inf')
        minX = float('inf')
        minY = float('inf')
        for n in dict.values():
            if float(n[0]) > maxX:
                maxX = float(n[0])
            if float(n[1]) > maxY:
                maxY = float(n[1])
            if float(n[0]) < minX:
                minX = float(n[0])
            if float(n[1]) < minY:
                minY = float(n[1])
        return minX, maxX, minY, maxY

    def scale(self, data, minScreen, maxScreen, min_data, max_data):
        return ((data - min_data) / (max_data-min_data)) * (maxScreen - minScreen) + minScreen

    def scaleX(self, data, minX, maxX):
        return self.scale(data, 50, WIDTH - 50, minX, maxX)

    def scaleY(self, data, minY, maxY):
        return self.scale(data, 50, HEIGHT - 50, minY, maxY)


