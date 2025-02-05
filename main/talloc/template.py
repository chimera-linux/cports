pkgname = "talloc"
pkgver = "2.4.2"
pkgrel = 1
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath",
    "--disable-rpath-install",
    "--builtin-libraries=replace",
    "--bundled-libraries=NONE",
]
hostmakedepends = [
    "pkgconf",
    "python",
    "gettext",
    "docbook-xsl-nons",
    "libxslt-progs",
]
makedepends = [
    "python-devel",
    "gettext-devel",
]
pkgdesc = "Hierarchical pool based memory allocator with destructors"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://talloc.samba.org"
source = f"https://download.samba.org/pub/talloc/talloc-{pkgver}.tar.gz"
sha256 = "85ecf9e465e20f98f9950a52e9a411e14320bc555fa257d87697b7e7a9b1d8a6"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
hardening = ["vis", "!cfi"]
options = ["!cross", "linkundefver"]


def configure(self):
    self.do(
        self.chroot_cwd / "configure",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        *configure_args,
    )


@subpackage("talloc-devel")
def _(self):
    return self.default_devel()


@subpackage("talloc-python-libs")
def _(self):
    self.subdesc = "Python utility library"
    # transitional
    self.provides = [self.with_pkgver("libpytalloc-util")]

    return ["usr/lib/libpytalloc-util.so.*"]


@subpackage("talloc-python")
def _(self):
    self.subdesc = "Python bindings"

    return ["usr/lib/python*"]
