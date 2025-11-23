pkgname = "tevent"
pkgver = "0.17.1"
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
    "cmocka-devel",
    "gettext-devel",
    "python-devel",
    "talloc-devel",
]
pkgdesc = "Event system based on talloc"
license = "LGPL-3.0-or-later"
url = "https://tevent.samba.org"
source = f"https://download.samba.org/pub/tevent/tevent-{pkgver}.tar.gz"
sha256 = "1be2dea737cde25fe06621f84945e63eb71259e0c43e9f8f5da482dab1a7be92"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
# FIXME check fails in some envs
options = ["!cross", "!check", "linkundefver"]


@subpackage("tevent-devel")
def _(self):
    return self.default_devel()


@subpackage("tevent-python")
def _(self):
    self.subdesc = "Python bindings"
    self.depends += ["python"]

    return ["usr/lib/python*"]
