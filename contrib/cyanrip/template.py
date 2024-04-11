pkgname = "cyanrip"
pkgver = "0.9.2"
pkgrel = 0
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
sha256 = "55ee337fde224fc98c954134f7ae42f38f9e7b59421514d8acce3a875e5ed2b7"
hardening = ["vis", "cfi"]
