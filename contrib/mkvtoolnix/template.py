pkgname = "mkvtoolnix"
pkgver = "84.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-optimization",
    "--disable-precompiled-headers",
    "--disable-update-check",
    "--with-docbook-xsl-root=/usr/share/xsl/docbook",
]
make_cmd = "rake"
make_dir = "."
make_check_target = ""
make_check_args = ["tests:unit", "tests:run_unit"]
hostmakedepends = [
    "automake",
    "docbook-xsl",
    "gettext",
    "ruby",
    "qt6-qtbase",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "boost-devel",
    "cmark-devel",
    "file-devel",
    "flac-devel",
    "fmt-devel",
    "gmp-devel",
    "gtest-devel",
    "libdvdread-devel",
    "libmatroska-devel",
    "libogg-devel",
    "libvorbis-devel",
    "nlohmann-json",
    "pcre2-devel",
    "pugixml-devel",
    "qt6-qtbase-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
]
pkgdesc = "Tooling for editing and inspecting Matroska files"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://mkvtoolnix.download/index.html"
source = f"https://mkvtoolnix.download/sources/mkvtoolnix-{pkgver}.tar.xz"
sha256 = "e9176dea435c3b06b4716fb131d53c8f2621977576ccc4aee8ff9050c0d9ea7a"

if self.profile().arch == "riscv64":
    broken = "qmake busted under emulation (https://bugreports.qt.io/browse/QTBUG-98951)"


@subpackage("mkvtoolnix-gui")
def _gui(self):
    self.depends += [
        f"{pkgname}={pkgver}-r{pkgrel}",
        "qt6-qtsvg",
    ]
    return [
        "usr/bin/mkvtoolnix-gui",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/man/man1/mkvtoolnix-gui.1",
        "usr/share/metainfo",
        "usr/share/mime",
        "usr/share/mkvtoolnix",
    ]
