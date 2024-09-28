pkgname = "tangle"
pkgver = "0.1.0"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "bash",
    "docbook-xsl-nons",
    "gperf",
    "meson",
    "pkgconf",
    "python-jinja2",
    "xsltproc",
]
makedepends = ["libcap-devel"]
checkdepends = ["dbus"]
pkgdesc = "Subset of libsystemd providing sd-bus and sd-event"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://github.com/chimera-linux/tangle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bab454b64f37c449f80e4ec1682f6cc1d28079e06a35c66fdccfd40c8dc2f2e7"


def post_install(self):
    # remove while elogind still provides them...
    self.uninstall("usr/share/man/man3")


@subpackage("tangle-progs")
def _(self):
    self.replaces = ["elogind<255.5-r4"]
    return self.default_progs()


@subpackage("tangle-devel")
def _(self):
    return self.default_devel()
