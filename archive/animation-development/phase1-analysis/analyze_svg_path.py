#!/usr/bin/env python3
"""
SVG Path Analysis for Solar Flare Animation Timing
Phase 1: Calculate exact locations of Gaussian peaks along the curve
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

def parse_svg_path(path_d):
    """Parse SVG path string into coordinate points"""
    # Current path: "M30,75 C50,74 65,72 75,68 C85,60 95,45 105,35 C115,25 125,28 135,40 C145,52 155,60 165,62 C175,58 185,50 195,38 C205,26 215,18 225,15 C235,18 245,28 255,42 C265,56 275,68 285,72 C295,74 310,75 330,75"
    
    # Extract all coordinate pairs
    coordinates = []
    
    # Start point M30,75
    coordinates.append((30, 75))
    
    # Parse cubic Bezier curves
    bezier_points = [
        # First curve: C50,74 65,72 75,68
        [(50, 74), (65, 72), (75, 68)],
        # Second curve: C85,60 95,45 105,35  
        [(85, 60), (95, 45), (105, 35)],
        # Third curve: C115,25 125,28 135,40
        [(115, 25), (125, 28), (135, 40)],
        # Fourth curve: C145,52 155,60 165,62
        [(145, 52), (155, 60), (165, 62)],
        # Fifth curve: C175,58 185,50 195,38
        [(175, 58), (185, 50), (195, 38)],
        # Sixth curve: C205,26 215,18 225,15
        [(205, 26), (215, 18), (225, 15)],
        # Seventh curve: C235,18 245,28 255,42
        [(235, 18), (245, 28), (255, 42)],
        # Eighth curve: C265,56 275,68 285,72
        [(265, 56), (275, 68), (285, 72)],
        # Ninth curve: C295,74 310,75 330,75
        [(295, 74), (310, 75), (330, 75)]
    ]
    
    return coordinates[0], bezier_points

def cubic_bezier(t, p0, p1, p2, p3):
    """Calculate point on cubic Bezier curve at parameter t (0-1)"""
    x = (1-t)**3 * p0[0] + 3*(1-t)**2*t * p1[0] + 3*(1-t)*t**2 * p2[0] + t**3 * p3[0]
    y = (1-t)**3 * p0[1] + 3*(1-t)**2*t * p1[1] + 3*(1-t)*t**2 * p2[1] + t**3 * p3[1]
    return (x, y)

def sample_full_path(start_point, bezier_segments, samples_per_segment=100):
    """Sample the entire SVG path into discrete points"""
    all_points = []
    current_point = start_point
    
    for segment in bezier_segments:
        p1, p2, p3 = segment
        p0 = current_point
        
        # Sample this segment
        for i in range(samples_per_segment):
            t = i / samples_per_segment
            point = cubic_bezier(t, p0, p1, p2, p3)
            all_points.append(point)
        
        # Update current point to end of this segment
        current_point = p3
    
    return np.array(all_points)

def find_peaks(points, min_prominence=8):
    """Find peaks in the Y-coordinates (flux values)"""
    y_values = points[:, 1]
    
    # Since SVG coordinates have Y increasing downward, we need to invert for peaks
    # Lower Y values = higher flux (peaks)
    
    # Find local minima in Y (which are peaks in flux)
    peaks = []
    peak_indices = []
    
    # Use a sliding window approach
    window_size = 50  # Larger window for better peak detection
    
    for i in range(window_size, len(y_values) - window_size):
        current_y = y_values[i]
        
        # Check if this is a local minimum (peak in flux)
        left_window = y_values[i-window_size:i]
        right_window = y_values[i+1:i+window_size+1]
        
        # Must be lower than surrounding points
        is_local_min = all(current_y <= y for y in left_window) and all(current_y <= y for y in right_window)
        
        if is_local_min:
            # Check prominence (how much it stands out)
            left_max = max(left_window) if len(left_window) > 0 else current_y
            right_max = max(right_window) if len(right_window) > 0 else current_y
            prominence = min(left_max - current_y, right_max - current_y)
            
            if prominence >= min_prominence:
                peaks.append((points[i][0], current_y))
                peak_indices.append(i)
    
    # Remove peaks that are too close to each other (keep the most prominent)
    if len(peaks) > 2:
        # Sort by prominence and keep top 2
        prominences = []
        for idx in peak_indices:
            left_max = max(y_values[max(0, idx-50):idx])
            right_max = max(y_values[idx+1:min(len(y_values), idx+51)])
            prom = min(left_max - y_values[idx], right_max - y_values[idx])
            prominences.append(prom)
        
        # Get indices of 2 most prominent peaks
        top_2_indices = sorted(range(len(prominences)), key=lambda i: prominences[i], reverse=True)[:2]
        peaks = [peaks[i] for i in top_2_indices]
        peak_indices = [peak_indices[i] for i in top_2_indices]
        
        # Sort by X position (time order)
        sorted_pairs = sorted(zip(peaks, peak_indices), key=lambda x: x[0][0])
        peaks = [p[0] for p in sorted_pairs]
        peak_indices = [p[1] for p in sorted_pairs]
    
    return peaks, peak_indices

def analyze_path():
    """Main analysis function"""
    print("=== Phase 1: SVG Path Analysis ===\n")
    
    # Parse the path
    start_point, bezier_segments = parse_svg_path("")
    print(f"Start point: {start_point}")
    print(f"Number of Bezier segments: {len(bezier_segments)}")
    
    # Sample the path
    points = sample_full_path(start_point, bezier_segments)
    print(f"Total sampled points: {len(points)}")
    
    # Find peaks
    peaks, peak_indices = find_peaks(points)
    print(f"\nFound {len(peaks)} peaks:")
    
    for i, (peak, idx) in enumerate(zip(peaks, peak_indices)):
        x, y = peak
        path_percentage = (idx / len(points)) * 100
        time_seconds = (idx / len(points)) * 6  # 6-second animation
        print(f"  Peak {i+1}: X={x:.1f}, Y={y:.1f} (flux height)")
        print(f"           Path: {path_percentage:.1f}% | Time: {time_seconds:.2f}s")
    
    # Find shoulder/valley between peaks if we have 2+ peaks
    if len(peaks) >= 2:
        # Find the highest Y value (lowest flux) between the two main peaks
        start_idx = peak_indices[0]
        end_idx = peak_indices[1]
        
        valley_idx = start_idx + np.argmax(points[start_idx:end_idx, 1])
        valley_point = points[valley_idx]
        valley_percentage = (valley_idx / len(points)) * 100
        valley_time = (valley_idx / len(points)) * 6
        
        print(f"\nValley/Shoulder between peaks:")
        print(f"  X={valley_point[0]:.1f}, Y={valley_point[1]:.1f}")
        print(f"  Path: {valley_percentage:.1f}% | Time: {valley_time:.2f}s")
    
    # Create visualization
    plt.figure(figsize=(12, 6))
    plt.plot(points[:, 0], points[:, 1], 'b-', linewidth=2, label='Flux Curve')
    plt.gca().invert_yaxis()  # Invert Y to match SVG coordinates
    
    # Mark peaks
    for i, (peak, idx) in enumerate(zip(peaks, peak_indices)):
        plt.plot(peak[0], peak[1], 'ro', markersize=10, label=f'Peak {i+1}')
    
    if len(peaks) >= 2:
        plt.plot(valley_point[0], valley_point[1], 'go', markersize=8, label='Valley/Shoulder')
    
    plt.xlabel('X Position (SVG coordinates)')
    plt.ylabel('Y Position (SVG coordinates - inverted for flux)')
    plt.title('Solar Flare X-Ray Flux Curve Analysis')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('svg_path_analysis.png', dpi=150, bbox_inches='tight')
    print(f"\nVisualization saved as 'svg_path_analysis.png'")
    
    return {
        'points': points,
        'peaks': peaks,
        'peak_indices': peak_indices,
        'peak_percentages': [(idx / len(points)) * 100 for idx in peak_indices],
        'peak_times': [(idx / len(points)) * 6 for idx in peak_indices]
    }

if __name__ == "__main__":
    results = analyze_path()
    
    print("\n=== IMPLEMENTATION OUTPUTS ===")
    print("Use these values for CSS animation timing:")
    
    for i, (percentage, time_sec) in enumerate(zip(results['peak_percentages'], results['peak_times'])):
        print(f"Peak {i+1}: {percentage:.1f}% of animation ({time_sec:.2f}s)")
        print(f"  Region {i+1} animation-delay: {time_sec:.2f}s")
        print(f"  Keyframe timing: {percentage:.1f}%")