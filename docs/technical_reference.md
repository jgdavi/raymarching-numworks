## Technical reference
### `screen_res`
**The `screen_res` variable determines the resolution of the rendered image or scene. It defines the number of pixels that will be displayed on the screen, both horizontally and vertically.**

Increasing the resolution significantly impacts the rendering time, as the algorithm needs to calculate and draw more pixels.

### `detection_threshold`
The `detection_threshold` variable in the ray marching algorithm serves as a criterion for determining when a ray has intersected or come very close to a surface in the scene. It represents a small distance value that defines the threshold for considering a ray as having "detected" a surface.

### `max_iter`
**The `max_iter` parameter determines the maximum number of iterations the algorithm will take before terminating.**

By setting this value to a moderate level, we strike a balance between rendering accuracy and computational efficiency. Therefore, the algorithm avoids excessive computation in cases where the ray does not intersect any surfaces.

### `marching_boundary`
**The `marching_boundary` parameter sets an upper bound on how far the ray marching algorithm will continue marching along a ray before stopping.**

This value helps prevent the algorithm from marching indefinitely or wasting computational resources when the ray does not intersect any surfaces or encounters a very distant surface. 

When the algorithm starts marching along a ray, it calculates the distance to the closest surface at each iteration. If the accumulated distance traveled exceeds `marching_boundary`, the algorithm stops marching and considers the ray to have reached its maximum allowed distance.

A larger value allows for rendering more distant objects, while a smaller value can improve rendering speed by limiting the search space.

## Methods
The `raymarch` method is the core of this algorithm. It takes a ray origin and direction as input and calculates the distance to the closest surface along that ray. It does this by taking small steps along the ray and checking the distance to surfaces at each step. The algorithm continues for a maximum number of iterations ([max_iter](#max_iter)) or until it finds a surface very close to the ray ([detection_threshold](#detection_threshold)).

### Distance to Surfaces
The `distance_to_surfaces` method calculates how far a given point is from the closest surface in the scene. In this code, the scene consists of spheres and a plane. The method finds the minimum distance from the point to any of these surfaces.

### Lighting Calculation
The `calculate_lighting` method figures out how much light reaches a specific point on a surface. It considers the direction of the light source, the orientation of the surface (using the surface normal), and whether the light is blocked by other objects (occlusion). It uses the dot product to determine the amount of diffuse lighting and performs a ray march to check for occlusion.

### Drawing and Rendering
The `draw` method takes a pixel coordinate `(x, y)` and calculates the color of that pixel based on the ray marching and lighting calculations.

By converting the pixel coordinate to a normalized UV coordinate, which is used to map colors or textures onto the 3D object, the method can then call other methods to find the closest surface and calculates the lighting at that point. The resulting lighting values determine the color of the pixel.

The `render` method puts everything together. It iterates over each pixel on the screen, calls the draw method to determine its color, and then uses turtle to set the color and draw the pixel at the corresponding position.
