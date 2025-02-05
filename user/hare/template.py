pkgname = "hare"
pkgver = "0.24.2"
pkgrel = 1
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_env = {"LOCALVER": "chimera"}
make_build_args = [
    f"ARCH={self.profile().arch}",
    f"{self.profile().arch.upper()}_CC=cc",
    f"{self.profile().arch.upper()}_LD=ld",
]
hostmakedepends = [f"binutils-{self.profile().arch}", "harec", "qbe", "scdoc"]
depends = ["binutils", "clang", "harec", "qbe", "tzdb"]
checkdepends = ["tzdb"]
pkgdesc = "Hare programming language"
maintainer = "triallax <triallax@tutanota.com>"
license = "MPL-2.0 AND GPL-3.0-only"
url = "https://harelang.org"
source = f"https://git.sr.ht/~sircmpwn/hare/archive/{pkgver}.tar.gz"
sha256 = "afba69fd537a63442da53d115d9b50f525918159b395843ede2a5473323e0776"
tools = {"AS": f"{self.profile().triplet}-as"}

match self.profile().arch:
    case "x86_64":
        make_build_args += ["QBEFLAGS=-tamd64_sysv"]
    case "aarch64":
        make_build_args += ["QBEFLAGS=-tarm64"]
    case "riscv64":
        make_build_args += ["QBEFLAGS=-trv64"]
        broken = "function not implemented when running hare on builder"
    case _:
        broken = f"unknown architecture {self.profile().arch}"

if self.profile().cross:
    hostmakedepends += ["hare"]
    make_build_args += ["HARE=hare"]
else:
    make_build_args += ["HARE=.bin/hare", "HAREC=/usr/bin/harec"]


def pre_build(self):
    self.cp(self.files_path / "config.mk", "config.mk")
