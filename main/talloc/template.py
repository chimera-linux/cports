pkgname = "talloc"
pkgver = "2.4.3"
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
    "docbook-xsl-nons",
    "gettext",
    "libxslt-progs",
    "pkgconf",
    "python",
]
makedepends = [
    "gettext-devel",
    "python-devel",
]
pkgdesc = "Hierarchical pool based memory allocator with destructors"
license = "LGPL-3.0-or-later"
url = "https://talloc.samba.org"
source = f"https://download.samba.org/pub/talloc/talloc-{pkgver}.tar.gz"
sha256 = "dc46c40b9f46bb34dd97fe41f548b0e8b247b77a918576733c528e83abd854dd"
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
