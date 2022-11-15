pkgname = "lvm2"
pkgver = "2.03.17"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-editline",
    "--enable-pkgconfig",
    "--enable-fsadm",
    "--enable-dmeventd",
    "--enable-cmdlib",
    "--enable-udev_sync",
    "--enable-udev_rules",
    "--enable-static-link",
    "--disable-selinux",
    "--with-symvers=no",
    "--with-usrsbindir=/usr/bin",
    "--with-udevdir=/usr/lib/udev/rules.d",
    "--with-default-pid-dir=/run",
    "--with-default-dm-run-dir=/run",
    "--with-default-run-dir=/run/lvm",
    "--with-default-locking-dir=/run/lock/lvm",
]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["gmake", "gsed", "pkgconf", "bash"]
makedepends = [
    "eudev-devel-static", "libblkid-devel-static",
    "libaio-devel-static", "libedit-devel-static",
    "musl-devel-static", "libunwind-devel-static",
    "ncurses-devel-static", "linux-headers",
]
# a bunch of the commands are scripts and they need bash
# TODO: check inside of them for gnuisms and fix them
depends = ["bash", "thin-provisioning-tools"]
pkgdesc = "Logical Volume Manager 2 utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://sourceware.org/lvm2"
source = f"https://mirrors.kernel.org/sourceware/{pkgname}/releases/LVM2.{pkgver}.tgz"
sha256 = "7286cfa9651828c589389509546333b8da965dfa84a1a4c8ab3e681a47fabae7"
# the tests are full of scary gnuisms + don't work rootless
options = ["!check"]
# otherwise we're in for a world of pain
exec_wrappers = [
    ("/usr/bin/gsed", "sed")
]

def pre_install(self):
    self.install_dir("usr/bin")
    self.install_link("bin", "usr/sbin")

def post_install(self):
    self.install_service(self.files_path / "dmeventd")
    self.install_service(self.files_path / "lvmetad")

    self.rm(self.destdir / "usr/sbin")

@subpackage("device-mapper-devel")
def _dmdev(self):
    self.pkgdesc = "Device Mapper userspace library and tools (development files)"
    self.depends += makedepends

    return [
        "usr/lib/pkgconfig/devmapper*.pc",
        "usr/include/libdevmapper*.h",
        "usr/include/lvm2cmd.h",
        "usr/lib/liblvm2cmd.so",
        "usr/lib/libdevmapper.so",
        "usr/lib/libdevmapper-event.so",
        "usr/lib/libdevmapper-event-lvm2.so",
        "usr/lib/*.a",
    ]

@subpackage("device-mapper")
def _dm(self):
    self.pkgdesc = "Device Mapper userspace library and tools"

    return [
        "etc/dinit.d/dmeventd",
        "usr/bin/dm*",
        "usr/lib/libdevmapper*.so*",
        "usr/lib/liblvm2cmd.so.*",
        "usr/lib/device-mapper",
        "usr/lib/udev/rules.d/10-dm.rules",
        "usr/lib/udev/rules.d/13-dm-disk.rules",
        "usr/lib/udev/rules.d/95-dm-notify.rules",
        "usr/share/man/man8/dm*",
    ]
