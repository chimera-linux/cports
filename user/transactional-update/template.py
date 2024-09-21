pkgname = "transactional-update"
pkgver = "4.8.3"
pkgrel = 0
build_style = "gnu_configure"
configure_env = {
    "SYSTEMDDIR": "/usr/lib/systemd/system",
    "TMPFILESDIR": "/usr/lib/tmpfiles.d",
    "DRACUTDIR": "/usr/lib/dracut/modules.d",
}
hostmakedepends = ["autoconf-archive", "automake", "pkgconf", "slibtool"]
makedepends = [
    "dbus-devel",
    "elogind-devel",
    "libeconf-devel",
    "libmount-devel",
    "udev-devel",
]
depends = ["snapper"]
pkgdesc = "Toolkit for atomic updates"
maintainer = "tulilirockz <tulilirockz@outlook.com>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://github.com/openSUSE/transactional-update"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2dc4e39b361d4d776ec3e9eef8ab6ca55e710a859b95477a77e5818d046838a7"


def post_install(self):
    self.install_service(self.files_path / "tukitd")
    self.install_initramfs(self.files_path / "tukit.hook")
    self.install_initramfs(self.files_path / "tukit.init-bottom", "init-bottom")


@subpackage("transactional-update-initramfs-tools")
def _(self):
    self.subdesc = "initramfs scripts"
    self.install_if = []
    self.depends = ["initramfs-tools", self.parent]
    return ["usr/share/initramfs-tools"]


@subpackage("transactional-update-devel")
def _(self):
    return self.default_devel()


@subpackage("transactional-update-libs")
def _(self):
    return self.default_libs()
