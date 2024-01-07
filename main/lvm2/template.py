pkgname = "lvm2"
pkgver = "2.03.22"
pkgrel = 1
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
    "--with-thin=internal",
    "--with-thin-check=/usr/bin/thin_check",
    "--disable-thin_check_needs_check",
    "--with-thin-dump=/usr/bin/thin_dump",
    "--with-thin-repair=/usr/bin/thin_repair",
    "--with-thin-restore=/usr/bin/thin_restore",
    "--with-cache-check=/usr/bin/cache_check",
    "--disable-cache_check_needs_check",
    "--with-cache-dump=/usr/bin/cache_dump",
    "--with-cache-repair=/usr/bin/cache_repair",
    "--with-cache-restore=/usr/bin/cache_restore",
    "--with-dmeventd-path=/usr/bin/dmeventd",
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
    "udev-devel-static",
    "libblkid-devel-static",
    "libaio-devel-static",
    "libedit-devel-static",
    "musl-devel-static",
    "libunwind-devel-static",
    "libatomic-chimera-devel-static",
    "ncurses-devel-static",
    "linux-headers",
]
pkgdesc = "Logical Volume Manager 2 utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://sourceware.org/lvm2"
source = f"https://mirrors.kernel.org/sourceware/{pkgname}/releases/LVM2.{pkgver}.tgz"
sha256 = "4c5a6923bd1ace7ce04474608a84937ce053ba91b1ace9f0b0017268e732dc7c"
# the tests are full of scary gnuisms + don't work rootless
options = ["!check"]
# otherwise we're in for a world of pain
exec_wrappers = [("/usr/bin/gsed", "sed")]

if self.profile().arch == "riscv64":
    # udev static library weirdness
    makedepends += ["libcap-devel-static"]
    configure_args += ["LIBS=-lcap"]


def pre_install(self):
    self.install_dir("usr/bin")
    self.install_link("bin", "usr/sbin")


def post_install(self):
    self.install_service(self.files_path / "dmeventd")
    self.install_service(self.files_path / "lvmetad")

    self.install_file(
        self.files_path / "dmsetup.hook",
        "usr/share/initramfs-tools/hooks",
        name="dmsetup",
        mode=0o755,
    )
    self.install_file(
        self.files_path / "lvm2.hook",
        "usr/share/initramfs-tools/hooks",
        name="lvm2",
        mode=0o755,
    )

    self.rm(self.destdir / "usr/sbin")


@subpackage("device-mapper-devel")
def _dmdev(self):
    self.pkgdesc = (
        "Device Mapper userspace library and tools (development files)"
    )
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
        "usr/share/initramfs-tools/hooks/dmsetup",
        "usr/share/man/man8/dm*",
    ]


@subpackage("lvm2-extra")
def _extra(self):
    self.pkgdesc = f"{pkgdesc} (extra utilities)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}", "bash", "ugetopt"]
    return [
        "usr/bin/blkdeactivate",
        "usr/bin/fsadm",
        "usr/bin/lvm_import_vdo",
        "usr/bin/lvmdump",
    ]


configure_gen = []
