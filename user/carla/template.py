pkgname = "carla"
pkgver = "2.5.10"
pkgrel = 0
build_style = "makefile"
make_check_target = "tests"
make_check_args = ["PEDANTIC_CFLAGS=", "PEDANTIC_CXXFLAGS="]
hostmakedepends = ["pkgconf"]
makedepends = [
    "chimerautils-devel",
    "file-devel",
    "fluidsynth-devel",
    "liblo-devel",
    "libpulse-devel",
    "libx11-devel",
    "linux-headers",
]
depends = ["python"]
pkgdesc = "Audio plugin host"
license = "GPL-2.0-or-later"
url = "https://kx.studio/Applications:Carla"
source = f"https://github.com/falkTX/Carla/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ae2835b12081f7271a6b0b25d34b87d36b022c40370028ca4a10f90fcedfa661"
tool_flags = {"LDFLAGS": ["-lfts"]}
# needs to exist, even if empty
file_modes = {"+usr/share/carla/resources": ("root", "root", 0o755, True)}
# check: no proper test suite
options = ["!check"]


def configure(self):
    # print which features will be built
    self.make.invoke(["features"])


@subpackage("carla-devel")
def _(self):
    return self.default_devel()
