pkgname = "libmad"
pkgver = "0.16.5"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DEXAMPLE=OFF"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "MPEG audio decoder library"
license = "GPL-2.0-or-later"
url = "https://codeberg.org/tenacityteam/libmad"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "e32320a010e3cc00bfa66e0cde523a969313cddfd81e07ec4e3ef06d10ad3fe0"
# decoding corrupt files will crash
hardening = ["!int"]


@subpackage("libmad-devel")
def _(self):
    return self.default_devel()
