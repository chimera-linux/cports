pkgname = "fonts-iosevka"
pkgver = "32.5.0"
pkgrel = 0
pkgdesc = "Versatile typeface for code, from code"
maintainer = "sewn <sewn@disroot.org>"
license = "OFL-1.1"
url = "https://typeof.net/Iosevka"
_download = f"https://github.com/be5invis/Iosevka/releases/download/v{pkgver}"
# Filled later in the template
source = [
    f"!https://github.com/be5invis/Iosevka/raw/refs/tags/v{pkgver}/LICENSE.md",
]
sha256 = [
    "52579dd4ebbda8e5a9d314e395dbfe40de82b4b7b3007ec8458876823af8dddd",
    "155e0e29ddd03d26ea132afa9014baa0bcba220ab00d495e7a72da5478c75d4b",
    "50d87e52d632bb14cf4beb03f4d45e5c1bcc204919d1746330629ad1ea67e38d",
    "768cdb9840a821623f7e5aa60d48f8beb3c563f2073972d0ad270233f5e98937",
    "3d636d73110775d5658c85dfc6a69990487eb4cd59a6ad7c025983c189a7903c",
    "0b578ef9e5a018c39a8bc83be72fdfe3b395ede41e54621bc8371443b441c00c",
    "6934ad8230e59957e81ed2b697816b5eecd852d3b89789b19f280ef50db8bc01",
    "d9ae3ba9b9ca169c97bdcf62b17d8e8b8e2740d966046cd23b3e7fab0d006032",
    "600d1a9a32d56e13d2cd6620a868a1f0f22b310c0efb29d79544008cdb10ca90",
    "4e02545898f38eb91c48252953c1f186c872bac41b0e324de866286a66408e4f",
    "209180c3100d32b38cce9ea4c978fe4aed661eab4a3cc7f6e7b06029ca4deacf",
]
options = ["empty"]

_fonts = [
    # family > sub-family > style
    ("base", ""),
    ("term", "Term"),
    ("aile", "Aile"),
    ("etoile", "Etoile"),
    ("slab", "Slab"),
    ("slab-term", "TermSlab"),
    ("slab-curly", "CurlySlab"),
    ("slab-term-curly", "TermCurlySlab"),
    ("curly", "Curly"),
    ("term-curly", "TermCurly"),
]


def install(self):
    self.install_file(
        "Iosevka*.ttf",
        "usr/share/fonts/iosevka",
        glob=True,
    )
    self.install_license(self.sources_path / "LICENSE.md")


def _font_subpackage(package, name):
    @subpackage(f"fonts-iosevka-{package}")
    def _(self):
        self.install_if = [self.parent]
        return [
            f"usr/share/fonts/iosevka/Iosevka{name}-*.ttf",
        ]


for _package, _name in _fonts:
    source.append(f"{_download}/PkgTTF-Iosevka{_name}-{pkgver}.zip")
    _font_subpackage(_package, _name)
