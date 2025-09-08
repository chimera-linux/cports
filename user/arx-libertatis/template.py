pkgname = "arx-libertatis"
# latest stable version has known crashes, e.g. in the first
# dungeon near the cobweb, due to c++ vector length-related bugs
pkgver = "1.2.1_git20240822"
pkgrel = 2
_gitrev = "5b95e4c5ca9d583f1b11c085326979772645e0f3"
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
license = "GPL-3.0-or-later"
url = "https://arx-libertatis.org"
source = [
    f"https://github.com/arx/ArxLibertatis/archive/{_gitrev}.tar.gz",
    "https://arx-libertatis.org/files/data/arx-libertatis-data-1.tar.xz",
]
source_paths = [".", "data-icons"]
sha256 = [
    "976a46086f256d33aa26fda9e62f423302a71a978f4a06d73fbe6d8f18c000d9",
    "79d943f060a48818e111fda658425d2879726ce53b02b6bb188a07b92aa88702",
]
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["!int"]
# not particularly useful
options = ["!check"]


def post_extract(self):
    self.mv("data-icons/icons/arx-libertatis-*", "data/icons", glob=True)
