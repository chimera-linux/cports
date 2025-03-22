pkgname = "i2pd"
pkgver = "2.56.0"
pkgrel = 0
build_style = "makefile"
make_build_args = ["DEBUG=no", "USE_STATIC=yes", "USE_UPNP=yes"]
makedepends = ["boost-devel", "zlib-ng-devel", "openssl3-devel", "miniupnpc"]
pkgdesc = "I2P Router written in C++"
license = "BSD-3-Clause"
url = "https://github.com/PurpleI2P/i2pd"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "eb83f7e98afeb3704d9ee0da2499205f73bab0b1becaf4494ccdcbe4295f8550"
# no check
options = ["!check"]


def pre_build(self):
    with open(f"{self.cwd}/Makefile", "r") as file:
        filedata = file.read()

    filedata = filedata.replace("$(shell $(CXX) -dumpmachine)", "freebsd")

    with open(f"{self.cwd}/Makefile", "w") as file:
        file.write(filedata)


def install(self):
    self.install_license("LICENSE")
    self.install_bin(f"{self.cwd}/i2pd")
