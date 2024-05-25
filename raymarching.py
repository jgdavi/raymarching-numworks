"""
raymarching - jgdavid

Raymarching for Numworks
https://github.com/jgdavi/raymarching-numworks

Non-exhaustive list of resources that have helped me:
- https://piped.video/watch?v=Ff0jJyyiVyw
- https://www.mathcentre.ac.uk/resources/uploaded/mc-ty-scalarprod-2009-1.pdf
- https://piped.video/watch?v=hUaYxqkrfjA
and various Reddit posts or Wikipedia articles.

Thorough explanation in the README
"""
import math
import turtle as t

SCREEN_RES = (100, 100) # max 320, 222

MAX_ITER = 35
MARCHING_BOUNDARY = 3

class RayMarchingRenderer:
    def __init__(self, screen_res=SCREEN_RES, max_iter=MAX_ITER, marching_boundary=20, detection_threshold=0.01):
        self.screen_res = screen_res
        self.max_iter = max_iter
        self.marching_boundary = marching_boundary
        self.detection_threshold = detection_threshold
        self.spheres = [
            [0.7, 1.2, 3.7, 0.5],
            [-0.4, 0.2, 2.4, 0.5]
        ]
        self.light_pos = [-3, 2, -2]
        self.colors = {
            'red': 39,
            'green': 150,
            'blue': 200
        }
        self.setup_turtle()

    def setup_turtle(self):
        t.hideturtle()
        t.penup()
        t.circle(1)
        t.speed(10)
        t.goto(-150, -20)
        t.write("Ray marching is a technique\nused in computer graphics\nto render 3D scenes\nby simulating light behavior.\n\nVersion 1.0 jgdavid 206")
        t.pendown()
        t.showturtle()

    def raymarch(self, ray_origin, ray_direction):
        ray_distance = 0
        for _ in range(self.max_iter):
            p = [sum(x) for x in zip(ray_origin, [ray_direction[i] * ray_distance for i in range(3)])]
            closest_surface_distance = self.distance_to_surfaces(p)
            ray_distance += closest_surface_distance

            if ray_distance >= self.marching_boundary or closest_surface_distance <= self.detection_threshold:
                break
        return ray_distance

    def surface_normal(self, p):
        d = self.distance_to_surfaces(p)
        e = [0.005, 0]
        sn = [
            d - self.distance_to_surfaces([p[0] - e[0], p[1] - e[1], p[2] - e[1]]),
            d - self.distance_to_surfaces([p[0] - e[1], p[1] - e[0], p[2] - e[1]]),
            d - self.distance_to_surfaces([p[0] - e[1], p[1] - e[1], p[2] - e[0]])
        ]
        return self.normalize(sn)

    def distance_to_surfaces(self, point):
        sphere_distances = [self.distance(point, sphere) - sphere[3] for sphere in self.spheres]
        plane_distance = point[1] + 0.4
        return min(sphere_distances + [plane_distance])

    def calculate_lighting(self, p):
        light_direction = self.normalize([self.light_pos[i] - p[i] for i in range(3)])
        sn = self.surface_normal(p)
        dot_product = sum(x * y for x, y in zip(light_direction, sn))
        diffused_light = max(0, min(dot_product, 1))

        d = self.raymarch([p[0] + sn[0] * self.detection_threshold * 2, p[1] + sn[1] * self.detection_threshold * 2, p[2] + sn[2] * self.detection_threshold * 2], light_direction)
        if d < self.distance(self.light_pos, p):
            diffused_light *= 0.1
        return diffused_light

    def distance(self, o, p):
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(o, p)))

    def normalize(self, vector):
        length = math.sqrt(sum(x ** 2 for x in vector))
        return [x / length for x in vector]

    def draw(self, x, y):
        col = [0, 0, 0]
        uv = [(x - self.screen_res[0] / 2) / self.screen_res[1], (y - self.screen_res[1] / 2) / self.screen_res[1]]
        ray_origin = [0, 0.5, 0]
        ray_direction = self.normalize([uv[0], uv[1], 1])
        d = self.raymarch(ray_origin, ray_direction)
        p = [ray_origin[i] + ray_direction[i] * d for i in range(3)]
        light = self.calculate_lighting(p)
        col = [int(light * self.colors[color]) for color in ['red', 'green', 'blue']]
        return col

    def render(self):
        for y in range(self.screen_res[1]):
            for x in range(self.screen_res[0]):
                if x in [99, 0]:
                    t.penup()
                    t.goto(x - 160, -y + 111)
                    t.pendown()
                t.color(self.draw(x, self.screen_res[1] - y))
                t.goto(x - 160, -y + 111)

def done():
    t.penup()
    t.pensize(5)
    t.color(0, 255, 0)
    t.goto(85, 13)
    t.pendown()
    t.circle(40)
    t.penup()
    t.goto(60, 59)
    t.pendown()
    t.right(32)
    t.forward(40)
    t.left(83)
    t.forward(70)
    t.penup()
    t.hideturtle()


if __name__ == "raymarching":
    renderer = RayMarchingRenderer().render()
    done()