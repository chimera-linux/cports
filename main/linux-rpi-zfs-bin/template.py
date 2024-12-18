pkgname = "linux-rpi-zfs-bin"
_kernver = "6.6.64"
_zfsver = "2.2.7"
pkgver = f"{_zfsver}.{_kernver}"
pkgrel = 0
archs = ["aarch64"]
hostmakedepends = ["perl", "python", "ckms"]
makedepends = ["linux-rpi-devel", "zfs-ckms"]
# provides the same thing as the ckms variant
depends = [f"linux-rpi~{_kernver}", f"zfs~{_zfsver}"]
pkgdesc = f"OpenZFS modules for kernel {_kernver}"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
options = ["!cross"]


def init_configure(self):
    from cbuild.util import linux

    self._linux_version = linux.get_version(self, _kernver)


def configure(self):
    from cbuild.util import linux

    linux.ckms_configure(self, "zfs", _zfsver, self._linux_version)


def build(self):
    from cbuild.util import linux

    linux.ckms_build(self, "zfs", _zfsver, self._linux_version)


def install(self):
    from cbuild.util import linux

    linux.ckms_install(self, "zfs", _zfsver, self._linux_version)

    srcp = linux.get_modsrc(self, "zfs", _zfsver)
    self.install_license(srcp / "COPYRIGHT")
    self.install_license(srcp / "LICENSE")
    self.install_license(srcp / "NOTICE")
