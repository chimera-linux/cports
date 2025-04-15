pkgname = "mygui"
pkgver = "3.4.2"
pkgrel = 6
build_style = "cmake"
configure_args = [
    "-DCMAKE_POLICY_VERSION_MINIMUM=3.5",
    "-DMYGUI_BUILD_DEMOS=OFF",
    "-DMYGUI_BUILD_TOOLS=OFF",
    "-DMYGUI_RENDERSYSTEM=1",
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen"]
makedepends = [
    "boost-devel",
    "freetype-devel",
    "libx11-devel",
    "mesa-devel",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Fast, flexible and simple GUI"
license = "MIT"
url = "https://github.com/MyGUI"
source = f"{url}/mygui/archive/MyGUI{pkgver}.tar.gz"
sha256 = "1cc45fb96c9438e3476778449af0378443d84794a458978a29c75306e45dd45a"
# unit tests are off
options = ["!check"]


def post_install(self):
    self.install_license("COPYING.MIT")


@subpackage("mygui-devel")
def _(self):
    return self.default_devel()
