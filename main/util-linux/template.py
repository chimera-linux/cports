pkgname = "util-linux"
pkgver = "2.40.2"
pkgrel = 3
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
    "-Dbuild-liblastlog2=disabled",
    "-Dbuild-logger=disabled",
    "-Dbuild-login=disabled",
    "-Dbuild-mesg=disabled",
    "-Dbuild-more=disabled",
    "-Dbuild-chfn-chsh=disabled",
    "-Dbuild-nologin=disabled",
    "-Dbuild-newgrp=disabled",
    "-Dbuild-pam-lastlog2=disabled",
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
    "bash",
    "bison",
    "flex",
    "gettext-devel",
    "meson",
    "pkgconf",
]
makedepends = [
    "bash-completion",
    "file-devel",
    "libcap-ng-devel",
    "linux-headers",
    "linux-pam-devel",
    "ncurses-devel",
    "zlib-ng-compat-devel",
]
checkdepends = ["xz", "iproute2", "socat", "procps"]
depends = [self.with_pkgver("util-linux-common")]
pkgdesc = "Miscellaneous Linux utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.kernel.org/pub/linux/utils/util-linux"
source = (
    f"$(KERNEL_SITE)/utils/util-linux/v{pkgver[:-2]}/util-linux-{pkgver}.tar.xz"
)
sha256 = "d78b37a66f5922d70edf3bdfb01a6b33d34ed3c3cafd6628203b2a2b67c8e8b3"
patch_style = "patch"
tool_flags = {"CFLAGS": ["-D_DIRENT_HAVE_D_TYPE"]}
# checkdepends are missing
options = ["!check"]


def post_extract(self):
    self.rm("tests/ts/lsns/ioctl_ns", force=True)
    self.rm("tests/ts/col/multibyte", force=True)


def init_configure(self):
    # https://github.com/pkgconf/pkgconf/issues/205
    # causes --variable=completionsdir for bash-completion to double-prefix otherwise
    self.env["PKG_CONFIG_FDO_SYSROOT_RULES"] = "1"


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

    self.install_sysusers(self.files_path / "sysusers.conf", name="uuidd")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf", name="uuidd")
    # services
    self.install_service(self.files_path / "uuidd")


@subpackage("util-linux-common")
def _(self):
    self.pkgdesc = "Common data for util-linux"
    self.options = ["empty"]

    return ["usr/share/locale"]


@subpackage("dmesg")
def _(self):
    self.pkgdesc = "Utility for kernel ring buffer manipulation"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/dmesg",
        "usr/share/bash-completion/completions/dmesg",
        "usr/share/man/man1/dmesg.1",
    ]


@subpackage("mount")
def _(self):
    self.pkgdesc = "The mount(8) program and related utilities"
    self.depends = [self.with_pkgver("util-linux-common")]
    self.file_modes = {
        "usr/bin/mount": ("root", "root", 0o4755),
        "usr/bin/umount": ("root", "root", 0o4755),
    }

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
        "usr/share/bash-completion/completions/findfs",
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
def _(self):
    self.pkgdesc = "Library for mount(8)"

    return ["usr/lib/libmount.so.*"]


@subpackage("libmount-devel")
def _(self):
    self.pkgdesc = "Library for mount(8)"

    return [
        "usr/lib/libmount.*",
        "usr/lib/pkgconfig/*mount*",
        "usr/include/libmount",
    ]


