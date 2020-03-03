This is completely copyrighted to Facebook AI Research.

# Installation


## Requirements

### Core library

The core library is written in PyTorch. Several components have underlying implementation in CUDA for improved performance. A subset of these components have CPU implementations in C++/Pytorch. It is advised to use PyTorch3d with GPU support in order to use all the features.

- Linux or macOS or Windows
- Python ≥ 3.6
- PyTorch 1.4
- torchvision that matches the PyTorch installation. You can install them together at pytorch.org to make sure of this.
- gcc & g++ ≥ 4.9
- CUDA 9.2 or 10.0 or 10.1
- [fvcore](https://github.com/facebookresearch/fvcore)

These can be installed by running:
```
conda create -n pytorch3d python=3.6
conda activate pytorch3d
conda install -c pytorch pytorch torchvision cudatoolkit=10.0
conda install -c conda-forge -c fvcore fvcore
```

### Tests/Linting and Demos

For developing on top of PyTorch3d or contributing, you will need to run the linter and tests. If you want to run any of the notebook tutorials as `docs/tutorials` you will also need matplotlib.
- scikit-image
- black
- isort
- flake8
- matplotlib
- tdqm
- jupyter
- imageio

These can be installed by running:
```
# Demos
conda install jupyter
pip install scikit-image matplotlib imageio

# Tests/Linting
pip install black isort flake8 flake8-bugbear flake8-comprehensions
```

## Build/Install Pytorch3d
After installing the above dependencies, run one of the following commands:

### 1. Install from Anaconda Cloud

```
# Anaconda Cloud
conda install pytorch3d -c pytorch3d
```

Or, to install a nightly (non-official, alpha) build:
```
# Anaconda Cloud
conda install pytorch3d -c pytorch3d-nightly
```

### 2. Install from GitHub
```
pip install 'git+https://github.com/facebookresearch/pytorch3d.git'
# (add --user if you don't have permission)
```

### 3. Install from a local clone
```
git clone https://github.com/facebookresearch/pytorch3d.git
cd pytorch3d && pip install -e .
```
To rebuild after installing from a local clone run, `rm -rf build/ **/*.so` then `pip install -e .`. You often need to rebuild pytorch3d after reinstalling PyTorch.

**Install from local clone on macOS:**
```
MACOSX_DEPLOYMENT_TARGET=10.14 CC=clang CXX=clang++ pip install -e .
```

**Install from local clone on Windows:**

If you are using pre-compiled pytorch 1.4 and torchvision 0.5, you should make the following changes to the pytorch source code to successfully compile with Visual Studio 2019 (MSVC 19.16.27034) and CUDA 10.1.

Change python/Lib/site-packages/torch/include/csrc/jit/script/module.h

L466, 476, 493, 506, 536
```
-static constexpr *
+static const *
```
Change python/Lib/site-packages/torch/include/csrc/jit/argument_spec.h

L190
```
-static constexpr size_t DEPTH_LIMIT = 128;
+static const size_t DEPTH_LIMIT = 128;
```

Change python/Lib/site-packages/torch/include/pybind11/cast.h

L1449
```
-explicit operator type&() { return *(this->value); }
+explicit operator type& () { return *((type*)(this->value)); }
```

After patching, you can go to "x64 Native Tools Command Prompt for VS 2019" to compile and install
```
cd pytorch3d
python3 setup.py install
```
After installing, verify whether all unit tests have passed
```
cd tests
python3 -m unittest discover -p *.py
```
