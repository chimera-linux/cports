pkgname = "arx-libertatis"
pkgver = "1.2.1"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "python"]
makedepends = [
    "boost-devel",
    "freetype-devel",
    "glew-devel",
    "glm",
    "libepoxy-devel",
    "mesa-devel",
    "openal-soft-devel",
    "sdl2-compat-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Improved open source engine for Arx Fatalis"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://arx-libertatis.org"
source = f"{url}/files/arx-libertatis-{pkgver}.tar.xz"
sha256 = "aafd8831ee2d187d7647ad671a03aabd2df3b7248b0bac0b3ac36ffeb441aedf"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["!int"]
# not particularly useful
options = ["!check"]
