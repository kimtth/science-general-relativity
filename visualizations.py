"""
General Relativity Visualizations - Core Concepts
==================================================
Simplified visualizations focusing on essential GR concepts.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Set style
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10
os.makedirs('visualizations', exist_ok=True)


def visualize_spacetime_curvature():
    """Visualize spacetime curvature - the rubber sheet analogy."""
    fig = plt.figure(figsize=(14, 6))
    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)
    
    # Create curved spacetime surface
    x = np.linspace(-10, 10, 80)
    y = np.linspace(-10, 10, 80)
    X, Y = np.meshgrid(x, y)
    R = np.maximum(np.sqrt(X**2 + Y**2), 0.5)
    Z = -1.0 / R  # Gravitational well
    
    # 3D surface
    ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8, edgecolor='none')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Curvature')
    ax1.set_title('Spacetime Curvature (Rubber Sheet)', fontweight='bold')
    ax1.view_init(25, 45)
    
    # Cross-section
    r = np.linspace(0.5, 10, 150)
    z = -1.0 / r
    ax2.plot(r, z, 'b-', linewidth=3)
    ax2.axvline(x=2, color='r', linestyle='--', label='Event Horizon (r=2M)')
    ax2.fill_between(r, z, 0, alpha=0.2)
    ax2.set_xlabel('Radial Distance')
    ax2.set_ylabel('Potential')
    ax2.set_title('Radial Cross-Section', fontweight='bold')
    ax2.legend()
    ax2.grid(alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('visualizations/01_spacetime_curvature.png', dpi=200, bbox_inches='tight')
    print("✓ Saved: 01_spacetime_curvature.png")
    plt.close()


def visualize_light_bending():
    """Visualize gravitational lensing."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    for ax, curved in [(ax1, False), (ax2, True)]:
        ax.set_xlim(-10, 10)
        ax.set_ylim(-8, 8)
        ax.add_patch(plt.Circle((0, 0), 0.5, color='gold', ec='orange', lw=2))
        
        # Light rays
        for y in np.linspace(-7, 7, 8):
            if abs(y) < 0.6:
                continue
            x = np.linspace(-10, 10, 150)
            if curved:
                deflection = 4 / abs(y)  # Simplified deflection
                y_path = y + deflection * (x**2 - 100) / 100
                mask = np.sqrt(x**2 + y_path**2) > 0.5
                ax.plot(x[mask], y_path[mask], 'r-', lw=1.5, alpha=0.7)
            else:
                ax.arrow(-10, y, 19.5, 0, head_width=0.3, head_length=0.5, 
                        fc='r', ec='r', lw=1.5, alpha=0.7)
        
        title = 'Curved Spacetime\n(Gravity bends light)' if curved else 'Flat Spacetime\n(Straight paths)'
        ax.set_title(title, fontweight='bold')
        ax.grid(alpha=0.3)
        ax.set_aspect('equal')
    
    plt.tight_layout()
    plt.savefig('visualizations/02_light_bending.png', dpi=200, bbox_inches='tight')
    print("✓ Saved: 02_light_bending.png")
    plt.close()


