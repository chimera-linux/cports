pkgname = "util-linux"
_mver = "2.37"
pkgver = f"{_mver}.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--exec-prefix=${prefix}",
    "--enable-libuuid",
    "--enable-libblkid",
    "--enable-fsck",
    "--enable-vipw",
    "--enable-newgrp",
    "--enable-chfn-chsh",
    "--enable-write",
    "--enable-fs-paths-extra=/usr/sbin:/usr/bin",
    "--disable-rpath",
    "--disable-makeinstall-chown",
    "--with-systemdsystemunitdir=no",
    "--without-udev",
    "--without-python",
]
make_cmd = "gmake"
make_install_args = ["usrsbin_execdir=/usr/bin"]
hostmakedepends = ["gmake", "gettext-tiny", "pkgconf"]
makedepends = [
    "kernel-libc-headers", "libcap-ng-devel", "linux-pam-devel", "zlib-devel"
]
checkdepends = ["xz", "iproute2", "socat", "procps-ng"]
depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
pkgdesc = "Miscellaneous Linux utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.kernel.org/pub/linux/utils/util-linux"
source = f"$(KERNEL_SITE)/utils/{pkgname}/v{_mver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "6a0764c1aae7fb607ef8a6dd2c0f6c47d5e5fd27aa08820abaad9ec14e28e9d9"
tool_flags = {"CFLAGS": ["-D_DIRENT_HAVE_D_TYPE"]}
suid_files = [
    "usr/bin/chfn",
    "usr/bin/chsh",
    "usr/bin/mount",
    "usr/bin/newgrp",
    "usr/bin/su",
    "usr/bin/umount",
    "usr/bin/wall",
    "usr/bin/write",
]
# checkdepends are missing
options = ["!check"]

# FIXME/TODO:
# - uuidd service
# - /usr/bin/{wall, write} should be owned by tty
# - maybe install libuuid license in its subpackage

def post_extract(self):
    self.rm("tests/ts/lsns/ioctl_ns", force = True)
    self.rm("tests/ts/col/multibyte", force = True)

def post_install(self):
    self.install_license("Documentation/licenses/COPYING.BSD-3-Clause")

    # fix permissions
    for f in suid_files:
        (self.destdir / f).chmod(0o4755)

    # these should be setgid and not setuid
    for f in ["wall", "write"]:
        (self.destdir / "usr/bin" / f).chmod(0o2755)

    # PAM login utils
    self.install_file(
        self.files_path / "login.pam", "etc/pam.d", name = "login"
    )
    self.install_file(self.files_path / "su.pam", "etc/pam.d", name = "su")
    self.install_file(self.files_path / "su.pam", "etc/pam.d", name = "su-l")
    self.install_file(
        self.files_path / "common.pam", "etc/pam.d", name = "chfn"
    )
    self.install_file(
        self.files_path / "common.pam", "etc/pam.d", name = "chsh"
    )

@subpackage("util-linux-libs")
def _libs(self):
    self.build_style = "meta"
    self.depends = [
        f"libfdisk={pkgver}-r{pkgrel}",
        f"libblkid={pkgver}-r{pkgrel}",
        f"libmount={pkgver}-r{pkgrel}",
        f"libsmartcols={pkgver}-r{pkgrel}",
        f"libuuid={pkgver}-r{pkgrel}",
    ]
    return []

@subpackage("util-linux-common")
def _common(self):
    self.pkgdesc += " (common files)"
    return ["usr/share/locale"]

@subpackage("libfdisk")
def _libfdisk(self):
    self.pkgdesc = "Library for fdisk(8)"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
    return ["usr/lib/libfdisk.so.*"]

@subpackage("libfdisk-devel")
def _libfdisk_devel(self):
    self.pkgdesc = "Library for fdisk(8) (development files)"
    return [
        "usr/lib/libfdisk.*",
        "usr/lib/pkgconfig/*fdisk*",
        "usr/include/libfdisk"
    ]

@subpackage("libmount")
def _libmount(self):
    self.pkgdesc = "Library for mount(8)"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
    return ["usr/lib/libmount.so.*"]

@subpackage("libmount-devel")
def _libmount_devel(self):
    self.pkgdesc = "Library for mount(8) (development files)"
    return [
        "usr/lib/libmount.*",
        "usr/lib/pkgconfig/*mount*",
        "usr/include/libmount"
    ]

@subpackage("libblkid")
def _libblkid(self):
    self.pkgdesc = "Library to handle device identification"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
    return ["usr/lib/libblkid.so.*"]

@subpackage("libblkid-devel")
def _libblkid_devel(self):
    self.pkgdesc = "Library to handle device identification (development files)"
    self.depends += [f"libuuid-devel={pkgver}-r{pkgrel}"]
    return [
        "usr/lib/libblkid.*",
        "usr/lib/pkgconfig/*blkid*",
        "usr/include/blkid",
        "usr/share/man/man3/libblkid.3"
    ]

@subpackage("libuuid")
def _libuuid(self):
    self.pkgdesc = "UUID library from util-linux"
    self.license = "BSD-3-Clause"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
    return ["usr/lib/libuuid.so.*"]

@subpackage("libuuid-devel")
def _libuuid_devel(self):
    self.pkgdesc = "UUID library from util-linux (development files)"
    self.license = "BSD-3-Clause"
    return [
        "usr/lib/libuuid.*",
        "usr/lib/pkgconfig/*uuid*",
        "usr/include/uuid",
        "usr/share/man/man3/uuid*"
    ]

@subpackage("libsmartcols")
def _libsmartcols(self):
    self.pkgdesc = "Table or Tree library from util-linux"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
    return ["usr/lib/libsmartcols.so.*"]

@subpackage("libsmartcols-devel")
def _libsmartcols_devel(self):
    self.pkgdesc = "Table or Tree library from util-linux (development files)"
    return [
        "usr/lib/libsmartcols.*",
        "usr/lib/pkgconfig/*smartcols*",
        "usr/include/libsmartcols"
    ]

