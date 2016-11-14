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

# Example output
|stat|blue|green|red|
|---|---:|---:|---:|
|count  |  5.000000   | 5.000000   | 5.000000|
|mean   | 90.800000 | 113.600000 | 127.200000|
|std    | 14.584238 |  17.184295 |  19.904773|
|min    | 80.000000 |  98.000000 | 107.000000|
|25%    | 82.000000 |  99.000000 | 113.000000|
|50%    | 83.000000 | 109.000000 | 119.000000|
|75%    | 94.000000 | 124.000000 | 148.000000|
|max    |115.000000 | 138.000000 | 149.000000|
