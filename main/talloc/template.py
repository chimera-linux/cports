pkgname = "talloc"
pkgver = "2.5.0"
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
sha256 = "912afa237510ae542a7733998eb18a12bcda35ab6729c8e2ddb43e8d0ebab007"
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
