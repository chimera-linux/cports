pkgname = "cryptsetup"
pkgver = "2.8.6"
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
    "libatomic-chimera-devel",
    "libatomic-chimera-devel-static",
    "libunwind-devel",
    "libunwind-devel-static",
    "linux-headers",
    "lvm2-devel",
    "lvm2-devel-static",
    "musl-devel",
    "musl-devel-static",
    "openssl3-devel",
    "openssl3-devel-static",
    "popt-devel",
    "popt-devel-static",
    "udev-devel",
    "udev-devel-static",
    "util-linux-blkid-devel",
    "util-linux-blkid-devel-static",
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
sha256 = "8004265fd993885d08f7b633dbe056851de1a210307613a4ebddc743fccefe5a"

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
