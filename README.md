Based on your project structure, here's a comprehensive README file for your BOM3D Viewer project:

```markdown
# BOM3D Viewer

A comprehensive STEP file processing and visualization tool that extracts Bill of Materials (BOM) data and provides 3D web visualization capabilities.

## 🚀 Features

- **BOM Extraction**: Convert STEP (.stp/.step) files to structured JSON format with assembly hierarchy
- **3D Web Visualization**: Interactive 3D viewer for STEP models in the browser
- **Web Format Conversion**: Convert STEP files to GLB format for web compatibility
- **Assembly Analysis**: Detailed analysis of assembly structure and components
- **Real-time Processing**: Direct processing and visualization workflow

## 📋 Prerequisites

- **Python**: 3.8 or higher
- **Conda Environment**: pyoccenv (or similar OpenCASCADE environment)
- **Web Browser**: Modern browser with WebGL support
- **Operating System**: Windows, macOS, or Linux

## ⚡ Quick Start

### 1. Environment Setup

Ensure your conda environment is activated:
```
conda activate pyoccenv
```

If you need to create the environment:
```
conda create -n pyoccenv python=3.9
conda activate pyoccenv
conda install -c conda-forge pythonocc-core
pip install cascadio
```

### 2. Project Structure
```
BOM3D Viewer/
├── model/                    # Input STEP files directory
│   └── your_model.step      # Place your STEP files here
├── output/                  # Generated output files
│   ├── bom/                # BOM JSON files
│   └── web/                # GLB and web assets
├── bom_extractor.py        # BOM extraction tool
├── web_converter.py        # STEP to GLB converter
├── index.html              # 3D Web Viewer
└── README.md               # This file
```

### 3. Usage Workflow

**Step 1: Place Your STEP File**
```
# Copy your STEP file to the model directory
cp your_model.step model/
```

**Step 2: Extract BOM Data**
```
python bom_extractor.py
```

**Step 3: Convert to Web Format**
```
python web_converter.py
```

**Step 4: View in Browser**
```
# Open index.html in your web browser
# Or use a local server:
python -m http.server 8000
# Then visit: http://localhost:8000
```

## 🛠️ Tools Description

### BOM Extractor (`bom_extractor.py`)
- **Purpose**: Extracts assembly structure from STEP files
- **Input**: STEP files from `model/` directory
- **Output**: `output/bom/bom_data.json`
- **Features**:
  - Assembly hierarchy analysis
  - Part counting and classification
  - Color information extraction
  - Component location data

**Example Output:**
```
{
  "filename": "example.step",
  "timestamp": "2025-08-14T12:30:00",
  "total_parts": 25,
  "total_assemblies": 5,
  "assembly_tree": [...]
}
```

### Web Converter (`web_converter.py`)
- **Purpose**: Converts STEP files to GLB format
- **Input**: STEP files from `model/` directory
- **Output**: `output/web/model.glb`
- **Features**:
  - Three.js compatible output
  - Geometry preservation
  - Optimized for web viewing

### 3D Web Viewer (`index.html`)
- **Purpose**: Interactive 3D visualization in browser
- **Features**:
  - Pan, zoom, rotate controls
  - Material and lighting
  - Assembly tree navigation
  - BOM data integration

## 📊 Supported File Formats

### Input Formats
- **.step** - STEP file format
- **.stp** - STEP file format (alternative extension)

### Output Formats
- **JSON** - Bill of Materials data
- **GLB** - Binary glTF for web visualization

## 🎯 Detailed Usage

### Processing a New Model

1. **Add STEP File**
```
# Place your STEP file in the model directory
cp "C:\path\to\your\model.step" model\
```

2. **Extract BOM**
```
conda activate pyoccenv
python bom_extractor.py
```
Output: Detailed console analysis + `output/bom/bom_data.json`

3. **Convert for Web**
```
python web_converter.py
```
Output: `output/web/model.glb`

4. **View Results**
```
# Open index.html in browser or run local server
python -m http.server 8000
```

### Batch Processing Multiple Files

```
# Process multiple STEP files
for file in model/*.step; do
    echo "Processing $file"
    python bom_extractor.py
    python web_converter.py
done
```

## 🔧 Configuration

### Environment Variables
```
# Optional: Set custom paths
export MODEL_DIR="path/to/models"
export OUTPUT_DIR="path/to/output"
```

### Web Viewer Settings
Edit `index.html` to customize:
- Camera settings
- Lighting configuration
- UI elements
- Color schemes

## 📈 Performance Guidelines

### File Size Recommendations
- **Small Models** ( 200MB): 5+ minutes

### System Requirements
- **RAM**: 4GB minimum, 8GB+ recommended
- **Storage**: 2x model file size free space
- **CPU**: Multi-core recommended for large files

## 🔍 Troubleshooting

### Common Issues

**1. "No module named 'OCC'" Error**
```
conda activate pyoccenv
conda install -c conda-forge pythonocc-core
```

**2. "Cascadio not found" Error**
```
pip install --upgrade cascadio
```

**3. "No STEP files found" Error**
- Verify files are in `model/` directory
- Check file extensions (.step, .stp)
- Ensure proper file permissions

**4. Web Viewer Not Loading**
- Use local server: `python -m http.server 8000`
- Check browser console for errors
- Verify GLB file exists in `output/web/`

**5. Empty BOM Output**
- Check STEP file integrity
- Verify file is a valid assembly
- Review console output for errors

### Performance Issues

**Slow Processing:**
- Close unnecessary applications
- Use SSD storage if available
- Process smaller files first to test

**Memory Errors:**
- Reduce model complexity
- Restart Python session
- Check available system memory

## 📦 Dependencies

### Required Packages
```
pythonocc-core>=7.6.0    # OpenCASCADE Python bindings
cascadio>=0.1.0          # STEP to GLB conversion
python>=3.8              # Python interpreter
```

### Optional Packages
```
numpy                    # Numerical computations
matplotlib               # Plotting and visualization
jupyter                  # Interactive development
```

## 🌐 Web Viewer Features

### Controls
- **Mouse**: Rotate view
- **Wheel**: Zoom in/out
- **Right-click + Drag**: Pan view
- **Double-click**: Reset view

### Interface Elements
- Model information panel
- Assembly tree navigator
- Part highlighting
- Material properties display

## 🔄 Workflow Integration

### Automated Pipeline
```
#!/bin/bash
# Process all STEP files in model directory
echo "Starting BOM3D processing pipeline..."

# Extract BOM data
python bom_extractor.py

# Convert to web format
python web_converter.py

# Start local server
echo "Starting web server..."
python -m http.server 8000

echo "Pipeline complete! Visit http://localhost:8000"
```

## 📚 API Reference

### BOMExtractor Class
```
from bom_extractor import BOMExtractor

extractor = BOMExtractor()
result = extractor.extract_bom_data(input_file, output_dir)
```

### WebConverter Class
```
from web_converter import WebConverter

converter = WebConverter()
result = converter.convert_to_web_format(input_file, output_dir)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with sample STEP files
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:

1. **Check Console Output**: Review error messages
2. **Verify Environment**: Ensure pyoccenv is activated
3. **File Compatibility**: Test with known good STEP files
4. **Browser Compatibility**: Use modern browsers with WebGL

## 📈 Project Roadmap

### Planned Features
- [ ] Multiple file batch processing UI
- [ ] Advanced material property extraction
- [ ] Export to other CAD formats
- [ ] Assembly animation capabilities
- [ ] Measurement tools in web viewer

### Recent Updates
- ✅ Initial BOM extraction functionality
- ✅ Web GLB conversion
- ✅ Interactive 3D viewer
- ✅ Assembly hierarchy analysis

---

## 🎉 Getting Started Checklist

- [ ] Activate conda environment: `conda activate pyoccenv`
- [ ] Place STEP file in `model/` directory
- [ ] Run BOM extraction: `python bom_extractor.py`
- [ ] Run web conversion: `python web_converter.py`
- [ ] Open `index.html` in browser
- [ ] Explore your 3D model!

**Happy 3D Viewing! 🚀**

---

*Last updated: August 14, 2025*
```

This README file provides comprehensive documentation for your BOM3D Viewer project, including setup instructions, usage examples, troubleshooting guides, and feature descriptions tailored to your specific project structure and files.