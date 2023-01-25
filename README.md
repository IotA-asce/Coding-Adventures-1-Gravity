# Coding-Adventures-1-Gravity

exploring the laws of gravitational force binding planets and stars in
space using pygame to handle the graphical representational section

## Architecture

A screen surface is utilized for the playground
Planet objects are spawned on Mouse-click at the mouse position

| Planet                    |
| size           | float    |
|----------------|----------|
| mass           | float    |
| position       | Vector2  |
| speed          | Vector2  |
| force          | Vector2  |
| set_position() | function |
| set_speed()    | function |
| set_force()    | function |

Vector2 is for all 2D vector calculations

| Vector2       |
|-------|-------|
| x     | float |
| y     | float |

the planets are kept in a list and at each frame update,
the compounded force is calculated on each planet
the del(S) is computed over unit time
positions are updated