pkgname = "tangle"
pkgver = "0.1.1"
pkgrel = 0
build_style = "meson"
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "bash",
    "docbook-xsl-nons",
    "gperf",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "python-jinja2",
]
makedepends = ["libcap-devel"]
checkdepends = ["dbus"]
pkgdesc = "Subset of libsystemd providing sd-bus and sd-event"
license = "LGPL-2.1-or-later"
url = "https://github.com/chimera-linux/tangle"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "709b21b489af546e6376d09b4fe64a9f7131a9ac9651336727d557d58470360c"


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
