pkgname = "tesseract"
pkgver = "5.4.1"
pkgrel = 0
build_style = "gnu_configure"
# also install training tools
make_build_args = ["training"]
make_install_args = ["training-install"]
hostmakedepends = [
    "asciidoc",
    "automake",
    "pkgconf",
    "slibtool",
    "xsltproc",
]
makedepends = [
    "icu-devel",
    "leptonica-devel",
    "libarchive-devel",
    "libcurl-devel",
    "pango-devel",
]
depends = [
    "tesseract-data-eng",
    "tesseract-data-osd",
]
pkgdesc = "OCR engine"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "Apache-2.0"
url = "https://tesseract-ocr.github.io"
source = f"https://github.com/tesseract-ocr/tesseract/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "c4bc2a81c12a472f445b7c2fb4705a08bd643ef467f51ec84f0e148bd368051b"
# check: tests require external data
options = ["!check"]


@subpackage("tesseract-training")
def _(self):
    self.subdesc = "training tools"

    def install():
        for tool in [
            "ambiguous_words",
            "classifier_tester",
            "cntraining",
            "combine_lang_model",
            "combine_tessdata",
            "dawg2wordlist",
            "lstmeval",
            "lstmtraining",
            "merge_unicharsets",
            "mftraining",
            "set_unicharset_properties",
            "shapeclustering",
            "text2image",
            "unicharset_extractor",
            "wordlist2dawg",
        ]:
            self.take(f"usr/bin/{tool}")
            self.take(f"usr/share/man/man1/{tool}.1")

    return install


@subpackage("tesseract-libs")
def _(self):
    return self.default_libs()


@subpackage("tesseract-devel")
def _(self):
    return self.default_devel()
