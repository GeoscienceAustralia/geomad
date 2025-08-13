# Geomad

A library for fast calculation of geomedian and median absolute deviation (MAD).

### Assumptions

We assume that the data stack dimensions are ordered so that the spatial dimensions are first (*y*,*x*), followed 
by the spectral dimension of size *p*, finishing with the temporal dimension. 

Algorithms reduce in the last dimension (typically, the temporal dimension).

----

For details of the scientific algorithms implemented, see:

- Roberts, D., Mueller, N., & McIntyre, A. (2017). High-dimensional pixel composites from earth observation time 
  series. IEEE Transactions on Geoscience and Remote Sensing, 55(11), 6254-6264.

- Roberts, D., Dunn, B., & Mueller, N. (2018). Open data cube products using high-dimensional statistics of time 
  series. In IGARSS 2018-2018 IEEE International Geoscience and Remote Sensing Symposium (pp. 8647-8650).
