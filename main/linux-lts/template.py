# update linux-lts-zfs-bin when bumping
pkgname = "linux-lts"
pkgver = "6.12.39"
pkgrel = 0
archs = [
    "aarch64",
    "loongarch64",
    "ppc64le",
    "ppc64",
    "ppc",
    "riscv64",
    "x86_64",
]
build_style = "linux_kernel"
configure_args = ["FLAVOR=generic", f"RELEASE={pkgrel}"]
make_dir = "build"
make_install_env = {"ZSTD_CLEVEL": "9"}
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = f"Linux kernel {pkgver[0 : pkgver.rfind('.')]}.x"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[0]}.x/linux-{pkgver}.tar.xz"
sha256 = "6e562502a8fd11639f558e43b74f0df0d85fa85e60f5332acb275a75a35f5345"
# no meaningful checking to be done
options = [
    "!check",
    "!debug",
    "!strip",
    "!scanrundeps",
    "!scanshlibs",
    "!lto",
    "textrels",
    "execstack",
    "foreignelf",  # vdso32
]

if self.current_target == "custom:generate-configs":
    hostmakedepends += ["base-cross", "ncurses-devel"]

if self.profile().cross:
    broken = "linux-devel does not come out right"


@subpackage("linux-lts-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-lts-dbg", self.build_dbg)
def _(self):
    self.options = [
        "!scanrundeps",
        "!strip",
        "!scanshlibs",
        "foreignelf",
        "execstack",
        "textrels",
    ]
    return ["usr/lib/debug", "usr/lib/modules/*/apk-dist/boot/System.map-*"]
