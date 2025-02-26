pkgname = "font-iosevka-ttf"
pkgver = "33.0.1"
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
    "c62c29fcbce39b4c726ce213fe3293d9b1021cdef6d476880e72609169451325",
    "fb069b872be9905f0ce83a6d0ad806f76a2dcad5a2a4c6b9fcf2c6a7c5bc88ea",
    "19f400f2dda272deeb812f42d05a1013c67aae501527b09a8c2e49c141eb1247",
    "da4ccdbc32647c995426058699cc17a9f1b1dca3f299e0b81dd4e525c1e26717",
    "c340410f1c8c634753aa5212b95030d8402ee0593e14d80439fe7d6643a1559a",
    "cc4134209df444ec89845abe1d87ecbd95274b21269af0c0ef3d6559f85c22ad",
    "024683a05e9d83f0985a3663ba0058264f7f3686f653e29e3a792201140a835e",
    "dea5cd9d56049d8c7e73badb6b2079889873860ba30e3a3000ad70335797ae4d",
    "84552e4f378a15075b4a580a6ad833c51b5c575fef9b395c9359a1c744bc9268",
    "08a20178c96604aa13b5d5c2ba7dbd959331c96dc3faee6ca6fd0965faa89ad5",
    "dde71054a77460c86e37c1810060a98ad5ec734ed3ecf697e0dbf6a0cdcabfca",
    "e139db199e5d1d2943a3a2ca794fa59e1705519c4c833dae84119956ed901137",
    "981794becd65f3242e24f6f73838bde41fe153d084586114c00d83b9417f39b6",
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
