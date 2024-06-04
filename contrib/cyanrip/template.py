pkgname = "cyanrip"
pkgver = "0.9.3"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libcurl-devel",
    "libmusicbrainz-devel",
]
pkgdesc = "Bule-ish CD ripper"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "LGPL-2.1-or-later"
url = "https://github.com/cyanreg/cyanrip"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "0a85ff156a0752e8bf082f6efaeeac882e9a6e9d1b5bdbae5f0e77310f3b22a0"
hardening = ["vis", "cfi"]
