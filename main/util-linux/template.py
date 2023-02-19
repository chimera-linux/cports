pkgname = "util-linux"
pkgver = "2.38.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--exec-prefix=${prefix}",
    "--enable-libuuid",
    "--enable-libblkid",
    "--enable-fsck",
    "--enable-write",
    "--enable-fs-paths-extra=/usr/sbin:/usr/bin",
    "--disable-rpath",
    "--disable-login",
    "--disable-makeinstall-chown",
    "--disable-chfn-chsh",
    "--disable-nologin",
    "--disable-sulogin",
    "--disable-su",
    # chimerautils conflicts
    "--disable-kill",
    "--disable-mesg",
    "--disable-ul",
    "--disable-wall",
    "--disable-write",
    "--with-systemdsystemunitdir=no",
    "--without-udev",
    "--without-python",
]
make_cmd = "gmake"
make_install_args = ["usrsbin_execdir=/usr/bin"]
hostmakedepends = ["gmake", "gettext-tiny", "pkgconf"]
makedepends = [
    "linux-headers", "libcap-ng-devel", "linux-pam-devel", "zlib-devel",
    "ncurses-devel",
]
checkdepends = ["xz", "iproute2", "socat", "procps-ng"]
# useradd for the system_users hook; this is installed early so enforce order
depends = ["shadow"]
pkgdesc = "Miscellaneous Linux utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.kernel.org/pub/linux/utils/util-linux"
source = f"$(KERNEL_SITE)/utils/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "60492a19b44e6cf9a3ddff68325b333b8b52b6c59ce3ebd6a0ecaa4c5117e84f"
tool_flags = {"CFLAGS": ["-D_DIRENT_HAVE_D_TYPE"]}
suid_files = [
    "usr/bin/mount",
    "usr/bin/umount",
]
# checkdepends are missing
options = ["!check"]

system_users = ["_uuidd"]

def post_extract(self):
    self.rm("tests/ts/lsns/ioctl_ns", force = True)
    self.rm("tests/ts/col/multibyte", force = True)

def post_install(self):
    self.install_license(
        "Documentation/licenses/COPYING.BSD-3-Clause", pkgname = "libuuid"
    )

    # fix permissions
    for f in suid_files:
        (self.destdir / f).chmod(0o4755)

    # conflicts with chimerautils, less, ugetopt
    for f in [
        "col", "colrm", "column", "getopt", "hexdump", "look", "more",
        "renice", "rev",
    ]:
        self.rm(self.destdir / f"usr/bin/{f}")
        self.rm(self.destdir / f"usr/share/man/man1/{f}.1", force = True)
        self.rm(self.destdir / f"usr/share/man/man8/{f}.8", force = True)
        self.rm(
            self.destdir / f"usr/share/bash-completion/completions/{f}",
            force = True
        )

    # agetty dinit helper
    self.install_file(
        self.files_path / "dinit-agetty", "usr/libexec", mode = 0o755
    )

    # services
    for s in [
        "agetty", "agetty-console", "agetty-hvc0", "agetty-hvsi0",
        "agetty-tty1", "agetty-tty2", "agetty-tty3", "agetty-tty4",
        "agetty-tty5", "agetty-tty6", "agetty-ttyS0", "agetty-ttyUSB0",
        "uuidd", "uuidd-dir"
    ]:
        self.install_service(self.files_path / s, enable = (s == "agetty"))

@subpackage("util-linux-dinit")
def _dinit(self):
    self.pkgdesc = f"{pkgdesc} (service files)"

    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "dinit-chimera"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "dinit-chimera"]

    return ["etc/dinit.d/agetty*", "usr/libexec/dinit-agetty"]

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

@subpackage("libfdisk")
def _libfdisk(self):
    self.pkgdesc = "Library for fdisk(8)"
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

@subpackage("libuuid-progs")
def _uuid(self):
    self.pkgdecs = "Runtime components for the UUID library"
    return [
        "etc/dinit.d",
        "usr/bin/uuid*",
        "usr/share/man/man[18]/uuid*",
        "usr/share/bash-completion/completions/uuid*",
    ]

@subpackage("libsmartcols")
def _libsmartcols(self):
    self.pkgdesc = "Table or Tree library from util-linux"
    return ["usr/lib/libsmartcols.so.*"]

@subpackage("libsmartcols-devel")
def _libsmartcols_devel(self):
    self.pkgdesc = "Table or Tree library from util-linux (development files)"
    return [
        "usr/lib/libsmartcols.*",
        "usr/lib/pkgconfig/*smartcols*",
        "usr/include/libsmartcols"
    ]
