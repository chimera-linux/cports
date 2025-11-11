pkgname = "cyanrip"
pkgver = "0.9.3.1"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["meson", "ninja", "pkgconf"]
makedepends = [
    "curl-devel",
    "ffmpeg-devel",
    "libcdio-devel",
    "libcdio-paranoia-devel",
    "libmusicbrainz-devel",
]
pkgdesc = "Bule-ish CD ripper"
license = "LGPL-2.1-or-later"
url = "https://github.com/cyanreg/cyanrip"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "01b2679eb5b74b03af0b1232877c2267d141c32be1574a27e7eac19f86cb109b"
hardening = ["vis", "cfi"]
