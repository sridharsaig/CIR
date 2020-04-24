# Modified-Camera_Position_Optimizer

Height Estimator is a project built upon Pytorch3D in QLAB (Makerspace Lab), Queen's University Belfast.

In brief, the project is an implement towards achieveing successful reconstruction of the conditions of a 3D scene given a native image of the selfsame scene and a wavefront obj format file.

This space focusses on concising installation requirements with supportive versions and documents the API & citations from Pytorch3D -

The Project Blog gives further insight of the project surplus the journey of developing this conception.

## Installation -

The following operating systems and libraries with quoted versions are requisites of the project :
 
   * Linux or macOS or Windows
   * Python ≥ 3.6
   * PyTorch 1.4 or 1.5
   * Torchvision 
   * gcc & g++ ≥ 4.9
   * fvcore
   * CUDA >= 9.2 

In detail, to install the above libraries [Install.md] (#INSTALL.md) is preferrable. In addition, libraries towards development of the project / altering the source code can be installed under the same md. 
  
## Documentation -

The complete API of the git can be didacted in the documentation - https://pytorch3d.readthedocs.io/en/latest/

The below are deep dive notes for the project in detail -

* [Heterogeneous Batching] (#) 
* [Mesh IO] (#) 
* [Differentiable Rendering] (#) 


## License 

Redistribuition of the script files are supportive of the conditions of Pytorch3D as retained by the LICENSE document.  
- [License.md](#LICENSE.md)

## Citation

The following creators cited here in 2020 for the development of Pytorch3D consequently forming the root of the development of this project.

```
@misc{ravi2020pytorch3d,
  author =       {Nikhila Ravi and Jeremy Reizenstein and David Novotny and Taylor Gordon
                  and Wan-Yen Lo and Justin Johnson and Georgia Gkioxari},
  title =        {PyTorch3D},
  howpublished = {\url{https://github.com/facebookresearch/pytorch3d}},
  year =         {2020}
}
```
