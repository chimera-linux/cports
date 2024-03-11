pkgname = "libvgm"
_commit = "223b6f9d629feda1982dc4bbeebd19fa63b987fb"
pkgver = "0_git20240103"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DLIBRARY_TYPE=SHARED"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["zlib-devel", "libpulse-devel"]
pkgdesc = "VGM playback library"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "custom:libvgm"
url = "https://github.com/ValleyBell/libvgm"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "fb1eebb0d75ac3203c5b7639e847dbcb0c306a852c874ff9ba64519b67fdae92"
options = ["!distlicense"]
restricted = "non-redistributable"


@subpackage("libvgm-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libvgm-progs")
def _progs(self):
    return self.default_progs()
