pkgname = "speechd"
pkgver = "0.12.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--libexecdir=/usr/lib",  # XXX drop libexec
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
checkdepends = ["texinfo"]
depends = ["python-pyxdg"]
install_if = [self.with_pkgver("speechd-meta")]
pkgdesc = "High level interface to speech synthesis"
license = "GPL-2.0-or-later"
url = "https://github.com/brailcom/speechd"
source = f"{url}/releases/download/{pkgver}/speech-dispatcher-{pkgver}.tar.gz"
sha256 = "b14a5238d287d2dcce4dd42bbd66ca65fa228e7e683708267f7b34036f7ba4b4"
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
