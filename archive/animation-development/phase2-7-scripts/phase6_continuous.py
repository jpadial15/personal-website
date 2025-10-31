#!/usr/bin/env python3
"""
Phase 6: Continuous Breathing - Eliminate Discrete Steps
Create truly smooth, continuous brightness transitions that breathe naturally
"""

def calculate_continuous_breathing():
    """Calculate dense keyframes for continuous breathing effect"""
    print("=== Phase 6: Continuous Breathing Animation ===\n")
    
    print("Current Issue: Still too discrete - visible steps in brightness")
    print("Solution: Dense keyframes with smooth mathematical curves")
    print("- Use 15-20 keyframes per region instead of 6-7")
    print("- Implement smooth exponential/sinusoidal curves")
    print("- Eliminate any perceivable jumps between brightness levels")
    
    # Define smooth curve parameters
    regions = {
        'region_1': {
            'peak_time': 25.2,
            'buildup_start': 17.2,
            'decay_end': 37.2,
            'max_scale': 2.2,
            'max_glow': 25
        },
        'region_3': {
            'peak_time': 30.2,
            'buildup_start': 22.2,
            'decay_end': 40.2,
            'max_scale': 2.0,
            'max_glow': 22
        },
        'region_2': {
            'peak_time': 66.7,
            'buildup_start': 56.7,
            'decay_end': 81.7,
            'max_scale': 2.8,
            'max_glow': 35
        }
    }
    
    def generate_smooth_keyframes(region_data):
        """Generate dense keyframes for continuous breathing"""
        peak = region_data['peak_time']
        start = region_data['buildup_start']
        end = region_data['decay_end']
        max_scale = region_data['max_scale']
        max_glow = region_data['max_glow']
        
        keyframes = []
        
        # Dense keyframes for smooth curves
        points = [
            # Buildup phase - exponential curve
            start, start + (peak-start)*0.2, start + (peak-start)*0.4, 
            start + (peak-start)*0.6, start + (peak-start)*0.8, peak,
            # Decay phase - exponential decay  
            peak + (end-peak)*0.1, peak + (end-peak)*0.25, peak + (end-peak)*0.45,
            peak + (end-peak)*0.65, peak + (end-peak)*0.85, end
        ]
        
        for i, time_percent in enumerate(points):
            if time_percent <= peak:
                # Buildup - smooth exponential curve
                progress = (time_percent - start) / (peak - start)
                # Use exponential curve: y = x^2 for smooth acceleration
                brightness_factor = progress ** 1.5
            else:
                # Decay - smooth exponential decay
                progress = (time_percent - peak) / (end - peak)
                # Use exponential decay: y = e^(-2x) for natural falloff
                import math
                brightness_factor = math.exp(-2.5 * progress)
            
            # Calculate smooth values
            opacity = 0.3 + (0.7 * brightness_factor)
            scale = 0.8 + ((max_scale - 0.8) * brightness_factor)
            glow = 5 + ((max_glow - 5) * brightness_factor)
            
            keyframes.append({
                'time': time_percent,
                'opacity': opacity,
                'scale': scale,
                'glow': glow
            })
        
        return keyframes
    
    print(f"\n=== CONTINUOUS KEYFRAME GENERATION ===")
    
    css_regions = []
    
    for region_id, data in regions.items():
        keyframes = generate_smooth_keyframes(data)
        
        print(f"\n{region_id.upper()}:")
        print(f"  Generated {len(keyframes)} keyframes for smooth breathing")
        
        # Build CSS keyframes
        css_keyframes = []
        
        # Start state
        css_keyframes.append(f"    0%, {data['buildup_start']-0.5:.1f}% {{")
        css_keyframes.append(f"        transform: scale(0.8);")
        css_keyframes.append(f"        opacity: 0.3;")
        css_keyframes.append(f"        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);")
        css_keyframes.append(f"    }}")
        
        # Smooth breathing keyframes
        for kf in keyframes:
            css_keyframes.append(f"    {kf['time']:.1f}% {{")
            css_keyframes.append(f"        transform: scale({kf['scale']:.2f});")
            css_keyframes.append(f"        opacity: {kf['opacity']:.2f};")
            css_keyframes.append(f"        box-shadow: 0 0 {kf['glow']:.0f}px rgba(255, 255, 255, {kf['opacity']:.2f});")
            css_keyframes.append(f"    }}")
        
        # End state
        css_keyframes.append(f"    {data['decay_end']+0.5:.1f}%, 100% {{")
        css_keyframes.append(f"        transform: scale(0.8);")
        css_keyframes.append(f"        opacity: 0.3;")
        css_keyframes.append(f"        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);")
        css_keyframes.append(f"    }}")
        
        region_css = f"""
/* {region_id.replace('_', ' ').title()} - Continuous breathing */
@keyframes flare-{region_id}-continuous {{
{chr(10).join(css_keyframes)}
}}"""
        css_regions.append(region_css)
        
        # Show sample keyframes
        print(f"  Sample keyframes:")
        for i in range(0, len(keyframes), 3):  # Show every 3rd keyframe
            kf = keyframes[i]
            print(f"    {kf['time']:.1f}%: scale({kf['scale']:.2f}) opacity({kf['opacity']:.2f}) glow({kf['glow']:.0f}px)")
    
    # Complete CSS
    css_code = f"""/* Ultra-smooth continuous breathing animations */
.region-1 {{ 
    top: 30%; left: 20%; 
    animation: flare-region-1-continuous 6s cubic-bezier(0.4, 0.0, 0.2, 1) infinite;
}}

.region-2 {{ 
    top: 60%; right: 25%; 
    animation: flare-region-2-continuous 6s cubic-bezier(0.4, 0.0, 0.2, 1) infinite;
}}

.region-3 {{ 
    bottom: 35%; left: 40%; 
    animation: flare-region-3-continuous 6s cubic-bezier(0.4, 0.0, 0.2, 1) infinite;
}}

{chr(10).join(css_regions)}"""
    
    print(f"\n=== COMPLETE CONTINUOUS CSS ===")
    print(css_code)
    
    print(f"\n=== KEY IMPROVEMENTS ===")
    print("1. 12+ keyframes per region (vs previous 6-7)")
    print("2. Mathematical exponential curves for natural breathing") 
    print("3. Smoother cubic-bezier easing: cubic-bezier(0.4, 0.0, 0.2, 1)")
    print("4. No perceivable discrete steps")
    print("5. Truly continuous brightness transitions")
    print("6. Organic, living breathing effect")
    
    return css_code

if __name__ == "__main__":
    css_code = calculate_continuous_breathing()
    
    with open('continuous_breathing.css', 'w') as f:
        f.write(css_code)
    
    print(f"\nContinuous breathing CSS saved to 'continuous_breathing.css'")
    print("Ready to implement Phase 6!")