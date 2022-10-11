# don't forget to update files/ckms.ini when bumping
# also update linux-modules-zfs
pkgname = "zfs"
pkgver = "2.1.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-config=user", "--with-mounthelperdir=/usr/bin",
    "--with-udevdir=/usr/lib/udev", "--with-udevruledir=/usr/lib/udev/rules.d",
    "--with-dracutdir=/usr/lib/dracut", "--with-tirpc",
]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool", "python"]
makedepends = [
    "libuuid-devel", "libblkid-devel", "linux-pam-devel", "libtirpc-devel",
    "attr-devel", "openssl-devel", "eudev-devel", "zlib-devel",
    "linux-headers",
]
pkgdesc = "OpenZFS for Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
source = f"https://github.com/openzfs/{pkgname}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "15339014f8d2131348eb937bf8893849806b6d2645ea607a18c7f117749dbd7a"

def post_patch(self):
    # clean up for ckms
    for f in self.patches_path.iterdir():
        self.rm(f.name)

def pre_configure(self):
    self.do("autoreconf", "-if")
    # compress source tree for ckms
    fn = f"{pkgname}-{pkgver}.tar"
    self.do("tar", "cf", fn, "--exclude", fn, ".")

def post_install(self):
    self.install_license("COPYRIGHT")
    self.install_license("LICENSE")
    self.install_license("NOTICE")

    self.rm(self.destdir / "usr/share/zfs/zfs-tests", recursive = True)
    self.rm(self.destdir / "etc/init.d", recursive = True)
    self.rm(self.destdir / "etc/default", recursive = True)
    self.rm(self.destdir / "etc/zfs/zfs-functions")
    self.rm(self.destdir / "usr/share/pam-configs/zfs_key")
    self.rm(self.destdir / "usr/share/man/man8/zfs-mount-generator.8")

    # install ckms source tree
    srcp = f"usr/src/{pkgname}-{pkgver}"
    self.install_dir(srcp)
    self.do(
        "tar", "xf",
        self.chroot_builddir / self.wrksrc / f"{pkgname}-{pkgver}.tar",
        wrksrc = self.chroot_destdir / srcp
    )
    self.install_file(self.files_path / "ckms.ini", srcp)

    self.install_service(self.files_path / "zed")

@subpackage("zfs-dracut")
def _dracut(self):
    self.pkgdesc = f"{pkgdesc} (dracut module)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dracut"]
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return ["usr/lib/dracut"]

@subpackage("zfs-devel")
def _devel(self):
    return self.default_devel()

@subpackage("zfs-ckms")
def _ckms(self):
    self.pkgdesc = f"{pkgdesc} (kernel sources)"
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "ckms"]
    self.depends = [
        f"{pkgname}={pkgver}-r{pkgrel}", "ckms", "perl", "python", "gmake"
    ]

    return ["usr/src"]
