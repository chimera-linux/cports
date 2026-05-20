pkgname = "dmenu"
pkgver = "5.4"
pkgrel = 0
build_style = "makefile"
make_use_env = True
hostmakedepends = [
    "freetype-devel",
    "libx11-devel",
    "libxft-devel",
    "libxinerama-devel",
    "pkgconf",
    "xorgproto",
]
pkgdesc = "Dynamic menu for X"
license = "MIT"
url = "https://tools.suckless.org/dmenu"
source = f"https://dl.suckless.org/tools/{pkgname}-{pkgver}.tar.gz"
sha256 = "8fbace2a0847aa80fe861066b118252dcc7b4ca0a0a8f3a93af02da8fb6cd453"
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("LICENSE")
