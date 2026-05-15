pkgname = "physfs"
pkgver = "3.2.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DCMAKE_POLICY_VERSION_MINIMUM=3.5"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
pkgdesc = "VFS abstraction library for archives"
license = "Zlib"
url = "https://github.com/icculus/physfs"
source = f"{url}/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "1991500eaeb8d5325e3a8361847ff3bf8e03ec89252b7915e1f25b3f8ab5d560"


@subpackage("physfs-devel")
def _(self):
    return self.default_devel()
