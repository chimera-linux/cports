pkgname = "carla"
pkgver = "2.5.9"
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
]
depends = ["python"]
pkgdesc = "Audio plugin host"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-2.0-or-later"
url = "https://kx.studio/Applications:Carla"
source = f"https://github.com/falkTX/Carla/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "226fb5d646b7541b82035080190e7440df1f92372fb798b4ad49289570e5ad81"
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
