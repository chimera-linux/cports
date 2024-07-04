# don't forget to update files/ckms.ini when bumping
# also update linux-*-zfs-bin
pkgname = "zfs"
pkgver = "2.2.4"
pkgrel = 2
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
    "zlib-ng-compat-devel",
    "linux-headers",
]
pkgdesc = "OpenZFS for Linux"
maintainer = "q66 <q66@chimera-linux.org>"
license = "CDDL-1.0"
url = "https://openzfs.github.io/openzfs-docs"
source = [
    f"https://github.com/openzfs/zfs/releases/download/{pkgname}-{pkgver}/{pkgname}-{pkgver}.tar.gz",
    # not shipped in tarballs? why
    f"!https://raw.githubusercontent.com/openzfs/zfs/zfs-{pkgver}/contrib/debian/tree/zfs-initramfs/usr/share/initramfs-tools/hooks/zdev>zdev-{pkgver}",
]
sha256 = [
    "9790905f7683d41759418e1ef3432828c31116654ff040e91356ff1c21c31ec0",
    "c541dfec33ba7dfec3fb85a4532fc9c7a72035316716e93074b2cfa030ca2d12",
]
hardening = ["!cfi"]  # TODO


def post_extract(self):
    self.cp(self.sources_path / f"zdev-{pkgver}", ".")


def post_patch(self):
    # clean up for ckms
    for f in self.patches_path.iterdir():
        self.rm(f.name)


def pre_configure(self):
    self.do("autoreconf", "-if")
    # unfuck the perms of files introduced by autoreconf
    self.chmod("config/config.guess", 0o755)
    self.chmod("config/config.sub", 0o755)
    self.chmod("config/install-sh", 0o755)
    # compress source tree for ckms
    fn = f"{pkgname}-{pkgver}.tar"
    self.do("tar", "cf", fn, "--exclude", fn, ".")


def post_install(self):
    self.install_license("COPYRIGHT")
    self.install_license("LICENSE")
    self.install_license("NOTICE")

    # TODO: clean up the initramfs + /etc/default/zfs of sysvinit cruft
    self.uninstall("usr/share/zfs/zfs-tests")
    self.uninstall("etc/init.d")
    self.uninstall("usr/share/pam-configs/zfs_key")
    self.uninstall("usr/share/man/man8/zfs-mount-generator.8")

    # install the zdev hook for udev rules (also handles enc keys)
    self.install_file(
        f"zdev-{pkgver}",
        "usr/share/initramfs-tools/hooks",
        name="zdev",
        mode=0o755,
    )

    # install ckms source tree
    srcp = f"usr/src/{pkgname}-{pkgver}"
    self.install_dir(srcp)
    self.do(
        "tar",
        "xf",
        self.chroot_cwd / f"{pkgname}-{pkgver}.tar",
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
