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
    "--disable-agetty",
    "--disable-cal",
    "--disable-kill",
    "--disable-logger",
    "--disable-login",
    "--disable-makeinstall-chown",
    "--disable-mesg",
    "--disable-chfn-chsh",
    "--disable-nologin",
    "--disable-scriptutils",
    "--disable-sulogin",
    "--disable-su",
    "--disable-ul",
    "--disable-wall",
    "--disable-whereis",
    "--disable-write",
    "--with-systemdsystemunitdir=no",
    "--without-udev",
    "--without-python",
]
make_cmd = "gmake"
make_install_args = ["usrsbin_execdir=/usr/bin"]
hostmakedepends = ["gmake", "gettext-tiny", "pkgconf"]
makedepends = [
    "linux-headers",
    "libcap-ng-devel",
    "linux-pam-devel",
    "zlib-devel",
    "ncurses-devel",
]
checkdepends = ["xz", "iproute2", "socat", "procps"]
depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
pkgdesc = "Miscellaneous Linux utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.kernel.org/pub/linux/utils/util-linux"
source = (
    f"$(KERNEL_SITE)/utils/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "60492a19b44e6cf9a3ddff68325b333b8b52b6c59ce3ebd6a0ecaa4c5117e84f"
tool_flags = {"CFLAGS": ["-D_DIRENT_HAVE_D_TYPE"]}
# checkdepends are missing
options = ["!check"]


def post_extract(self):
    self.rm("tests/ts/lsns/ioctl_ns", force=True)
    self.rm("tests/ts/col/multibyte", force=True)


def post_install(self):
    self.install_license(
        "Documentation/licenses/COPYING.BSD-3-Clause", pkgname="libuuid"
    )

    # fix permissions
    for f in ["mount", "umount"]:
        (self.destdir / "usr/bin" / f).chmod(0o4755)

    # conflicts with chimerautils, less, ugetopt
    for f in [
        "addpart",
        "col",
        "colrm",
        "column",
        "ctrlaltdel",
        "delpart",
        "fallocate",
        "flock",
        "fsfreeze",
        "getopt",
        "ionice",
        "isosize",
        "hexdump",
        "look",
        "mcookie",
        "more",
        "pivot_root",
        "resizepart",
        "renice",
        "rev",
        "setarch",
        "setsid",
        "switch_root",
        "taskset",
    ]:
        self.rm(self.destdir / f"usr/bin/{f}")
        self.rm(self.destdir / f"usr/share/man/man1/{f}.1", force=True)
        self.rm(self.destdir / f"usr/share/man/man8/{f}.8", force=True)
        self.rm(
            self.destdir / f"usr/share/bash-completion/completions/{f}",
            force=True,
        )

    # dynamic aliases that may differ per arch
    for f in (self.destdir / "usr/bin").iterdir():
        if f.is_symlink() and f.readlink().name == "setarch":
            f.unlink()
    for f in (self.destdir / "usr/share/man/man8").iterdir():
        if f.is_symlink() and f.readlink().name == "setarch.8":
            f.unlink()

    # services
    for s in ["uuidd", "uuidd-dir"]:
        self.install_service(self.files_path / s)


@subpackage("util-linux-common")
def _common(self):
    self.pkgdesc = "Common data for util-linux"
    self.build_style = "meta"

    return ["usr/share/locale"]


@subpackage("dmesg")
def _dmesg(self):
    self.pkgdesc = "Utility for kernel ring buffer manipulation"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/dmesg",
        "usr/share/bash-completion/completions/dmesg",
        "usr/share/man/man1/dmesg.1",
    ]


@subpackage("mount")
def _mnt(self):
    self.pkgdesc = "The mount(8) program and related utilities"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]
    self.suid_files = [
        "usr/bin/mount",
        "usr/bin/umount",
    ]

    return [
        "usr/bin/blkid",
        "usr/bin/blockdev",
        "usr/bin/eject",
        "usr/bin/findfs",
        "usr/bin/findmnt",
        "usr/bin/fsck*",
        "usr/bin/losetup",
        "usr/bin/lsblk",
        "usr/bin/mount*",
        "usr/bin/partx",
        "usr/bin/swapoff",
        "usr/bin/swapon",
        "usr/bin/umount",
        "usr/share/bash-completion/completions/blkid",
        "usr/share/bash-completion/completions/blockdev",
        "usr/share/bash-completion/completions/eject",
        "usr/share/bash-completion/completions/findmnt",
        "usr/share/bash-completion/completions/fsck*",
        "usr/share/bash-completion/completions/losetup",
        "usr/share/bash-completion/completions/lsblk",
        "usr/share/bash-completion/completions/mount*",
        "usr/share/bash-completion/completions/partx",
        "usr/share/bash-completion/completions/swapoff",
        "usr/share/bash-completion/completions/swapon",
        "usr/share/bash-completion/completions/umount",
        "usr/share/man/man1/eject.1",
        "usr/share/man/man1/mount*.1",
        "usr/share/man/man5/fstab.5",
        "usr/share/man/man8/blkid.8",
        "usr/share/man/man8/blockdev.8",
        "usr/share/man/man8/findfs.8",
        "usr/share/man/man8/findmnt.8",
        "usr/share/man/man8/fsck*.8",
        "usr/share/man/man8/losetup.8",
        "usr/share/man/man8/lsblk.8",
        "usr/share/man/man8/mount*.8",
        "usr/share/man/man8/partx.8",
        "usr/share/man/man8/swapoff.8",
        "usr/share/man/man8/swapon.8",
        "usr/share/man/man8/umount.8",
    ]


