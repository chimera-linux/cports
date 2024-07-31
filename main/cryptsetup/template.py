pkgname = "cryptsetup"
pkgver = "2.7.4"
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
    f"$(KERNEL_SITE)/utils/cryptsetup/v{pkgver[:-2]}/cryptsetup-{pkgver}.tar.xz"
)
sha256 = "dce29903a58f7b774fe61191e7e6de955de0f40d9e27b0028ffcf3438c0e9480"

if self.profile().arch == "riscv64":
    # udev static library weirdness
    makedepends += ["libcap-devel-static"]
    configure_args += ["LIBS=-lcap"]


@subpackage("cryptsetup-static-bin")
def _sbin(self):
    self.subdesc = "static binaries"

    return ["usr/bin/*.static"]


@subpackage("libcryptsetup")
def _lib(self):
    self.subdesc = "runtime library"

    return self.default_libs()


@subpackage("cryptsetup-devel")
def _devel(self):
    return self.default_devel()
