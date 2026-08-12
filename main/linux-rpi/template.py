# update linux-rpi-zfs-bin when bumping
pkgname = "linux-rpi"
pkgver = "6.18.44"
pkgrel = 0
archs = ["aarch64"]
build_style = "linux_kernel"
configure_args = ["FLAVOR=rpi", f"RELEASE={pkgrel}"]
make_dir = "build"
# necessary for efistub
make_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
_commit = "ce0873cb5e0c24dd4730d87f4777982035733a0d"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = (
    f"Linux kernel {pkgver[0 : pkgver.rfind('.')]}.x for Raspberry Pi 3/4/5"
)
license = "GPL-2.0-only"
url = "https://github.com/raspberrypi/linux"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "7deaf0b488c289e48dd67320de7d83ed0ab4b5abc6e2dfa8f9db1c5469e3a405"
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
elif self.profile().cross:
    broken = "linux-devel does not come out right"


def post_patch(self):
    # this breaks dtbinst kbuild
    self.rm("arch/arm64/boot/dts/overlays/README")


@subpackage("linux-rpi-devel")
def _(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "execstack", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]


@subpackage("linux-rpi-dbg", self.build_dbg)
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
