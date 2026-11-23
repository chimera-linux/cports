pkgname = "patchelf"
pkgver = "0.19.3"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Utility to modify the dynamic linker and RPATH of ELF executables"
license = "GPL-3.0-or-later"
url = "https://github.com/NixOS/patchelf"
source = f"{url}/releases/download/{pkgver}/patchelf-{pkgver}.tar.bz2"
sha256 = "20dbe23e9dbc4ad769078a867ad002c04297a069ff93c95fb72242dd55d4dd6f"
hardening = ["vis", "cfi"]
# don't run for some reason
options = ["!check"]
