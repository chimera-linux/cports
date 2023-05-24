# don't forget to update files/ckms.ini when bumping
# also update linux-*-zfs-bin
pkgname = "zfs"
pkgver = "2.1.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-config=user",
    "--with-mounthelperdir=/usr/bin",
    "--with-udevdir=/usr/lib/udev",
    "--with-udevruledir=/usr/lib/udev/rules.d",
    "--with-dracutdir=/usr/lib/dracut",
    "--with-tirpc",
]
# we generate, then create tarball, then configure, so do that manually
configure_gen = []
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf", "automake", "libtool", "python"]
makedepends = [
    "libuuid-devel",
    "libblkid-devel",
    "linux-pam-devel",
    "libtirpc-devel",
    "attr-devel",
    "openssl-devel",
    "udev-devel",
    "zlib-devel",
    "linux-headers",
]
pkgdesc = "OpenZFS for Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
source = f"https://github.com/openzfs/{pkgname}/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a54fe4e854d0a207584f1799a80e165eae66bc30dc8e8c96a1f99ed9d4d8ceb2"
hardening = ["!cfi"]  # TODO


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

    # TODO: clean up the initramfs + /etc/default/zfs of sysvinit cruft
    self.rm(self.destdir / "usr/share/zfs/zfs-tests", recursive=True)
    self.rm(self.destdir / "etc/init.d", recursive=True)
    self.rm(self.destdir / "usr/share/pam-configs/zfs_key")
    self.rm(self.destdir / "usr/share/man/man8/zfs-mount-generator.8")

    # install ckms source tree
    srcp = f"usr/src/{pkgname}-{pkgver}"
    self.install_dir(srcp)
    self.do(
        "tar",
        "xf",
        self.chroot_builddir / self.wrksrc / f"{pkgname}-{pkgver}.tar",
        wrksrc=self.chroot_destdir / srcp,
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
        f"{pkgname}={pkgver}-r{pkgrel}",
        "ckms",
        "perl",
        "python",
        "gmake",
    ]

    return ["usr/src"]
