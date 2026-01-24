pkgname = "virt-manager"
pkgver = "5.1.0"
pkgrel = 0
build_style = "meson"
_deps = [
    "libarchive-progs",
    "libosinfo",
    "libxml2-python",
    "python-gobject",
    "python-libvirt",
    "python-requests",
    "qemu-img",
    "xorriso",
]
hostmakedepends = [
    "gettext",
    "gtk+3-update-icon-cache",
    "meson",
    "python-docutils",
]
depends = [
    "gtk-vnc",
    "gtksourceview4",
    "libvirt-glib",
    "python",
    "spice-gtk",
    "vte-gtk3",
    self.with_pkgver("virt-manager-progs"),
]
checkdepends = ["python-pytest", *_deps]
pkgdesc = "GUI for managing virtual machines"
license = "GPL-2.0-or-later"
url = "https://virt-manager.org"
source = (
    f"https://releases.pagure.org/virt-manager/virt-manager-{pkgver}.tar.xz"
)
sha256 = "ccfc44b6c1c0be8398beb687c675d9ea4ca1c721dfb67bd639209a7b0dec11b1"


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/share")


@subpackage("virt-manager-progs")
def _(self):
    self.depends = [*_deps]
    self.pkgdesc = "Programs to create and clone virtual machines"

    return [
        "usr/bin/virt-clone",
        "usr/bin/virt-install",
        "usr/bin/virt-xml",
        "usr/share/man/man1/virt-install.1",
        "usr/share/man/man1/virt-clone.1",
        "usr/share/man/man1/virt-xml.1",
        "usr/share/virt-manager/virtinst",
        "usr/share/bash-completion/completions/virt-install",
        "usr/share/bash-completion/completions/virt-clone",
        "usr/share/bash-completion/completions/virt-xml",
    ]
