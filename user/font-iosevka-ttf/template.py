pkgname = "font-iosevka-ttf"
pkgver = "33.2.7"
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
    "e03a65db743025e85dd888e7f6c91db2a2b39a4eb158e837ba5def29f886d011",
    "9f0e52e314adbaf30b7fa460e94415034eaefae841a3df88642cad0ff85a35b0",
    "c5b3e565ec41c7596959cb839c70789890898accae1ce98e13a85ee3e891829d",
    "6f457c283ecb4008582534f28147ef9f13338f192451efa32dbbac460d08911d",
    "c0eb4935aede1cdb71c92d70d12fef6755714268fb18469dc3a4b2d732f5af25",
    "3f1c9f499f23a734d2481a259c2d4d2d7b91d8e1c9ecc4c08ac5e18eec9c3bdf",
    "13f0f253ea41c6967231b5ee4bfcf69efbff4906bbade10c416d3c0cc1b7c2be",
    "9d8641bf41c8ded9779dae41a588c2eaa5c29eb3109c6c0297f91f562a728491",
    "1be47880e78140facaa9b74d450ff2b707ee0954bac1c73e664656369dade2e0",
    "c7a047ed1b17a0c78444403f0e8c4544fed657df00a065af0bac3a012215f2c9",
    "e453f3345dc4539a79dba5bc4548bf7b7709a9aaa37ce6b8349177acac0a5bf6",
    "6e4cccdcf3f2be836252da4c7fd957c2bedcf8be478d16c7c50efccf1396d3f0",
    "313fdb49add46f2decacef6bd45f041b3d948f4c5431c267eda806e4e8c1a65f",
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
