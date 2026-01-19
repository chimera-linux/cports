pkgname = "mkvtoolnix"
pkgver = "97.0"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-optimization",
    "--disable-update-check",
    "--with-docbook-xsl-root=/usr/share/xsl-nons/docbook",
    # boost 1.89: work around custom build macros
    "--with-boost-system=c",
]
make_cmd = "rake"
make_dir = "."
make_check_target = ""
make_check_args = ["tests:unit", "tests:run_unit"]
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "gettext",
    "libxslt-progs",
    "pkgconf",
    "qt6-qtbase",
    "ruby",
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
license = "GPL-2.0-only"
url = "https://mkvtoolnix.download"
source = f"{url}/sources/mkvtoolnix-{pkgver}.tar.xz"
sha256 = "5d43bf66e011ff5af09516a2dba2fb717b1631791a3a7498fcf74849a86929d3"


@subpackage("mkvtoolnix-gui")
def _(self):
    self.depends += [
        self.parent,
        "qt6-qtsvg",
    ]
    return [
        "cmd:mkvtoolnix-gui",
        "usr/share/applications",
        "usr/share/icons",
        "usr/share/metainfo",
        "usr/share/mime",
        "usr/share/mkvtoolnix",
    ]
