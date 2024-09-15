# keep in sync with texlive
pkgname = "texmf"
pkgver = "20240312"
pkgrel = 0
pkgdesc = ""  # TODO
maintainer = "Subhaditya Nath <sn03.general@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://tug.org/texlive"
source = f"https://ftp.math.utah.edu/pub/tex/historic/systems/texlive/{pkgver[:4]}/texlive-{pkgver}-texmf.tar.xz"
sha256 = "c8eae2deaaf51e86d93baa6bbcc4e94c12aa06a0d92893df474cc7d2a012c7a7"


def post_extract(self):
    # delete binaries from /usr/share
    self.rm("texmf-dist/doc/luatex/opbible/txs-gen/mod2tex")
    self.rm("texmf-dist/doc/fonts/gnu-freefont/tools/generate/buildutils.pyc")


def install(self):
    self.install_files("texmf-dist", "usr/share")


@subpackage("texmf-doc")
def _(self):
    return ["usr/share/texmf-dist/doc"]


@subpackage("texmf-fonts")
def _(self):
    self.subdesc = "fonts - metapackage"
    self.install_if = [self.parent]
    self.options = ["empty"]
    self.depends = [
        self.with_pkgver("texmf-fonts-core"),
        self.with_pkgver("texmf-fonts-type1"),
        self.with_pkgver("texmf-fonts-opentype"),
        self.with_pkgver("texmf-fonts-truetype"),
    ]
    return []


@subpackage("texmf-fonts-type1")
def _(self):
    self.subdesc = "Type 1 fonts"
    return ["usr/share/texmf-dist/fonts/type1"]


@subpackage("texmf-fonts-opentype")
def _(self):
    self.subdesc = "OpenType fonts"
    return ["usr/share/texmf-dist/fonts/opentype"]


@subpackage("texmf-fonts-truetype")
def _(self):
    self.subdesc = "TrueType fonts"
    return ["usr/share/texmf-dist/fonts/truetype"]


@subpackage("texmf-fonts-core")
def _(self):
    self.subdesc = "font data"
    return ["usr/share/texmf-dist/fonts"]
