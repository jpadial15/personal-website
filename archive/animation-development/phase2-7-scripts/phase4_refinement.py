#!/usr/bin/env python3
"""
Phase 4: Fine-tuning - Multi-region First Peak
Divide first Gaussian into two overlapping regions, keep second peak as single region
"""

def calculate_refined_timing():
    """Calculate refined timing for realistic multi-region first peak"""
    print("=== Phase 4: Fine-Tuning Multi-Region Animation ===\n")
    
    # Original timing from Phase 2
    first_peak_time = 1.61  # 26.8%
    valley_time = 2.67      # 44.4% 
    second_peak_time = 4.00 # 66.7%
    animation_duration = 6.0
    
    print("New Animation Strategy:")
    print("- First Gaussian (1.61s): Two overlapping regions (1 + 3)")
    print("- Valley (2.67s): Keep region 3 dim after first peak")
    print("- Second Gaussian (4.00s): Single bright region (2)")
    
    # Calculate first peak subdivision
    peak1_start = first_peak_time - 0.4  # 1.21s
    peak1_end = first_peak_time + 0.5    # 2.11s
    peak1_duration = peak1_end - peak1_start  # 0.9s
    
    # Divide first peak into thirds
    third_duration = peak1_duration / 3  # 0.3s each
    
    region1_start = peak1_start                           # 1.21s - early starter
    region1_peak = peak1_start + third_duration          # 1.51s - peaks in 1st third
    region1_fade = peak1_start + 2 * third_duration      # 1.81s - fades in 2nd third
    
    region3_start = peak1_start + third_duration         # 1.51s - starts in 1st third
    region3_peak = peak1_start + 2 * third_duration      # 1.81s - peaks in 2nd third  
    region3_fade = peak1_end                             # 2.11s - fades at end
    
    # Convert to percentages
    def time_to_percent(time_sec):
        return (time_sec / animation_duration) * 100
    
    print(f"\n=== REFINED TIMING BREAKDOWN ===")
    print(f"First Peak Period: {peak1_start:.2f}s to {peak1_end:.2f}s")
    print(f"Duration: {peak1_duration:.2f}s, divided into {third_duration:.2f}s thirds")
    
    print(f"\nRegion 1 (Early starter):")
    print(f"  Start: {region1_start:.2f}s ({time_to_percent(region1_start):.1f}%)")
    print(f"  Peak:  {region1_peak:.2f}s ({time_to_percent(region1_peak):.1f}%)")
    print(f"  Fade:  {region1_fade:.2f}s ({time_to_percent(region1_fade):.1f}%)")
    
    print(f"\nRegion 3 (Late starter):")
    print(f"  Start: {region3_start:.2f}s ({time_to_percent(region3_start):.1f}%)")
    print(f"  Peak:  {region3_peak:.2f}s ({time_to_percent(region3_peak):.1f}%)")
    print(f"  Fade:  {region3_fade:.2f}s ({time_to_percent(region3_fade):.1f}%)")
    
    print(f"\nRegion 2 (Single second peak):")
    print(f"  Remains at: {second_peak_time:.2f}s ({time_to_percent(second_peak_time):.1f}%)")
    
    # Generate CSS
    css_code = f"""
/* Region-specific animations with multi-region first peak */
.region-1 {{ 
    top: 30%; left: 20%; 
    animation: flare-region-1-early 6s ease-in-out infinite;
}}

.region-2 {{ 
    top: 60%; right: 25%; 
    animation: flare-region-2-single 6s ease-in-out infinite;
}}

.region-3 {{ 
    bottom: 35%; left: 40%; 
    animation: flare-region-3-late 6s ease-in-out infinite;
}}

/* Region 1 - Early starter in first peak */
@keyframes flare-region-1-early {{
    0%, {time_to_percent(region1_start - 0.1):.1f}% {{
        transform: scale(0.8);
        opacity: 0.3;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }}
    {time_to_percent(region1_peak):.1f}% {{
        transform: scale(2.2);
        opacity: 1;
        box-shadow: 0 0 25px rgba(255, 255, 255, 1);
    }}
    {time_to_percent(region1_fade):.1f}%, 100% {{
        transform: scale(0.8);
        opacity: 0.3;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }}
}}

/* Region 3 - Late starter in first peak, overlaps with Region 1 */
@keyframes flare-region-3-late {{
    0%, {time_to_percent(region3_start - 0.1):.1f}% {{
        transform: scale(0.8);
        opacity: 0.3;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }}
    {time_to_percent(region3_peak):.1f}% {{
        transform: scale(2.0);
        opacity: 0.9;
        box-shadow: 0 0 22px rgba(255, 255, 255, 0.95);
    }}
    {time_to_percent(region3_fade):.1f}%, 100% {{
        transform: scale(0.8);
        opacity: 0.3;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }}
}}

/* Region 2 - Single dominant second peak */
@keyframes flare-region-2-single {{
    0%, {time_to_percent(second_peak_time - 0.3):.1f}% {{
        transform: scale(0.8);
        opacity: 0.3;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }}
    {time_to_percent(second_peak_time):.1f}% {{
        transform: scale(2.8);
        opacity: 1;
        box-shadow: 0 0 35px rgba(255, 255, 255, 1);
    }}
    {time_to_percent(second_peak_time + 0.5):.1f}%, 100% {{
        transform: scale(0.8);
        opacity: 0.3;
        box-shadow: 0 0 5px rgba(255, 255, 255, 0.4);
    }}
}}"""
    
    print(f"\n=== COMPLETE REFINED CSS CODE ===")
    print(css_code)
    
    print(f"\n=== EXPECTED BEHAVIOR ===")
    print(f"1. At ~1.5s: Region 1 starts brightening (first part of first peak)")
    print(f"2. At ~1.8s: Region 3 starts brightening while Region 1 still bright (overlap)")
    print(f"3. At ~2.1s: Both regions fade, creating the complete first Gaussian")
    print(f"4. At ~4.0s: Region 2 flares alone and brightest (second Gaussian)")
    print(f"5. Result: Complex first peak, simple second peak - much more realistic!")
    
    return css_code

if __name__ == "__main__":
    css_code = calculate_refined_timing()
    
    with open('refined_timing.css', 'w') as f:
        f.write(css_code)
    
    print(f"\nRefined CSS saved to 'refined_timing.css'")
    print("Ready to implement Phase 4!")