def visualize_metric_tensor():
    """Visualize metric tensor components."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    r = np.linspace(0.1, 10, 150)
    r_s = 2.0  # Schwarzschild radius
    
    # Time component g_tt
    ax1 = axes[0]
    ax1.plot(r, -np.ones_like(r), 'b--', lw=2, label='Flat (Minkowski)')
    ax1.plot(r, -(1 - r_s/r), 'r-', lw=3, label='Curved (Schwarzschild)')
    ax1.axvline(r_s, color='orange', ls='--', lw=2, label='Event Horizon')
    ax1.axhline(0, color='k', ls=':', alpha=0.3)
    ax1.set_xlabel('Radial Distance')
    ax1.set_ylabel('$g_{tt}$')
    ax1.set_title('Time Component', fontweight='bold')
    ax1.legend()
    ax1.grid(alpha=0.3)
    ax1.set_ylim(-2, 0.5)
    
    # Time dilation
    ax2 = axes[1]
    ax2.plot(r, np.ones_like(r), 'b--', lw=2, label='Flat')
    ax2.plot(r, np.sqrt(np.abs(1 - r_s/r)), 'g-', lw=3, label='Curved')
    ax2.axvline(r_s, color='orange', ls='--', lw=2)
    ax2.fill_between(r, 0, np.sqrt(np.abs(1 - r_s/r)), alpha=0.2, color='g')
    ax2.set_xlabel('Radial Distance')
    ax2.set_ylabel('$d\\tau/dt$')
    ax2.set_title('Time Dilation Factor', fontweight='bold')
    ax2.legend()
    ax2.grid(alpha=0.3)
    ax2.set_ylim(0, 1.2)
    
    plt.tight_layout()
    plt.savefig('visualizations/03_metric_tensor.png', dpi=200, bbox_inches='tight')
    print("✓ Saved: 03_metric_tensor.png")
    plt.close()


def visualize_curvature_tensors():
    """Visualize tensor contraction flow."""
    fig, ax = plt.subplots(figsize=(10, 9))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    ax.text(5, 9.5, 'Metric → Curvature → Einstein', ha='center', fontsize=16, fontweight='bold')
    
    # Flow
    tensors = [
        (5, 8.2, '$g_{\\mu\\nu}$', 'Metric', 'lightcoral'),
        (5, 6.8, '$\\Gamma^{\\lambda}_{\\mu\\nu}$', 'Christoffel', 'lightblue'),
        (5, 5.4, '$R^{\\rho}_{\\sigma\\mu\\nu}$', 'Riemann (20)', 'lightblue'),
        (3, 3.8, '$R_{\\mu\\nu}$', 'Ricci (10)', 'lightyellow'),
        (7, 3.8, '$R$', 'Scalar (1)', 'lightgreen'),
        (5, 2.2, '$G_{\\mu\\nu}$', 'Einstein', 'plum')
    ]
    
    for x, y, tex, label, color in tensors:
        ax.text(x, y, f'{tex}\n{label}', ha='center', va='center', fontsize=11,
                bbox=dict(boxstyle='round,pad=0.5', fc=color, ec='black', lw=2))
    
    # Arrows
    arrow_props = dict(arrowstyle='->', lw=2, color='darkgreen')
    ax.annotate('', xy=(5, 7.5), xytext=(5, 7.9), arrowprops=arrow_props)
    ax.text(6, 7.7, '$\\partial g$', fontsize=9, style='italic')
    
    ax.annotate('', xy=(5, 6.1), xytext=(5, 6.5), arrowprops=arrow_props)
    ax.text(6.5, 6.3, '$\\partial\\Gamma + \\Gamma\\Gamma$', fontsize=9, style='italic')
    
    ax.annotate('', xy=(3, 4.5), xytext=(4.5, 5.1), arrowprops=arrow_props)
    ax.text(3.5, 4.9, 'Contract', fontsize=8)
    
    ax.annotate('', xy=(7, 4.5), xytext=(5.5, 5.1), arrowprops=arrow_props)
    ax.text(6.5, 4.9, 'Double', fontsize=8)
    
    ax.annotate('', xy=(5, 2.9), xytext=(3.2, 3.5), arrowprops=arrow_props)
    ax.annotate('', xy=(5, 2.9), xytext=(6.8, 3.5), arrowprops=arrow_props)
    
    ax.annotate('', xy=(5, 1.5), xytext=(5, 1.9), arrowprops=dict(arrowstyle='->', lw=2.5, color='red'))
    
    # Einstein equation
    ax.text(5, 0.8, '$G_{\\mu\\nu} = 8\\pi T_{\\mu\\nu}$', ha='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.6', fc='lightcyan', ec='darkblue', lw=3))
    ax.text(5, 0.3, 'Field Equation', ha='center', fontsize=11, fontweight='bold')
    
    plt.savefig('visualizations/04_curvature_tensors.png', dpi=200, bbox_inches='tight')
    print("✓ Saved: 04_curvature_tensors.png")
    plt.close()


def visualize_tensor_indices():
    """Visualize contravariant vs covariant components using standard geometric construction."""
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Common vector for both panels
    vector_x, vector_y = 3.0, 2.5
    
    # Basis vectors (non-orthogonal) - matching the reference style
    e1_x, e1_y = 2.0, 0.2
    e2_x, e2_y = 0.7, 1.8
    
    # Left Panel: Contravariant Components (Parallel Projections)
    ax1 = axes[0]
    ax1.set_xlim(-0.3, 4.5)
    ax1.set_ylim(-0.3, 3.5)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3, linestyle='--')
    
    # Draw basis vectors with labels
    ax1.arrow(0, 0, e1_x, e1_y, head_width=0.12, head_length=0.12, fc='blue', ec='blue', lw=2.5, length_includes_head=True)
    ax1.arrow(0, 0, e2_x, e2_y, head_width=0.12, head_length=0.12, fc='red', ec='red', lw=2.5, length_includes_head=True)
    ax1.text(e1_x + 0.15, e1_y - 0.2, '$e_1$', fontsize=13, fontweight='bold', color='blue')
    ax1.text(e2_x - 0.3, e2_y + 0.15, '$e_2$', fontsize=13, fontweight='bold', color='red')
    
    # Draw the vector v
    ax1.arrow(0, 0, vector_x, vector_y, head_width=0.15, head_length=0.15, fc='darkgreen', ec='darkgreen', lw=3.5, length_includes_head=True, zorder=10)
    ax1.text(vector_x + 0.15, vector_y + 0.15, '$\\mathbf{v}$', fontsize=14, fontweight='bold', color='darkgreen')
    
    # Contravariant components: PARALLEL lines to basis vectors
    # Find v^1 and v^2 by solving: v = v^1*e1 + v^2*e2
    # [e1_x, e2_x] [v^1]   [vector_x]
    # [e1_y, e2_y] [v^2] = [vector_y]
    det = e1_x * e2_y - e2_x * e1_y
    v1_contra = (vector_x * e2_y - vector_y * e2_x) / det
    v2_contra = (e1_x * vector_y - e1_y * vector_x) / det
    
    # Draw parallel lines
    # Line parallel to e2 through tip of v (to find v^1)
    t_range = np.array([-1.5, 1.0])
    parallel_e2_x = vector_x + t_range * e2_x
    parallel_e2_y = vector_y + t_range * e2_y
    ax1.plot(parallel_e2_x, parallel_e2_y, 'b--', lw=2.5, alpha=0.7)
    
    # Line parallel to e1 through tip of v (to find v^2)
    parallel_e1_x = vector_x + t_range * e1_x
    parallel_e1_y = vector_y + t_range * e1_y
    ax1.plot(parallel_e1_x, parallel_e1_y, 'r--', lw=2.5, alpha=0.7)
    
    # Show component vectors
    ax1.arrow(0, 0, v1_contra*e1_x, v1_contra*e1_y, head_width=0.1, head_length=0.1, fc='cyan', ec='cyan', lw=2.5, alpha=0.7, length_includes_head=True)
    ax1.arrow(v1_contra*e1_x, v1_contra*e1_y, v2_contra*e2_x, v2_contra*e2_y, head_width=0.1, head_length=0.1, fc='orange', ec='orange', lw=2.5, alpha=0.7, length_includes_head=True)
    
    # Labels for components
    mid1_x, mid1_y = v1_contra*e1_x/2, v1_contra*e1_y/2
    ax1.text(mid1_x, mid1_y - 0.3, '$v^1 e_1$', fontsize=12, fontweight='bold', color='cyan', bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.8))
    
    mid2_x, mid2_y = v1_contra*e1_x + v2_contra*e2_x/2, v1_contra*e1_y + v2_contra*e2_y/2
    ax1.text(mid2_x + 0.2, mid2_y + 0.1, '$v^2 e_2$', fontsize=12, fontweight='bold', color='orange', bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.8))
    
    ax1.set_xlabel('$x$', fontsize=12)
    ax1.set_ylabel('$y$', fontsize=12)
    ax1.set_title('Contravariant: $\\mathbf{v} = v^i e_i$\\n(Parallel to basis)', fontweight='bold', fontsize=13)
    ax1.text(0.5, -0.08, 'Lines parallel to basis vectors', ha='center', fontsize=10, style='italic', color='gray', transform=ax1.transAxes)
    
    # Middle Panel: Covariant Components (Perpendicular Projections)
    ax2 = axes[1]
    ax2.set_xlim(-0.3, 4.5)
    ax2.set_ylim(-0.3, 3.5)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3, linestyle='--')
    
    # Same basis vectors
    ax2.arrow(0, 0, e1_x, e1_y, head_width=0.12, head_length=0.12, fc='blue', ec='blue', lw=2.5, length_includes_head=True)
    ax2.arrow(0, 0, e2_x, e2_y, head_width=0.12, head_length=0.12, fc='red', ec='red', lw=2.5, length_includes_head=True)
    ax2.text(e1_x + 0.15, e1_y - 0.2, '$e_1$', fontsize=13, fontweight='bold', color='blue')
    ax2.text(e2_x - 0.3, e2_y + 0.15, '$e_2$', fontsize=13, fontweight='bold', color='red')
    
    # Same vector
    ax2.arrow(0, 0, vector_x, vector_y, head_width=0.15, head_length=0.15, fc='darkgreen', ec='darkgreen', lw=3.5, length_includes_head=True, zorder=10)
    ax2.text(vector_x + 0.15, vector_y + 0.15, '$\\mathbf{v}$', fontsize=14, fontweight='bold', color='darkgreen')
    
    # Calculate perpendicular projections properly
    # Project v onto e1: v_dot_e1 = (v·e1) / |e1|²
    e1_dot_e1 = e1_x**2 + e1_y**2
    v_dot_e1 = vector_x * e1_x + vector_y * e1_y
    proj_e1_scalar = v_dot_e1 / e1_dot_e1
    proj_e1_x = proj_e1_scalar * e1_x
    proj_e1_y = proj_e1_scalar * e1_y
    
    # Project v onto e2: v_dot_e2 = (v·e2) / |e2|²
    e2_dot_e2 = e2_x**2 + e2_y**2
    v_dot_e2 = vector_x * e2_x + vector_y * e2_y
    proj_e2_scalar = v_dot_e2 / e2_dot_e2
    proj_e2_x = proj_e2_scalar * e2_x
    proj_e2_y = proj_e2_scalar * e2_y
    
    # Draw perpendicular lines from vector tip to projection points
    ax2.plot([vector_x, proj_e1_x], [vector_y, proj_e1_y], 'b--', lw=2.5, alpha=0.8)
    ax2.plot([vector_x, proj_e2_x], [vector_y, proj_e2_y], 'r--', lw=2.5, alpha=0.8)
    
    # Draw projection points
    ax2.plot(proj_e1_x, proj_e1_y, 'bo', markersize=10, zorder=5)
    ax2.plot(proj_e2_x, proj_e2_y, 'ro', markersize=10, zorder=5)
    
    # Draw right angle markers
    def draw_right_angle(ax, p1, p2, p3, size=0.12, color='black'):
        """Draw right angle marker at p2 between lines p1-p2 and p2-p3."""
        v1 = np.array([p1[0] - p2[0], p1[1] - p2[1]])
        v2 = np.array([p3[0] - p2[0], p3[1] - p2[1]])
        if np.linalg.norm(v1) > 0 and np.linalg.norm(v2) > 0:
            v1 = v1 / np.linalg.norm(v1) * size
            v2 = v2 / np.linalg.norm(v2) * size
            corner = p2 + v1 + v2
            ax.plot([p2[0] + v1[0], corner[0], p2[0] + v2[0]], 
                    [p2[1] + v1[1], corner[1], p2[1] + v2[1]], 
                    color=color, lw=1.8)
    
    draw_right_angle(ax2, [vector_x, vector_y], [proj_e1_x, proj_e1_y], [0, 0], size=0.15, color='blue')
    draw_right_angle(ax2, [vector_x, vector_y], [proj_e2_x, proj_e2_y], [0, 0], size=0.15, color='red')
    
    # Show covariant component values
    v1_cov = v_dot_e1
    v2_cov = v_dot_e2
    
    # Labels for covariant components
    ax2.text(proj_e1_x/2, proj_e1_y/2 - 0.35, f'$v_1 = {v1_cov:.2f}$', fontsize=11, fontweight='bold', color='blue', bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.9))
    ax2.text(proj_e2_x/2 + 0.3, proj_e2_y/2, f'$v_2 = {v2_cov:.2f}$', fontsize=11, fontweight='bold', color='red', bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.9))
    
    ax2.set_xlabel('$x$', fontsize=12)
    ax2.set_ylabel('$y$', fontsize=12)
    ax2.set_title('Covariant: $v_i = \\mathbf{v} \\cdot e^i$\\n(Perpendicular to basis)', fontweight='bold', fontsize=13)
    ax2.text(0.5, -0.08, 'Lines perpendicular to basis vectors', ha='center', fontsize=10, style='italic', color='gray', transform=ax2.transAxes)
    
    # Right Panel: Index Operations
    ax3 = axes[2]
    ax3.axis('off')
    ax3.text(0.5, 0.95, 'Index Operations', ha='center', fontsize=15, fontweight='bold', transform=ax3.transAxes)
    
    # Contravariant
    ax3.text(0.5, 0.78, '$v^\\mu$', ha='center', fontsize=20, 
             bbox=dict(boxstyle='round,pad=0.5', fc='lightblue', ec='blue', lw=2.5), transform=ax3.transAxes)
    ax3.text(0.5, 0.69, 'Contravariant (upper index)', ha='center', fontsize=10, transform=ax3.transAxes)
    ax3.text(0.5, 0.63, 'Parallel projections', ha='center', fontsize=9, style='italic', color='gray', transform=ax3.transAxes)
    
    # Lower arrow
    ax3.annotate('', xy=(0.5, 0.53), xytext=(0.5, 0.60), 
                 arrowprops=dict(arrowstyle='->', lw=3, color='green'), transform=ax3.transAxes)
    ax3.text(0.72, 0.565, 'Lower index', fontsize=9, color='green', style='italic', transform=ax3.transAxes)
    ax3.text(0.12, 0.565, '$v_\\mu = g_{\\mu\\nu}v^\\nu$', fontsize=10, color='green', transform=ax3.transAxes)
    
    # Covariant
    ax3.text(0.5, 0.42, '$v_\\mu$', ha='center', fontsize=20,
             bbox=dict(boxstyle='round,pad=0.5', fc='lightcoral', ec='red', lw=2.5), transform=ax3.transAxes)
    ax3.text(0.5, 0.33, 'Covariant (lower index)', ha='center', fontsize=10, transform=ax3.transAxes)
    ax3.text(0.5, 0.27, 'Perpendicular projections', ha='center', fontsize=9, style='italic', color='gray', transform=ax3.transAxes)
    
    # Raise arrow
    ax3.annotate('', xy=(0.5, 0.22), xytext=(0.5, 0.15),
                 arrowprops=dict(arrowstyle='->', lw=3, color='purple'), transform=ax3.transAxes)
    ax3.text(0.72, 0.185, 'Raise index', fontsize=9, color='purple', style='italic', transform=ax3.transAxes)
    ax3.text(0.12, 0.185, '$v^\\mu = g^{\\mu\\nu}v_\\nu$', fontsize=10, color='purple', transform=ax3.transAxes)
    
    # Contraction
    ax3.text(0.5, 0.05, 'Contraction: $v^\\mu w_\\mu = $ scalar', ha='center', fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', fc='yellow', ec='orange', lw=2.5), transform=ax3.transAxes)
    
    plt.tight_layout()
    plt.savefig('visualizations/04_tensor_indices.png', dpi=200, bbox_inches='tight')
    print("✓ Saved: 04_tensor_indices.png")
    plt.close()


def visualize_gravitational_waves():
    """Visualize gravitational waves."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Wave propagation
    ax1 = axes[0]
    x, t = np.linspace(-5, 5, 80), np.linspace(0, 10, 80)
    X, T = np.meshgrid(x, t)
    Z = 0.5 * np.sin(2 * (T - X))
    
    contour = ax1.contourf(X, T, Z, levels=15, cmap='coolwarm', alpha=0.8)
    fig.colorbar(contour, ax=ax1, label='Strain $h$')
    ax1.set_xlabel('Space')
    ax1.set_ylabel('Time')
    ax1.set_title('Wave Propagation', fontweight='bold')
    
    # Polarization effect
    ax2 = axes[1]
    n_particles = 12
    theta = np.linspace(0, 2*np.pi, n_particles, endpoint=False)
    r0 = 1
    x0, y0 = r0 * np.cos(theta), r0 * np.sin(theta)
    
    times = [0, 0.5]
    for i, t in enumerate(times):
        h_plus = 0.3 * np.cos(t * np.pi)
        x = x0 * (1 + h_plus)
        y = y0 * (1 - h_plus)
        ax2.plot(x, y, 'o-', lw=2, ms=6, label=f't = {t}T')
    
    ax2.plot(0, 0, 'r*', ms=15)
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_aspect('equal')
    ax2.grid(alpha=0.3)
    ax2.set_title('Plus Polarization $h_+$', fontweight='bold')
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('visualizations/05_gravitational_waves.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: 05_gravitational_waves.png")
    plt.close()


def visualize_geodesics():
    """Visualize orbital geodesics."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Orbital paths
    ax1 = axes[0]
    circle = plt.Circle((0, 0), 0.3, color='gold', ec='orange', lw=2)
    ax1.add_patch(circle)
    
    theta = np.linspace(0, 2*np.pi, 100)
    ax1.plot(3*np.cos(theta), 3*np.sin(theta), 'b-', lw=2, label='Circular')
    ax1.plot(4*np.cos(theta), 2.5*np.sin(theta), 'g-', lw=2, label='Elliptical')
    
    t = np.linspace(-2, 2, 100)
    x_hyp = 2 * np.cosh(t)
    y_hyp = 2 * np.sinh(t)
    mask = x_hyp < 8
    ax1.plot(x_hyp[mask], y_hyp[mask], 'r-', lw=2, label='Hyperbolic')
    
    ax1.set_xlim(-8, 8)
    ax1.set_ylim(-6, 6)
    ax1.set_aspect('equal')
    ax1.grid(alpha=0.3)
    ax1.legend()
    ax1.set_title('Orbital Types', fontweight='bold')
    
    # Precession comparison
    ax2 = axes[1]
    circle2 = plt.Circle((0, 0), 0.3, color='gold', ec='orange', lw=2)
    ax2.add_patch(circle2)
    
    theta_n = np.linspace(0, 4*np.pi, 300)
    a_n, e_n = 4, 0.6
    r_n = a_n * (1 - e_n**2) / (1 + e_n * np.cos(theta_n))
    ax2.plot(r_n * np.cos(theta_n), r_n * np.sin(theta_n), 'b--', lw=2, label='Newton', alpha=0.6)
    
    theta_e = theta_n + 0.15 * theta_n / (2*np.pi)
    r_e = a_n * (1 - e_n**2) / (1 + e_n * np.cos(theta_n))
    ax2.plot(r_e * np.cos(theta_e), r_e * np.sin(theta_e), 'r-', lw=3, label='Einstein (precessing)', alpha=0.8)
    
    ax2.set_xlim(-8, 8)
    ax2.set_ylim(-8, 8)
    ax2.set_aspect('equal')
    ax2.grid(alpha=0.3)
    ax2.legend()
    ax2.set_title('Orbital Precession', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('visualizations/06_geodesics.png', dpi=200, bbox_inches='tight')
    print("✓ Saved: 06_geodesics.png")
    plt.close()


def main():
    """Generate all visualizations."""
    print("=" * 60)
    print("Generating General Relativity Visualizations")
    print("=" * 60)
    
    visualizations = [
        ("Spacetime Curvature", visualize_spacetime_curvature),
        ("Light Bending", visualize_light_bending),
        ("Metric Tensor Components", visualize_metric_tensor),
        ("Tensor Indices", visualize_tensor_indices),
        ("Gravitational Waves", visualize_gravitational_waves),
        ("Geodesics", visualize_geodesics),
    ]
    
    for i, (name, func) in enumerate(visualizations, 1):
        print(f"\n[{i}/{len(visualizations)}] Creating: {name}")
        try:
            func()
        except Exception as e:
            print(f"✗ Error creating {name}: {e}")
    
    print("\n" + "=" * 60)
    print("✓ All visualizations completed!")
    print("=" * 60)
    print("\nVisualization files saved in: visualizations/")
    print("\nGenerated files:")
    print("  01_spacetime_curvature.png")
    print("  02_light_bending.png")
    print("  03_metric_tensor.png")
    print("  04_tensor_indices.png")
    print("  05_gravitational_waves.png")
    print("  06_geodesics.png")


if __name__ == "__main__":
    main()
