pkgname = "font-iosevka-ttf"
pkgver = "33.2.8"
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
    "9f59dc5c5db58275dedc47e19b73552f6070c98a46621f41031aac7d5ba9770b",
    "34f7f16e5a5f81c0618b6fd731ce4721b02339112346a6fc95772a87d09f77df",
    "8db381943884e5d2a77562548135a1b960eec08595327d333c9ce821e3aa09e3",
    "676e68916df77f4339ad1a6e721e0ccb7c787c145531ad9d6b83eaa84cf55270",
    "bc1d4e901fd1434c14ad11e28de975f1a3427789f30faff790e9331413aab28f",
    "655b8db5317a204ca5770fcdd0405a529f3e765d6b93df77c5553fb4702775c2",
    "6ad9a26492c6dfbcd799860ff84de80d47471ff2b7bd409c942113198647b253",
    "ff9e5639d14351575b594bf492778d1483a37e7c5f20652cb47536aff25f0bee",
    "964b28d6ddd3cf77016f37a9f8b9d29f9a88873c28ce8682b2c3fd04bebb38b5",
    "c9660a3b2736f35f40ab43e3e94d2529365047988c37a669005bae46a657aeee",
    "ba43be36d29585852e11d2b56640fea2d48149ab46b1e0bb6e9affad6cbb70c8",
    "b44d83690d6ef4701bc404124df289fa3a6f86e04f20cea36d6594ee2a134003",
    "dc88059aa4f95396cd584e323fb3312b4c50687c9f234678e972fac832b917c7",
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
