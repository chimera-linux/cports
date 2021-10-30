pkgname = "linux"
pkgver = "5.14.14"
pkgrel = 0
make_dir = "build"
hostmakedepends = [
    "bash", "bc-gh", "binutils", "bison", "findutils", "flex",
    "elftoolchain-devel", "gmake", "gsed", "gtar", "kmod",
    "linux-headers", "openssl-devel", "perl", "python",
]
pkgdesc = "Linux kernel (5.14.x)"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://kernel.org"
source = f"https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-{pkgver}.tar.xz"
sha256 = "4dff4e96d4052195002538027f8a810411ba6116a41bff5575952702d509d06a"
# no meaningful checking to be done
options = [
    "!check", "!debug", "!strip", "!scanrundeps", "!scanshlibs", "!cross"
]

match current.profile().arch:
    case "ppc64le": _arch = "powerpc"
    case "aarch64": _arch = "arm64"
    case _:
        broken = f"Unknown CPU architecture: {current.profile().arch}"

def do_configure(self):
    cfgarch = self.profile().arch
    cfgname = f"config-{cfgarch}.generic"

    self.cp(self.files_path / cfgname, self.cwd)

    epoch = self.source_date_epoch or 0

    self.do("chimera-buildkernel", [
        "prepare",
        f"ARCH={_arch}",
        f"CONFIG_FILE={self.chroot_cwd}/{cfgname}",
        f"OBJDIR={self.make_dir}",
        f"JOBS={self.make_jobs}",
        f"LOCALVERSION=-{pkgrel}-generic",
        f"EPOCH={epoch}"
    ])

def do_build(self):
    self.do("chimera-buildkernel", ["build"])

def do_install(self):
    self.do("chimera-buildkernel", ["install", self.chroot_destdir])

@subpackage("linux-devel")
def _devel(self):
    self.depends += ["binutils"]
    return ["usr/src", "usr/lib/modules/*/build"]

@subpackage("linux-dbg")
def _dbg(self):
    self.pkgdesc += " (debug files)"
    self.options = ["!scanrundeps", "!strip", "!scanshlibs"]
    return ["usr/lib/debug", "boot/System.map-*"]
