pkgname = "dmidecode"
pkgver = "3.6"
pkgrel = 0
# smbios/dmi support
archs = ["aarch64", "riscv64", "x86_64"]
build_style = "makefile"
make_install_args = ["prefix=/usr", "sbindir=/usr/bin"]
hostmakedepends = ["pkgconf"]
makedepends = ["bash-completion"]
pkgdesc = "Utility for reporting system hardware"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://nongnu.org/dmidecode"
source = f"https://download.savannah.gnu.org/releases/dmidecode/dmidecode-{pkgver}.tar.xz"
sha256 = "e40c65f3ec3dafe31ad8349a4ef1a97122d38f65004ed66575e1a8d575dd8bae"
hardening = ["vis", "cfi"]
# none present
options = ["!check"]
