pkgname = "mupdf"
pkgver = "1.25.4"
_sover = f"{pkgver[pkgver.find('.') + 1 :]}"
pkgrel = 0
build_style = "makefile"
make_dir = "."
make_use_env = True
hostmakedepends = [
    "automake",
    "python",
    "pkgconf",
    "xxd",
]
makedepends = [
    "curl-devel",
    "freeglut-devel",
    "freetype-devel",
    "gtest-devel",
    "gumbo-parser-devel",
    "harfbuzz-devel",
    "jbig2dec-devel",
    "lcms2-devel",
    "leptonica-devel",
    "libjpeg-turbo-devel",
    "openjpeg-devel",
    "openssl-devel",
    "tesseract-devel",
    "zlib-ng-compat-devel",
]
provides = [
    f"{self.with_pkgver('so:libmupdf')}",
    f"{self.with_pkgver(f'so:libmupdf.so.{_sover}')}",
]
pkgdesc = "Framework for viewing and converting PDF, XPS, and E-book documents"
maintainer = "ttyyls <contact@behri.org>"
license = "AGPL-3.0-or-later"
url = "http://www.mupdf.com"
source = f"https://mupdf.com/downloads/archive/mupdf-{pkgver}-source.tar.gz"
sha256 = "74b943038fe81594bf7fc5621c60bca588b2847f0d46fb2e99652a21fa0d9491"
# no tests defined and non standard so versionning
options = ["!check", "!scanshlibs"]


def init_configure(self):
    self.make_build_args = [
        "USE_SYSTEM_LIBS=yes",
        "USE_SYSTEM_MUJS=no",
        "USE_SYSTEM_LCMS2=yes",
        f"LD={self.get_tool('CC')}",
        "shared=yes",
        "verbose=yes",
        f"XCFLAGS={self.get_cflags(shell=True)}",
        f"XLDFLAGS={self.get_ldflags(shell=True)}",
    ]


def post_build(self):
    with open(self.cwd / "mupdf.pc", "w") as outf:
        outf.write(
            f"""
            Name: mupdf
            Description: {self.pkgdesc}
            URL: {self.url}
            Version: {self.pkgver}
            Libs: -lmupdf
            """
        )


def install(self):
    self.install_license("COPYING")
    self.install_man("docs/man/*.1", glob=True)
    self.install_file(
        self.files_path / "mupdf.desktop",
        "usr/share/applications",
    )
    with self.pushd("docs/logo"):
        self.install_file(
            "mupdf-logo.svg",
            "usr/share/icons/hicolor",
            name="mupdf.svg",
        )
        for i in [16, 24, 32, 48, 72, 128, 256, 512]:
            self.install_file(
                f"mupdf-icon-{i}.png",
                f"usr/share/icons/hicolor/{i}x{i}/apps",
                name="mupdf.png",
            )
    self.install_files("include/mupdf", "usr/include")
    self.install_file("mupdf.pc", "usr/lib/pkgconfig")
    with self.pushd("build/shared-release"):
        self.install_lib(f"libmupdf.so.{_sover}")
        self.install_lib("libmupdf.so")
        self.install_bin("mupdf-x11")
        self.install_bin("mupdf-x11-curl")
        self.install_bin("mupdf-gl")
        self.install_bin("mutool")
        self.install_bin("muraster")


@subpackage("mupdf-viewer-x11-default")
def _(self):
    self.depends = [self.with_pkgver("mupdf-viewer-x11")]
    self.provides = ["mupdf-viewer=0"]
    self.provider_priority = 0
    return ["@usr/bin/mupdf=>/usr/bin/mupdf-x11"]


@subpackage("mupdf-viewer-x11")
def _(self):
    self.subdesc = "x11 backend"
    return [
        "cmd:mupdf-x11",
        "cmd:mupdf-x11-curl",
    ]


@subpackage("mupdf-viewer-gl-default")
def _(self):
    self.depends = [self.with_pkgver("mupdf-viewer-gl")]
    self.provides = ["mupdf-viewer=0"]
    self.provider_priority = 100
    return ["@usr/bin/mupdf=>/usr/bin/mupdf-gl"]


@subpackage("mupdf-viewer-gl")
def _(self):
    self.subdesc = "OpenGl backend"
    return ["cmd:mupdf-gl"]


@subpackage("mupdf-devel")
def _(self):
    self.depends = [self.parent]
    return self.default_devel()


@subpackage("mupdf-progs")
def _(self):
    return self.default_progs()
