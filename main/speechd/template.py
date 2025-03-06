pkgname = "speechd"
pkgver = "0.12.0"
pkgrel = 1
build_style = "gnu_configure"
configure_args = [
    "--disable-static",
    "--with-espeak-ng",
    "--without-baratinoo",
    "--without-flite",
    "--without-ibmtts",
    "--without-kali",
    "--without-voxin",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "libtool",
    "pkgconf",
    "python",
]
makedepends = [
    "dotconf-devel",
    "espeak-ng-devel",
    "glib-devel",
    "libpulse-devel",
    "libsndfile-devel",
]
depends = ["python-pyxdg"]
install_if = [self.with_pkgver("speechd-meta")]
pkgdesc = "High level interface to speech synthesis"
license = "GPL-2.0-or-later"
url = "https://github.com/brailcom/speechd"
source = f"{url}/releases/download/{pkgver}/speech-dispatcher-{pkgver}.tar.gz"
sha256 = "e1dd0bfa24b8338545e165451330adf51c4c0dca862b1b67e76fba5142dbbb74"
# strcasestr
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}


@subpackage("speechd-devel")
def _(self):
    return self.default_devel()


@subpackage("speechd-libs")
def _(self):
    return self.default_libs()


@subpackage("speechd-meta")
def _(self):
    self.subdesc = "recommends package"
    self.options = ["empty"]
    return []
