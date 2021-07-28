# Tutorial for Deep Learning Theory Summer School at Princeton

This tutorial will cover the following aspects of over-parameterization discussed in https://arxiv.org/abs/2105.14368: 

1.  Interpolation is not at odds with generalization even in the presence of label noise (e.g. using larger and larger models is often beneficial for generalization).    
2.  Under certain conditions, as width goes to infinity, training neural networks with gradient descent is equivalent to solving kernel regression with the neural tangent kernel (NTK).  

These results are reviewed in Jupyter notebooks, which we suggest be read/walked through in the following order: 

1. **DoubleDescentTutorial.ipynb** - A review of the double descent phenomenon for neural networks where only the last layer is trained.  In this notebook, we begin by reviewing the connection between Random Fourier Features and the Gaussian kernel.  We then review the connection between random nonlinear networks and the corresponding neural network Gaussian process (NNGP) kernel.  
2. **DoubleDescentTutorialPart2.ipynb** - A review of the double descent phenomenon for neural networks where all layers are trained.  In this notebook, we demonstrate that the performance of neural networks improves as width increases (for classification of a subset of MNIST digits).  We then compare this with the performance of the infinite width limit of neural networks given by the NTK.  We demonstrate that the NTK is very easy to compute and use and gives superior performance than training neural networks in this setting. 



## A note on library dependencies.  
Most of this tutorial is meant to be run without a GPU (the GPU would be useful for training large neural networks).  I've attached a dl_environment.yml file that gives a list of all libraries I've downloaded along with versions.  I also downloaded auto_tqdm (i.e. pip install auto_tqdm) to keep track of progress bars for training neural networks (this is only used in *DoubleDescentTutorialPart2.ipynb* so far).  