@subpackage("fdisk")
def _(self):
    self.pkgdesc = "The fdisk(8) program and related utilities"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/*fdisk",
        "usr/share/bash-completion/completions/*fdisk",
        "usr/share/man/man8/*fdisk.8",
    ]


@subpackage("libfdisk")
def _(self):
    self.pkgdesc = "Library for fdisk(8)"

    return ["usr/lib/libfdisk.so.*"]


@subpackage("libfdisk-devel")
def _(self):
    self.pkgdesc = "Library for fdisk(8)"

    return [
        "usr/lib/libfdisk.*",
        "usr/lib/pkgconfig/*fdisk*",
        "usr/include/libfdisk",
    ]


@subpackage("mkfs")
def _(self):
    self.pkgdesc = "Utilities for filesystem manipulation"
    self.depends = [self.with_pkgver("util-linux-common")]

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
def _(self):
    self.pkgdesc = "SSD trimming utilities"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/fstrim",
        "usr/bin/blkdiscard",
        "usr/share/bash-completion/completions/fstrim",
        "usr/share/bash-completion/completions/blkdiscard",
        "usr/share/man/man8/fstrim.8",
        "usr/share/man/man8/blkdiscard.8",
    ]


@subpackage("rfkill")
def _(self):
    self.pkgdesc = "Tool for enabling and disabling wireless devices"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/rfkill",
        "usr/share/bash-completion/completions/rfkill",
        "usr/share/man/man8/rfkill.8",
    ]


@subpackage("irqtop")
def _(self):
    self.pkgdesc = "Utility to display kernel interrupt information"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/irqtop",
        "usr/share/bash-completion/completions/irqtop",
        "usr/share/man/man1/irqtop.1",
    ]


@subpackage("lscpu")
def _(self):
    self.pkgdesc = "Utility to display CPU information"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/lscpu",
        "usr/share/bash-completion/completions/lscpu",
        "usr/share/man/man1/lscpu.1",
    ]


@subpackage("rename")
def _(self):
    self.pkgdesc = "Bulk rename utility"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/rename",
        "usr/share/bash-completion/completions/rename",
        "usr/share/man/man1/rename.1",
    ]


@subpackage("runuser")
def _(self):
    self.pkgdesc = "Utilities to run commands with different privileges"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/runuser",
        "usr/bin/setpriv",
        # "usr/share/bash-completion/completions/runuser",
        "usr/share/bash-completion/completions/setpriv",
        "usr/share/man/man1/runuser.1",
        "usr/share/man/man1/setpriv.1",
    ]


@subpackage("zramctl")
def _(self):
    self.pkgdesc = "Set up and control zram devices"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/zramctl",
        "usr/share/bash-completion/completions/zramctl",
        "usr/share/man/man8/zramctl.8",
    ]


@subpackage("util-linux-ns")
def _(self):
    self.pkgdesc = "Namespace-related utilities"
    self.depends = [self.with_pkgver("util-linux-common")]

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
def _(self):
    self.pkgdesc = "IPC-related utilities"
    self.depends = [self.with_pkgver("util-linux-common")]

    return [
        "usr/bin/*ipc*",
        "usr/share/bash-completion/completions/*ipc*",
        "usr/share/man/man1/*ipc*.1",
    ]


@subpackage("util-linux-utmp")
def _(self):
    self.pkgdesc = "UTMP-related utilities"
    self.depends = [self.with_pkgver("util-linux-common")]

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
def _(self):
    self.pkgdesc = "Library to handle device identification"

    return ["usr/lib/libblkid.so.*"]


@subpackage("libblkid-devel")
def _(self):
    self.pkgdesc = "Library to handle device identification"
    self.depends += [self.with_pkgver("libuuid-devel")]

    return [
        "usr/lib/libblkid.*",
        "usr/lib/pkgconfig/*blkid*",
        "usr/include/blkid",
        "usr/share/man/man3/libblkid.3",
    ]


@subpackage("libuuid")
def _(self):
    self.pkgdesc = "UUID library from util-linux"
    self.license = "BSD-3-Clause"

    return ["usr/lib/libuuid.so.*"]


@subpackage("libuuid-devel")
def _(self):
    self.pkgdesc = "UUID library from util-linux"
    self.license = "BSD-3-Clause"
    self.options = ["!distlicense"]

    return [
        "usr/lib/libuuid.*",
        "usr/lib/pkgconfig/*uuid*",
        "usr/include/uuid",
        "usr/share/man/man3/uuid*",
    ]


@subpackage("libuuid-progs")
def _(self):
    self.pkgdecs = "Runtime components for the UUID library"
    self.depends = [self.with_pkgver("util-linux-common"), "shadow"]
    self.install_if = [self.with_pkgver("libuuid")]

    return [
        "etc/dinit.d",
        "usr/bin/uuid*",
        "usr/lib/sysusers.d",
        "usr/lib/tmpfiles.d",
        "usr/share/man/man[18]/uuid*",
        "usr/share/bash-completion/completions/uuid*",
    ]


@subpackage("libsmartcols")
def _(self):
    self.pkgdesc = "Table or Tree library from util-linux"

    return ["usr/lib/libsmartcols.so.*"]


@subpackage("libsmartcols-devel")
def _(self):
    self.pkgdesc = "Table or Tree library from util-linux"

    return [
        "usr/lib/libsmartcols.*",
        "usr/lib/pkgconfig/*smartcols*",
        "usr/include/libsmartcols",
    ]
