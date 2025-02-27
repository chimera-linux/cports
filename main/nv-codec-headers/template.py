pkgname = "nv-codec-headers"
pkgver = "13.0.19.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Headers for Nvidia codec APIs"
license = "MIT"
url = "https://github.com/FFmpeg/nv-codec-headers"
source = f"{url}/archive/refs/tags/n{pkgver}.tar.gz"
sha256 = "86d15d1a7c0ac73a0eafdfc57bebfeba7da8264595bf531cf4d8db1c22940116"
# no tests, no license file
options = ["!check", "!distlicense"]
