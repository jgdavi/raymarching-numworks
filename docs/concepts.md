## Concepts
This part explains the key mathematical and rendering concepts used.

### Surface Normal
The surface normal is a vector that describes the orientation of a surface at a particular point. It is perpendicular to the surface and points outward. Surface normals are important for calculating lighting effects, such as diffuse and specular reflections. In the code, the `surface_normal` method estimates the surface normal by taking finite differences of the distance function. It helps determine the direction in which the surface is facing, which is crucial for calculating the lighting contribution at that point.

### Euclidean Distance
Euclidean distance is a measure of the length between two points in a three-dimensional space. It is calculated using the Pythagorean theorem and the Cartesian coordinates of the points. In the code, this distance calculation is used to determine the proximity of a point to various surfaces in the scene.

### Dot Product
The dot product (AKA scalar product) of two vectors gives a scalar value. It represents the projection of one vector onto another and is calculated by multiplying their corresponding components and summing them up. In lighting calculations, it determines the angle between the light direction and surface normal, influencing reflected light and shading.

### UV mapping
UV mapping is a technique used in computer graphics to map textures or colors onto 3D objects. It involves defining a coordinate system, known as UV coordinates, on the surface of the object. These UV coordinates are typically defined in the range of [0, 1], where each point on the surface is assigned a corresponding UV coordinate.

### Diffuse Lighting
Diffuse lighting is a type of lighting model that simulates the scattering of light off a rough surface. It assumes that light reflects evenly in all directions, creating a soft and diffuse illumination. In the code, the dot product between the light direction and surface normal is used to calculate this lighting component.

### Occlusion
Occlusion simply refers to the blocking or obscuring of light due to intervening objects. In the code, occlusion is checked by performing a ray march from the surface point in the direction of the light source. If the light source is blocked by another object along the way, it means the light is occluded, and the diffuse lighting is reduced accordingly. This adds realism to the rendering by simulating the attenuation of light when objects cast shadows on each other.
