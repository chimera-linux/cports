pkgname = "cryptsetup"
pkgver = "2.7.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-crypto_backend=openssl",
    "--enable-libargon2",
    "--enable-static-cryptsetup",
    "--disable-ssh-token",
    "--disable-asciidoc",
]
hostmakedepends = [
    "automake",
    "bash",
    "gettext-devel",
    "libtool",
    "pkgconf",
]
makedepends = [
    "device-mapper-devel-static",
    "openssl-devel-static",
    "popt-devel-static",
    "json-c-devel-static",
    "libuuid-devel-static",
    "argon2-devel-static",
    "libatomic-chimera-devel-static",
    "linux-headers",
]
checkdepends = ["procps", "xz"]
pkgdesc = "Open source Linux disk encryption setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/cryptsetup/cryptsetup"
source = (
    f"$(KERNEL_SITE)/utils/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "da5d1419e2a86e01aa32fd79582cd54d208857cb541bca2fd426a5ff1aaabbc3"

if self.profile().arch == "riscv64":
    # udev static library weirdness
    makedepends += ["libcap-devel-static"]
    configure_args += ["LIBS=-lcap"]


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
