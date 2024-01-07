pkgname = "util-linux"
pkgver = "2.39.3"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-feature=enabled",
    "-Dtinfo=disabled",
    "-Dncurses=disabled",
    "-Deconf=disabled",
    "-Dselinux=disabled",
    "-Dslang=disabled",
    "-Dlibutil=disabled",
    "-Dlibuser=disabled",
    "-Dlibutempter=disabled",
    "-Dreadline=disabled",
    "-Dbuild-plymouth-support=disabled",
    "-Dfs-search-path-extra=/usr/sbin:/usr/bin",
    "-Dbuild-agetty=disabled",
    "-Dbuild-cal=disabled",
    "-Dbuild-fallocate=disabled",
    "-Dbuild-kill=disabled",
    "-Dbuild-logger=disabled",
    "-Dbuild-login=disabled",
    "-Dbuild-mesg=disabled",
    "-Dbuild-more=disabled",
    "-Dbuild-chfn-chsh=disabled",
    "-Dbuild-nologin=disabled",
    "-Dbuild-newgrp=disabled",
    "-Dbuild-pivot_root=disabled",
    "-Dbuild-switch_root=disabled",
    "-Dbuild-sulogin=disabled",
    "-Dbuild-su=disabled",
    "-Dbuild-ul=disabled",
    "-Dbuild-vipw=disabled",
    "-Dbuild-wall=disabled",
    "-Dbuild-write=disabled",
    "-Dbuild-python=disabled",
    "-Dsystemd=disabled",
    "-Dsysvinit=disabled",
]
hostmakedepends = [
    "meson",
    "ninja",
    "bison",
    "flex",
    "gettext-devel",
    "pkgconf",
    "bash-completion",
]
makedepends = [
    "linux-headers",
    "libcap-ng-devel",
    "linux-pam-devel",
    "zlib-devel",
    "file-devel",
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
sha256 = "7b6605e48d1a49f43cc4b4cfc59f313d0dd5402fa40b96810bd572e167dfed0f"
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
        "cal",
        "col",
        "colrm",
        "column",
        "ctrlaltdel",
        "delpart",
        "flock",
        "fsfreeze",
        "getopt",
        "ionice",
        "isosize",
        "hexdump",
        "kill",
        "login",
        "look",
        "mcookie",
        "resizepart",
        "renice",
        "rev",
        "script",
        "scriptlive",
        "scriptreplay",
        "setarch",
        "setsid",
        "sulogin",
        "taskset",
        "whereis",
    ]:
        self.rm(self.destdir / f"usr/bin/{f}", force=True)
        self.rm(self.destdir / f"usr/share/man/man1/{f}.1", force=True)
        self.rm(self.destdir / f"usr/share/man/man8/{f}.8", force=True)
        self.rm(
            self.destdir / f"usr/share/bash-completion/completions/{f}",
            force=True,
        )

    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="uuidd.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="uuidd.conf",
    )
    # services
    self.install_service(self.files_path / "uuidd")


@subpackage("util-linux-common")
def _common(self):
    self.pkgdesc = "Common data for util-linux"
    self.options = ["empty"]

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
        # "usr/share/bash-completion/completions/runuser",
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
    self.options = ["!distlicense"]

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

    return [
        "etc/dinit.d",
        "usr/bin/uuid*",
        "usr/lib/sysusers.d",
        "usr/lib/tmpfiles.d",
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
