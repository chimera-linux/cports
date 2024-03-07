pkgname = "ecl"
pkgver = "23.9.9"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = ["autoreconf", "-if", "src"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = ["automake", "gmake"]
makedepends = [
    "gc-devel",
    "gmp-devel",
    "libatomic_ops-devel",
    "libffi-devel",
]
pkgdesc = "Embeddable Common Lisp"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "LGPL-2.1-or-later"
url = "https://ecl.common-lisp.dev"
source = f"https://gitlab.com/embeddable-common-lisp/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "2ccda77461f651089d474f57d34c2fcee380ae54e734779b1bf4a4126e2a4686"
options = ["!cross", "!lto"]


def do_check(self):
    build = self.chroot_cwd / "build"
    ecl = build / "bin/ecl"
    self.make.check(
        args=[f"ECL={ecl}"],
        env={
            "LD_LIBRARY_PATH": build,
            "TEST_IMAGE": ecl,
            "ECLDIR": f"{build}/",  # Trailing slash required
        },
    )


def post_install(self):
    self.install_license("LICENSE")

    self.rm(self.destdir / f"usr/lib/ecl-{pkgver}/COPYING")
    self.rm(self.destdir / f"usr/lib/ecl-{pkgver}/LICENSE")
    self.rm(self.destdir / f"usr/lib/ecl-{pkgver}/build-stamp")


@subpackage("ecl-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            f"usr/lib/ecl-{pkgver}/*.a",
            f"usr/lib/ecl-{pkgver}/TAGS",
            f"usr/lib/ecl-{pkgver}/dpp",
            f"usr/lib/ecl-{pkgver}/ecl_min",
        ]
    )


@subpackage("ecl-libs")
def _libs(self):
    return self.default_libs(
        extra=[
            f"usr/lib/ecl-{pkgver}/*.asd",
            f"usr/lib/ecl-{pkgver}/*.fas",
            f"usr/lib/ecl-{pkgver}/help.doc",
            f"usr/lib/ecl-{pkgver}/encodings",
        ]
    )
