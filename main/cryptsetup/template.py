pkgname = "cryptsetup"
pkgver = "2.7.5"
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
sha256 = "d2be4395b8f503b0ebf4b2d81db90c35a97050a358ee21fe62a0dfb66e5d5522"

if not self.has_lto(force=True):
    # udev static library weirdness
    makedepends += ["libcap-devel-static"]
    configure_args += ["LIBS=-lcap"]


@subpackage("cryptsetup-static-bin")
def _(self):
    self.subdesc = "static binaries"

    return ["usr/bin/*.static"]


@subpackage("libcryptsetup")
def _(self):
    self.subdesc = "runtime library"

    return self.default_libs()


@subpackage("cryptsetup-devel")
def _(self):
    return self.default_devel()
