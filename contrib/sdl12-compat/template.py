pkgname = "sdl12-compat"
pkgver = "1.2.68"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["sdl-devel"]
pkgdesc = "SDL-1.2 compatibility layer"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Zlib"
url = "https://github.com/libsdl-org/sdl12-compat"
source = f"{url}/archive/refs/tags/release-{pkgver}.tar.gz"
sha256 = "63c6e4dcc1154299e6f363c872900be7f3dcb3e42b9f8f57e05442ec3d89d02d"


@subpackage("sdl12-compat-devel")
def _devel(self):
    return self.default_devel()
