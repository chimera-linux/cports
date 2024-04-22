pkgname = "cryptsetup"
pkgver = "2.7.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--with-crypto_backend=openssl",
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
    "json-c-devel-static",
    "libatomic-chimera-devel-static",
    "libuuid-devel-static",
    "linux-headers",
    "openssl-devel-static",
    "popt-devel-static",
]
checkdepends = ["procps", "xz"]
pkgdesc = "Open source Linux disk encryption setup"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/cryptsetup/cryptsetup"
source = (
    f"$(KERNEL_SITE)/utils/{pkgname}/v{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
)
sha256 = "219ebf74e8eddf96624a0376477e5a6f8f350a67aaf36e7dadb114d94b3afef4"

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
