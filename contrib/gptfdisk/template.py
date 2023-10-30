pkgname = "gptfdisk"
pkgver = "1.0.9"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_dir = "."
make_check_target = "test"
hostmakedepends = ["gmake"]
makedepends = [
    "linux-headers",
    "libuuid-devel",
    "ncurses-devel",
    "popt-devel",
]
pkgdesc = "Fdisk-like partitioning tool for GPT disks"
maintainer = "reocat <ng.ct_ml@tuta.io>"
license = "GPL-2.0-or-later"
url = "https://sourceforge.net/projects/gptfdisk"
source = f"$(SOURCEFORGE_SITE)/gptfisk/{pkgver}/gptfdisk-{pkgver}.tar.gz"
sha256 = "dafead2693faeb8e8b97832b23407f6ed5b3219bc1784f482dd855774e2d50c2"
hardening = ["vis", "cfi"]


def do_check(self):
    self.do(
        "sh",
        "gdisk_test.sh",
    )


def do_install(self):
    self.install_bin("cgdisk")
    self.install_bin("fixparts")
    self.install_bin("gdisk")
    self.install_bin("sgdisk")
