# image-compare
for comparing images using Python
a helper for a class project in my [Research Methods in Digital Humanities](https://libbyh.github.io/research-methods-in-digital-humanities/) class (Fall 2016)

# Steps I followed
    git clone http://github.com/libbyh/image-compare
    cd image-compare
    conda env create -f environment.yml
    source activate image-compare
    python avg-color.py
  
That returns the descriptive statistics of the BGR averages of the images in the image folder. We can then talk about the variation in blues, greens, and reds among those images.
