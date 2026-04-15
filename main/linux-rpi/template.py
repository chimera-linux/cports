# update linux-rpi-zfs-bin when bumping
pkgname = "linux-rpi"
pkgver = "6.12.81"
pkgrel = 0
archs = ["aarch64"]
build_style = "linux_kernel"
configure_args = ["FLAVOR=rpi", f"RELEASE={pkgrel}"]
make_dir = "build"
# necessary for efistub
make_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
_commit = "bc0c440ce8a9ba7dbcd22fcee403ef91daf5a9ec"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = (
    f"Linux kernel {pkgver[0 : pkgver.rfind('.')]}.x for Raspberry Pi 3/4/5"
)
license = "GPL-2.0-only"
url = "https://github.com/raspberrypi/linux"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "a6c09135b730a8a3dbabc2c5408289ccaaafcfb9190a2cccdfb9648fded0ef7a"
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

if self.profile().cross:
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
