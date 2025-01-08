import cadquery as cq
import cqkit as kit


def make_outer_chassis():
    path = [
        ("start", {"position": (0, 10), "direction": 90, "width": 0.5}),
        ("line", {"length": 2}),
        ("arc", {"radius": 2, "angle": -90}),
        ("line", {"length": 10}),
        ("arc", {"radius": 2, "angle": -90}),
        ("line", {"length": 10}),
        ("arc", {"radius": 2, "angle": -90}),
        ("line", {"length": 10}),
        ("arc", {"radius": 2, "angle": -90}),
        ("line", {"length": 2}),
    ]

    ribbon = kit.Ribbon("XY", path)
    return ribbon.render().extrude(10)


def make_fan(workplane: cq.Workplane, diameter: float):
    # Just a simple cube
    return workplane.box(diameter, diameter, 24)


outer_chassis = make_outer_chassis()
fan = make_fan(cq.Workplane("XY"), 120)
