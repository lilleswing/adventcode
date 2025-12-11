from shapely import Point, Polygon



class Point2(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return

    def area(self, other):
        dx = abs(self.x - other.x) + 1
        dy = abs(self.y - other.y) + 1
        return dx * dy

def part1():
    lines = open('day09.in').readlines()
    lines = [x.strip() for x in lines]
    points = []
    for l in lines:
        x, y = l.split(',')
        x, y = int(x), int(y)
        points.append(Point2(x, y))

    areas = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1 = points[i]
            p2 = points[j]
            area = p1.area(p2)
            areas.append(area)
    print(max(areas))

def shap_area(p1, p2):
    dx = int(abs(p1.x - p2.x) + 1)
    dy = int(abs(p1.y - p2.y) + 1)
    return dx * dy

def is_included(polygon, p1, p2):
    """

    :param polygon:
    :param p1:
    :param p2:
    :return:

    all four corners need to be covered by the polygon
    also no line segments can intersecting the polygon
    """
    mi_x, ma_x = min(p1.x, p2.x), max(p1.x, p2.x)
    mi_y, ma_y = min(p1.y, p2.y), max(p1.y, p2.y)
    rect_coords = [(mi_x, mi_y), (ma_x, mi_y), (ma_x, ma_y), (mi_x, ma_y)]
    rectangle = Polygon(rect_coords)

    if not polygon.covers(rectangle):
        return False
    return True



def part2():
    lines = open('day09.in').readlines()
    lines = [x.strip() for x in lines]
    points = []
    for l in lines:
        x, y = l.split(',')
        x, y = int(x), int(y)
        points.append(Point(x, y))

    polygon = Polygon(points)
    areas = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            p1 = points[i]
            p2 = points[j]
            if is_included(polygon, p1, p2):
                areas.append(shap_area(p1, p2))

    print(max(areas))




if __name__ == "__main__":
    part1()
    part2()