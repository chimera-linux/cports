# update linux-stable-zfs-bin when bumping
pkgname = "linux-stable"
pkgver = "6.15.7"
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
sha256 = "3507dd105b0a0e1101bd43d294472fccf853429a259a5fa7c67467bba318f8e9"
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


@subpackage("linux-stable-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-stable-dbg", self.build_dbg)
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
