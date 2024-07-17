import math
import sys
import neat
import pygame
import imageio
import os

# Set the size of the screen
width = 1500
height = 800
generation = 0

class autonomouscar:
    def __init__(self):
        self.initialize()
    
    def initialize(self):
        self.surface = pygame.transform.scale(pygame.image.load("C:\\Users\\dknjy\\.anaconda\\autonomous\\Self-Driving Car\\GreenCarAsset.png"), (100, 100))
        self.rotate_surface = self.surface
        self.pos = [700, 650]
        self.distance = 0
        self.speed = 0
        self.angle = 0
        self.center = [self.pos[0] + 50, self.pos[1] + 50]
        self.radars = []
        self.radar_lines = []  # 레이더 선들을 저장할 리스트
        self.is_alive = True
        self.time_spent = 0

    
    def position(self, display):
        display.blit(self.rotate_surface, self.pos)
        if self.radar_lines:  # 레이더 선들이 비어 있지 않은지 확인
            for line in self.radar_lines:
                pygame.draw.line(display, (0, 255, 0), line[0], line[1], 1)  # 초록색 선을 그림
    
    def avoid_collision(self, track):
        self.is_alive = True
        for i in self.box_corner:
            if track.get_at((int(i[0]), int(i[1]))) == (255, 255, 255, 255):
                self.is_alive = False
                break
    
    def radardetection(self, degree, track):
        length = 0
        x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
        y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)
        
        while not track.get_at((x, y)) == (255, 255, 255, 255) and length < 300:
            length += 1
            x = int(self.center[0] + math.cos(math.radians(360 - (self.angle + degree))) * length)
            y = int(self.center[1] + math.sin(math.radians(360 - (self.angle + degree))) * length)
        
        distance = int(math.sqrt(math.pow(x - self.center[0], 2) + math.pow(y - self.center[1], 2)))
        self.radars.append([(x, y), distance])
        self.radar_lines.append((self.center, (x, y)))  # 선의 시작점과 끝점을 저장

    
    def positionupdate(self, map):
        self.speed = 10

        self.rotate_surface = pygame.transform.rotate(self.surface, self.angle)
        self.pos[0] += math.cos(math.radians(360 - self.angle)) * self.speed
        self.pos[0] = max(20, min(self.pos[0], width - 120))

        self.distance += self.speed
        self.time_spent += 1
        self.pos[1] += math.sin(math.radians(360 - self.angle)) * self.speed
        self.pos[1] = max(20, min(self.pos[1], height - 120))

        self.center = [int(self.pos[0]) + 50, int(self.pos[1]) + 50]
        length = 40
        self.box_corner = [
            [self.center[0] + math.cos(math.radians(360 - (self.angle + 30))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 30))) * length],
            [self.center[0] + math.cos(math.radians(360 - (self.angle + 150))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 150))) * length],
            [self.center[0] + math.cos(math.radians(360 - (self.angle + 210))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 210))) * length],
            [self.center[0] + math.cos(math.radians(360 - (self.angle + 330))) * length, self.center[1] + math.sin(math.radians(360 - (self.angle + 330))) * length]
        ]
        
        self.avoid_collision(map)
        self.radars.clear()
        self.radar_lines.clear()  # 이전 프레임의 레이더 선 데이터를 지움
        for j in range(-90, 120, 45):
            self.radardetection(j, map)
    
    def radar_data(self):
        radars = self.radars
        radarlist = [0, 0, 0, 0, 0]
        for a, b in enumerate(radars):
            radarlist[a] = int(b[1] / 35)
        return radarlist
    
    def add_reward(self):
        return self.distance / 50
    
    def check_alive(self):
        return self.is_alive

def run_autonomouscar(genomes, configuration):
    pygame.init()
    display = pygame.display.set_mode((width, height))
    cartrack = pygame.image.load("C:\\Users\\dknjy\\.anaconda\\autonomous\\Self-Driving Car\\cartrack.png")
    neuralnetworks = list()
    cars = list()
    frames = []
    frame_rate = 60
    clock = pygame.time.Clock()
    
    for i, j in genomes:
        neuralnetwork = neat.nn.FeedForwardNetwork.create(j, configuration)
        neuralnetworks.append(neuralnetwork)
        j.fitness = 0
        cars.append(autonomouscar())
    
    recording = False
    recording_name = "virtual_simulation.mp4"
    writer = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    recording = not recording
                    if recording:
                        frames = []
                        print("Recording started.")
                    else:
                        print("Recording stopped.")
                        imageio.mimsave(recording_name, frames, fps=frame_rate)
                        writer = imageio.get_writer(recording_name, fps=frame_rate)
        
        if recording:
            frames.append(pygame.surfarray.array3d(display))
        
        for k, car in enumerate(cars):
            result = neuralnetworks[k].activate(car.radar_data())
            a = result.index(max(result))
            if a == 0:
                car.angle += 10
            else:
                car.angle -= 10
        
        remaining = 0
        for m, car in enumerate(cars):
            if car.check_alive():
                remaining += 1
                car.positionupdate(cartrack)
                genomes[m][1].fitness += car.add_reward()
        
        if remaining == 0:
            break

        display.blit(cartrack, (0, 0))
        for y in cars:
            if y.check_alive():
                y.position(display)
        
        pygame.display.flip()
        clock.tick(frame_rate)

    if writer:
        writer.close()
        
def simulation():
    configurationfile = "C:\\Users\\dknjy\\.anaconda\\autonomous\\Self-Driving Car\\neat_config.txt"
    
    # neat.Config에 파일 경로 전달
    configuration = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, configurationfile)
    
    sample_population = neat.Population(configuration)
    sample_population.add_reporter(neat.StdOutReporter(True))
    statisticaldata = neat.StatisticsReporter()
    sample_population.add_reporter(statisticaldata)
    idealcar = sample_population.run(run_autonomouscar, 8)
    return idealcar

if __name__ == "__main__":
    simulation()
