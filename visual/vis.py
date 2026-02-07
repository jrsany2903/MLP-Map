import pyvista as pv

# Create a sphere (Earth placeholder)
sphere = pv.Sphere(radius=1.0, theta_resolution=360, phi_resolution=180)
t = pv.Texture("textest.png")  # Placeholder texture


sphere.texture_map_to_sphere(inplace=True)  # Map texture to sphere

# Create the plotter
plotter = pv.Plotter()
plotter.add_mesh(sphere, texture=t) 

plotter.set_background("black")  # Set background color

# Show interactively
plotter.show()