# DemAPI
> Make customizable demotivators and motivators through imgonline.com.ua API. Supports async-await style

![Example](https://raw.githubusercontent.com/deknowny/demapi/main/assets/example.png)
***
__Documentation__: Check out [GUIDE.md](https://github.com/deknowny/demapi/blob/main/GUIDE.md)

[![Coverage Status](https://coveralls.io/repos/github/deknowny/demapi/badge.svg?branch=main)](https://coveralls.io/github/deknowny/demapi?branch=main)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/demapi)
![PyPI - Downloads](https://img.shields.io/pypi/dm/demapi)
![PyPI](https://img.shields.io/pypi/v/demapi)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/demapi)

# Features
* Sync and `async-await` style
* Customizable titles and explanation (size, colors etc.)
* Flexible output image (line breaks showed correctly)
* Not CPU-bound (through unlimited API)
* Full tests coverage
* Full typed

## Overview
Configure request params such as text, color, size etc.
And then download the image. Optionally save to disk otherwise
use `image.content` for raw bytes object
```python
import demapi


conf = demapi.Configure(
    base_photo="example.png",
    title="The first line",
    explanation="The second line"
)
image = conf.download()
image.save("example.png")
```

Or via `await` (based on `aiohttp`):

```python
image = await conf.coroutine_download()
```

# Installation
Install the latest version through `GitHub`:
```shell
python -m pip install https://github.com/deknowny/demapi/archive/main.zip
```
Or through `PyPI`
```shell
python -m pip install demapi
```

# Contributing
Check out [CONTRIBUTING.md](./CONTRIBUTING.md)

