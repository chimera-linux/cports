pkgname = "ecl"
pkgver = "24.5.10"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["autoreconf", "-if", "src"]
make_dir = "."
hostmakedepends = ["automake"]
makedepends = [
    "gc-devel",
    "gmp-devel",
    "libatomic_ops-devel",
    "libffi8-devel",
]
pkgdesc = "Embeddable Common Lisp"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "LGPL-2.1-or-later"
url = "https://ecl.common-lisp.dev"
source = f"https://gitlab.com/embeddable-common-lisp/ecl/-/archive/{pkgver}/ecl-{pkgver}.tar.gz"
sha256 = "7d21ac3bd99132cfb1bb2d73d31d602a536f3a31dac6b982007a8291372dd0bf"
options = ["!cross", "!lto"]


def check(self):
    build = self.chroot_cwd / "build"
    ecl = build / "bin/ecl"
    self.make.check(
        args=[f"ECL={ecl}", "SHELL=/bin/sh"],
        env={
            "LD_LIBRARY_PATH": build,
            "TEST_IMAGE": ecl,
            "ECLDIR": f"{build}/",  # Trailing slash required
        },
    )


def post_install(self):
    self.install_license("LICENSE")

    self.uninstall(f"usr/lib/ecl-{pkgver}/COPYING")
    self.uninstall(f"usr/lib/ecl-{pkgver}/LICENSE")
    self.uninstall(f"usr/lib/ecl-{pkgver}/build-stamp")


@subpackage("ecl-devel")
def _(self):
    return self.default_devel(
        extra=[
            f"usr/lib/ecl-{pkgver}/*.a",
            f"usr/lib/ecl-{pkgver}/TAGS",
            f"usr/lib/ecl-{pkgver}/dpp",
            f"usr/lib/ecl-{pkgver}/ecl_min",
        ]
    )


@subpackage("ecl-libs")
def _(self):
    return self.default_libs(
        extra=[
            f"usr/lib/ecl-{pkgver}/*.asd",
            f"usr/lib/ecl-{pkgver}/*.fas",
            f"usr/lib/ecl-{pkgver}/help.doc",
            f"usr/lib/ecl-{pkgver}/encodings",
        ]
    )
