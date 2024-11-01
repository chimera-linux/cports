pkgname = "libvpx"
pkgver = "1.15.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--enable-shared",
    "--enable-pic",
    "--enable-vp8",
    "--enable-vp9",
    "--enable-multithread",
    "--enable-postproc",
    "--enable-vp9-postproc",
    "--enable-temporal-denoising",
    "--enable-vp9-temporal-denoising",
    "--enable-experimental",
    "--enable-runtime-cpu-detect",
    "--disable-static",
    "--disable-install-srcs",
]
hostmakedepends = ["pkgconf", "perl", "nasm"]
makedepends = ["linux-headers"]
pkgdesc = "VP8 and VP9 codec implementation"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "http://www.webmproject.org"
source = [f"https://github.com/webmproject/libvpx/archive/v{pkgver}.tar.gz"]
sha256 = ["e935eded7d81631a538bfae703fd1e293aad1c7fd3407ba00440c95105d2011e"]
# tests take several hours and require ~a gigabyte of test data
options = ["!check"]

_testing = False

# if you really feel like it, toggle the above
if _testing:
    options = []
    configure_args += ["--enable-unit-tests"]
    source += [
        (
            f"http://distfiles.gentoo.org/distfiles/20/libvpx-testdata-{pkgver}.tar.xz",
            False,
        )
    ]
    sha256 += [
        "779005d9d52f37244f7d80da9aa9e04573574a163ead0a0e5f8ca9337eb371f7"
    ]

match self.profile().arch:
    case "aarch64":
        _tgt = "arm64-linux-gcc"
    case "ppc64le":
        _tgt = "ppc64le-linux-gcc"
    case "x86_64":
        _tgt = "x86_64-linux-gcc"
        tools = {"AS": "nasm"}
    case _:
        _tgt = "generic-gnu"

configure_args += [f"--target={_tgt}"]


def post_extract(self):
    if not _testing:
        return

    self.do(
        "tar",
        "xf",
        self.chroot_sources_path / f"libvpx-testdata-{pkgver}.tar.xz",
    )


def init_install(self):
    self.make_install_args += [f"DIST_DIR={self.chroot_destdir / 'usr'}"]


def post_install(self):
    self.install_license("LICENSE")


def init_check(self):
    self.make_check_env = {
        "LIBVPX_TEST_DATA_PATH": str(self.chroot_cwd / "libvpx-testdata")
    }


@subpackage("libvpx-devel")
def _(self):
    return self.default_devel()


@subpackage("libvpx-progs")
def _(self):
    return self.default_progs()
