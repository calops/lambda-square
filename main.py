import cqkit as kit


def make_outer_chassis():
    path = [
        ("start", {"position": (0.0, 10.0), "direction": 90.0, "width": 0.5}),
        ("line", {"length": 2.0}),
        ("arc", {"radius": 2.0, "angle": -90.0}),
        ("line", {"length": 10.0}),
        ("arc", {"radius": 2.0, "angle": -90.0}),
        ("line", {"length": 10.0}),
        ("arc", {"radius": 2.0, "angle": -90.0}),
        ("line", {"length": 10.0}),
        ("arc", {"radius": 2.0, "angle": -90.0}),
        ("line", {"length": 2.0}),
    ]

    ribbon = kit.Ribbon("XY", path)
    return ribbon.render().extrude(10)


outer_chassis = make_outer_chassis()
