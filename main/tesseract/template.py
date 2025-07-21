pkgname = "tesseract"
pkgver = "5.5.1"
pkgrel = 0
build_style = "gnu_configure"
# also install training tools
make_build_args = ["training"]
make_install_args = ["training-install"]
hostmakedepends = [
    "asciidoc",
    "automake",
    "libxslt-progs",
    "pkgconf",
    "slibtool",
]
makedepends = [
    "curl-devel",
    "icu-devel",
    "leptonica-devel",
    "libarchive-devel",
    "pango-devel",
]
depends = [
    "tesseract-data-eng",
    "tesseract-data-osd",
]
pkgdesc = "OCR engine"
license = "Apache-2.0"
url = "https://tesseract-ocr.github.io"
source = f"https://github.com/tesseract-ocr/tesseract/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "a7a3f2a7420cb6a6a94d80c24163e183cf1d2f1bed2df3bbc397c81808a57237"
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
