# update linux-lts-zfs-bin when bumping
pkgname = "linux-lts"
pkgver = "6.1.0"
pkgrel = 0
make_dir = "build"
hostmakedepends = ["base-kernel-devel"]
depends = ["base-kernel"]
provides = ["linux"]
pkgdesc = "Linux kernel 6.1.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[0]}.x/linux-{pkgver[:-2]}.tar.xz"
sha256 = "2ca1f17051a430f6fed1196e4952717507171acfd97d96577212502703b25deb"
# no meaningful checking to be done
options = [
    "!check", "!debug", "!strip", "!scanrundeps", "!scanshlibs",
    "!lto", "textrels", "foreignelf" # vdso32
]

_flavor = "generic"

match self.profile().arch:
    case "aarch64" | "ppc64le" | "ppc64" | "riscv64" | "x86_64":
        pass
    case _:
        broken = f"Unknown CPU architecture: {self.profile().arch}"

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

@subpackage("linux-lts-devel")
def _devel(self):
    self.depends += ["clang"]
    self.options = ["foreignelf", "!scanshlibs"]
    return ["usr/src", "usr/lib/modules/*/build"]

@subpackage("linux-lts-dbg")
def _dbg(self):
    self.pkgdesc += " (debug files)"
    self.options = [
        "!scanrundeps", "!strip", "!scanshlibs", "foreignelf", "textrels"
    ]
    return ["usr/lib/debug", "boot/System.map-*"]
