#!/usr/bin/env python3
"""
Phase 7: Enhanced Blending - Extended Overlapping Periods
Extend timing ranges so regions blend together more naturally
"""

def calculate_blended_timing():
    """Calculate extended timing ranges for better region blending"""
    print("=== Phase 7: Enhanced Blending Animation ===\n")
    
    print("Goal: More natural blending between regions")
    print("- Extend Region 1 decay to overlap more with Region 3")
    print("- Extend Region 3 decay to bridge to Region 2")
    print("- Start Region 2 earlier for smoother transition")
    print("- Create continuous 'handoff' between regions")
    
    # New extended timing ranges
    regions = {
        'region_1': {
            'name': 'First Peak - Extended decay for blending',
            'buildup_start': 17.2,
            'peak_time': 25.2,
            'decay_end': 42.0,      # Extended from 37.2% to 42%
            'max_scale': 2.2,
            'max_glow': 25
        },
        'region_3': {
            'name': 'Overlap/Shoulder - Extended bridge',
            'buildup_start': 22.2,
            'peak_time': 30.2,
            'decay_end': 58.0,      # Extended from 40.2% to 58%
            'max_scale': 2.0,
            'max_glow': 22
        },
        'region_2': {
            'name': 'Dominant Second Peak - Earlier start',
            'buildup_start': 53.0,  # Earlier from 56.7% to 53%
            'peak_time': 66.7,
            'decay_end': 82.2,
            'max_scale': 2.8,
            'max_glow': 35
        }
    }
    
    def generate_blended_keyframes(region_data):
        """Generate keyframes with extended blending periods"""
        peak = region_data['peak_time']
        start = region_data['buildup_start']
        end = region_data['decay_end']
        max_scale = region_data['max_scale']
        max_glow = region_data['max_glow']
        
        keyframes = []
        
        # More gradual buildup points
        buildup_points = [
            start, 
            start + (peak-start)*0.15,  # Very early
            start + (peak-start)*0.35,  # Early
            start + (peak-start)*0.60,  # Mid
            start + (peak-start)*0.85,  # Late
            peak                        # Peak
        ]
        
        # Extended decay points for better blending
        decay_points = [
            peak + (end-peak)*0.08,   # Just after peak
            peak + (end-peak)*0.20,   # Early decay
            peak + (end-peak)*0.35,   # Mid decay
            peak + (end-peak)*0.55,   # Late decay
            peak + (end-peak)*0.75,   # Very late decay
            peak + (end-peak)*0.90,   # Final fade
            end                       # End
        ]
        
        all_points = buildup_points + decay_points[1:]  # Skip duplicate peak
        
        for i, time_percent in enumerate(all_points):
            if time_percent <= peak:
                # Buildup - smooth exponential curve
                progress = (time_percent - start) / (peak - start)
                brightness_factor = progress ** 1.3  # Gentler curve for blending
            else:
                # Decay - very gradual exponential decay for extended blending
                progress = (time_percent - peak) / (end - peak)
                import math
                brightness_factor = math.exp(-1.8 * progress)  # Slower decay for blending
            
            # Calculate smooth values with minimum brightness for blending
            min_opacity = 0.25  # Higher minimum for better blending
            opacity = min_opacity + ((1.0 - min_opacity) * brightness_factor)
            scale = 0.8 + ((max_scale - 0.8) * brightness_factor)
            glow = 4 + ((max_glow - 4) * brightness_factor)
            
            keyframes.append({
                'time': time_percent,
                'opacity': opacity,
                'scale': scale,
                'glow': glow
            })
        
        return keyframes
    
    print(f"\n=== EXTENDED BLENDING PERIODS ===")
    
    css_regions = []
    
    for region_id, data in regions.items():
        keyframes = generate_blended_keyframes(data)
        
        print(f"\n{region_id.upper()} - {data['name']}:")
        print(f"  Buildup: {data['buildup_start']:.1f}% - {data['peak_time']:.1f}%")
        print(f"  Peak: {data['peak_time']:.1f}%")
        print(f"  Decay: {data['peak_time']:.1f}% - {data['decay_end']:.1f}%")
        print(f"  Total duration: {data['decay_end'] - data['buildup_start']:.1f}% of animation")
        
        # Build CSS keyframes with extended periods
        css_keyframes = []
        
        # Start state with higher minimum for blending
        css_keyframes.append(f"    0%, {data['buildup_start']-1.0:.1f}% {{")
        css_keyframes.append(f"        transform: scale(0.8);")
        css_keyframes.append(f"        opacity: 0.25;")  # Higher minimum
        css_keyframes.append(f"        box-shadow: 0 0 4px rgba(255, 255, 255, 0.3);")
        css_keyframes.append(f"    }}")
        
        # Blended keyframes
        for kf in keyframes:
            css_keyframes.append(f"    {kf['time']:.1f}% {{")
            css_keyframes.append(f"        transform: scale({kf['scale']:.2f});")
            css_keyframes.append(f"        opacity: {kf['opacity']:.2f};")
            css_keyframes.append(f"        box-shadow: 0 0 {kf['glow']:.0f}px rgba(255, 255, 255, {kf['opacity']:.2f});")
            css_keyframes.append(f"    }}")
        
        # End state with gradual return to minimum
        css_keyframes.append(f"    {data['decay_end']+2.0:.1f}%, 100% {{")
        css_keyframes.append(f"        transform: scale(0.8);")
        css_keyframes.append(f"        opacity: 0.25;")  # Higher minimum
        css_keyframes.append(f"        box-shadow: 0 0 4px rgba(255, 255, 255, 0.3);")
        css_keyframes.append(f"    }}")
        
        region_css = f"""
/* {region_id.replace('_', ' ').title()} - Enhanced blending */
@keyframes flare-{region_id}-blended {{
{chr(10).join(css_keyframes)}
}}"""
        css_regions.append(region_css)
    
    # Complete CSS with enhanced blending
    css_code = f"""/* Enhanced blending with extended overlapping periods */
.region-1 {{ 
    top: 30%; left: 20%; 
    animation: flare-region-1-blended 6s cubic-bezier(0.35, 0.0, 0.25, 1) infinite;
}}

.region-2 {{ 
    top: 60%; right: 25%; 
    animation: flare-region-2-blended 6s cubic-bezier(0.35, 0.0, 0.25, 1) infinite;
}}

.region-3 {{ 
    bottom: 35%; left: 40%; 
    animation: flare-region-3-blended 6s cubic-bezier(0.35, 0.0, 0.25, 1) infinite;
}}

{chr(10).join(css_regions)}"""
    
    print(f"\n=== BLENDING IMPROVEMENTS ===")
    print("1. Extended Region 1 decay: 25.2% → 42% (overlaps with Region 3)")
    print("2. Extended Region 3 decay: 30.2% → 58% (bridges to Region 2)")
    print("3. Earlier Region 2 start: 56.7% → 53% (overlaps with Region 3)")
    print("4. Higher minimum opacity: 0.3 → 0.25 for better blending")
    print("5. Gentler decay curves for smoother transitions")
    print("6. Continuous 'handoff' between all three regions")
    
    print(f"\n=== OVERLAP PERIODS ===")
    print("Region 1 & 3 overlap: 22.2% - 42% (19.8% of animation)")
    print("Region 3 & 2 overlap: 53% - 58% (5% of animation)")
    print("Total coverage: 17.2% - 82.2% (65% of animation has active flaring)")
    
    return css_code

if __name__ == "__main__":
    css_code = calculate_blended_timing()
    
    with open('blended_timing.css', 'w') as f:
        f.write(css_code)
    
    print(f"\nBlended timing CSS saved to 'blended_timing.css'")
    print("Ready to implement Phase 7!")