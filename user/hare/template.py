pkgname = "hare"
pkgver = "0.24.0"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_env = {"VERSION": pkgver, "LOCALVER": "chimera"}
make_build_args = [
    f"ARCH={self.profile().arch}",
    f"{self.profile().arch.upper()}_CC=cc",
    f"{self.profile().arch.upper()}_LD=ld",
]
hostmakedepends = [f"binutils-{self.profile().arch}", "harec", "qbe", "scdoc"]
# hare is a metapackage pointing to the current target hare
depends = [f"hare-{self.profile().arch}"]
checkdepends = ["tzdata"]
pkgdesc = "Hare programming language"
maintainer = "triallax <triallax@tutanota.com>"
license = "MPL-2.0 AND GPL-3.0-only"
url = "https://harelang.org"
source = f"https://git.sr.ht/~sircmpwn/hare/archive/{pkgver}.tar.gz"
sha256 = "7061dad3c79cca51a1662a71b1c6f8ec001f52ef3053dd3c2dbb95ae9beff7bc"
tools = {"AS": f"{self.profile().triplet}-as"}

match self.profile().arch:
    case "x86_64":
        _qbe_arch = "amd64_sysv"
    case "aarch64":
        _qbe_arch = "arm64"
    case "riscv64":
        _qbe_arch = "rv64"
    case _:
        broken = f"unknown architecture {self.profile().arch}"
        _qbe_arch = ""

make_build_args.append(f"QBEFLAGS=-t{_qbe_arch}")

if self.profile().cross:
    hostmakedepends.append("hare")
    make_build_args.append("HARE=hare")
else:
    make_build_args.append("HARE=.bin/hare")


def pre_build(self):
    self.cp(self.files_path / "config.mk", "config.mk")


def _add_cross_package(arch, native):
    @subpackage(f"hare-{arch}")
    def _cross_pkg(self):
        self.pkgdesc = f"{pkgdesc} ({arch})"
        self.depends = [
            f"{pkgname}={pkgver}-r{pkgrel}",
            "harec",
            "qbe",
            "tzdata",
        ]
        self.options = ["empty"]

        if native:
            self.depends += ["clang", "binutils"]
        else:
            self.depends += [f"base-cross-{arch}", f"binutils-{arch}"]

        return []


for _arch in archs:
    _add_cross_package(_arch, _arch == self.profile().arch)