@subpackage("libmount")
def _mnt_lib(self):
    self.pkgdesc = "Library for mount(8)"

    return ["usr/lib/libmount.so.*"]


@subpackage("libmount-devel")
def _mnt_devel(self):
    self.pkgdesc = "Library for mount(8) (development files)"

    return [
        "usr/lib/libmount.*",
        "usr/lib/pkgconfig/*mount*",
        "usr/include/libmount",
    ]


@subpackage("fdisk")
def _fdisk(self):
    self.pkgdesc = "The fdisk(8) program and related utilities"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/*fdisk",
        "usr/share/bash-completion/completions/*fdisk",
        "usr/share/man/man8/*fdisk.8",
    ]


@subpackage("libfdisk")
def _fdisk_lib(self):
    self.pkgdesc = "Library for fdisk(8)"

    return ["usr/lib/libfdisk.so.*"]


@subpackage("libfdisk-devel")
def _fdisk_devel(self):
    self.pkgdesc = "Library for fdisk(8) (development files)"

    return [
        "usr/lib/libfdisk.*",
        "usr/lib/pkgconfig/*fdisk*",
        "usr/include/libfdisk",
    ]


@subpackage("mkfs")
def _mkfs(self):
    self.pkgdesc = "Utilities for filesystem manipulation"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/mkfs*",
        "usr/bin/mkswap",
        "usr/bin/swaplabel",
        "usr/bin/wipefs",
        "usr/share/bash-completion/completions/mkfs*",
        "usr/share/bash-completion/completions/mkswap",
        "usr/share/bash-completion/completions/swaplabel",
        "usr/share/bash-completion/completions/wipefs",
        "usr/share/man/man8/mkfs*.8",
        "usr/share/man/man8/mkswap.8",
        "usr/share/man/man8/swaplabel.8",
        "usr/share/man/man8/wipefs.8",
    ]


@subpackage("fstrim")
def _fstrim(self):
    self.pkgdesc = "SSD trimming utilities"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/fstrim",
        "usr/bin/blkdiscard",
        "usr/share/bash-completion/completions/fstrim",
        "usr/share/bash-completion/completions/blkdiscard",
        "usr/share/man/man8/fstrim.8",
        "usr/share/man/man8/blkdiscard.8",
    ]


@subpackage("rfkill")
def _rfkill(self):
    self.pkgdesc = "Tool for enabling and disabling wireless devices"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/rfkill",
        "usr/share/bash-completion/completions/rfkill",
        "usr/share/man/man8/rfkill.8",
    ]


@subpackage("irqtop")
def _irqtop(self):
    self.pkgdesc = "Utility to display kernel interrupt information"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/irqtop",
        "usr/share/bash-completion/completions/irqtop",
        "usr/share/man/man1/irqtop.1",
    ]


@subpackage("lscpu")
def _lscpu(self):
    self.pkgdesc = "Utility to display CPU information"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/lscpu",
        "usr/share/bash-completion/completions/lscpu",
        "usr/share/man/man1/lscpu.1",
    ]


@subpackage("rename")
def _rename(self):
    self.pkgdesc = "Bulk rename utility"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/rename",
        "usr/share/bash-completion/completions/rename",
        "usr/share/man/man1/rename.1",
    ]


@subpackage("runuser")
def _runuser(self):
    self.pkgdesc = "Utilities to run commands with different privileges"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/runuser",
        "usr/bin/setpriv",
        "usr/share/bash-completion/completions/runuser",
        "usr/share/bash-completion/completions/setpriv",
        "usr/share/man/man1/runuser.1",
        "usr/share/man/man1/setpriv.1",
    ]


@subpackage("zramctl")
def _zramctl(self):
    self.pkgdesc = "Set up and control zram devices"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/zramctl",
        "usr/share/bash-completion/completions/zramctl",
        "usr/share/man/man8/zramctl.8",
    ]


@subpackage("util-linux-ns")
def _ns(self):
    self.pkgdesc = "Namespace-related utilities"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/lsns",
        "usr/bin/nsenter",
        "usr/bin/unshare",
        "usr/share/bash-completion/completions/lsns",
        "usr/share/bash-completion/completions/nsenter",
        "usr/share/bash-completion/completions/unshare",
        "usr/share/man/man1/nsenter.1",
        "usr/share/man/man1/unshare.1",
        "usr/share/man/man8/lsns.8",
    ]


@subpackage("util-linux-ipc")
def _ipc(self):
    self.pkgdesc = "IPC-related utilities"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/*ipc*",
        "usr/share/bash-completion/completions/*ipc*",
        "usr/share/man/man1/*ipc*.1",
    ]


@subpackage("util-linux-utmp")
def _utmp(self):
    self.pkgdesc = "UTMP-related utilities"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}"]

    return [
        "usr/bin/last*",
        "usr/bin/lslogins",
        "usr/bin/utmpdump",
        "usr/share/bash-completion/completions/last*",
        "usr/share/bash-completion/completions/lslogins",
        "usr/share/bash-completion/completions/utmpdump",
        "usr/share/man/man1/last*.1",
        "usr/share/man/man1/lslogins.1",
        "usr/share/man/man1/utmpdump.1",
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
        "usr/share/man/man3/libblkid.3",
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
        "usr/share/man/man3/uuid*",
    ]


@subpackage("libuuid-progs")
def _uuid(self):
    self.pkgdecs = "Runtime components for the UUID library"
    self.depends = [f"util-linux-common={pkgver}-r{pkgrel}", "shadow"]
    self.install_if = [f"libuuid={pkgver}-r{pkgrel}"]
    self.system_users = ["_uuidd"]

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
        "usr/include/libsmartcols",
    ]


configure_gen = []
