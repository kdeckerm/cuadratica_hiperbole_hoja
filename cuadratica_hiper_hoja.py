import numpy as np
import matplotlib.pyplot as plt

# Definir el rango y los valores para las coordenadas
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

# Ecuación del hiperboloide de una hoja
expr = 9 * (X**2 / 9 + (Y + 3)**2 / 4 - 1)
Z_plus = np.where(expr > -1e-10, 2 + np.sqrt(np.maximum(expr, 0)), np.nan)
Z_minus = np.where(expr > -1e-10, 2 - np.sqrt(np.maximum(expr, 0)), np.nan)

# Calcular puntos de intersección
intersections = []

# Intersección con el plano x = 0
for y_val in np.linspace(-10, 10, 50):
    expr_z = 9 * (0 + (y_val + 3)**2 / 4 - 1)
    if expr_z >= 0:
        z_plus = 2 + np.sqrt(expr_z)
        z_minus = 2 - np.sqrt(expr_z)
        intersections.append((0, y_val, z_plus))
        intersections.append((0, y_val, z_minus))

# Intersección con el plano y = 0
for x_val in np.linspace(-10, 10, 50):
    expr_z = 9 * (x_val**2 / 9 + 0 - 1)
    if expr_z >= 0:
        z_plus = 2 + np.sqrt(expr_z)
        z_minus = 2 - np.sqrt(expr_z)
        intersections.append((x_val, 0, z_plus))
        intersections.append((x_val, 0, z_minus))

# Intersección con el plano z = 0
for x_val in np.linspace(-10, 10, 50):
    for y_val in np.linspace(-10, 10, 50):
        expr_z = x_val**2 / 9 + (y_val + 3)**2 / 4 - 1
        if np.isclose(expr_z, -9 / 9):  # Asegurarnos de que z=0 cumpla
            intersections.append((x_val, y_val, 0))

# Convertir intersecciones a arrays para graficar
intersections = np.array(intersections)
X_int, Y_int, Z_int = intersections[:, 0], intersections[:, 1], intersections[:, 2]

# Crear la figura
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie para la parte superior e inferior
ax.plot_surface(X, Y, Z_plus, alpha=0.7, cmap='viridis', edgecolor='none')
ax.plot_surface(X, Y, Z_minus, alpha=0.7, cmap='viridis', edgecolor='none')

# Graficar puntos de intersección
ax.scatter(X_int, Y_int, Z_int, color='red', label='Intersecciones', s=20)

# Configurar etiquetas y título
ax.set_title("Hiperboloide de una hoja con intersecciones", fontsize=14)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

# Agregar leyenda
ax.legend()

# Guardar la figura
save_path = "/home/decker/Documentos/Carpeta.py/cuadratica_hiper_hoja_intersections.png"
plt.savefig(save_path)

# Mostrar advertencia si no hay entorno interactivo, pero no detener el flujo
try:
    plt.show()
except:
    print(f"La figura se ha guardado en: {save_path}")

