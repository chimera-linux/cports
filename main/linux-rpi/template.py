pkgname = "linux-rpi"
pkgver = "5.15.61"
pkgrel = 0
archs = ["aarch64"]
make_dir = "build"
_commit = "c9921a3fcc60cd657047d540e3706eb51f3bede5"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
pkgdesc = "Linux kernel for Raspberry Pi 3 and 4 (5.15.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/raspberrypi/linux"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "740c5f9bf23f22481733f83907e62b882cffd1d0a7fc13cd2fb61daddafcdef5"
# no meaningful checking to be done
options = [
    "!check", "!debug", "!strip", "!scanrundeps", "!scanshlibs",
    "!lto", "textrels", "foreignelf" # vdso32
]

if self.profile().cross:
    broken = "linux-devel does not come out right"

def do_configure(self):
    self.cp(self.files_path / "config", self.cwd)

    epoch = self.source_date_epoch or 0
    args = []

    if self.profile().cross:
        args += [f"CROSS_COMPILE={self.profile().triplet}"]

    self.do(
        "chimera-buildkernel",
        "prepare",
        f"ARCH=arm64",
        f"CONFIG_FILE={self.chroot_cwd}/config",
        f"OBJDIR={self.make_dir}",
        f"JOBS={self.make_jobs}",
        f"LOCALVERSION=-{pkgrel}-rpi",
        f"EPOCH={epoch}",
        *args
    )

def do_build(self):
    self.do("chimera-buildkernel", "build")

def do_install(self):
    self.do("chimera-buildkernel", "install", self.chroot_destdir)

@subpackage("linux-rpi-devel")
def _devel(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]

@subpackage("linux-rpi-dbg")
def _dbg(self):
    self.pkgdesc += " (debug files)"
    self.options = [
        "!scanrundeps", "!strip", "!scanshlibs", "foreignelf", "textrels"
    ]
    return ["usr/lib/debug", "boot/System.map-*"]
