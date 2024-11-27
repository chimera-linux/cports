pkgname = "patchelf"
pkgver = "0.18.0"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Utility tomodify the dynamic linker and RPATH of ELF executables"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://github.com/NixOS/patchelf"
source = f"https://github.com/NixOS/patchelf/releases/download/{pkgver}/patchelf-{pkgver}.tar.bz2"
sha256 = "1952b2a782ba576279c211ee942e341748fdb44997f704dd53def46cd055470b"
hardening = ["vis", "cfi"]
# don't run for some reason
options = ["!check"]
