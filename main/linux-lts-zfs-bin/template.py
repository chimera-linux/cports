pkgname = "linux-lts-zfs-bin"
_kernver = "6.6.71"
_zfsver = "2.2.7"
pkgver = f"{_zfsver}.{_kernver}"
pkgrel = 0
hostmakedepends = ["perl", "python", "ckms"]
makedepends = ["linux-lts-devel", "zfs-ckms"]
# provides the same thing as the ckms variant
depends = [f"linux-lts~{_kernver}", f"zfs~{_zfsver}"]
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
