pkgname = "tevent"
pkgver = "0.16.1"
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
    "talloc-devel",
    "cmocka-devel",
    "gettext-devel",
]
pkgdesc = "Event system based on talloc"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tevent.samba.org"
source = f"https://download.samba.org/pub/tevent/tevent-{pkgver}.tar.gz"
sha256 = "362971e0f32dc1905f6fe4736319c4b8348c22dc85aa6c3f690a28efe548029e"
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
