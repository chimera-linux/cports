pkgname = "faad2"
pkgver = "2.11.2"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_SHARED_LIBS=ON"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Free AAC decoder"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/faac"
source = f"https://github.com/knik0/faad2/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "3fcbd305e4abd34768c62050e18ca0986f7d9c5eca343fb98275418013065c0e"


@subpackage("faad2-devel")
def _(self):
    return self.default_devel()
