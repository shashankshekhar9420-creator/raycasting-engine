# Python Raycaster

A 2.5D raycasting engine built from scratch in Python with Pygame, rendering a real-time first-person 3D view from a 2D tile-based map — in the style of Wolfenstein 3D.
<br>

https://github.com/user-attachments/assets/77c49e28-c76d-438a-9a56-7d60b2fb8740

<br>


## Features

- Grid-based ray-wall intersection using horizontal/vertical step-casting
- Fisheye distortion correction via perpendicular distance projection
- Distance-based shading, with horizontal and vertical wall faces shaded differently for depth
- Circle-vs-grid collision detection with axis-separated movement, so the player slides along walls instead of clipping through them
- Real-time render loop at 60 FPS, casting 120 rays per frame across a 60° field of view

## Controls

| Key | Action |
|---|---|
| `↑` | Move forward |
| `↓` | Move backward |
| `←` | Turn left |
| `→` | Turn right |

## Requirements

- Python 3.x
- [Pygame](https://www.pygame.org/)

```bash
pip install pygame
```

## Running it

```bash
python main.py
```

## Project Structure

```
.
├── main.py        # Game loop: input, update, render
├── player.py       # Player state, movement, collision
├── map.py          # Tile grid and wall lookup
├── ray.py          # Single-ray casting and distance calculation
├── raycaster.py     # Casts all rays each frame and draws the 3D view
├── settings.py       # Constants (window size, FOV, tile size, ray count)
└── background.png    # Sky/floor background image
```

## How It Works

Each frame, `Raycaster` casts a fan of rays across the player's field of view. For every ray, `ray.py` steps outward along the grid in two passes — one checking horizontal grid-line crossings, one checking vertical — until it hits a wall tile, then keeps whichever hit is closer to the player. That distance is corrected for fisheye distortion (multiplied by the cosine of the angle between the ray and the player's facing direction) and converted into a vertical wall strip: closer walls render taller and brighter, farther walls shorter and dimmer. Drawing all 120 strips side by side produces the pseudo-3D view.

Collision detection checks four points around the player (left/right/top/bottom of a fixed radius) against the map on each axis independently, which is what lets the player slide along a wall instead of getting stuck when approaching it at an angle.

## Known Limitations

- Single hardcoded map — no level loading or editor
- No textures — walls are flat-shaded
- No sprites, enemies, or items
- Minimap and top-down debug view exist in the code but are disabled by default

## Roadmap

- [ ] Textured walls
- [ ] Minimap toggle
- [ ] Multiple/loadable levels
- [ ] Sprites (enemies, items)
