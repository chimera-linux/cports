pkgname = "nv-codec-headers"
pkgver = "12.2.72.0"
pkgrel = 0
build_style = "makefile"
hostmakedepends = ["pkgconf"]
pkgdesc = "Headers for Nvidia codec APIs"
maintainer = "Denis Strizhkin <strdenis02@gmail.com>"
license = "MIT"
url = "https://github.com/FFmpeg/nv-codec-headers"
source = f"{url}/archive/refs/tags/n{pkgver}.tar.gz"
sha256 = "dbeaec433d93b850714760282f1d0992b1254fc3b5a6cb7d76fc1340a1e47563"
# no tests, no license file
options = ["!check", "!distlicense"]
