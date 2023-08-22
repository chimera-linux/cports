pkgname = "talloc"
pkgver = "2.4.1"
pkgrel = 0
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
    "xsltproc",
]
makedepends = [
    "python-devel",
    "gettext-devel",
]
pkgdesc = "Hierarchical pool based memory allocator with destructors"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://talloc.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "410a547f08557007be0e88194f218868358edc0ab98c98ba8c167930db3d33f9"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
# FIXME cfi
hardening = ["vis", "!cfi"]
options = ["!cross"]


def do_configure(self):
    self.do(
        self.chroot_cwd / "configure",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        *configure_args,
    )


@subpackage("talloc-devel")
def _devel(self):
    return self.default_devel()


@subpackage("libpytalloc-util")
def _util(self):
    self.pkgdesc = f"{pkgdesc} (Python utility library)"

    return ["usr/lib/libpytalloc-util.so.*"]


@subpackage("talloc-python")
def _python(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"

    return ["usr/lib/python*"]
