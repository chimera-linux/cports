pkgname = "hunspell-en"
pkgver = "2020.12.07"
pkgrel = 0
pkgdesc = "English language dictionaries for hunspell"
maintainer = "psykose <alice@ayaya.dev>"
license = "MIT"
url = "http://wordlist.aspell.net/dicts"
source = [
    f"$(SOURCEFORGE_SITE)/wordlist/speller/{pkgver}/hunspell-en_US-{pkgver}.zip",
    f"$(SOURCEFORGE_SITE)/wordlist/speller/{pkgver}/hunspell-en_CA-{pkgver}.zip",
    f"$(SOURCEFORGE_SITE)/wordlist/speller/{pkgver}/hunspell-en_AU-{pkgver}.zip",
    f"$(SOURCEFORGE_SITE)/wordlist/speller/{pkgver}/hunspell-en_GB-large-{pkgver}.zip",
]
sha256 = [
    "616348ad645a716d91c8a6645065e710f15e9dda3ffef60cdf7ec8a4e27975af",
    "ff6b91e4ed768348c61ae7c326e848059810fa43a5d601df6b3f45ad9c0ef5bf",
    "dc20557c48ae1979784e79fae6f965e999c8db2e9a0f846348e70057fce78254",
    "f86beb77228c737c8c69468ffc4ea067512872278869b98a5d3ec18f125107bd",
]


def do_install(self):
    self.install_license("README_en_CA.txt")
    self.install_license("README_en_GB-large.txt")
    self.install_license("README_en_US.txt")

    self.install_file("./en_*.dic", "usr/share/hunspell", glob=True)
    self.install_file("./en_*.aff", "usr/share/hunspell", glob=True)
