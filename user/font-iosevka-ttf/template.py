pkgname = "font-iosevka-ttf"
pkgver = "33.2.0"
pkgrel = 0
pkgdesc = "Versatile typeface for code, from code"
license = "OFL-1.1"
url = "https://typeof.net/Iosevka"
_download = f"https://github.com/be5invis/Iosevka/releases/download/v{pkgver}"
# Filled later in the template
source = [
    f"!https://github.com/be5invis/Iosevka/raw/refs/tags/v{pkgver}/LICENSE.md",
    f"{_download}/PkgTTF-Iosevka-{pkgver}.zip",
]
sha256 = [
    "52579dd4ebbda8e5a9d314e395dbfe40de82b4b7b3007ec8458876823af8dddd",
    "fdab635ad44112f354e4dee1cc49a177d755082780aa5914f61e1dd9ca59ed72",
    "1d8a9b0ba00eef56b3de8d0978622c4129acb5b2ba86a961a7a0286489f72468",
    "26bed9932bfd8cae7f5ce7f626da29380cbba7da14483544cb9e8394664f0f01",
    "3324c8c62feb9dd03a238bed799fbe6e27e4d66adcb7a17eca1bfc77be43f80b",
    "deb0a54880cb8de1cedb19839ed370c0330f8ed13d076a834d51bdc01fc1baf8",
    "c2c9350059f8bf24a43d499dff65c01e68faa440b8003582041ce32285f892b6",
    "5cc60b873af064a12c6e9688b0fb1f46d4ada9c55a2cc65c303fe24f706e04e7",
    "d155b32198cf411381944fbea99837b6048c0286206b62eba0e21bdac2039049",
    "52e3cfc2d5a510a632df9c9cf50b7922153a8fd1486d047d15bd864d642d9d76",
    "4022bab25181debc670e6a4c82b5eb0feeb3b158aefe01536d33a36652708ac2",
    "b9a2dca08bd408a1825d7eeb0bb015bce8f78d60e053445cd6c83f99f11d6fa3",
    "7a492d5e14ec11f14593a64aad553b64c0594a9d2c65d7f1d7d6ec848dec2f3c",
    "197900e4f98b093210069790d67f04d56a8239a0cb2c935b5a410a82b851e39c",
]

_variants = [
    "Term",
    "Aile",
    "Etoile",
    "Slab",
    "TermSlab",
    "FixedSlab",
    "CurlySlab",
    "TermCurlySlab",
    "FixedCurlySlab",
    "Curly",
    "TermCurly",
    "FixedCurly",
]


def install(self):
    self.install_file(
        "Iosevka*.ttf",
        "usr/share/fonts/iosevka",
        glob=True,
    )
    self.install_license(self.sources_path / "LICENSE.md")


def _font_subpackage(package, variant):
    @subpackage(f"font-iosevka{package}-ttf")
    def _(self):
        return [
            f"usr/share/fonts/iosevka/Iosevka{variant}-*.ttf",
        ]


for _variant in _variants:
    _package = "".join(
        ["-" + c.lower() if c.isupper() else c for c in _variant]
    )
    source.append(f"{_download}/PkgTTF-Iosevka{_variant}-{pkgver}.zip")
    _font_subpackage(_package, _variant)
