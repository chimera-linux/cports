pkgname = "tesseract"
pkgver = "5.5.0"
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
    "libxslt-progs",
]
makedepends = [
    "icu-devel",
    "leptonica-devel",
    "libarchive-devel",
    "curl-devel",
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
sha256 = "f2fb34ca035b6d087a42875a35a7a5c4155fa9979c6132365b1e5a28ebc3fc11"
# check: tests require external data
options = ["!check"]


@subpackage("tesseract-training")
def _(self):
    self.subdesc = "training tools"

    return [
        "cmd:ambiguous_words",
        "cmd:classifier_tester",
        "cmd:cntraining",
        "cmd:combine_lang_model",
        "cmd:combine_tessdata",
        "cmd:dawg2wordlist",
        "cmd:lstmeval",
        "cmd:lstmtraining",
        "cmd:merge_unicharsets",
        "cmd:mftraining",
        "cmd:set_unicharset_properties",
        "cmd:shapeclustering",
        "cmd:text2image",
        "cmd:unicharset_extractor",
        "cmd:wordlist2dawg",
    ]


@subpackage("tesseract-libs")
def _(self):
    return self.default_libs()


@subpackage("tesseract-devel")
def _(self):
    return self.default_devel()
