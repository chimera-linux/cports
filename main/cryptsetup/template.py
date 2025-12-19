pkgname = "cryptsetup"
pkgver = "2.8.0"
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
    "json-c-devel",
    "json-c-devel-static",
    "libatomic-chimera-devel-static",
    "linux-headers",
    "lvm2-devel",
    "lvm2-devel-static",
    "openssl3-devel",
    "openssl3-devel-static",
    "popt-devel",
    "popt-devel-static",
    "util-linux-uuid-devel",
    "util-linux-uuid-devel-static",
]
checkdepends = ["procps", "xz"]
pkgdesc = "Open source Linux disk encryption setup"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/cryptsetup/cryptsetup"
source = (
    f"$(KERNEL_SITE)/utils/cryptsetup/v{pkgver[:-2]}/cryptsetup-{pkgver}.tar.xz"
)
sha256 = "cc9e2d37c25a871cea37520b28d532207b0c1670fb10fc54d68071f63f5243a2"

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
