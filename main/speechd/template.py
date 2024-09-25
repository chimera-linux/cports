pkgname = "speechd"
pkgver = "0.11.5"
pkgrel = 5
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
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://github.com/brailcom/speechd"
source = f"{url}/releases/download/{pkgver}/speech-dispatcher-{pkgver}.tar.gz"
sha256 = "1ce4759ffabbaf1aeb433a5ec0739be0676e9bdfbae9444a7b3be1b2af3ec12b"
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
