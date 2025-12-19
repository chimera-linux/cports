pkgname = "linux-stable-zfs-bin"
pkgver = "2.3.5.6.18.2"
_zfsver = ".".join(pkgver.split(".")[0:3])
_kernver = pkgver[len(_zfsver) + 1 :]
pkgrel = 1
hostmakedepends = ["perl", "python", "ckms"]
makedepends = ["linux-stable-devel", "zfs-ckms"]
# provides the same thing as the ckms variant
depends = [f"linux-stable~{_kernver}", f"zfs~{_zfsver}"]
pkgdesc = f"OpenZFS modules for kernel {_kernver}"
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
