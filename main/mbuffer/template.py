pkgname = "mbuffer"
pkgver = "20250429"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
make_dir = "."
hostmakedepends = ["cmake", "ninja"]
makedepends = [
    "linux-headers",
    "openssl3-devel",
]
pkgdesc = "Tool for buffering data streams"
license = "GPL-3.0-only"
url = "https://www.maier-komor.de/mbuffer.html"
source = f"https://www.maier-komor.de/software/mbuffer/mbuffer-{pkgver}.tgz"
sha256 = "a853ef720d5fc3ef47c1788f9657477b76d70ab0c9b8a7d96e995e31e3536bbf"
tool_flags = {"CFLAGS": ['-DSYSCONFDIR="/etc"']}


def pre_configure(self):
    self.do("sh", "mkversion.sh")
