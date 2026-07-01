pkgname = "font-iosevka-ttf"
pkgver = "34.4.0"
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
    "fcaf1c13038f47dc28ebd88014419e194b70f39a2823aa09f962f51a78b1a56b",
    "80c34db9a193578dda22b89780f153a40e4d3982162019bea3894fa9313c789c",
    "23f27046c75a456a121a132296be498bf199dd75a779d4af35143de5ba0fad74",
    "ef0e85e38c8f97111a1a9db5706bd69f0a660d1244a6c93e3a9edcaf26ff2224",
    "e419d34a8080bb4a588339ea98489b64b1068bb65c964356931e678f39bcecea",
    "dcb87a902ab2d753dfb912a2646b83d404db13559a03745a8a01f36fa921b23d",
    "cab5209874b83a1628d211d20cc7953083fe2d1ec7447ed2dc34cb8b7e379855",
    "f0d7e25eb84993ab1340342155a03d42f855ccf01191327eab8b77d6299cfdad",
    "b81aa146aeae04486d7b7f1ba367be99dde6286b6d27be540d37729b10f4331d",
    "4341a8e0004df5927ce01c0095026d70ef51bf848c4db8bc6c642f5af8048bf8",
    "81a1a3c55e8d495cf5dbb0d6f615cff65e314ffd84c004638335f86392eb6725",
    "3db76f82e1c25d46e7f761301756984234472d5b6e1068ca3cfb08d0886bb75f",
    "1836d77abf119b65b4a61d4a74622b69b48fc60122b1b32eb68f7fde0ce3d715",
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
