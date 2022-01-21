pkgname = "cryptsetup"
pkgver = "2.4.3"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-crypto_backend=openssl", "--enable-cryptsetup-reencrypt",
    "--enable-libargon2", "--enable-static-cryptsetup", "--disable-ssh-token",
]
hostmakedepends = ["pkgconf", "bash"]
makedepends = [
    "device-mapper-devel-static", "openssl-devel-static", "popt-devel-static",
    "json-c-devel-static", "libuuid-devel-static", "argon2-devel-static",
    "linux-headers",
]
checkdepends = ["procps-ng", "xz"]
pkgdesc = "Open source Linux disk encryption setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/cryptsetup/cryptsetup"
source = f"$(KERNEL_SITE)/utils/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fc0df945188172264ec5bf1d0bda08264fadc8a3f856d47eba91f31fe354b507"

@subpackage("cryptsetup-static-bin")
def _sbin(self):
    self.pkgdesc = f"{pkgdesc} (static binaries)"

    return ["usr/bin/*.static"]

@subpackage("libcryptsetup")
def _lib(self):
    self.pkgdesc = f"{pkgdesc} (runtime library)"

    return self.default_libs()

@subpackage("cryptsetup-devel")
def _devel(self):
    return self.default_devel()
