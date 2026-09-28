pkgname = "patchelf"
pkgver = "0.19.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["automake"]
pkgdesc = "Utility to modify the dynamic linker and RPATH of ELF executables"
license = "GPL-3.0-or-later"
url = "https://github.com/NixOS/patchelf"
source = f"{url}/releases/download/{pkgver}/patchelf-{pkgver}.tar.bz2"
sha256 = "2cce01de93653829f6ab68a20c2ec275e1c00a946110704a27e928d2e6e88716"
hardening = ["vis", "cfi"]
# don't run for some reason
options = ["!check"]
