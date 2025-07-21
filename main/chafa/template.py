pkgname = "chafa"
pkgver = "1.16.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-man"]
configure_env = {"NOCONFIGURE": "1"}
configure_gen = ["./autogen.sh"]
hostmakedepends = [
    "automake",
    "docbook-xsl-nons",
    "gm4",
    "libtool",
    "libxml2-progs",
    "libxslt-progs",
    "pkgconf",
]
makedepends = [
    "freetype-devel",
    "glib-devel",
    "libavif-devel",
    "libjpeg-turbo-devel",
    "librsvg-devel",
    "libtiff-devel",
    "libwebp-devel",
]
pkgdesc = "Character art facsimile generator"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://hpjansson.org/chafa"
source = f"https://github.com/hpjansson/chafa/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "0a7de92eda166bed79dce00e7d4050935d30258b10829053c6584df0a4fa9f89"


def post_install(self):
    for shell in ["fish", "zsh"]:
        self.install_completion(
            f"tools/completions/{shell}-completion.{shell}", shell
        )


@subpackage("chafa-devel")
def _(self):
    return self.default_devel()
