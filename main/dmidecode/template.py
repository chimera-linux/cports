pkgname = "dmidecode"
pkgver = "3.7"
pkgrel = 0
# smbios/dmi support
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_install_args = ["prefix=/usr", "sbindir=/usr/bin"]
hostmakedepends = ["pkgconf"]
makedepends = ["bash-completion"]
pkgdesc = "Utility for reporting system hardware"
license = "GPL-2.0-or-later"
url = "https://nongnu.org/dmidecode"
source = f"https://download.savannah.gnu.org/releases/dmidecode/dmidecode-{pkgver}.tar.xz"
sha256 = "2c3aed12c85a1e6a9410d406d5e417c455466dc1bc7c89278bb32cf7cad91e8a"
hardening = ["vis", "cfi"]
# none present
options = ["!check"]
