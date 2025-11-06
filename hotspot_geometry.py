
import settings


def compute_top_hotspot_geometry():
    """ !TODO: I will attach the calculation for this later """
    m = settings.SpriteMap
    w = m.TopHotspotWidth
    h = m.TopHotspotHeight
    x = (m.FrameWidth - w) / 2.0
    y = 0.0
    return (x, y, w, h)
