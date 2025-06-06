def get_ai_recommendation(biomarkers, logic_gate, input_signals, output):
    """
    Generate analysis and recommendations for quantum dot logic circuits.
    
    Args:
        biomarkers (list): List of selected biomarkers
        logic_gate (str): Name of the selected logic gate
        input_signals (list): List of input signals (0 or 1)
        output (int): Result of the logic gate operation
        
    Returns:
        str: Analysis and recommendations
    """
    # Create a detailed analysis based on the inputs
    analysis = f"""
### Circuit Analysis
- **Selected Biomarkers**: {', '.join(biomarkers)}
- **Logic Gate**: {logic_gate}
- **Input Signals**: {input_signals}
- **Output**: {output}

### Recommendations
1. **Biomarker Selection**:
   - The combination of {', '.join(biomarkers)} provides good coverage for breast cancer detection
   - Consider adding ER/PR biomarkers for more comprehensive analysis

2. **Logic Gate Choice**:
   - The {logic_gate} gate is appropriate for this application
   - This gate helps in {'confirming multiple conditions' if logic_gate in ['AND', 'NAND'] else 'detecting any of the conditions' if logic_gate == 'OR' else 'inverting the detection signal'}

3. **Quantum Dot Selection**:
   - Use pH-sensitive QDs for better tissue penetration
   - Consider NIR QDs for deeper tissue imaging
   - Ensure proper surface functionalization for biomarker binding

4. **Experimental Considerations**:
   - Optimize incubation time for biomarker binding
   - Use appropriate controls for each biomarker
   - Consider multiplexing capabilities of selected QDs
    """
    
    return analysis 