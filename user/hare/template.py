pkgname = "hare"
pkgver = "0.25.2"
pkgrel = 0
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_dir = "."
make_build_args = [
    f"ARCH={self.profile().arch}",
    f"{self.profile().arch.upper()}_CC=cc",
    f"{self.profile().arch.upper()}_LD=ld",
    f"VERSION={pkgver}-chimera",
    "LIBEXECDIR=/usr/lib",  # XXX libexecdir
]
make_install_args = [*make_build_args]
hostmakedepends = [
    f"binutils-{self.profile().arch}",
    "harec",
    "qbe",
    "scdoc",
]
depends = ["binutils", "clang", "harec", "qbe", "tzdb"]
checkdepends = ["tzdb"]
pkgdesc = "Hare programming language"
license = "MPL-2.0 AND GPL-3.0-only"
url = "https://harelang.org"
source = f"https://git.sr.ht/~sircmpwn/hare/archive/{pkgver}.tar.gz"
sha256 = "d0baf74f4e20a3a875ddd8e2b299032ada4e5de17d8413053cad0f709446348e"
tools = {"AS": f"{self.profile().triplet}-as"}

match self.profile().arch:
    case "x86_64":
        make_build_args += ["QBEFLAGS=-tamd64_sysv"]
    case "aarch64":
        make_build_args += ["QBEFLAGS=-tarm64"]
    case "riscv64":
        make_build_args += ["QBEFLAGS=-trv64"]
    case _:
        broken = f"unknown architecture {self.profile().arch}"

if self.profile().cross:
    hostmakedepends += ["hare"]
    make_build_args += ["HARE=hare", "HAREDOC=haredoc"]
else:
    make_build_args += [
        "HARE=.bin/hare",
        "HAREC=/usr/bin/harec",
        "HAREDOC=.bin/haredoc",
    ]


def pre_build(self):
    self.cp("configs/linux.mk", "config.mk")
