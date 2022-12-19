# update linux-rpi-zfs-bin when bumping
pkgname = "linux-rpi"
pkgver = "6.1.0"
pkgrel = 0
archs = ["aarch64"]
make_dir = "build"
# necessary for efistub
make_env = {"CBUILD_BYPASS_STRIP_WRAPPER": "1"}
_commit = "b91c411ff7d4a35970d0100ac4257bcf9afd7e12"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = "Linux kernel for Raspberry Pi 3 and 4 (6.1.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://github.com/raspberrypi/linux"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "be0be442c494005896b8a293b9763ecd85743252cd13ece40c50b82a2f375a2a"
# no meaningful checking to be done
options = [
    "!check", "!debug", "!strip", "!scanrundeps", "!scanshlibs",
    "!lto", "textrels", "foreignelf" # vdso32
]

_flavor = "rpi"

if self.profile().cross:
    broken = "linux-devel does not come out right"

def init_configure(self):
    # generate scriptlets for packaging, just hooking to base-kernel helpers
    from cbuild.util import linux
    linux.generate_scriptlets(self, _flavor)

def do_configure(self):
    from cbuild.util import linux
    linux.configure(self, _flavor)

def do_build(self):
    from cbuild.util import linux
    linux.build(self, _flavor)

def do_install(self):
    from cbuild.util import linux
    linux.install(self, _flavor)

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
