pkgname = "libei"
pkgver = "1.6.0"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsd-bus-provider=libelogind",
    "-Dliboeffis=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "python-jinja2",
]
makedepends = [
    "elogind-devel",
    "libevdev-devel",
    "libxkbcommon-devel",
]
checkdepends = [
    "dbus",
    "glib",
    "python-attrs",
    "python-dbusmock",
    "python-gobject",
    "python-pytest",
    "python-pyyaml",
    "python-structlog",
]
pkgdesc = "Emulated Input Library"
license = "MIT"
url = "https://gitlab.freedesktop.org/libinput/libei"
_munit = "fbbdf1467eb0d04a6ee465def2e529e4c87f2118"
source = [
    f"https://gitlab.freedesktop.org/libinput/libei/-/archive/{pkgver}/libei-{pkgver}.tar.bz2",
    f"https://github.com/nemequ/munit/archive/{_munit}.tar.gz",
]
source_paths = [".", "subprojects/munit"]
sha256 = [
    "5ed6078fa63afd554cc04b1001675615da0ed8fe23b80492ab63403140b5a830",
    "d0c8bf80b9804d4df5301bd428702352fe7e14f84f22027c3a2c084a0d9f69a7",
]


def post_extract(self):
    # clock skew caused by bad tarball dates
    for f in self.cwd.rglob("*"):
        f.touch()


def post_install(self):
    self.install_license("COPYING")


@subpackage("libei-devel")
def _(self):
    return self.default_devel()
