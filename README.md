# CIR 

Camera Information Retriever (CIR) is a Pytorch3D project developed in QLAB-Makerspace, Queen's University Belfast.

In brief, CIR is designed to retrieve the 3D position of the camera that produced a given native 256x256 2D image in a virtual atmosphere. This information is naturally used to reconstruct the imagery scene in virtuality by a 3D developmental tool like Blender.

The project aims to become an implement to reconstruct scenes for forensic purposes ranging from crime investigation to scientific applications in the real world.  

That said, this space focusses on concising the installation requirements of the retriever with it's supportive versions and documents the API & citations of the project.


## Installation -

The following operating systems and libraries with quoted versions are supportive requisites of the project :
 
   * Linux or macOS or Windows
   * Python ≥ 3.6
   * PyTorch 1.4 or 1.5
   * Torchvision 
   * gcc & g++ ≥ 4.9
   * fvcore
   * CUDA >= 9.2 

In detail, to install the above libraries direct into - [INSTALL.md](INSTALL.md). Libraries towards development of the project / altering the code can be installed under the same md. 
- [INSTALL.md](INSTALL.md)
  
## Documentation -

The complete API of the git can be didacted in the documentation - https://pytorch3d.readthedocs.io/en/latest/

The below are deep dive notes for the integral classes in this project in detail -

* [Heterogeneous Batching](docs/notes/batching.md)
* [Mesh IO](docs/notes/meshes_io.md)
* [Differentiable Rendering](docs/notes/renderer_getting_started.md)  


## License - 

Redistribuition of the script files are supportive of the conditions of Pytorch3D as retained by the LICENSE document.  
- [LICENSE.md](LICENSE)

## Citations

The following creators are cited here in 2020 for the development of Pytorch3D obliquely forming the root of the development of this project.

```
@misc{ravi2020pytorch3d,
  author =       {Nikhila Ravi and Jeremy Reizenstein and David Novotny and Taylor Gordon
                  and Wan-Yen Lo and Justin Johnson and Georgia Gkioxari},
  title =        {PyTorch3D},
  howpublished = {\url{https://github.com/facebookresearch/pytorch3d}},
  year =         {2020}
}
```
