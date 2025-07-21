pkgname = "cryptsetup"
pkgver = "2.7.5"
pkgrel = 2
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
    "json-c-devel-static",
    "libatomic-chimera-devel-static",
    "linux-headers",
    "lvm2-devel-static",
    "openssl3-devel-static",
    "popt-devel-static",
    "util-linux-uuid-devel-static",
]
checkdepends = ["procps", "xz"]
pkgdesc = "Open source Linux disk encryption setup"
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


@subpackage("cryptsetup-libs")
def _(self):
    # transitional
    self.provides = [self.with_pkgver("libcryptsetup")]

    return self.default_libs()


@subpackage("cryptsetup-devel")
def _(self):
    return self.default_devel()
